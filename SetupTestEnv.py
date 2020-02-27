#!/usr/bin/python
#Alex Wen, alex.wen@canonical.com
import os
import commands
import subprocess

repo = '''
deb http://ppa.launchpad.net/hardware-certification/public/ubuntu xenial main
deb-src http://ppa.launchpad.net/hardware-certification/public/ubuntu xenial main
deb https://xxxx:8SC07M6lWDl11xM5Knnl@private-ppa.launchpad.net/oem-services-qa/ppa/ubuntu xenial main #hidden the username
deb-src https://xxxx:8SC07M6lWDl11xM5Knnl@private-ppa.launchpad.net/oem-services-qa/ppa/ubuntu xenial main #hidden the username
'''

packages = '''vim ssh plainbox python3-plainbox checkbox-gui checkbox-ng checkbox-ng-service plainbox-insecure-policy plainbox-provider-resource-generic plainbox-provider-checkbox python3-checkbox-ng python3-checkbox-support plainbox-provider-certification-client canonical-hw-collection iperf glmark2 render-bench sysstat phoronix-test-suite fwts obexftp gtkperf bonnie++ wmctrl expect ntpdate canonical-certification-client checkbox-oem-bug plainbox-provider-oem-sutton'''

#TargetFile="/etc/apt/sources.list"
TargetFile = "sources.list"

with open(TargetFile,'a') as f:
    f.write(repo)

while True:
    status = subprocess.call("""sudo apt-get update""",shell=True)
    if status == 0:
        for package in packages.split(" "):
            print "***=== Prepare to install package %s ===***" %package 
            subprocess.call('sudo apt-get install %s -y' %package,shell=True) 
        break
    else:
        print "Import GPG key"
        subprocess.call("""sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key xxxx""",shell=True) #hidden gpg-code
        subprocess.call("""sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key xxxx""",shell=True) #hidden gpg-code
        continue

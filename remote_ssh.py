#remote_ssh.py
from paramiko.client import SSHClient
import sys
import os
import paramiko
import threading
#pip3 install paramiko

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

source_file = open("ip_list.cfg", "r")
#print("Source:")
#print(source_file.read())

with open('ip_list.cfg', 'r') as f:
    l = [[num for num in line.split(' ')] for line in f if line.strip() != ""]

#print(l)
print(l[0][0])
print(l[0][1])
print(l[0][2])


def execute_command_readlines(address, usr, pwd, command):
    try:
        logger.debug("ssh " + usr + "@" + address + ", running : " +
                     command)
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        client.connect(address, username=usr, password=pwd)
        stdout = client.exec_command(command)[1]
        for line in stdout:
            # Process each line in the remote output
            print(line)
        client.close()
    except IOError:
        logger.warning(".. host " + address + " is not up")
        return "host not up", "host not up"

    except IndexError:
        pass

sciezka = "/mnt/pve/Netbook"
#result = execute_command_readlines("netbook", "willy", "sirozzy", "cd /mnt/pve/Netbook; pwd ; python3 filtering.py &") #/home/willy/dict/filtering.py"

def function_that_downloads(my_args):
    print("hello")



def my_inline_function(some_args):
    # do some stuff
    download_thread = threading.Thread(target=execute_command_readlines, args=some_args)
    download_thread.start()
    # continue doing stuff

result = my_inline_function(("netbook", "willy", "sirozzy", "cd /mnt/pve/Netbook; pwd ; python3 filtering.py &"))
result = my_inline_function(("10.0.0.12", "willy", "sirozzy", "cd /mnt/pve/Netbook; pwd ; python3 filtering.py &"))


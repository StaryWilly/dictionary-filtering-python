#remote_ssh.py
from paramiko.client import SSHClient
import paramiko
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
        _, ss_stdout, ss_stderr = client.exec_command(command)
        r_out, r_err = ss_stdout.readlines(), ss_stderr.read()
        logger.debug(r_err)
        if len(r_err) > 5:
            r_err[-1] = r_err[-1].strip()
            logger.error(r_err)
        else:
            r_out[-1] = r_out[-1].strip()
            logger.debug(r_out)
        client.close()
    except IOError:
        logger.warning(".. host " + address + " is not up")
        return "host not up", "host not up"

    return r_out, r_err
result = execute_command_readlines("netbook", "willy", "sirozzy", "pwd")
print(result[0])
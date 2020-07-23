#remote_ssh.py
from paramiko.client import SSHClient
#pip3 install paramiko


source_file = open("ip_list.cfg", "r")
print("Source:")
print(source_file.read())

with open('ip_list.cfg', 'r') as f:
    l = [[num for num in line.split(' ')] for line in f]
print(l)

# client = SSHClient()
# client.load_system_host_keys()
# client.connect('linuxip', username='your_user', password='very_secret')
# stdin, stdout, stderr = client.exec_command('python /home/your_user/your/path/to/scripty.py')

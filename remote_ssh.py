#remote_ssh.py
from paramiko.client import SSHClient

client = SSHClient()
client.load_system_host_keys()
client.connect('linuxip', username='your_user', password='very_secret')
stdin, stdout, stderr = client.exec_command('python /home/your_user/your/path/to/scripty.py')

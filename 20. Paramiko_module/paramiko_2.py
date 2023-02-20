import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.30.142', username='root', password='redhat',port=22)
#ssh.connect(hostname='192.168.30.142', username='root', key_filename=='id_rsa',port=22)
stdin, stdout, stderr = ssh.exec_command('whoami')
stdin, stdout, stderr = ssh.exec_command('uptime')
stdin, stdout, stderr = ssh.exec_command('free -m')

print("The output is : ")
print(stdout.readlines())


print("The error is: ")
print(stderr.readlines())

ssh.close()

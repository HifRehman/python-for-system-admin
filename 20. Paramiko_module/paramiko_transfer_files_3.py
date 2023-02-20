'''
Transfer a file from local server to remote server and vice versa using paramiko of python

'''
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.30.142', username='root', password='redhat',port=22)

sftp_client = ssh.open_sftp()
#print(dir(sftp_client))
#sftp_client.get('/root/anaconda-ks.cfg','/home/ansadmin/py-for-sys/anaconda.txt' )
#sftp_client.chdir('/root/')
#print(sftp_client.getcwd())
#sftp_client.get('demo-paramiko.txt','/home/ansadmin/py-for-sys/downloaded-file.txt' )
sftp_client.put("/home/ansadmin/py-for-sys/with_loop.txt", "/root/with_loop.txt")


sftp_client.close()
ssh.close()
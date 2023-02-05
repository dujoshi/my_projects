"""
Run a particular command on a remote machine via Paramiko at 
a certain intervel 

Another Info: 
I've tried all the methods described here and here without success, and finally realized that you need to use channels instead of using the SSHClient directly for calling exec_command (this does not work in background):

client = paramiko.SSHClient()
client.connect(ip_address, username='root', pkey=paramiko_key, timeout=5)
client.exec_command('python script.py > /dev/null 2>&1 &')
You should create and use a channel, this works in background:

client = paramiko.SSHClient()
client.connect(ip_address, username='root', pkey=paramiko_key, timeout=5)
transport = client.get_transport()
channel = transport.open_session()
channel.exec_command('python script.py > /dev/null 2>&1 &')



"""
import paramiko, pdb
from datetime import datetime, timedelta
import time
hostname = "x.x.x.x"
port = 22
username = "username"
password = "password"
file = '/home/xxx/data/my_timestamp'
date_format = '%d/%b/%Y %H:%M:%S'
delta = 10

def need_trigger(current, previous, delta):
    current_time = datetime.strptime(current, date_format)
    previous_time = datetime.strptime(previous, date_format)
    next_expected_run = previous_time + timedelta(seconds=delta)
    print('Last command triggered at %s'%str(previous_time))
    print('Current time is  %s'%str(current_time))

    if current_time >= next_expected_run:
       print('As %d Time passed since last Logbay run'%delta)
       print('Triggering Logbay')

       return True
    return False
def do_it():
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.connect(hostname, port, username, password)
    command = "ls %s"%file
    stdin, stdout, stderr = s.exec_command(command)
    if stdout.readlines():
       command = "cat %s"%file
       stdin, stdout, stderr = s.exec_command(command)
       out = stdout.readlines()
       last_command_run = out[-1].strip('\n')

       command = "date +\'%s\'"%(date_format)
       stdin, stdout, stderr = s.exec_command(command)
       current_time = stdout.readlines()[-1].strip('\n')

       if need_trigger(current_time, last_command_run, delta):
          print ("Need Trigger")
          time.sleep(5)
          command = "date +\'%s\' >> %s"%(date_format, file)
          print("\n updating new timestamp in command log")
          stdin, stdout, stderr = s.exec_command(command)
       else:
          print("No Need to Trigger")
    else:
       print("/n Creating a logaby timestamp file ")
       command = "date +\'%s\' > %s"%(date_format, file)
       print(command)
       stdin, stdout, stderr = s.exec_command(command)

    s.close()

if __name__ == "__main__":
   while(1) :
      do_it()

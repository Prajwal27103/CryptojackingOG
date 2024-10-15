import paramiko
# Define SSH connection details (localhost, since both processes are on the same machine)
VICTIM_IP = '127.0.0.1'  # Loopback address (localhost)
USERNAME = 'your_username'  # Replace with your Linux username
PASSWORD = 'your_password'  # Replace with your Linux password

# Create an SSH client
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(VICTIM_IP, username=USERNAME, password=PASSWORD)

# Execute a command on the victim machine
stdin, stdout, stderr = ssh_client.exec_command('python3 /path/to/victim_script.py')
print(stdout.read().decode())
print(stderr.read().decode())

# Close the SSH connection
ssh_client.close()
print("Cryptojacking simulation executed on the victim's machine.")
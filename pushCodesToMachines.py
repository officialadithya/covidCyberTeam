import generateRandomCode
import time
import paramiko

"""Function sshSession()
@param username: username of target machine
@param password: password of target machine
@param port: ssh port
Description: The sshSession() function takes input from two files in
             the form of IP Addresses. Then, a certain file on each target
             machine will be created.
"""
def sshSession(username="root", password="toor", port=22):
    # Creates a Code Using generateRandomCode.py
    code = generateRandomCode.generateRandomCode(generateRandomCode.usedCodes)
    # Gets IP addresses from an input file and appends each IP to a list.
    ipAddresses = []
    with open("ipFile.txt","r") as inputIPAddresses:
        for line in inputIPAddresses.readlines():
            ipAddresses.append(line.strip())

    # Loops through each IP and executes each command using paramiko's SSH client.
    try:
        for ip in ipAddresses:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip, port, username, password)
            stdin, stdout, stderr = ssh.exec_command("mkdir covidCodes")
            stdin, stdout, stderr = ssh.exec_command("touch covidCodes/%s"%(code))
            result = stdout.readlines()

    except:
        print("An error has occured.")
        exit()

if __name__ == "__main__":
    while True:
        time.sleep(5)
        sshSession()

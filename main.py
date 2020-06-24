import generateRandomCode
import time
import paramiko
import os

"""Function sshSession()
@param username: username of target machine
@param password: password of target machine
@param port: ssh port
Description: The sshSession() function takes input from two files in
             the form of IP Addresses. Then, a certain file on each target
             machine will be created.
"""
def sshSession(isDiagnosed, username="root", password="toor", port=22):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    if not isDiagnosed:
        # Creates a Code Using generateRandomCode.py
        global code
        code = generateRandomCode.generateRandomCode(generateRandomCode.usedCodes)
        # Gets IP addresses from an input file and appends each IP to a list.
        ipAddresses = []
        with open("ipFile.txt","r") as inputIPAddresses:
            for line in inputIPAddresses.readlines():
                ipAddresses.append(line.strip())

        # Loops through each IP and executes each command using paramiko's SSH client.
        try:
            for ip in ipAddresses:
                ssh.connect(ip, port, username, password)
                stdin, stdout, stderr = ssh.exec_command("mkdir covidCodes")
                stdin, stdout, stderr = ssh.exec_command("touch covidCodes/%s.txt"%(code))
                result = stdout.readlines()

        except:
            print("An error has occured.")
            exit()
    else:
        for ip in ipAddresses:
            ssh.connect(ip, port, username, password)
            stdin, stdout, stderr = ssh.exec_command("touch sentCodes/POSITIVE_TEST.txt"%(code))
            result = stdout.readlines()

"""Function isDiagnosed()
@param username: directory in which a diagnosis, if it exists, will be shown.
Description: The generateRandomCode() function takes in one parameter, description,
which is set to sentCodes. then, the os.path.exists() function is used to see if a
diagnosis file is present. If it is, the user has been diagnosed.
"""
def isDiagnosed(directory="sentCodes"):
    if os.path.exists("%s/POSITIVE_TEST.txt"%(directory)):
        return True
    return False


# Driver
if __name__ == "__main__":
    # Keeps Track of Sent Codes
    os.system("mkdir sentCodes")

    # Infinite Loop to Send Codes
    while True:
        time.sleep(5)
        sshSession(isDiagnosed())
        os.system("touch sentCodes/%s.txt"%(code))

        if isDiagnosed():
            sshSession(isDiagnosed())
            exit()

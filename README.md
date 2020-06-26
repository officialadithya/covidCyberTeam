# covidCyberTeam
This bundle is meant to show a proof-of-concept of a cybersecurity-focused method of initiating contact tracing with COVID-19. Before using the bundle, all machines must have a unique IP address assigned to them. Furthermore, the script must be ran from a machine that is on the network. 

	Required Dependencies:

		python3
		paramiko
    
			
python3 is the language in which the script is written in. If python3 is not installed on the system where the script will be ran, install it by going to https://www.python.org/downloads/ and downloading the latest stable version. From there, follow all directions. To run the file after all dependencies are installed, execute python3 adminNetwork.py

paramiko allows us to start an SSH session. If paramiko is not installed on the system where the script will be ran, install it by executing  pip install paramiko.

	Input Format:

For the file ipFile.txt, input all IP addresses that you wish to run the simulation on. Enter each IP address on a new line in the format of w.x.y.z.

	Example:

		192.168.0.1
		192.168.0.2
		192.168.0.3
  	192.168.0.4
	 	192.168.0.5
	 	192.168.0.6

The methodology that this bundle uses is as follows:
  
  While two devices are close to each other for a certain time, each device will send a code to all other devices that it is close to. Each device will keep track of the codes that it has sent and the codes it has received. Then, when a device is diagnosed with COVID-19, it will stop sending codes and will direct all other devices it has sent codes to in the past to stop as well. Ideally, the codes are completely independed from the devices that send or receive them, to preserve privacy.
  
  The methodology was inspired by the following video: https://www.youtube.com/watch?v=D__UaR5MQao

import string
import random

mainFolder = [] #This is where the unique codes get uploaded to
infectedFolder = [] #This is where unique code associated with infected people get moved to
#These folders would be located on the server ^

machineOneSent = []#This is where all the codes machine one has sent in the past 14 days are stored
machineOneRecived = []#This is where all the codes machine one has recived in the past 14 days are stored
machineTwoSent = []#This is where all the codes machine two has sent in the past 14 days are stored
machineTwoRecived = []#This is where all the codes machine two has recived in the past 14 days are stored

def randomCode(): #Dumbed down vesion of the code generator
  availableCharacters = string.digits+string.ascii_letters
  code = ''.join(random.choice(availableCharacters) for i in range(10))
  return code

#Machine 1 and 2 are nearby each other and they create random codes and send them to each other, while saving it to their own device, adn uploading it to the server

currentCode = ''#This is used so we can store a code and see where it is being used

#Machine 1 creates a code and sends it to the server and machine 2, while storing it on the device

currentCode = randomCode()
#print(currentCode)
machineOneSent.append(currentCode)
machineTwoRecived.append(currentCode)
mainFolder.append(currentCode)#**

#Machine 2 does the same thing
currentCode = randomCode()
#print(currentCode)
machineTwoSent.append(currentCode)
machineOneRecived.append(currentCode)
mainFolder.append(currentCode)#**

#The double atsriks are there to let you know that the codes are not going to be dumped directly into the folder. They will have to go through a "screening process." The server side is explained farther below

#Both machines check the infected folder on the server against their Recived folder

for i in machineOneRecived:
  for k in infectedFolder:
    if i == k:
      print("uh oh, you have been near someone infected!")
    else:
      pass

for i in machineTwoRecived:
  for k in infectedFolder:
    if i == k:
      print("uh oh, you have been near someone infected!")
    else:
      pass

#this process repeats a couple more times while machine 1 and machine 2 are near each other

for i in range(1, 5):
  currentCode = randomCode()
  #print(currentCode)
  machineOneSent.append(currentCode)
  machineTwoRecived.append(currentCode)
  mainFolder.append(currentCode)#**
  currentCode = randomCode()
  #print(currentCode)
  machineTwoSent.append(currentCode)
  machineOneRecived.append(currentCode)
  mainFolder.append(currentCode)#**
  for i in machineOneRecived:
    for k in infectedFolder:
      if i == k:
        print("uh oh, you have been near someone infected!")
      else:
        pass
  for i in machineTwoRecived:
    for k in infectedFolder:
      if i == k:
        print("uh oh, you have been near someone infected!")
      else:
        pass

#The following code would run on ther server; whenever it recive a new unique code, it would check to see if it already has that code. If the server is reciving a code it already has, that means that a user has gotten covid, and the device is sending all if its recent codes to the server again. The server then copies the codes into the infected folder. 

#This part mimicks machine 1 sending its codes again since its user got tested for covid and came back positive
def sendSentCodeToServer():
  #This would be the machine sshing into the server to send its recent codes
  pass
sendSentCodeToServer()

#This part is the server code
#Pretend newConnection is the data that was recived on the server during machine 1's sendCodeToServer()
newConnection = machineOneSent
for i in newConnection:
  for k in mainFolder:
    if i==k:
      infectedFolder.append(i)
    else:
      mainFolder.append(i)

#Now machine 2 does its routine check against the infected folder.

for i in machineTwoRecived:
  for k in infectedFolder:
    if i == k:
      print("uh oh, you have been near someone infected!")
      break
    else:
      pass

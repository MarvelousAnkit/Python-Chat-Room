****************Requirement****************************
1) Latest Version of Python should be Installed on the sytem
2) Visual Studio Code should Be Installed on the system
3) Two Systems are required Weather It Can Be Laptop or PC.

Condition : Both System should be connected on The Same Wifi Network

Steps 1  
Paste The Server code in visual studio code of system 1
and paste the client code in visual studio code of System 2

Step 2 : Before Running The Code Do Some Changes
 
Whatever You will be chat in the Console, data will be Stored in A notepad file, So We have to do some changes in Server Code 
You will see a code like this 

from socket import  *
f1=open("C:\\Users\\ANKIT\\Desktop\\Python Chat Room\\chats.txt","a")

C:\\Users\\ANKIT\\Desktop\\Python Chat Room  --> Just replace this location with the original location of chats.txt in your System.

Step 3

Run the server code first It will ask Enter Port Number U can enter any value greator than 1024 for ex 5566,9999 etc
Now Run The Client Code, You Have to enter the same port number that you have entered in  server code. After pressing enter both system will be connected.

Hurrey !! Congratulation.



 
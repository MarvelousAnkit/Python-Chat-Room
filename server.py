#CODE BY ANKIT SINGH. For More Information Pls Connect with me on LINKEDIN - https://www.linkedin.com/in/ankitizsmartz/
from socket import  *
f1=open("C:\\Users\\ANKIT\\Desktop\\Python Chat Room\\chats.txt","a")
sc=socket()# To Make socket an object
sadd=gethostbyname(gethostname())
sport=int(input("Enter port no: "))
sc.bind((sadd,sport))
print("server is binded on address :" ,sadd ,"on port" ,sport)
sc.listen()
print("server is waiting for client to be connected")
cc,cadd=sc.accept()
print("client is connected" ,cadd)
cc.send(bytes("Welcome to The Ankit Chat Application" , "utf-8"))

while True:
    m=input("Server Say: ")
    f1.write("\nServer :")
    f1.write(str(m))
    cc.send(bytes(m , "utf-8"))
    
    
    if(m=="bye"):
        print("chat ended by you")

        break
        cc.close()

    cm=cc.recv(1024).decode()
    f1.write("\nClient :")
    f1.write(str(cm))
    if (cm == "bye"):
        cc.send(bytes("bye" , "utf-8"))
        print("chat ended by client")
        break
        cc.close()
    else:
        print("Client Say" , cm)
f1.close()
cc.close()

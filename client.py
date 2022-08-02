from socket import*
cc = socket()
cadd = gethostbyname(gethostname())
cportt = int(input("Enter ur port: "))
cc.connect((cadd,cportt))
print("connected with server",cadd)
print("Message: ",cc.recv(1024).decode())

while True:
    sm = cc.recv(1024).decode()
    if(sm=="bye"):
        cc.send(bytes("bye", "utf-8"))
        print("chat ended by server ")
        break
        cc.close
    else:
        print("Server Say: ",sm)
    
        m=input("Client Say: ")
        cc.send(bytes(m,"utf-8"))
       
        if( m=="bye"):
            print("chat ended by you")
            break
            cc.close()
cc.close()

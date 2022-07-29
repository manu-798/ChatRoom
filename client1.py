import socket
from threading import Thread



name= input("Enter your Name : ")
if name == 'admin':
    password=int(input("enter your password: "))
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("192.168.29.112",9999))
stop_thread= False
client.send(name.encode())
if client.recv(1024).decode() == "PASS":
    client.send("password".encode())
    if client.recv(1024).decode() == "REFUSE":
        stop_thread =True
def send(client):
    while True:    
        data = f'{name} : {input()}'
        client.send(data.encode())

def receive(client):
    while True:
        try:
            data = client.recv(1024).decode()
            print(data)
        except:
            client.close()
            break
if stop_thread == False:

    thread1 = Thread(target= send,args=(client,))
    thread1.start()
    thread2 = Thread(target = receive,args=(client,))
    thread2.start()

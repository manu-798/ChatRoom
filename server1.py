import socket
from threading import Thread

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("192.168.29.112",9999))
server.listen()
all_clients ={}

def client_thread(client):
    while True:
        try:
            msg = client.recv(1024)
            for c in all_clients:
                c.send(msg)
        except:
            for c in all_clients:
                if c!= client:
                    c.send((f"** {name} has left the chat **").encode())
            del all_clients[client]
            client.close()
            break
    
while True:
    print("waiting for connection....")
    client, address = server.accept()
    print(address)
    print("connection established")
    name= client.recv(1024).decode()
    if name == 'admin':
        client.send('PASS'.encode())
        password = client.recv(1024).decode()
        if password != 1234:
            client.send('REFUSE'.encode())
            client.close()
            continue
    all_clients[client] = name
    
    for c in all_clients:
        if c!= client:
            c.send((f"** {name} has joined the chat **").encode())
    
    thread = Thread(target = client_thread, args = (client,))
    thread.start()
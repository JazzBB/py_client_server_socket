#!/usr/bin/python
import socket
import os

socket_server = socket.socket()
host = '192.168.49.128'
port = 12345
socket_server.bind((host, port))
socket_server.listen(5)

print("#######################")
print("started server side")
print("#######################")

no_data = 0

def listener():
        data = client.recv(4096).decode()
        print('Command received from -'+ str(addr) +' - ' + data)


        if data == 'srv_uptime':
            return_payload = os.popen('uptime').read()
            client.send(str(return_payload))
            print('Response was :' + return_payload)
            return listener()
   
        if data == 'srv_shut':
            return_payload = 'Linux shut down initiated'
            client.send(str(return_payload))
            os.system('shutdown -P')
            return listener()

        if data == 'close':
            return_payload = 'Client-side request has been received\nClosing connection'
            print(return_payload)
            client.close()
            #no_data = 1
            #eturn no_data


while no_data == 0:
    client, addr = socket_server.accept()
    client.send('Connection : '+ host)
    print('Accepted connection request from: ' + str(addr))
    listener()
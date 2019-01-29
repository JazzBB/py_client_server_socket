import socket            # Import socket module
import datetime
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
host = '192.168.49.128' # Get local machine name
port = 12345                # Reserve a port for your service.


def command_input():
	payload = input('Command>>> ')
	if payload == 'close':
		s.send(str('close').encode())	
		close_connect()
		exit()
	if payload == '':
		print('Please give an input MOFO')
		payload = input('Command: ')
	else:
		payload_to_send = str(payload).encode()
		s.send(payload_to_send)
		receive_from_server()
		return main()

def receive_from_server():
	response_from_server = s.recv(4096)
	print(response_from_server.decode('utf-8'))
	return main()
	
def close_connect():
	s.close()                     # Close the socket when done
	
def main():
	command_input()

s.connect((host, port))
s.settimeout(None)
print(s.recv(4096).decode('utf-8'))	
	
while True:
	main()
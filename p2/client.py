import socket

HEADER = 64
PORT = 5050
DISCONNECT_MESSAGE = "!DISCONNECT"
FORMAT = 'utf-8'
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
	message = msg.encode(FORMAT)
	msg_lenght = len(message)
	send_lenght = str(msg_lenght).encode(FORMAT)
	send_lenght += b' ' * (HEADER - len(send_lenght))
	client.send(send_lenght)
	client.send(message)
	print(client.recv(2048).decode(FORMAT))

while True:
	send(input("Please provide a message: "))
send(DISCONNECT_MESSAGE)

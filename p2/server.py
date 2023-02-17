import socket
import threading

HEADER = 64
PORT = 5050
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)
#SERVER = socket.gethostbyname(socket.gethostname())
#print(SERVER)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
	print(f"[NEW CONNECTION] {addr} connected.")

	connected = True
	while connected:
		msg_lenght = conn.recv(HEADER).decode(FORMAT)
		if msg_lenght:
			msg_lenght = int(msg_lenght)
			msg = conn.recv(msg_lenght).decode(FORMAT)
			if msg == DISCONNECT_MESSAGE:
				connected = False

			print(f"[{addr}] {msg}")
			conn.send("...message delivered...".encode(FORMAT))
	conn.close()


def start():
	server.listen()
	print(f"[LISTENING] Server is listening on {SERVER}")
	while True:
		conn, addr = server.accept()
		thread = threading.Thread(target=handle_client, args=(conn, addr))
		thread.start()
		print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[STARTING] Server is starting...")
start()

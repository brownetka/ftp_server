import socket

class Exit(Exception):
	pass

sock = socket.socket()
server = input('Enter Server: ')
port = input('Enter Port: ')
print()

try:
	sock.connect((server, int(port)))

	# server
	print(f"Server IP: {server}; Port: {port}")

	# client
	host = sock.getsockname()
	print(f"Client IP: {host[0]}; Port: {host[1]}")

except ConnectionRefusedError as c:
	print(f"ERROR {c}")
	exit()


while True:

	try:
		data = sock.recv(1024).decode("utf8")

		# отключение от сервера
		if len(data) == 0 or data.lower() == 'stop' or data.lower() == 'exit':
			raise Exception("You disconnected.")

	except ConnectionResetError as e:
		print(f"ERROR: {e}")
		sock.close()
		exit()

	except Exception as s:
		print(f"ERROR: {s}")
		sock.close()
		exit()

	print(f"\nServer: {data}")


	try:
		promt = input("\nYou: ")
	except KeyboardInterrupt as k:
		print(f"ERROR: {k}")
		exit()


	try:
		result = sock.send(promt.encode())
		if not result:
			raise Exception("Date not found")
	except Exception as e:
		print(f"ERROR: {e}")
		exit()


sock.close()

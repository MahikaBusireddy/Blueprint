import socket

try:
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[C]: Client socket created")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()

server_binding = ("localhost", 9999)
cs.connect(server_binding)

# Receive welcome message from server
data_from_server = cs.recv(1024)
message = data_from_server.decode()
print("[C]: Data received from server: " + message)

# Send username and password to server
username = input("Enter username: ")
password = input("Enter password: ")
cs.send(username.encode())
cs.send(password.encode())

# Receive response from server
response = cs.recv(1024).decode()
print("[C]: Data received from server: " + response)

# Close the client socket
cs.close()

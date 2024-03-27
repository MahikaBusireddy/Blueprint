import threading
import socket
import sqlite3
import hashlib

# Import sqlite3 for database operations

# Function to verify user credentials
def verify_user(username, password):
    conn = sqlite3.connect('projectDatabase.db')
    cursor = conn.cursor()

    # Check if username and password match a record in the database
    cursor.execute("SELECT * FROM projectDatabase WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()

    conn.close()

    return result is not None

# Function to handle client connections
def start_connection(c):
    msg = "Welcome to the login server!"
    c.send(msg.encode())

    # Receive username and password from client
    username = c.recv(1024).decode()
    password = c.recv(1024).decode()

    # Verify user credentials
    if verify_user(username, password):
        response = "Login successful!"
    else:
        response = "Invalid username or password."

    # Send response to client
    c.send(response.encode())

    # Close connection
    c.close()

try:
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[S]: Server socket created")
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

server_binding = ("localhost", 9999)
ss.bind(server_binding)
ss.listen()

while True:
    client, addr = ss.accept()
    t2 = threading.Thread(target=start_connection, args=(client,))
    t2.start()
	
    ss.close()
    exit()

# Close the server socket
#ss.close()

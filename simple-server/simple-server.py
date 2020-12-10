import socket
import sys

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(("", 23))

    server.listen(1)

    print("The server has been started.")

    connection, address = server.accept()

    with connection:
        print("A client has been connected.")

        connection.sendall(b"Hello, World!\n")

        while True:
            string = connection.recv(1)

            connection.close()
            print("A connection closed.")

            sys.exit()
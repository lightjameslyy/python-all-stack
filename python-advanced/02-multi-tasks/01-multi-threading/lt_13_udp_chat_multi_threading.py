import socket
import threading

LOCAL_IP_PORT = ("", 8888)
DEST_IP_PORT = ("192.168.56.1", 8888)


def recv_msg(udp_socket):
    """receive data and print"""

    # reveive data
    while True:
        recv_data = udp_socket.recvfrom(1024)
        if recv_data[0].decode("utf-8") == "exit":
            break
        print(recv_data)


def send_msg(udp_socket):
    """send data"""

    # send data
    while True:
        send_data = input("data to send: ")
        if send_data == "exit":
            break
        udp_socket.sendto(send_data.encode("utf-8"), DEST_IP_PORT)


def main():
    """udp chat main procedures"""

    # 1. create socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. bind local info
    udp_socket.bind(LOCAL_IP_PORT)

    # 3. create 2 threads to send and recv at the same time
    t1 = threading.Thread(target=send_msg, args=(udp_socket,))
    t2 = threading.Thread(target=recv_msg, args=(udp_socket,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == '__main__':
    main()

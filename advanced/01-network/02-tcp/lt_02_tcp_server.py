import socket


def main():
    # 1. 创建tcp套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 绑定本地信息
    tcp_server_socket.bind(("", 8888))

    # 3. listen
    tcp_server_socket.listen(128)

    # 4. accept
    print("11111")
    client_socket, client_addr = tcp_server_socket.accept()
    print("22222")
    print(client_addr)

    # receive
    recv_data = client_socket.recv(1024)
    print(recv_data)

    # 回送消息给客户端
    client_socket.send("ok".encode("utf-8"))

    # 关闭套接字
    client_socket.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()

import socket


def main():
    # 1. 创建tcp套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 链接服务器
    # tcp_socket.connect(("192.168.0.105", 8888))
    server_ip = input("server ip:")
    server_port = int(input("server port:"))
    server_addr = (server_ip, server_port)
    tcp_socket.connect(server_addr)

    # 3. 发送/接收数据
    send_data = input("data to send:")
    tcp_socket.send(send_data.encode("utf-8"))

    # 4. 关闭套接字
    tcp_socket.close()


if __name__ == '__main__':
    main()

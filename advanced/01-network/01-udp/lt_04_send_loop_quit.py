import socket


def main():
    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:

        # 从键盘获取数据
        send_data = input("请输入要发送的数据：")

        if send_data == "exit":
            break

        # 使用套接字收发数据
        # udp_socket.sendto(b"hahaha\n", ("10.2.152.29", 8080))
        udp_socket.sendto(send_data.encode("utf-8"), ("10.2.152.29", 8080))

    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()

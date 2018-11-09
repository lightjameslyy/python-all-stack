import socket


def main():
    # 1. 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 绑定一个本地地址
    local_addr = ("", 7788)  # 只能绑定自己电脑的ip和port
    udp_socket.bind(local_addr)

    while True:

        # 3. 接收数据
        recv_data = udp_socket.recvfrom(1024)

        # recv_data是一个tuple：(数据,(发送方ip, port))
        recv_msg = recv_data[0]
        send_addr = recv_data[1]

        # 4. 打印接收的数据
        print("%s: %s" % (str(send_addr), recv_msg.decode("utf-8")))

    # 5. 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()

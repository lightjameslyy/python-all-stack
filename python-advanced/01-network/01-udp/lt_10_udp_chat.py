import socket


def send_msg(udp_socket):
    """发送消息"""

    # 获取对方的ip:port
    dest_ip = input("dest ip:")
    dest_port = int(input("dest port:"))
    # 获取发送内容
    send_data = input("请输入要发送的数据：")
    # 使用套接字收发数据
    udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def recv_msg(udp_socket):
    """接收数据"""
    recv_data = udp_socket.recvfrom(1024)
    print("receive from %s: %s" % (str(recv_data[1]), recv_data[0].decode("utf-8")))


def main():
    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定信息
    udp_socket.bind(("", 8888))

    # 循环处理
    while True:
        # 发送
        send_msg(udp_socket)

        # 接收并显示
        recv_msg(udp_socket)

    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()

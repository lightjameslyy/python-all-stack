import socket


def send_file_to_client(client_socket, client_addr):
    # 1. 接收客户端要下载的文件名
    file_name = client_socket.recv(1024).decode("utf-8")
    print("client %s want to download [%s]" % (str(client_addr), file_name))

    file_content = None
    # 2. 打开文件，读取数据
    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("can't find file [%s]" % file_name)

    # 发送文件数据给客户端
    if file_content:
        client_socket.send(file_content)


def main():
    # 1. 创建tcp套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 绑定本地信息
    tcp_server_socket.bind(("", 8888))

    # 3. listen
    tcp_server_socket.listen(128)

    while True:
        # 4. accept
        client_socket, client_addr = tcp_server_socket.accept()

        # 5. 像客户端发送数据
        send_file_to_client(client_socket, client_addr)

        # 关闭套接字
        client_socket.close()

    tcp_server_socket.close()


if __name__ == '__main__':
    main()

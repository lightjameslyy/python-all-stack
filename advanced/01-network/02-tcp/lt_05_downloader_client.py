import socket


def main():
    # 1. 创建tcp套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 获取服务器ip、port
    dest_ip = input("dest ip: ")
    dest_port = int(input("dest port: "))

    # 3. 链接服务器
    tcp_socket.connect((dest_ip, dest_port))

    # 4. 获取要下载文件的文件名
    download_file_name = input("download file name: ")

    # 5. 将文件名发送到服务器
    tcp_socket.send(download_file_name.encode("utf-8"))

    # 6. 接收文件数据
    recv_data = tcp_socket.recv(1024*1024)

    # 7. 保存接收的数据到文件中
    if recv_data:
        with open("downloaded_" + download_file_name, "wb") as f:
            f.write(recv_data)

    # 8. 关闭套接字
    tcp_socket.close()


if __name__ == '__main__':
    main()

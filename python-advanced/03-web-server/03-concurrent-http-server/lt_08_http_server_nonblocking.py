import socket
import re
import time


def serve_client(client_socket):
    """为客户端提供服务并返回数据"""

    # 1. 接受http请求
    # GET / HTTP/1.1
    # ...
    request = client_socket.recv(1024).decode("utf-8")
    # print("=" * 80)
    # print(request)

    request_lines = request.splitlines()
    print()
    print("=" * 80)
    print(request_lines)

    file_name = ""
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    if ret:
        file_name = ret.group(1)
        print("*" * 10, file_name)
        if file_name == "/":
            file_name = "/index.html"

    # 2. 返回http格式的数据给浏览器

    try:
        f = open("html" + file_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "page not found"
        client_socket.send(response.encode("utf-8"))
    else:
        # 2.1 准备给浏览器的数据--header
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        # 2.2 准备给浏览器的数据--body
        html_content = f.read()
        f.close()

        # 2.3 发送数据
        # header
        client_socket.send(response.encode("utf-8"))
        # body
        client_socket.send(html_content)

    # 3. 关闭套接字
    client_socket.close()


def main():
    """整体控制"""

    # 1. 创建套接字
    http_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 绑定
    http_server_socket.bind(("", 8888))

    # 3. listen
    http_server_socket.listen(128)

    # 4. 设置套接字为非阻塞方式
    http_server_socket.setblocking(False)

    # 5. 记录当前提供服务的套接字列表
    client_socket_list = list()

    while True:
        time.sleep(0.5)

        # 6. 非阻塞的等待客户端到来
        try:
            new_socket, client_addr = http_server_socket.accept()
        except Exception as ret:
            print("---no client comes---")
        else:
            print("---new client---")
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)

        # 7. 遍历client_socket_list提供服务，或释放套接字
        for client_socket in client_socket_list:
            try:
                recv_data = client_socket.recv(1024)
            except Exception as ret:
                print("---no recv data yet---")
            else:
                if recv_data:
                    # 客户端发来数据
                    print("---客户端发来数据了---")
                    print(recv_data)
                else:
                    # 客户端调用close导致recv_data=""
                    print(recv_data)
                    client_socket_list.remove(client_socket)
                    client_socket.close()
                    print("客户端关闭")

    # 8. 关闭套接字
    http_server_socket.close()


if __name__ == '__main__':
    main()

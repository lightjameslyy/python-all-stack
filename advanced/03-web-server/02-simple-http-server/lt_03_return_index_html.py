import socket

INDEX_HTML_PATH = "../../../data/html/index.html"

def serve_client(client_socket):
    """为客户端提供服务并返回数据"""

    # 1. 接受http请求
    # GET / HTTP/1.1
    # ...
    request = client_socket.recv(1024)
    print("=" * 80)
    print(request)

    # 2. 返回http格式的数据给浏览器
    # 2.1 准备给浏览器的数据--header
    response = "HTTP/1.1 200 OK\r\n"
    response += "\r\n"
    # 2.1 准备给浏览器的数据--body
    # response += "<h1>Hello HTTP.</h1>"

    f = open(INDEX_HTML_PATH, "rb")
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
    http_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2. 绑定
    http_server_socket.bind(("", 8888))

    # 3. listen
    http_server_socket.listen(128)

    while True:
        # 4. 等待新的客户端链接
        client_socket, client_addr = http_server_socket.accept()

        # 5. 为客户端服务
        serve_client(client_socket)

    # 6. 关闭套接字
    http_server_socket.close()


if __name__ == '__main__':
    main()

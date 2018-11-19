import socket
import re


def serve_client(client_socket, request):
    """为客户端提供服务并返回数据"""

    # 1. 接受http请求
    # GET / HTTP/1.1
    # ...
    # request = client_socket.recv(1024).decode("utf-8")
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

        html_content = f.read()
        f.close()

        response_body = html_content

        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += "\r\n"

        response = response_header.encode("utf-8") + response_body
        client_socket.send(response)


def main():
    """整体控制"""

    # 1. 创建套接字
    http_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    http_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    http_server_socket.setblocking(False)

    # 2. 绑定
    http_server_socket.bind(("", 8888))

    # 3. listen
    http_server_socket.listen(128)

    client_socket_list = list()
    while True:
        # 4. 等待新的客户端链接
        try:
            new_socket, client_addr = http_server_socket.accept()
        except Exception as ret:
            pass
        else:
            client_socket_list.append(new_socket)
            new_socket.setblocking(False)

        for client_socket in client_socket_list:
            try:
                recv_data = client_socket.recv(1024).decode("utf-8")
            except Exception as ret:
                pass
            else:
                if recv_data:
                    serve_client(client_socket, recv_data)
                else:
                    client_socket.close()
                    client_socket_list.remove(client_socket)

    # 6. 关闭套接字
    http_server_socket.close()


if __name__ == '__main__':
    main()

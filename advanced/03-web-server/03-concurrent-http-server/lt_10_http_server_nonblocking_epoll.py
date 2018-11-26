import socket
import select
import re

HTML_ROOT_PATH = "../../../data/html"

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
        f = open(HTML_ROOT_PATH + file_name, "rb")
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

    # 生成epoll对象
    epl = select.epoll()

    # 注册http server
    epl.register(http_server_socket.fileno(), select.EPOLLIN)

    fd_event_dict = dict()

    while True:
        # 阻塞直到有事件通知，获取fd和event的列表
        fd_event_list = epl.poll()

        for fd, event in fd_event_list:
            # http server等待新的客户端到来
            if fd == http_server_socket.fileno():
                # 为什么此处不用try？因为if判断成功意味着accept成功返回了
                new_socket, client_addr = http_server_socket.accept()
                epl.register(new_socket.fileno(), select.EPOLLIN)
                fd_event_dict[new_socket.fileno()] = new_socket
            elif event == select.EPOLLIN:
                # 检查客户端发过来的数据
                recv_data = fd_event_dict[fd].recv(1024).decode("utf-8")
                if recv_data:
                    serve_client(fd_event_dict[fd], recv_data)
                else:
                    fd_event_dict[fd].close()
                    epl.unregister(fd)
                    del fd_event_dict[fd]

    # 6. 关闭套接字
    http_server_socket.close()


if __name__ == '__main__':
    main()

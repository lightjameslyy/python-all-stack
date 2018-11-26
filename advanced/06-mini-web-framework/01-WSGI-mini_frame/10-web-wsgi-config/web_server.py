import socket
import re
import multiprocessing
import time
#import dynamic.mini_frame
import sys

class WSGIServer(object):

    def __init__(self, port, app, static_path):
        # 1. 创建套接字
        self.http_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.http_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 2. 绑定
        self.http_server_socket.bind(("", port))

        # 3. listen
        self.http_server_socket.listen(128)

        self.app = app
        self.static_path = static_path


    def serve_client(self, client_socket):
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
        # 2.1 如果请求的资源不是*.py，视为静态资源
        if not file_name.endswith(".py"):
            try:
                f = open(self.static_path + file_name, "rb")
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
        else:
        # 2.2 动态资源的请求，使用WSGI协议

            env = dict()
            env['PATH_INFO'] = file_name
            # {"PATH_INFO": "/index.py"}
            body = self.app(env, self.set_response_header)

            header = "HTTP/1.1 %s\r\n" % self.status
            for tmp in self.headers:
                header += "%s:%s\r\n" % (tmp[0], tmp[1])
            header += "\r\n"

            response = header + body;

            # 发送response给浏览器
            client_socket.send(response.encode("utf-8"))

        # 3. 子进程关闭套接字
        client_socket.close()

    def set_response_header(self, status, headers):
        self.status = status
        self.headers = [("Server", "mini frame v0.0")]
        self.headers += headers

    def run_forever(self):
        """整体控制"""

        while True:
            # 4. 等待新的客户端链接
            client_socket, client_addr = self.http_server_socket.accept()

            # 5. 为客户端服务
            # 创建进程执行serve_client()
            # 注意：传入的client_socket会拷贝到创建的进程，跟主进程中的client_socket不是同一个对象
            p = multiprocessing.Process(target=self.serve_client, args=(client_socket,))
            p.start()

            # 主进程关闭套接字，子进程关闭后才真正关闭
            client_socket.close()

        # 6. 关闭套接字
        self.http_server_socket.close()


def main():
    """整体控制，创建一个web服务器对象，然后调用这个对象的run_forever方法运行"""
    if len(sys.argv) == 3:
        try:
            port = int(sys.argv[1])
        except Exception as ret:
            print("端口输入错误...")
            return
        frame_app_name = sys.argv[2]
    else:
        print("请按照以下方式运行：")
        print("python3 web_server.py 8888 mini_frame:application")
        return

    # mini_frame:application
    ret = re.match(r"([^:]+):(.*)", frame_app_name)
    if ret:
        frame_name = ret.group(1)  # mini_frame
        app_name = ret.group(2)  # application
    else:
        print("请按照以下方式运行：")
        print("python3 web_server.py 8888 mini_frame:application")
        return

    with open("./web_server.conf") as f:
        conf_info = eval(f.read())

    # 此时conf_info是一个字典
    # {
    #     "static_path": "./static",
    #     "dynamic_path": "./dynamic"
    # }

    sys.path.append(conf_info['dynamic_path'])
    # import frame_name --> wrong, find frame_name.py
    frame = __import__(frame_name)
    app = getattr(frame, app_name)

    wsgi_server = WSGIServer(port, app, conf_info['static_path'])
    wsgi_server.run_forever()


if __name__ == '__main__':
    main()

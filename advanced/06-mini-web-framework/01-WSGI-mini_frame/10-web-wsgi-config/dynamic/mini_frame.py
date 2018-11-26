
def index():
    with open("./templates/index.html") as f:
        content = f.read()
    return content


def login():
    with open("./templates/center.html") as f:
        return f.read()


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])

    file_name = env['PATH_INFO']
    if file_name == "/index.py":
        return index()
    if file_name == "/center.py":
        return login()
    else:
        return 'Hello World! 你好！'

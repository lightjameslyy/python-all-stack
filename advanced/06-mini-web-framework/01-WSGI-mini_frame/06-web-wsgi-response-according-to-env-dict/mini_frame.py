
def index():
    return "home page"

def login():
    return "login page"


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])

    file_name = env['PATH_INFO']
    if file_name == "/index.py":
        return index()
    if file_name == "/login.py":
        return login()
    else:
        return 'Hello World! 你好！'

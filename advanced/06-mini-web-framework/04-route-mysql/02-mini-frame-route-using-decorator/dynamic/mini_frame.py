import re


"""
URL_FUNC_DICT = {
    "/index.py": index,
    "/center.py": center
}
"""

URL_FUNC_DICT = dict()


def route(url):
    def set_func(func):
        # URL_FUNC_DICT["/index.py"] = index
        URL_FUNC_DICT[url] = func
        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func


@route("/index.py")
def index():
    with open("./templates/index.html") as f:
        content = f.read()

    my_stock_info = "hello, 这是你的本月明细..."

    content = re.sub(r"\{%content%\}", my_stock_info, content)

    return content


@route("/center.py")
def center():
    with open("./templates/center.html") as f:
        content = f.read()

    my_stock_info = "这是从mysql查询出来的数据..."

    content = re.sub(r"\{%content%\}", my_stock_info, content)

    return content


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])

    file_name = env['PATH_INFO']

    """
    if file_name == "/index.py":
        return index()
    if file_name == "/center.py":
        return center()
    else:
        return 'Hello World! 你好！'
    """
    
    try:
        # func = URL_FUNC_DICT[file_name]
        # return func()
        return URL_FUNC_DICT[file_name]()
    except Exception as ret:
        return "exception: %s" % str(ret) 

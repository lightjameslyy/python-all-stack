import re
from pymysql import connect


"""
URL_FUNC_DICT = {
    r"/index.html": index,
    r"/center.html": center,
    r"/add/\d+\.html": add_focus
}
"""

URL_FUNC_DICT = dict()


def route(url):
    def set_func(func):
        # URL_FUNC_DICT["/index.html"] = index
        URL_FUNC_DICT[url] = func
        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func


@route(r"/index.html")
def index():
    with open("./templates/index.html") as f:
        content = f.read()

    # my_stock_info = "hello, 这是你的本月明细..."
    # content = re.sub(r"\{%content%\}", my_stock_info, content)

    # 连接数据库
    conn = connect(host="localhost", port=3306, user="root", password="root", database="stock_db", charset="utf8")
    # get cursor object
    cs = conn.cursor()

    cs.execute("select * from info;")
    stock_infos = cs.fetchall()
    cs.close()
    conn.close()

    tr_template = """
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
            <input type="button" value="添加" id="toAdd" name="toAdd" systemidvalue="%s">
            </td>
        </tr>          
    """

    html = ""
    for line_info in stock_infos:
        html += tr_template % (line_info[0], line_info[1], line_info[2], line_info[3], line_info[4], line_info[5], line_info[6], line_info[7], line_info[1])
    
    content = re.sub(r"\{%content%\}", html, content)

    return content


@route(r"/center.html")
def center():
    with open("./templates/center.html") as f:
        content = f.read()

    # my_stock_info = "这是从mysql查询出来的数据..."
    # content = re.sub(r"\{%content%\}", my_stock_info, content)

    # 连接数据库
    conn = connect(host="localhost", port=3306, user="root", password="root", database="stock_db", charset="utf8")
    # get cursor object
    cs = conn.cursor()

    cs.execute("select s.code, s.short, s.chg, s.turnover, s.price, s.highs, f.note_info from info as s inner join focus as f on f.info_id = s.id;")
    stock_infos = cs.fetchall()
    cs.close()
    conn.close()

    tr_template = """
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
            <input type="button" value="修改" id="toAdd" name="toAdd" systemidvalue="%s">
            </td>
            <td>
            <input type="button" value="删除" id="toAdd" name="toAdd" systemidvalue="%s">
            </td>
        </tr>          
    """

    html = ""
    for line_info in stock_infos:
        html += tr_template % (line_info[0], line_info[1], line_info[2], line_info[3], line_info[4], line_info[5], line_info[6], line_info[0], line_info[0])
    
    content = re.sub(r"\{%content%\}", html, content)

    return content


# 给路由添加正则表达式的原因：在实际开发时，url中往往会带有很多参数，例如/add/000007.html中000007就是参数，
# 如果没有正则的话，那么就需要编写N次@route来进行添加 url对应的函数 到字典中，此时字典中的键值对有N个，浪费空间
# 而采用了正则的话，那么只要编写1次@route就可以完成多个 url例如/add/00007.html /add/000036.html等对应同一个函数，此时字典中的键值对个数会少很多
@route(r"/add/\d+\.html")
def add_focus():
    return "add ok..."


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])

    file_name = env['PATH_INFO']

    """
    if file_name == "/index.html":
        return index()
    if file_name == "/center.html":
        return center()
    else:
        return 'Hello World! 你好！'
    """
    
    try:
        # func = URL_FUNC_DICT[file_name]
        # return func()
        # return URL_FUNC_DICT[file_name]()

        for url, func in URL_FUNC_DICT.items():
            """
            URL_FUNC_DICT = {
                r"/index.html": index,
                r"/center.html": center,
                r"/add/\d+\.html": add_focus
            }
            """
            ret = re.match(url, file_name)
            if ret:
                return func()
        else:
            return "no such url: %s" % file_name

    except Exception as ret:
        return "exception: %s" % str(ret) 

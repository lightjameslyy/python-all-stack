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
def index(ret=None):
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
def center(ret):
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
                <a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
            </td>
            <td>
                <input type="button" value="删除" id="toDel" name="toDel" systemidvalue="%s">
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
@route(r"/add/(\d+)\.html")
def add_focus(ret):

    # 1. get stock code
    stock_code = ret.group(1)

    # 2. check if the stock exist
    conn = connect(host="localhost", port=3306, user="root", password="root", database="stock_db", charset="utf8")
    cs = conn.cursor()
    sql = """select * from info where code=%s;"""
    cs.execute(sql, (stock_code,))
    if not cs.fetchone():
        cs.close()
        conn.close()
        return "no such stock..."

    # 3. check if the stock already focused
    sql = """select * from info as i inner join focus as f on i.id=f.info_id where i.code=%s;"""
    cs.execute(sql, (stock_code,))
    if cs.fetchone():
        cs.close()
        conn.close()
        return "you have already focused the stock..."
    
    # 4. add focus
    sql = """insert into focus (info_id) select id from info where code=%s"""
    cs.execute(sql, (stock_code,))
    conn.commit()
    cs.close()
    conn.close()

    return "关注成功..."


@route(r"/del/(\d+)\.html")
def del_focus(ret):

    # 1. get stock code
    stock_code = ret.group(1)

    # 2. check if the stock exist
    conn = connect(host="localhost", port=3306, user="root", password="root", database="stock_db", charset="utf8")
    cs = conn.cursor()
    sql = """select * from info where code=%s;"""
    cs.execute(sql, (stock_code,))
    if not cs.fetchone():
        cs.close()
        conn.close()
        return "no such stock..."

    # 3. check if the stock already focused
    sql = """select * from info as i inner join focus as f on i.id=f.info_id where i.code=%s;"""
    cs.execute(sql, (stock_code,))
    if not cs.fetchone():
        cs.close()
        conn.close()
        return "you haven't focused the stock..."
    
    # 4. del focus
    # sql = """insert into focus (info_id) select id from info where code=%s;"""
    sql = """delete from focus where info_id = (select id from info where code=%s);"""
    cs.execute(sql, (stock_code,))
    conn.commit()
    cs.close()
    conn.close()

    return "取消关注成功..."

@route(r"/update/(\d+)\.html")
def show_update_page(ret):
    """显示更新被指页面"""
        
    # 1. get stock code
    stock_code = ret.group(1)

    # 2. open template
    with open("./templates/update.html") as f:
        content = f.read()
    
    # 3. get old note info
    conn = connect(host="localhost", port=3306, user="root", password="root", database="stock_db", charset="utf8")
    cs = conn.cursor()
    sql = """select f.note_info from info as i inner join focus as f on i.id=f.info_id where i.code=%s;"""
    cs.execute(sql, (stock_code,))
    stock_infos = cs.fetchone()
    note_info = stock_infos[0]  # get the corresponding note info
    cs.close()
    conn.close()

    content = re.sub(r"\{%note_info%\}", note_info, content)
    content = re.sub(r"\{%code%\}", stock_code, content)

    return content


@route(r"/update/(\d+)/(.*)\.html")
def save_update_page(ret):
    """保存修改的xx"""

    stock_code = ret.group(1)
    comment = ret.group(2)

    conn = connect(host="localhost", port=3306, user="root", password="root", database="stock_db", charset="utf8")
    cs = conn.cursor()
    sql = """update focus set note_info=%s where info_id=(select id from info where code=%s);"""
    cs.execute(sql, (comment, stock_code,))
    conn.commit()
    cs.close()
    conn.close()
    
    return "修改成功"


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
                return func(ret)
        else:
            return "no such url: %s" % file_name

    except Exception as ret:
        return "exception: %s" % str(ret) 

import re


def add(tmp):
    strNum = tmp.group()
    num = int(strNum) + 1
    return str(num)


def main():
    # sub: 先匹配，后替换，然后返回整个字符串
    ret = re.sub(r"\d+", "0", "阅读次数为 9999, c: 3245")
    print(ret)

    # sub还支持函数调用
    ret = re.sub(r"\d+", add, "阅读次数为 9999, c: 3245")
    print(ret)

    job_description = """<dd class="job_bt">
        <h3 class="description">职位描述：</h3>
        <div>
        <p>岗位职责：</p>
<p>1. 负责听云产品Server相关功能研发、改进、Bug修复及其他日常维护</p>
<p>2.&nbsp;编写单元测试用例，并配合测试部门编写及完善数据采集相关自动化测试用例</p>
<p><br></p>
<p>岗位要求：</p>
<p>1. 计算机相关专业，全日制大学本科及以上学历，英语读写良好。</p>
<p>2. 熟知计算机原理，及编程相关知识。</p>
<p>3. 3年及以上python经验，有经常阅读源代码更佳</p>
<p>4. 熟练使用python经典特性，如生成器、闭包、装饰器等，以及monkey-pacth技术。</p>
<p>5. 熟悉python WEB应用部署、开发技术 ，如django、tornado等。</p>
<p>6. 理解HTTP协议、数据库等相关技术，具备良好的代码风格</p>
<p>7. 善于思考，能独立分析和解决问题&nbsp;</p>
<p>8. 责任心强，具备良好的团队合作精神和承受压力的能力</p>
<p><br></p>
<p>加分项：</p>
<p>1. 熟练使用Java者优先</p>
<p>2. 精通HTTP协议</p>
<p>3.&nbsp;精通python解释器原理，以及源代码等</p>
        </div>
    </dd>"""
    ret = re.sub(r"<[^>]*>|&nbsp;| ", "", job_description)
    print(ret)


if __name__ == '__main__':
    main()

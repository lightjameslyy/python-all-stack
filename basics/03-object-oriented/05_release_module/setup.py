from distutils.core import setup

setup(name="lt_message",  # 包名
      version="1.0",  # 版本
      description="terryleo's 发送和接收消息模块",  # 描述信息
      long_description="完整的发送和接收消息模块",  # 完整描述信息
      author="terryleo",  # 作者
      author_email="terryleo@terryleo.com",  # 作者邮箱
      url="www.terryleo.com",  # 主页
      py_modules=["lt_message.send_message",
                  "lt_message.receive_message"])

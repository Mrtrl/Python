import time
import re

g_templates_root = "./templates"

def index(path):
    """首页"""
    path = path.replace(".py", ".html")
    f = open(g_templates_root + path)
    content = f.read()
    f.close()

    html = "<h1>首页数据: 这里是从mysql数据库中读取的动态数据</h1>"
    # 完成数据的替换
    content = re.sub(r"\{%content%\}",html,content)
    return content

def center(path):
    """个人中心"""

    path = path.replace(".py", ".html")
    "/index.py  --> /index.html"
    f = open(g_templates_root + path)
    content = f.read()
    f.close()
    html = "<h1>个人中心数据: 这里是从mysql数据库中读取的动态数据</h1>"
    # 完成数据的替换
    content = re.sub(r"\{%content%\}", html, content)
    return content



# 装饰器 @语法糖 内部是如何实现程序员不需要关心
# 学习装饰器内部是如何试实现 --> 先学习闭包 --> 和函数类似  -- 需要提前预习闭包和装饰器
g_func_path_dict = {
    "/index.py" : index,
    "/center.py": center

}


def app(environ, start_response):
    """
    :param environ: 服务器传递的参数  是字典类型
    :param start_response: 服务器模块中的函数的引用
    :return: 返回body信息
    """
    path = environ["PATH_INFO"]
    print(path, "在框架中被打印++++")
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    # 响应头信息传递给服务器
    start_response(status, response_headers)
    # 将body信息通过返回值传递给服务器
    # 读取对应路径下的模板数据 将模板数据做为body 数据返回给服务器
    # if path == "/index.py":
    #     # 获取index.html这个模板
    #     index(path)
    # if path == "/center.py":
    #     center(path)
    # 如果键不存在返回 None
    func = g_func_path_dict.get(path)
    if func:
        # 返回的了body数据
        return func(path)
    else:
        return "没有对应的路径"

# application
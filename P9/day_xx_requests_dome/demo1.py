# -*- coding: UTF-8 -*-

import requests
import json
from PIL import Image
from io import BytesIO


# 不带参数的get请求
def f1():
    res = requests.get("http://www.baidu.com")
    return res


# reseponse = f1()
# print(reseponse.content.decode("utf-8"))
# print(reseponse.text.encode("utf-8"))

# 带参数的get请求  -- 添加请求头
def f2():
    kw = {"wd": "python"}

    header = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive"
    }

    r2 = requests.get("http://www.baidu.com/s", params=kw, header=header)
    return r2


# reseponse = f2()
# print(reseponse.content.decode("utf-8"))

# 微信公众号--获取token--get请求
def f3():
    data = {'grant_type': 'client_credential', 'appid': 'wxb637f897f0bf1f0d',
            'secret': '501123d2d367b109a5cb9a9011d0f084'}
    response = requests.get("https://api.weixin.qq.com/cgi-bin/token", params=data)
    return response


# re = f3()
# print(re.content.decode("utf-8"))  # 获取响应正文
# # 获取响应信息
# # 响应状态码
# print (re.status_code)
# # 响应的状态信息
# print (re.reason)
# # 响应头
# print (re.headers['Content-Type'])  # 以字典的形式返回
# # 获取请求的地址
# print (re.url)
# # 获取cookies
# print (re.cookies)
# # 获取编码形式
# print (re.encoding)


# dbshop获取登录token
def f4():
    r4 = requests.get("http://192.168.1.9/DBshop/user/login")
    return r4


# print (f4().content)

# dbshop登录
def f5():
    login = {

    }

    r5 = requests.post("http://192.168.1.9/DBshop/user/login", data=login)
    return r5


# print (f5().content.decode("utf-8"))

# 添加微信标签
def f6():
    token = {
        "access_token": "46_Gp3aLz-gsAZm4oaJaQeBTIOqgtktxWpc-RCMP5a1rZsU_6Rj_WXkNNN9ig54AjFT3_3FqdG9qf_0R4fWfuJRf84QIz_cSRyIHeo32n0ntuBobkDX5lbBM7vx5v3o0a-4jjqoswiNDY_PW4WgUFYgAEAPAT"
    }
    tag_name = {"tag": {"name": "csc"}}
    headers = {"Content-Type": "application/json"}
    host = "https://api.weixin.qq.com/cgi-bin/tags/create"
    # r6 = requests.post(host, params=token, data=json.dumps(tag_name))  # json.dumps 把字典转换成json对象
    r6 = requests.post(host, paramas=token, headers=headers, json=tag_name)
    return r6


# print (f6().content.decode("utf-8"))
'''
如果post请求的参数是json类型，则有两种处理方式：
1.先导入json模块，然后把参数定义成字典，然后传参数 ：data = json.dumps(参数名)
2.添加请求头： headers = {"Content-Type": "application/json"} 然后把参数定义成字典，传参数是使用 json = 参数名
'''


def f7():
    # 保存百度图片
    r = requests.get('https://www.baidu.com/img/bd_logo1.png')
    img = Image.open(BytesIO(r.content))
    img.save('baidu1.png')


# f7()

# 响应数据--字节流
def f8():
    r8 = requests.get("https://www.baidu.com", stream=True)
    return r8


# print (f8().raw.read())


# requests 高级操作
# 1.设置代理： 打开代理工具：charles 127.0.0.1：8888
# 2.设置超时时间
def f9():
    proxies = {"http": "http://127.0.0.1:8888", "https": "https://127.0.0.1:8888"}
    r5 = ""
    try:
        r9 = requests.get("http://v3.dbshop.net/shop-user", proxies=proxies, timeout=2)  # 设置的是响应超时
        r5 = requests.get("http://v3.dbshop.net/shop-user", proxies=proxies, timeout=(0.1, 0.200))  # 请求超时--响应超时
    except Exception as e:
        print (e)
    return r5


# print (f9())

# 3.重定向：requests是自动重定向
def f10():
    r10 = requests.get("http://www.360buy.com", allow_redirects=False)  # allow_redirects 关闭重定向
    return r10


# print (f10().content)


# 4.session处理 seesion:处理
def f11():
    s = requests.Session()
    post_data = {
        "name": "luoman876@163.com",
        "password": "luomang1994"
    }
    login_url = "http://www.renren.com/PLogin.do"
    s.post(login_url, params=post_data)
    r11 = s.get("https://www.renren.com/personal/233407190")
    return r11


# print (f11().content.decode("utf-8"))

def f12():
    s = requests.Session()
    post_data = {
        "name": "lishouwu",
        "password": "lishouwu2021.Q"
    }
    login_url = "http://www.xmxblog.com/wp-login.php"
    s.post(login_url, data=post_data)
    r12 = s.get("http://www.xmxblog.com/wp-admin")
    return r12


# print (f12().content.decode("utf-8"))

# 5.cookie session存在服务器 与cookie存在客户端的区别
def f13():
    cookies = {
        "wordpress_ba63aa81206b2c007de8843c1865ccf9": "lishouwu%7C1625974745%7Cyn5zHi40GdCI64ou1Gu16ZJGZc3AIowh7ep18Kel267%7Ce3cccaf0e877b73503749e5c9b135ff8c9017e5bd24df0c48cb68d2d1a6842f9;",
        " Hm_lvt_a32bdb517a74a4b2bc468be27c35d634":"1624765058",
        "Hm_lpvt_a32bdb517a74a4b2bc468be27c35d634":"1624765058",
        " wordpress_test_cookie":"WP+Cookie+check;",
        " wordpress_logged_in_ba63aa81206b2c007de8843c1865ccf9":"lishouwu%7C1625974745%7Cyn5zHi40GdCI64ou1Gu16ZJGZc3AIowh7ep18Kel267%7C25b773cba58bed8fd2a5e3ca46af66a72d35c87ea85ea77512582f81ea479fbd"
    }

    r13 = requests.get("http://www.xmxblog.com/wp-admin",cookies=cookies)
    return  r13
print (f13().content.decode("utf-8"))
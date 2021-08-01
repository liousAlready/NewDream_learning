#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: test_001.py
@time: 2021/6/1 16:27
'''

#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: test_login.py
@time: 2021/6/1 15:07
'''
import ddt
from task.day13.testdata import login_datas as td
from task.day13.PageObject.login_page import LoginPage
from task.day13.testcases.conftest import Conftest
from task.day13.comm.createrbrower import CreaterBrower


class TestLogin(Conftest):

    def test_login_success(self):
        """
        测试正常登录
        :return:
        """
        LoginPage(Conftest).login(*td.user)




    # #@ddt.data("case", *td.invalid_data)
    # def test_login_false(self):
    #     """
    #     测试登录异常
    #     :return:
    #     """
    #     LoginPage(Conftest).login(td.invalid_data["user"], td.invalid_data["password"])

'''
@File : day9_selenium1.py
@Time : 2021/5/12 20:46
@Author: luoman
'''
# import lib
from selenium import webdriver
import os

def createdriver():
    # chromePath = 'D:\\driver\\chromedriver.exe'
    # os.environ[webdriver.chrome.driver] = chromePath  # gecko  ie等
    # driver = webdriver.Chrome(executable_path=chromePath)  # Firefox、Ie等
    #
    #
    driver = webdriver.Chrome()
    driver.get('http://www.xmxbbs.com/')



createdriver()
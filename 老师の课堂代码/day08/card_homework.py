'''
@File : card_作业.py
@Time : 2021/5/9 08:36
@Author: luoman
'''
# import lib
class Card:
    def __init__(self, face, suite):
        self.face = face
        self.suite = suite


    def getFace(self):
        return self.face

    def getSuite(self):
        return  self.suite


    def __str__(self):

        return self.suite + self.face



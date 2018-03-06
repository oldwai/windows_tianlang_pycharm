#coding:utf-8
'''
@author:oldwai
'''

# simple.py

import sys
from PyQt4 import QtCore, QtGui
class MyWindow(QtGui.QWidget):      # 通过继承QtGui.QWidget创建类
    def __init__(self):        # 初始化方法
        QtGui.QWidget.__init__(self)    # 调用父类初始化方法
        self.setWindowTitle('PyQt')     # 设置窗口标题
        self.resize(300,100)      # 设置窗口大小

        label1 = QtGui.QLabel(u'验证码') # 创建标签
        label1.setAlignment(QtCore.Qt.AlignCenter)
        edit1 = QtGui.QLineEdit()     # 创建单行文本框
        Enter_button=QtGui.QPushButton(u"确定")

        gridlayout = QtGui.QGridLayout()   # 创建布局组件
        gridlayout.addWidget(label1, 0, 0 )
        gridlayout.addWidget(edit1, 0, 1)
        gridlayout.addWidget(Enter_button, 0, 2)


        #self.connect(Enter_button,QtCore.SIGNAL()SIGNAL=("clicked()"),self.hs_Enter_button)
        self.setLayout(gridlayout)
    # def hs_Enter_button(self):
    #     QtGui.QMessageBox.information(self,"information",
    #                                           self.tr("提交成功"))
    #     self.lable.setText(u"确定 MessageBox")


app = QtGui.QApplication(sys.argv)     # 创建QApplication对象
mywindow = MyWindow()        # 创建MyWindow对象
mywindow.show()          # 显示窗口
app.exec_()           # 进入消息循环
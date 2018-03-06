# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com


# 此脚本用于测试添加ISLI 目标的数据
import datetime
import time
from uiautomator import device as d


def click(device, location):
    '''
    :param device: 连接的设备
    :param location: 元素位置
    :return:
    '''
    if device(text=location).exists:
        device(text=location).click()


skip_num = 0
s = 0
for i in range(1, 500):
    s = i
    time.sleep(0.5)
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    str1 = str(i) + '---------' + 'auto_add ISLI target ' + str(now_time)
    if d(text="添加").exists:
        print("这是第 %d 次输入内容，输入的值为 %s" % (i, str1))
        d(text="添加").click()
        # 输入框元素位置
        resource_id = "com.mpr.mprepubreader:id/note_content"
        class_name = "android.widget.EditText"
        d(resourceId=resource_id, className=class_name).click()
        d(resourceId=resource_id, className=class_name).set_text(str1)
        real_text = d(resourceId=resource_id, className=class_name).text
        if real_text != str1:
            skip_num += 1
        d(text="保存").click()

print("一共执行了 %d 次 \n输入和输出的结果不一样的次数为 %d 次" % (s, skip_num))

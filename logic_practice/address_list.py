# -*- coding:utf-8 -*-
#全局变量，else语句
#列表退到的*

#address_list  通讯录
print('|---欢迎进入李金龙通讯录程序---|')
print('|---1：查询联系人资料---|')
print('|---2：出入新的联系人---|')
print('|---3：删除已有联系人---|')
print('|---4：退出通讯录程序---|')
data ={'caolh':'0452','xuzj':'0001','lixd':'0002'}
print(data['caolh'])
while 1:
    #instruct = input('请输入相关的指令代码：')
    instruct = input('请输入相关的指令代码：')
    if instruct.isdigit():
        instructs = int(instruct)
        if instructs==1:
            #name = input('请输入联系人姓名：')
            name = input('请输入联系人姓名：')
            if name in data:
                print(name,u'的联系电话是:',data[name])
            else:
                print(u'您输入的内容不存在')
        elif instructs ==2:
            name = input('请输入联系人姓名：')
            if name in data:
                print('您输入的内容已经存在',data[name])
                affirm = input('是否修改用户资料YES/NO：')
                if affirm == 'YES':
                    data[name] = input('请输入用户联系电话：')
                    print(name,'最新联系方式为：',data[name])
                else:
                    print('您已取消修改。',name,'的联系方式是',data[name])
            else:
                data[name] = input('请输入用户联系电话：')
                print(name,'联系电话：',data[name])
        elif instructs==3:
            name = input('请输入联系人姓名：')
            if name in data:
                data.pop(name)
                print('已删除',name,'相关信息')
            else:
                print('您需要删除的人物不存在')
        elif instructs ==4:
           break
    else:
        print('输入错误，请重新输入')
print('|---感谢您使用李金龙通讯录程序---|')
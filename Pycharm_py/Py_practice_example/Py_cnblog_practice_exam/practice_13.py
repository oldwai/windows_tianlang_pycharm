#coding:utf-8
#打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。
def main():
    for i in range(100,1000):
        a= i%10
        b= i/100
        c= (int(i/10))%10
        if i==a**3+b**3+c**3:
            print "%5d"%(i),

if __name__=="__main__":
    main()
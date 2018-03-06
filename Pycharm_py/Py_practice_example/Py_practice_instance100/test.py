list_num=[1,2,3,4]
all_num=[]
for i in list_num:
    for j in list_num:
        for k in list_num :
#            if (i!=j) and (i!=k) and (j!=k):
                num=i*100+j*10+k
                all_num.append(num)
print(all_num)
print('A total of %d numbers.' %len(all_num))
# 在这个文件里编写代码
weight=input("请输入你在地球上的体重")
w=float(weight)
m=float(weight)
for i in range(1,11):
    w+=0.5
    print("第{}年地球上的体重为{:.2f}".format(i,w))
for i in range(1,11):
    m+=0.5
    moonweight=m*0.165
    print("第{}年月球上的体重为{:.2f}".format(i,moonweight))

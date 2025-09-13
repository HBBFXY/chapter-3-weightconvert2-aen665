# 在这个文件里编写代码
weight=float(input("请输入你在地球上的体重"))
for i in range(1,11):
    weight+=0.5
    moonweight=m*0.165
    print(f"第{i}年，地球上的体重为{weight:.2f}kg,月球上的体重为{moonweight:.2f}kg")

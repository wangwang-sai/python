

#1号衣服
id1 = 1
name1 = "A001"
price1 = 180
qulity1 = "A+"
type1 = "风衣"
number1 = 32
#2号衣服
id2 = 2
name2 = "B002"
price2 = 650
qulity2 = "A+"
type2 = "羽绒服"
number2 = 15
#3号衣服
id3 = 3
name3 = "C003"
price3 = 135
qulity3 = "B+"
type3 = "牛仔裤"
number3 = 25
#4号衣服
id4 = 4
name4 = "D004"
price4 = 120
qulity4 = "B+"
type4 = "鞋"
number4 = 14


print("------------------------欢迎来到艾莱依商城------------------------------")
print("编号      衣服名称      价格        品质         类型        销量")
print("--------------------------------------------------------------------")
print(id1 ,"\t\t",name1 ,"\t\t",price1,"\t\t",qulity1,"\t\t",type1,"\t\t",number1)
print(id2 ,"\t\t",name2 ,"\t\t",price2,"\t\t",qulity2,"\t\t",type2,"\t\t",number2)
print(id3 ,"\t\t",name3 ,"\t\t",price3,"\t\t",qulity3,"\t\t",type3,"\t\t",number3)
print(id4 ,"\t\t",name4 ,"\t\t",price4,"\t\t",qulity4,"\t\t",type4,"\t\t",number4)
print("--------------------------------------------------------------------")
print("总金额为：￥",(price1 * number1 + price2 * number2 + price3 * number3 + price4 * number4))



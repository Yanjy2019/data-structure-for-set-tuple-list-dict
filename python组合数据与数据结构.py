#python里面的组合数据类型

#集合的相关操作符
s={1,2,"hello world",1,2,"yanjiangyi"}
print(s)   #可以自动过滤掉相同的元素，没有顺序的概念、
print(len(s))    #输出独一无二元素的个数
print(type(s))     #输出集合的数据类型
s={1,2,3,"yjy","11",123,24}
t={1,3,"yjy",1243}
print(s-t)   #差集
print(s&t)  #交集
print(s^t)  #补集
print(s|t)  #并集
#集合的常用操作函数与方法:先操作再输出
s.add("人工智能")    #增加元素
print(s)
s.remove("yjy")      #删除元素
print(s)
s.clear()            #清空元素
print(s)
print(len(s))       #输出集合的长度
print(1 in s)       #检查元素是否位于s里面
print("yjy" not in s)        #检查元素是否不在s中
#set函数可以定义一个空集合变量
a=set()
print(a)
s="知之为知之不知为不知，是知也!"
print(set(s))          #set函数可以将其他组合数据转变为集合数据类型，清除很过滤相同的部分

#列表类型和相关操作
s=[1,2,3,4,"yjy","甜圈圈","珍珠奶茶",1,2]   #存贮多种数据类型，并且数据之间时独立的，不会过滤相同的元素，是有序号的
print(s)
print(type(s))
print(list("我的人生没有彩排，每天都是现场直播！"))
#列表的操作方法与函数
print(3*s)  #复制列表元素n次，然后拼接起来
t=[1,2,3,4]
print(s+t)     #直接进行多个列表的拼接
print(s.index(2))   #列表元素的第一个索引值输出
print(s[1:5:2])   #列表的切片与索引
print(s.count(2))   #输出；列表中某个元素的个数
s=[1010,"1010",1010,[1,2,3,4],"12"]
print(s)
print(type(s[2]))
print(s[-2])     #列表的索引方式
for i in s:
    print(i)  #遍历循环寻找列表的每一个元素
print(s[0:4:2])
print(s[-5:-1:2])
print(s[1:4])   #列表的常见切片操作
#列表的相关操作
s.append(1)        #append是指在列表的最后位置增加一个元素
print(s)
s.insert(2,"yjy")  #insert是指在列表地i索引位置出增加一个元素x
print(s)
s.pop(2)          #pop方法是指删除列表索引i处的元素
print(s)
s.remove("1010")   #remove是指删除列表中第一次出现的元素x
print(s)
s.reverse()
print(s)           #reverse是指将列表中的元素直接进反转
t=[1,2,3,5,113,67,89,546799]
t.sort()         #sort列表中元素按照从小到大的顺序进行排列分布
print(t)
p=t         #=是将t的地址给p，因此p和t是一致的
p=t.copy()  #copy是指将列表进行复制操作，开辟新的数据，t的变化不会引起p的变化
print(t)
t.clear()         #clear清空列表中的元素
print(t)
print(p)
#元组数据类型和相关操作
s=(1,2,3,4,5,57,6,87,"yjy",[1,2,2,"yjy"])
print(s)
print(type(s))                 #输出类型为元组
print(s.count(1))
print(s.index("yjy"))          #元组是不可以随便修改里面的元素，信息不可修改，具有很很好的保证安全性，不可以修改元组里面的任何元素
print(s[3])                    #元组的元素索引
print(s*2)                     #对元组数据类型进行复制
s=[1,2,3,3,6576,34,"yjy"]
s=tuple(s)   #列表转换为元组，可以进行数据的保护
print(s)
print(tuple("我建议，你走吧"))  #tuple元组函数可以进行数据之间的转换和操作

#字典的组合数据:和集合一样，还没有顺序的，实现的是key-value之间的映射关系
s={"yjy":1234,"青蒿素":"屠呦呦","杂交水稻之父":"袁隆平",1:123}
print(s)
print(s["yjy"])   #字典的键值对应查询，字典的索引方式，只可以通过键值来进行相关的索引
print(s[1])
s[1]="邓稼先"   #进行字典的value值修改
print(s)
t={}             #定义一个空的字典
t[2019]="tsinghua university"   #对于字典进行元素的扩充
print(t)
s={"201801":"勒布朗","201802":"德里克罗斯"}
print(len(s))
print(max(s))
print(min(s))  #输出键的最大最小值
x=dict()
print(x)
#字典的操作方法
print(type(s.keys()))
print(s.keys())      #输出字典的键值，以列表的方式输出
print(s.items())    #输出字典的所有键值对：以元组的形式输出
print(s.values())   #输出字典的所有value值
print(s.get("201801"))   #输出键值对应的value值，如果不存在则将返回后面自己定义的默认值
print(s)
print(s.get("201803"),"不存在该数据")
print(s.popitem())    #输出字典里随机的键值对，随后将其删除
print(s.pop("201801"),"不存在该数据的键值")   #输出键值对应的value值，如果存在将直接删除存在的这对键值对，不存在的话将会返回默认值
print(s)
print("201801" in s)    #只可以判断字典里面是否有键值，不可判断value值
s={"201801":"勒布朗","201802":"德里克罗斯"}
for k in s:
    print("字典里面的键和值分别为：{}和{}".format(k,s.get(k)))
    print(k)     #遍历循环的时候输出的字典的键值


# 早上第一个作业：
name =input('请输入姓名:')
age =input('请输入年龄:')
gender =input('请输入性别:')
print(
'''****************************
姓名：{0}
年龄: {2}
性别: {1}
****************************
'''.format(name,age,gender ) )
# 早上第二个作业：
str1 ='python hello aaa 123123aabb'
print(str1 [0:6])
print( str1.find('o a'))
print( str1.find('he'))
print( str1.find('ab'))
str =str1.replace("python","lemon" )
print(str)
print(str1.index('aaa'))
 # 8月19日下午作业
print("""第一题""")
a=[1,2,'6''summer']
# if i in a:
#
print('i' in a)
print("""第二题""")
dict_1={"class_id":45,'num':20,"ab":1123}
num =int(input("上课人数："))
if num > 5:
    print(num)
elif num < 5 :
    print("上课人数不足5人")
print("""第三题""")

print("""第一种""")
dict_2={"囧囧":['姓名:囧囧','性别:男','年龄:22','城市:湖南'],
        "唐僧":['姓名:唐僧','性别:男','年龄:22','城市:湖南'],
        "旧模样":['姓名:旧模样','性别:女','年龄:22','城市:湖南'],
        "ouyang":['姓名:ouyang','性别:男','年龄:22','城市:湖南'],
        "Nacy":['姓名:Nacy','性别:男','年龄:22','城市:湖南'],
        "土豆江":['姓名:土豆江','性别:男','年龄:22','城市:湖南']}
print(dict_2)
list5 =list(dict_2)
print(list5)
print("""第二种""")
listTD =[]
listTD.append('姓名:囧囧 性别:男 年龄:18 城市:火星')
listTD.append('姓名:唐僧 性别:男 年龄:100000000000000000000000000000000城市:东土大唐')
listTD.append('姓名:旧模样 性别:女 年龄:18 城市:水星')
listTD.append('姓名:ouyang 性别:男 年龄:18 城市:神雕侠侣')
listTD.append('姓名:Nacy 性别:男 年龄:18 城市:黑客帝国')
listTD.append('姓名:土豆江 性别:男 年龄:18 城市:石头城')
print(listTD)






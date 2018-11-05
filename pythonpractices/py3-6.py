
# names=["nana","weiwei","yazheng","yanmei"]
# lon=len(names)
# for i in range(0,lon):
#     #print(names[i])



# pep=['xue','meizhi','junmei','lina']
# bulai='junmei'
# pep.remove('junmei')
# pep.append('yanxia')
# lon=len(pep)
# print(bulai+" will not come, what a pity!")
# print("I found a bigger desk !")
# pep.insert(0,'tingting')
# pep.insert(int(lon/2),'siyao')
# pep.append('wenwen')
# lon2=len(pep)
# for i in range(0,lon2):
#     print("I want to invite ",pep[i].title()," to have dinner today.")
# print("I want to invite ",len(pep)," people to have dinner today.")
#
# print("I could only invite two of them !")
# while len(pep) > 2:
#     p = pep.pop()
#     print("I am sorry that I couldn't invite ",p," to have dinner today.")
# lon3=len(pep)
# for i in range(0,lon3):
#     print("hey you can still come to the dinner " , pep[i].title())
# while pep:
#     del pep[0]
# print(pep)



#3-8、9、10
#
# place=['yunnan','lanzhou','xizang','qinghai','xinjiang','xiamen','taiwan']
# print(place)
# print(sorted(place))
# print(place)
# place.reverse()
# print(place)
# place.reverse()
# print(place)
# place.sort()
# print(place)
# place.sort()
# print(place）




#4-3、4、5、6、7、8、9

# for i in range(1,21):
#     print(i)

# list1=range(1,1000001)
# print(min(list1))
# print(max(list1))
# print(sum(list1))

#
# list1=range(1,20,2)
# for i in list1:
#     print(i)

#
# dig=[]
# for i in range(3,30):
#     if i%3==0:
#        dig.append(i)
#
# for i in dig:
#     print(i)

#
# list1=[dig**3 for dig in range(1,11)]
# print(list1)


#4-10\11\12

# place=['taiwan','riben','xizang','qinghai','shanghai','yunnan']
# print('The first three items are : ',place[0:3])
# print('The items from the middle of the list are : ',place[1:4])
# print('The last three items in the list are : ',place[-3:])
#
# place1=place[:]
# place1.append('qinghai')
# print('I want travel to :')
# for i in place:
#     print(i)
#
# print('my friends want to travel to :')
# for i in place1:
#     print(i)


#4-13

# foods=('baozi','dabing','miantiao','lvhuo','roujiamo')
# for food in foods:
#     print(food)
#
# #foods[2]='mantou'  #错误代码
#
# foods=('zhou','tang','miantiao','lvhuo','roujiamo')
# for food in foods:
#     print(food)


#5-3\4\5\6\7

# alien_color='green'
# if alien_color == 'green':
#     print("you got 5 points!")
# elif alien_color == 'yello':
#     print("you got 10 points!")
# elif alien_color == 'red':
#     print("you got 15 points!")
#
# fruits=['apple','banana','grape']
# if 'apple' in fruits:
#     print('You really like apples !')
# if 'banana' in fruits:
#     print('You really like bananas !')


#5-10\11
# current_users=['mingming','lilei','hongmei','sunshaoping','tianxiaoxia']
# new_users=['Sunshaoping','Tianxiaoxia','fengtang','yuhua','muxin']
#
# for new_user in new_users:
#     if new_user.lower() in current_users:
#         print(new_user,'already used !')
#     else:
#         print(new_user,'is OK !')

#
# num=[1,2,3,4,5,6,7,8,9]
# for i in num:
#     if i == 1:
#         print("1st")
#     elif i == 2:
#         print('2nd')
#     elif i == 3:
#         print('3rd')
#     else:
#         print(i,'th',sep='')


#6-1\2\3
# xue={'name':'xue','age':'29','city':'Tianjin'}
# # print(xue)
# # num={'xue':8,'di':8,'fang':6,'wen':9,'na':5}
# # print("xue's favourite num is",num['xue'],'.\n'
# #     "di's favourite num is", num['di'], '.\n'
# #     "fang's favourite num is", num['fang'], '.\n'
# #     "wen's favourite num is", num['wen'], '.\n'
# #     "na's favourite num is", num['na'], '.\n')



#6-5\6
# rivers={'nile': 'egypt','changjaing':'china','huangnhe':'zhonghua'}
# for key in rivers.keys():
#     print('The', key,'runs through ',rivers[key])
#
# for name in rivers.keys():
#     print(name)
#
# for value in rivers.values():
#     print(value)


# namelist=['mingming','lilei','hongmei','sunshaoping','tianxiaoxia']
# namein={'1':'mingming','2':'lilei'}
# for name in namelist:
#     if name in namein.values():
#         print(name,"thank you !")
#     else:
#         print(name,"please come to join us !")



#6-7\8\9\10
#
# xue={'name':'xue','age':'29','city':'Tianjin'}
# zheng={'name':'zheng','age':'20','city':'xilinhaote'}
# zhi={'name':'zhi','age':'32','city':'Tianjin'}
#
# people=[xue,zheng,zhi]
#
# for pe in people:
#     print(pe)
#
#
# favorite_places={
#     'wang': ['yingguo','meiguo','aodaliya'],
#     'liu': ['hainan','sichuan','shandong'],
# }
#
# for name,places in favorite_places.items():
#     print(name,"'s favourite places are:",sep='')
#     for place in places:
#         print(place)




# cities={
#     'tianjin':{'nation':'zhongguo','renkou':'100','shishi':'dougen'},
#     'beijing':{'nation':'china','renkou':'1000','shishi':'zhuai'},
#     'shanghai':{'nation':'zhongguo','renkou':'10000','shishi':'dese'}
#     }
#
# for city,dics in cities.items():
#     print(city,"is a city that:")
#     nation = dics['nation']
#     renkou = dics['renkou']
#     shishi = dics['shishi']
#     print('nation is :',nation,'renkou is :',renkou,'shishi is :',shishi,'\n')



#7-1、2、3、

car=input('what car do you want to rent ?')
print('Let me see if I can find you a',car)


cus=int(input('how many people are having lunch ?'))
if cus > 8:
    print('please wait !')
else:
    print('you can come in.')


num=int(input('please input a int number :'))
if num % 10 ==0:
    print('yes')
else:
    print('no')



ing="please input what you need to make a pizza :"
ing += "\nif you want to quit , please input 'quit'.\n"

while True:
    a = input(ing)
    if a != 'quit':
        print("we will input ",a,"to your pizza.")
    else:
        break


tip='please input your age:'
tip += "\nif you want to quit , please input '0'.\n"

while True:
    age = int(input(tip))
    if age >0 and age < 3:
        print('free')
    elif age >= 3 and age <= 12:
        print('10 dollars')
    elif age > 12:
        print("15 dollars")
    else:
        break















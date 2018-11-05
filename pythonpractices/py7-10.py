#coding:utf-8

#7-8

# sandwich_orders=['a','b','c','pastrami','pastrami','pastrami','d']
# finished_sandwiches=[]
# print('the pastrami has been sold out .')
# for sandwich in sandwich_orders:
#     if sandwich == 'pastrami':
#         sandwich_orders.remove(sandwich)
#     else:
#         print('I made your '+sandwich+' sandwich')
#         finished_sandwiches.append(sandwich)
# print('all of the sandwiches has been done :')
# for sandwich in finished_sandwiches:
#     print(sandwich)





#7-10
# cities=[]
# active = True
# while active:
#     city=input('If you could visit one place in the world, where would you go?')
#     print(city)
#     if city == 'no':
#         active = False
#     else:
#         cities.append(city)
#
# print(cities)



#8-1、2
# def display_message():
#     print('in this chapter you will learn 函数。')
#
# display_message()



# def favorite_book(title):
#     print('One of my favorite books is '+title)
# favorite_book("moon")


#8-3\4\5

# def make_shirt(size,describe='I love Python'):
#     print('the size of the shirt is :',size,'and the describe is :',describe)
#
# make_shirt('大号')
# make_shirt('中号')
# make_shirt('x','i am beautiful')


# def describe_city(name,nation='China'):
#     print(name,'is in',nation)
#
# describe_city('London','England')
# describe_city('beijing')
# describe_city('newyork','america')



#8-6\7\8\
# def city_country(city,nation):
#     str= city+','+nation
#     return str
#
# print(city_country('shanghai',"china"))
#
#
#
#
# def make_album(singer,album,num=''):
#     if num=='':
#         zh={singer:album}
#     else:
#         zh = {singer:album,'shuliang':num}
#     return zh
# # print(make_album('zhoujielun','yehuimei'))
# # print(make_album('zhangshaohan','yinxingdechibang','8'))
#
# while True:
#     print('please input the name and album of a singer:')
#     print('if you want to quit , please input q .')
#
#     singer=input("singer name :")
#     if singer == 'q':
#         break
#     else:
#         album=input('album name :')
#         if album == 'q':
#             break
#     print(make_album(singer,album))


#8-9\10\11
# magicians=['a','b','tom','goffi']
#
# def show_magicians(magicians):
#     for magician in magicians:
#         print(magician)
#
# def make_great(magicians):
#     for index,magician in enumerate(magicians):
#         magicians[index] = 'the grate '+magician
#     return magicians
#
# rtn=make_great(magicians[:])
# show_magicians(rtn)
# show_magicians(magicians)



#8-12\13\14

# def make_sandwichs(*ingre):
#     print("you should add ",ingre)
#
# make_sandwichs("baicai","shuiguo","xihongshi")
# make_sandwichs("shanzha","lajiao","doufu")




# def build_profile(first, last, **user_info):
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items(): profile[key] = value
#     return profile
#
# user_profile = build_profile('wendy', 'zang', location='beijing',
#                              field='software')
# print(user_profile)


#
# def make_cars(make,size,**others):
#     car = {}
#     car['make'] = make
#     car['size'] = size
#     for k,v in others.items():
#         car[k] = v
#     return car
#
# car = make_cars('s','out',color='blue',pow=True)
# print(car)




#9-1、2、3、4、5
# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print(self.cuisine_type)
#         print(self.restaurant_name)
#
#     def open_restaurant(self):
#         print("it is openning")
#
#     def set_number_served(self,num):
#         self.number_served = num
#
#     def increment_number_served(self,incre):
#         self.number_served += incre
#
#
# re=Restaurant("wendy","china")
# print(re.number_served,'people had dinner here.')
#
# re.set_number_served(9)
# print(re.number_served,'people had dinner here.')
#
# re.increment_number_served(8)
# print(re.number_served,'people had dinner here.')




# re1=Restaurant('hi','baby')
# re1.describe_restaurant()
# print(re.restaurant_name)
# print(re.cuisine_type)
#
# re.describe_restaurant()
# re.open_restaurant()




#
# class User():
#     def __init__(self,first_name,last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.login_attempts = 0
#
#     def describe_user(self):
#         print(self.first_name,self.last_name)
#
#
#     def greet_user(self):
#         print('hi',self.first_name,self.last_name,'.')
#
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#
# u1=User('wendy','zang')
# # u1.describe_user()
# # u1.greet_user()
#
# u1.increment_login_attempts()
# u1.increment_login_attempts()
# u1.increment_login_attempts()
# print(u1.login_attempts)
# u1.reset_login_attempts()
# print(u1.login_attempts)



#9-6\7\8

# class IceCreamStand(Restaurant):
#     def __init__(self,restaurant_name,cuisine_type):
#         super().__init__(restaurant_name,cuisine_type)
#         self.flavors = ['sweet','hot','acid']
#
#     def show_icecream(self):
#         print("this restaurant provides :")
#         for i in self.flavors:
#             print(i)
#
#
# ice = IceCreamStand('a','b')
# ice.show_icecream()






# class Admin(User):
#     def __init__(self,restaurant_name,cuisine_type):
#         super().__init__(restaurant_name,cuisine_type)
#         self.priv = Privileges()
#  #      self.privileges = ['can add post','can delete post','can ban user']
#
#     # def show_privileges(self):
#     #     print('the privileges of an admin are :')
#     #     for privilege in self.privileges:
#     #         print(privilege)
#
#
#
# class Privileges():
#     def __init__(self):
#         self.privileges = ['can add post','can delete post','can ban user']
#
#     def show_privileges(self):
#         print('the privileges of an admin are :')
#         for privilege in self.privileges:
#             print(privilege)
#
#
# ad=Admin('jay','chou')
# ad.priv.show_privileges()


#10-3\4\5
# with open('guest.txt','a') as file_object:
#     tips=input("please input your username:")
#     file_object.write(tips)

#
#
# with open('guest_book.txt','a') as file:
#     active = True
#     while active:
#         guest = input("please input your username:")
#         if guest == 'q':
#             active = False
#         else:
#             file.writelines(guest+'\n')
#             print('hi ',guest)


#10-6、7、8



try:
    a = int(input("please input int number a:"))
    try:
        b = int(input("please input int number b:"))
        print(a + b)
    except ValueError:
        print("b type is wrong!")
except ValueError:
    print("a type is wrong!")












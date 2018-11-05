from employee import Employee

my_em = Employee('xu','xiaoxiao',10000)
money = my_em.money

def give_raise(money):
    user = input("do you want to increase default monye? please input y/n ")
    try:
        if user == 'y':
            money += 5000
        elif user == 'n':
            incre = int(input("please input your number?"))
            money += incre
    except TypeError:
        print("please input the right type!")
    return(money)

#give_raise(money)
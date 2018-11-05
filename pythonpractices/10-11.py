#coding:utf-8

import json

filename = 'number.json'

try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    num = int(input("please input your favourite number:"))
    with open(filename,'w') as f:
        json.dump(num,f)

with open(filename) as f:
    num = json.load(f)
    print("I know your favourite number ! it's",num)


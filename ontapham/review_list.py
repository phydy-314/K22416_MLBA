import random
list =[]
for i in range(10):
    x = random.Random().randint(0,100)
    list.append(x)
print(list)

print(" Giá trị tại phần tử thứ 2 =",list[2])
def Isprime(x):
    count = 0 
    for i in range(1,x+1):
        if x % i == 0 :
            count += 1
    return count == 2

def listprime(list):
    for item in list:
        if Isprime(item):
            print(item, end =' ')
print('Các số nguyên tố trong danh sách')
listprime(list)
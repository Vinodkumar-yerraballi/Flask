is_rain=True
is_cold=True
if is_rain and is_cold:
    print("Bring umbrella and jacket")
elif is_rain and not(is_cold):
    print("Bring umbrella")
elif not(is_rain) and is_cold:
    print("Bring jacket")
else:
    print("don't take umbrella")

mode = input('Enter math operation(+,-,*,/) or f for Celsius to Fahrenheit conversion: ')
num1 = float(input('Enter first number: '))
if mode.lower() == 'f':
    print(f'{num1} Celsius is equivalent to {(num1*9/5)+32 } fahrenheit')
else:
    num2 = float(input('Enter second number: '))

    if mode == '+':
        print(f'Answer is: {num1 + num2}')
    elif mode == '-':
        print(f'Answer is: {num1 - num2}')
    elif mode == '*':
        print(f'Answer is: {num1 * num2}')
    elif mode == '/':
        print(f'Answer is: {num1 / num2}')
    else:
        print('Input error!') 

string='Vinod'
print(string[::-1])
sentence="Hello good morning"
print(sentence[2:len(sentence)-2])

list_a=['Apple','Banna','Cat','Dog','elephant']
# for i in list_a:
print(list_a[2:len(list_a)-2])
list_b=[1,4,7,9,1,1,3]
empty_list=[]
for i in list_b:
    if i not in empty_list:
        empty_list.append(i)
print(empty_list)
sentence="Welcome to the home"
print(sentence.split()[::-1])
print(sentence.translate({190:110}))
a="1"
b="2"
print(a+b)
print("Hello" + " "+"World")
username="Vinod Kumar"
print("Hello "+ username)
c="@"*5
print(c)
s="Vinod"
result=("* " * 3)+ s + (" *" *3)
print(result)
list_a=[1,2,4,5,6]
for i in range(1,len(list_a)):
    for j in range(1,len(list_a)-1):
        print(list_a[j])
usernames_length=input()
length=len(usernames_length)
print(length)
# word = input()
# length = len(word)
# index = word[-1]
# print(index)

print(input()[-1])
print(len(input())-1)
#Remove the last two element in the given string
print(len(input())-2)
# The output should be Q****
word=input()
print(word[0]+"*"*(len(word)-1))
#divided the length of the string divided by 2
print(len(input())/2)
a = [print("* *") for row in range(3)]
for i in range(3):
    print("* *")
for i in range(3):
    print("* * *")
for i in range(1,4):
    print("* "*i)
w = input()
print("*"*len(w)+ " "+w +" "+ "*"*len(w))
w2 = input()
print(len(w2)-1)
w1 = input()
w2 = input()
print(w2)
print("###")
print(w1)
w =input()
print(w[0])
print(w[-1])
a= input()
b = input()
c = input()
print(a[:1]+b[:1]+c[:1])
mes='Hi VinodKumar'
print(mes[3:len(mes)-0])
#Print the after the first three letters
print(mes[3:])
#print the first three letters
print(mes[:3])
print(mes[:])
vari=len(mes)-1
for i in range(1,5):
    for j in range(1,5-1):
           print("*"*j)
a="5"
print(int(a))
print(type(a))
a=int(a)
print(type(a))
a=input()
a=int(a)
b=input()
b=int(b)
result=a+b
print("Sum:",str(result))
a= int(input())
b = int(input())
print(a/b)
length_of_traingle=int(input())
breath_of_traingle=int(input())
result=length_of_traingle*breath_of_traingle
print(result)
length=int(input())
breadth=int(input())
result=2*(length+breadth)
print(result)
a=int(input())
b=int(input())
print(int(a/b))
a=float(input())
b=float(input())
print(a-b)
a=int(input())
print(100-a)
a=float(input())
b=float(input())
result=a+b
print("Sum:",format(result))
# Kilometers
a=float(input())
b=a*1000
print(int(b))
# Percentage
a=int(input())
result=(a/100)*200
print(result)
# Remainder
a=int(input())
b=int(input())
print(a%b)

a=input()
result=int(a[0])+int(a[1])+int(a[2])
print(result)

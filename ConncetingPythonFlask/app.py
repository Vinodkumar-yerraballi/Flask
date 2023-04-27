print('Welcome to Python 101 on Scrimba')
name="Vinod"
print(f'Hi {name} you\'re welcome')
age=input("Enter you're age")
print(f'Hi {name} you\'re age is {age}')
# Variable concept
falied_subject='6'
name='john'
print(name + ' is falied in '+falied_subject + 'subjects.')
print(name + ' is attemeting ' + falied_subject + 'but he fails')
name='Roy'
print(name + ' is good at the mathematics')
store="Pickel foods"
price=45
is_invetory=True
print(store,price,is_invetory)
a=6
b=2
print("Addition", a+b)
print("subtraction", a-b)
print("multplication", a*b)
print("division", a/b)
print("division(float)", a//b)
print("modulus", a%b)
print("squre", a**b)

message="welcome to python programming"
print(message)
print(message.upper())
print(message.lower())
print(message.title())
print(message.capitalize())
print(len(message))
print(message.count('o'))
print(message[-1])
#starting and ending
print(message[:7])
print(message[2:20])

msg='welcome to Python 101: Strings'
msg1=msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]  
print(msg1.title())
print(msg1[::-1].title())
print(msg.find('P'))
print(msg.replace('Python','Java'))
print('Python' in msg)
color='red'
msg1='[' + name+ '] love this' + color.lower()+'!'
print(msg1)
name='John'
msg2= f'[{name}] loves the color {color.lower()}!'
print(msg2)

name = input('Enter your name: ')
distance_km = input('Enter distance in km: ')
distance_mi = float(distance_km)/1.609
print(f'Hi {name.title()}! {distance_km}km is equivalent to {distance_mi} miles.')

friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
print(friends)
friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)
friends.reverse()
print(friends)
print(max(cars))
print(sum(cars))
friends.append('Terry')
friends.insert(1,'Tom')
friends[2]='william'
#combine the two list
friends.extend(cars)
#remove
friends.remove('Jonn')
friends.pop(-1)
print(friends)
friends.clear()
del friends[2]
#fist method
new_friends1=friends[:]
#second method
new_friends2=friends.copy()
new_friends = list(friends)
print(friends)
print(new_friends)

sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
new_day = input('Enter #of lemonades for new day: ')
sales_w2.append(int(new_day))
sales.extend(sales_w1)
sales.extend(sales_w2)
sales = sales_w1 + sales_w2
sales.sort()
worst_day_prof = sales[0] * 1.5
best_day_prof = sales[-1] * 1.5
print(f'Worst day profit:$ {worst_day_prof}')
print(f'Best day profit:$ {best_day_prof}')
print(f'Combined profit:$ {worst_day_prof + best_day_prof}')
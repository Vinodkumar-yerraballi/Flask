def greeting(name,age):
    # return f'Hello {name} how are you!'
    print(f'Hello {name} you age is {age}!')

greeting('vinod',"22")


def greeting(name, age=28, color = 'red'):
    #Greets user with 'name' from 'input box' and 'age' next year, if available, default age is used
    # also includes favorite color
    print('Hello '  +  name.capitalize() + ', you will be ' + str(age+1) +' next birthday!')
    print(f'Hello {name.capitalize()}, you will be {age+1} next birthday!')
    print(f'We hear you like the color {color.lower()}!')

name = input('Enter your name: ')
age = input('Enter your age: ')
color = input('Enter favorite color: ')
greeting(name, int(age), color)

def tax_calculation(amount):
    tax=amount*0.25
    amount=tax*1.05
    return amount
amount=tax_calculation(100)
print("The tax amount ",amount)
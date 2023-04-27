friends_list='Welcome  to  Python  101: Split  and Join'
print(friends_list.split())
print(friends_list.split(' '),type(friends_list.split(' ')))
friends=['Eric','John','Michael','Terry','Graham']
print('-'.join(friends))
print(','.join(friends))
print(''.join(friends_list.split()))
print(friends_list.replace(' ',''))
csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list_test=(','.join(','.join(csv.split(';')).split(':')).split(','))
print(friends_list_test)
print('replace',csv.replace(':',',').replace(';',',').split(','))
friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']

print('Eric' in friends and 'John' in friends)
print(friends.union(my_friends))
print(friends.intersection(my_friends))
print(friends | my_friends)
print(friends & my_friends)
print(friends.difference(my_friends))
print('symetric',friends.symmetric_difference(my_friends))
print(friends ^ my_friends)
print(friends - my_friends)
cars_duplicate=set(cars)
print(cars_duplicate)
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

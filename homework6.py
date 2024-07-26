my_dict = {'Anna': 1956, 'Vladimir': 2001, 'Kirill': 1989, 'Svetlana': 2014, 'Andrey': 1929}
print('Dict: ', my_dict)
print('Existing value: ', my_dict['Vladimir'])
print('Not existing value: ', my_dict.get('Valeriy'))
my_dict.update({'Georgiy': 1999, 'Aynura': 1975})
print('Deleted value: ', my_dict.pop('Anna'))
print('Modified dictionary: ', my_dict)
print('--------------------------------------------------------------------------------------')
my_set = {1, 1, 1, 2.5, 2.5, 'Hello', 'Hello'}
print(my_set)
my_set.add(8)
my_set.add('Bye')
my_set.discard(1)
print(my_set)


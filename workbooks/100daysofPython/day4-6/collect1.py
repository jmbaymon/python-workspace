from collections import defaultdict,namedtuple,Counter,deque
import csv
import random
from urllib.request import urlretrieve

# normal tuple
user = ('bob', 'coder')
print('Tuple')
print(f'{user[0]} is a {user[1]}')


# Named tuple
User = namedtuple('User', 'name role')

user = User(name='bob', role='coder')

print(user.name)
print(user.role)
print('Named Tuple')
print(f'{user.name} is a {user.role}')




from collections import Counter, defaultdict, OrderedDict

li = [1,2,3,4,5,6,7,7]

print(Counter(li))

dictionary = defaultdict(lambda: 'Does not exist', {'a': 1, 'b': 2})
print(dictionary['c'])
print(dictionary['b'])

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

print(d2 == d)

import datetime

print(datetime.date.today())

from array import array 

arr = array('i', [1,2,3])

print(arr[0])
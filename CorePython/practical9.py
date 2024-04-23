# use lambda expression and the filter() function to filter out words form  alist that don't start with the letter 's'

a = ['soup', 'dog', 'salad', 'cat', 'great']
a = list(filter(lambda x: 's' in x, a))
print(a)
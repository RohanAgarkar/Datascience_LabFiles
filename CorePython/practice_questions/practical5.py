a = input('number>>> ')
b = int(a)
c = list(a)
c = list(map(int, c))
sum = 0
for i in c:
  sum += i ** len(c)

if sum == b:
  print('it is an armstrong number')
else:
  print('it is not an armstrong number')
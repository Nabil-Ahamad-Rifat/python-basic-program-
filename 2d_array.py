
l=[
  [0 for j in range(5)]
  for i in range(5)
]
for i in range(5):
  for j in range(5):
    print(f'{i}{j}',end=' ')
    p=int (input(f'{i}{j}:'))
    l[i][j]=p
  print('\n')
# print(l);
for i in range(5):
  for j in range(5):
    print(f'{i}{j}: {l[i][j]}',end=' ')
  print('\n')
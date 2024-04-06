import time 
print('this time is ')
'''
houre ---> %H
Minit ---> %M
secend---->%S
month/day/year ---->%D
only day---->%d
only month---->%m
only year ---->%y
'''
timein= time.strftime('%H:%M:%S')
print(timein)
date= time.strftime('%D ')
print(date)
month= time.strftime('%m ')
print(month);
year = time.strftime('%Y')
print(year)
year = time.strftime('%d')
print(year)
h = int( time.strftime('%H'));
print(h)
if h >=1 and h<12 :
  print('good morning')
elif h>=12 and h<19 :
  print('good after non')
else :
  print('good night ')
print(t)
#you can build this many way so i this this you know mendetory for  time factor 
# thank you 
letter = "hey i am {0} ,i am from {1}"
name = 'Nabil Ahmad Rifat '
country ='bangladesh'
print(letter.format(name ,country))

# write it another wey
print(f' hy ,i am {name},i am form {country}')

'''
use this floating poing or reduce in after decemel point number 
number.2f ---> it take only 2 decemal point after point 

'''

text = 'for only {price:.2f} dolar this work '
print(text.format(price= 23.99087))
# it can also write this way 
price= 23.99087
text = f'for only {price:.2f} dolar this work '
print(text)



# this is pythone 3 come so it work like normal calculation you can do like this 
print(f'{20*30}')
print(type(f'{20*30}'))




#  if you wnat to need kallibridge then what you do  for this you need to know this ok
print(f'nameis what {name} this are represent the namme variable if you need this then you need to run this {{name}}ok i this you undersent ')

country =('bangladesh','india','pakistan','feland','torki')
'''
here tuple to list convertion use only list (tuple variable name)
tuple---->list ==list( tuple variable)
here list  to tuple  convertion use only tuple(list variable name)
list---->tuple ==tuple( list variable)

'''
temp=list(country)
print(temp)
temp.append('fenlend')
temp.pop()
temp[2]='Russia'


tu= tuple(temp);
print(country)
print(tu)
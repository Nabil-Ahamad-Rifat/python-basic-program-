   
# def my_function():
#     '''Demonstrates triple double quotes
#     docstrings and does nothing really.'''
  
#     return None
 
# print("Using __doc__:")
# print(my_function.__doc__)
 
# print("Using help:")
# # help(my_function)
# print(my_function.__doc__);
# def nabil ():
#   '''hello this is fucking comment do not take it wisdfthout secr'
#   'hello this is fucking comment do not take it witsdfefahout secr
#   'hello this is fucking comment do not take it wisdfthout secr'''
# #   hello how are you is is not print able i this 
# print(nabil.__doc__)
import inspect

def nabil():
    '''hello this is fucking comment do not take it wisdfthout secr'
    'hello this is fucking comment do not take it witsdfefahout secr
    'hello this is fucking comment do not take it wisdfthout secr'''
    #   hello how are you is is not print able i this 

# Accessing source code of the function
source_code = inspect.getsource(nabil)

# Splitting the source code by newlines and filtering for commented lines
commented_lines = [line.strip()[2:] for line in source_code.split('\n') if line.strip().startswith('#')]

# Printing the desired commented line
print(commented_lines[-1]) 
'''import re
str="wlecome to all"
x=re.search("all",str)
print(x)
'''
#split
'''
import re
str="apt bangalore to welcome "
x=re.split(" ",str,3)
print(x)
'''
'''
#subtitu
import re
str="aptech bangalore to welcome  alam"
x=re.sub("a","A",str,2)
print(x)
'''
'''
import re
str="aptech bangalore to welcome  alam"
x=re.findall("^aptech",str)
print(x)
'''
'''
import re
str="aptech bangalore to welcome  alam"
x=re.findall("^ap...",str) # .add the next one char,..add tjhe next 2 char)
print(x)
'''
'''
import re
str="aptech bangalore to welcome  alam"
x=re.findall("^ap$",str) #empte
print(x)
'''
'''
import re
str="example for meta character in regular expression "
x=re.findall("e+",str) #
print(x)
'''
'''
import re
str="friend in need is a friend in deed"
x=re.findall("fr{1}",str) 
print(x)
'''
'''
#dot. diffrence bet \W and \s,\w and \S  [Both te same]
#use the this method \d[0-9],\D[all chr and with spece ],\w[only chr],\W[only spece],
#\s,\S 
import re
str="123friend in need 4557is a friend in deed"
x=re.findall("\w",str) 
print(x)
'''

'''
import re
str="123friend in need is a friend in deed"
x=re.findall("\D",str) 
print(x)
'''

import re
def text_match(text):
    patterns='a..*b$'
    if re.search(patterns,text):
        return 'found a match'
    else:
        return('not match')
print(text_match("5ac"))
print(text_match("abb"))

import re

def check_mobile_number(string):
  
    pattern = re.compile(r'^9\d{9}$')
    return bool(pattern.match(string))
def check_email(string):
 
    pattern = re.compile('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{4,}$')
    return bool(pattern.match(string))

# Test the functions
print(check_mobile_number('9123456789'))  # true
print(check_mobile_number('6123456789'))  #  false

print(check_email('example@example.coms'))  # 
print(check_email('example@.com'))
'''str= input("enter any string")
vowel=['a','e','i,','o','u']
contvowel=0
constconst=0







'''

string=input("Enetr a string:-")
lcount=dcount=special=''
for c in string:
    if c.isdigit():

        dcount+=c
    elif c.isalpha():
        lcount+=c

    else:
        special+=c
print("no of letter:",lcount)
print("no of digits:",dcount)
print("no of special:",special)
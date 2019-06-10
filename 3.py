dict = { 'black' :'r', 
  'hero':'e', 
  'go':'g', 
  'clue':'i',
  'mean':'q',
  'groan':'o',
  'sin':'p',
  'pint':'u',
  'tone':'n',
  'graze':'s',
  'sea':'t',
  'plant':'a'}
print(dict)

def compare(string):
    count = 0
    for i in range(len(string)):
        if string[i] in values:
            count+=1
    if(count == len(string)):
        return string

keys = []
values = []
for i in dict:
    keys.append(i)
    values.append(dict[i])
print(keys)
print(values)
temp =[]
for i in keys:
    temp.append(compare(i))


count1 = 0
for i in range(len(temp)):
    if(temp[i] == None):
        count1+=1
for i in range(count1):
    temp.remove(None)

print("Final list:",temp)


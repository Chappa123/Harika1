lot = [(1,2,3),(4,5),(7,8),(1,2,3),(4,5),("abc","xyz"),("abc","def"),("abc","xyz")]
dict = {}
for i in lot:
    dict[i] = dict.get(i, 0) +1
print(dict)
for j in dict:
    print("Number of",j ,"tuples:", dict[j])    


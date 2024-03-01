import random

dic ={}
with open('testmincut.txt' , 'rt') as f:
       x = f.readlines()
numb = []
for i in x:
       numb.append( i.split() )

for i in range (200):
       numb[i].pop(0)
       dic[int(i+1)] = [int(j) for j in numb[i]]
firstnode = 2
while len(dic) > 2:
       secondenode = dic[firstnode][0]
       dic[secondenode].extend(dic[firstnode])
       dic.pop(firstnode)

       for i in dic.values():
              for j in range(len(i)):
                     if i[j] == firstnode:
                            i[j]=secondenode

       for k in list(dic[secondenode]):
              if k == secondenode or k == firstnode :
                     dic[secondenode].remove(k)

       firstnode = random.randint(1,200)
       while not (firstnode in dic):
              firstnode = random.randint(1, 200)


print(len( list(dic.values())[0]))
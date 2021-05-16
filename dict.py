#Dict
#dict construktor

nameAge = [("anna",34),("bob",48)]
d = dict(nameAge)
print(nameAge) #[('anna', 34), ('bob', 48)]
print(d) #{'anna': 34, 'bob': 48}

phonetci = dict(a="alfa", b="bravo", c="charlie")
print(phonetci) #{'a': 'alfa', 'b': 'bravo', 'c': 'charlie'}

d = dict(a=3,b=4,f=5)
f=dict(d) # för att få en copy
print(d)
print(f)
f.update(d)
print(f) #om samma key uppdateras värdet
r = dict(t=3,y=4,u=5)
f.update(r)
print(f)#{'a': 3, 'b': 4, 'f': 5, 't': 3, 'y': 4, 'u': 5}

for key in f:
    print(f"{key} => {f[key]}")
#a => 3
#b => 4
#f => 5
#t => 3
#y => 4
#u => 5

#eller
for value in f.values():
    print(value) #vilket bara blir siffrorna



#each pair called item
# dict.items()
#smidigast!!!
for key, value in f.items():
    print(f"{key} => {value}")


print('y' in f) #True

from pprint import pprint as pp
print(f)
pp(f)






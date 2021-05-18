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




#Set
p = {6,35,65,78}
print(type(p))

d = {} #blir ju en tom dict
#så
e = set()
print(e)
s = set([2,4,16,64])
print(s)
t = [1,3,3,3,5,7,8,8]
tt = set(t) #tar bort dubletter
print(t)
print(tt)

tt.add(999)
print(tt) #{1, 3, 5, 7, 8, 999}

tt.update([1,2,3,4])
print(tt) #{1, 2, 3, 4, 5, 7, 8, 999} Oftast inte i ordning!!
#kolla med "2 in tt" eller "2 not in tt"
tt.remove(1) #måste finnas annars error
tt.discard(88)# behöver inte finnas

j = tt.copy() #shallow copy (not objects)

m = set(tt)

# Sets kan jämföras för att se subset, mm
#typ ett set med blonda och ett med blåa ögon
#blue_eyes.union(blond_hair)
#blue_eyes.intersection(blond_hair)
#blue_eyes.difference(blond_hair)
#symetric_difference
#issubset
#issuperset
#isdisjoint






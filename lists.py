#Listor
enLista=[1,2,3,4,5,6,7]
print(enLista[-1]) #ger 7

#slicing
#a_list[start:stop]

t = enLista
print(t is enLista) #True
r = enLista[:]
print(r is enLista) #False
print(r == enLista) #True
# men ovan är "shallow list"
#dvs listan är en kopia men inte objekten den innehåller
a = [[1,2],[3,4]]
b = a[:]
print(a is b) #False
print(a == b) #True
print(a[0] is b[0]) #True alltså samma objekt!!!!!!!

#Ovanligt med riktiga kopior, men kolla copy-modulen


w = "the quick brown fox jumps over the lazy dog".split()
i = w.index('fox')
print(i)
n = w.count('the')
print(n)

#ta bort
del w[2]
print(w) #['the', 'quick', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

w.remove('quick')
print(w) #['the', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']


w.insert(2,'hej')
print(w)#['the', 'fox', 'hej', 'jumps', 'over', 'the', 'lazy', 'dog']

print(' '.join(w))

w.extend(['1','2','3'])
print(w) #['the', 'fox', 'hej', 'jumps', 'over', 'the', 'lazy', 'dog', '1', '2', '3']

#reverse an sort
w.reverse()
print(w) #['3', '2', '1', 'dog', 'lazy', 'the', 'over', 'jumps', 'hej', 'fox', 'the']
w.sort()
print(w) #['1', '2', '3', 'dog', 'fox', 'hej', 'jumps', 'lazy', 'over', 'the', 'the']

# Key parameter to list.sort

o = 'inte en så lång mening som jag ska splitta'.split()
o.sort(key=len)
print(o) #['en', 'så', 'som', 'jag', 'ska', 'inte', 'lång', 'mening', 'splitta']
print(' '.join(o)) #en så som jag ska inte lång mening splitta

q = [4,9,2,1]
b = sorted(q)
print(b) #[1, 2, 4, 9]
print(q) #[4, 9, 2, 1]

p = [9,3,1,0]
e = reversed(p)
print(e) #<list_reverseiterator object at 0x104f32550>
print(list(e))#[0, 1, 3, 9] men ändrar inte e

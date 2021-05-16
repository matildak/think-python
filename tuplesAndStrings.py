#BuiltInCollections

#Tuple
t=("Norway",3,535,3)
print(t[0])
print("längden på t",len(t))

for item in t:
    print(item)

#nested tuple
a=((1,2),(3,4),(5,6))
print(a[1][1])

p=(1,2,3,4,5,6)
print(type(p))

def minmax(items):
    return min(items), max(items)

mm = minmax([2,3,4,5,6,7,7,8])
print("minmax-result",mm)
print("minmax-result-type",type(mm))

#swop
a = "jelly"
b = "bean"
a,b = b,a

print(a)
print(b)

#tuple constructor (skapa tuple från lista):
x = tuple([1,2,3,4,5,6,7,8])
print(x)
print(type(x)) #tuple

if 5 in x:
    print("yes")

if 5 not in x:
    print("no")

#String
#lägg ihop och separera med ;
colors = ';'.join(['#45ff23','#2321fa','#1298a3'])
print(colors)
print(colors.split(';'))
#->  #45ff23;#2321fa;#1298a3
#->  ['#45ff23', '#2321fa', '#1298a3']

#To concatenate 
#invoke join on empty text
#Something from nothing
#ie use empty string as separator:
y=''.join(['high','way','man'])
print(y)


#partition:
z = "unforgetable".partition('forget')
print(z) #('un', 'forget', 'able')

departure, separator, arrival = "London:Edinburgh".partition(':')
print(departure)
print(arrival)
#underscore for dummy value not used
origin, _, destination = "Oslo-Stockholm".partition('-')
print(origin)
print(destination)


#String Formatting
"{0} north {1} east".format(59.7,10.4)
#replacement fields         format arguments
import math
print("Math constants: pi={m.pi}, e={m.e}".format(m=math))
#Math constants: pi=3.141592653589793, e=2.718281828459045

#f-string för att slippa skriva så många nycklar (PEP 498)
#Evaluated and inserted at runtime
print(f"one plus one is {1 + 1}")

value = 4 * 20
print(f'the value is {value}')
import datetime
print(f'The current time is {datetime.datetime.now().isoformat()}')

# Eller mattegrejen ovan:
print(f'MathCon: pi={math.pi}')
print(f'MathCon: pi={math.pi:.3f}')
#MathCon: pi=3.141592653589793
#MathCon: pi=3.142


help(str)

#Range
#Skapa lista
listan=list(range(5,10))
listan2=list(range(5,10,2))
print("listan: ",listan) #listan:  [5, 6, 7, 8, 9]
print("listan2: ",listan2) #listan2:  [5, 7, 9]

for p in enumerate(listan):
    print(p)

#Snyggare med packa upp med f-string
for i, v in enumerate(listan):
    print(f'i = {i}, v = {v}')

    

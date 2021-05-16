
#Argument passing

#No copy is made!!
m = [9,15,24]
def modify(k):
    k.append(39)
    print("k =", k)

modify(m)
print("m =", m)

#pekar om till ny lista direkt i def
f = [1,2,3]
def replace(g):
    g = [4,5,6] # pekas om här
    print("g =", g)

replace(f)
print("f =", f)

#Default Argument values
def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


print(banner("Matildas kod"))
print(banner("Matildas kod","*"))
#mer lättläslig kod
print(banner("Matildas kod", border="*"))


#Visar att def körs bara en gång vid inläsningen.
#make delay
import time
print(time.ctime())
time.sleep(3)
def show_default(arg=time.ctime()):
    print("def-tid: ",arg)
print(show_default())
time.sleep(3)
print(show_default())
print(time.ctime())







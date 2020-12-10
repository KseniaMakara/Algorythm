# Для даного двовимірного масиву розмірності nxm знайти середнє арифметичне найбільшого і
# найменшого значень його елементів. Замінити цим значенням всі елементи заданого рядка.
import random
n=int(input('Enter n = '))
m=int(input('Enter m = '))
a = [[random.randint(-100,100) for j in range(n)] for i in range(m)]
def print_matrix(a):
    for el in a:
        print(el)
print_matrix(a)
c=[]
for i in range(m):
    c.extend(a[i])
p = (max(c)+min(c))/2
k=int(input( 'enter k = '))
a[k] = [ p for i in range(n) ]
print(a)
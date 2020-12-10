#Написати програму, що підраховує кількість цифр у введеному цілому числі n
n=int(input('Enter n = '))
i=0
k=abs(n)
if k==0:
    print('The figure of numbers in n is 1')
else:
    while k>0:
        k//=10
        i+=1
    print('The figure of numbers in n is {0}'.format(i))
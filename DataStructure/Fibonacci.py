#时间复杂度为O(n)的斐波那契数列，非递归

import time

def Fib_2(n):
    if n == 1 or n == 0:
        return 1
    else:
        a, b = 1, 1
        for i in range(1, n+1):
            a, b = b, a + b
        return a

start = time.clock()
Fib = Fib_2(30)
end = time.clock()

print('%s' %(end-start))
print(Fib)



#时间复杂度为O(2^n)的斐波那契数列，递归

import time

def Fib_1(n):
    if n == 1 or n == 0:
        return 1
    else:
        return(Fib_1(n-1)+Fib_1(n-2))

start = time.clock()
Fib = Fib_1(30)
end = time.clock()

print('%s' %(end-start))
print(Fib)

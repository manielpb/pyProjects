# raw programming
n = int(input("Enter n (remember n is the last element you want to end your fib sequence numbers): "))

# initialize the first two variables ie a and b
a = 0
b = 1
# get their addition
c = a + b
# print em out, this logically prints out the first 3 elements in the fibonacci ie 0,1,1
print(a)
print(b)
print(c)

# a,b,c changes to accommodate this idea of fib sequence
for i in range(0, n - 3):
    a = b
    b = c
    c = a + b
    print(c)

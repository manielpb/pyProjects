# take input from user
x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))

if x % 3 == 0 and y % 3 == 0 and z % 3 == 0:
    odd = max(x, y, z)
    print(odd)
elif x % 3 != 0 and y % 3 == 0 and z % 3 == 0:
    odd = max(y, z)
    print(odd)
elif x % 3 == 0 and y % 3 != 0 and z % 3 == 0:
    odd = max(x, z)
    print(odd)
elif x % 3 == 0 and y % 3 == 0 and z % 3 != 0:
    odd = max(x, y)
    print(odd)
else:
    print("none of em mfs is odd")

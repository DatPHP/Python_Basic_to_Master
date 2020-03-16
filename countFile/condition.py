a = 333
b = 200
if a < b:
    print("Yes. A less than b ")
elif a > b:
    print("yes. a better than b")
else:
    print("yes. a and b are equal.")
# short hand if ... else

if a > b: print("A is better than B ")
c = 100
d = 150
print("c is better d") if a > d else print("c is less than d")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 200
b = 33
c = 500
# and
if a > b and c > a:
    print("Both conditions are True")
# or
if a > b or a > c:
    print("At least one of the conditions is True")

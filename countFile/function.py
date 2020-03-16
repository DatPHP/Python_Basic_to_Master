def printme(str):
    "This prints a passed string into this function"
    print(str)
    return


printme("I'm first call to user defined function!")
printme("Again second call to the same function")


### add value

# Function definition is here
def changeme(mylist):
    "This changes a passed list into this function"
    mylist.append([1, 2, 3, 4]);
    mylist.append("Dat");
    print("Values inside the function: ", mylist)
    return


# Now you can call changeme function
mylist = [10, 20, 30];
changeme(mylist);
print("Values outside the function: ", mylist)
''' 
There is one more example where argument is being passed by
 reference and the reference is being overwritten
  inside the called function.
  '''
# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print ("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme(mylist);
print("Values outside the function: ", mylist)
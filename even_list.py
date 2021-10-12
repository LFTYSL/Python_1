def collectlist(mylist):
    for a in list:
        if (int(a) % 2 == 0):
            print(a)

mylist = input("Enter a list element seperated by space: ")
list = mylist.split()
try:
    collectlist(mylist)
except ValueError:
    print("input an integer value")

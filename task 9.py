#Task 1: Create a Dictionary of Student Marks

Dictionary={"mohit":"85"}
name=input("enter the name:")
if name in Dictionary:
    print("{}'s marks are: {}".format(name, Dictionary[name]))
else:
    print("Student not found")    


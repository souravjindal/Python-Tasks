#Task 1: Read a File and Handle Errors 

try:
    file=open('sample.txt','r')
    read_file=file.read()
    print(read_file)
    file.close
except:
    print("The file sample.txt was not found")    


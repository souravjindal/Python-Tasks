#Task 2: Write and Append Data to a File

user=input("Enter text to write to the file : ")
file=open('output.txt','r+')
input_file=file.write(user)
file.close

print("Data successfully written to output.txt")

file=open('output.txt','a')
append_file=file.write("learning file handling in python")
file.close

print("Data successfully appended")

file=open('output.txt','r+')
read_file=file.read()
print(read_file)
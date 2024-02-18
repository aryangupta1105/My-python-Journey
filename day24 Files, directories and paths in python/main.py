file2 = open("my_file.txt") 
contents = file2.read()
print(contents + " : old file")

with open("new_file.txt", mode='w') as file:
    file.write("New file.")

# Reopen the file or seek to the beginning before reading
with open("new_file.txt", mode='r') as file2:
    content2 = file2.read()
    print(content2 + " : new file")

file2.close(  )
 
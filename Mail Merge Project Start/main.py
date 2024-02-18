#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
with open("Input/Letters/starting_letter.txt" , mode='r') as letter:
    content = letter.read()
with open("Input/Names/invited_names.txt" , mode='r') as names:
    name = names.read()
names_list = name.split("\n")
for name in names_list:
    letter = content.replace('[name]' , name)
    invite = f"{name}_letter.txt"
    with open(f"invitation_letters/{invite}" ,mode='w') as letters_newfile:
        letters_newfile.write(letter)
        
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
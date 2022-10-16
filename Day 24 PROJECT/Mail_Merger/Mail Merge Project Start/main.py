#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

CHANGE_NAME = "[name]"

with open("./Input/Names/invited_names.txt") as invited_ppl:
    ppl = invited_ppl.readlines()


with open("./Input/Letters/starting_letter.txt") as start_let:
    content = start_let.read()
    for person in ppl:
        fixed_name = person.strip()
        new_letter = content.replace(CHANGE_NAME, fixed_name)
        with open(f"./Output/ReadyToSend/{fixed_name}.txt", mode="w") as newfile:
            newfile.write(new_letter)
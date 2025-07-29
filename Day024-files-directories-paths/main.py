#Read an existing file
with open("my_file.txt") as file:
    content = file.read()
    print(content)

#Write to existing file
with open("my_file.txt","w") as file:
    file.write("I love Python! ")

#append to existing file
with open("my_file.txt","a") as file:
    file.write("\nMy name is Edward!")

#Write to a new created file
with open("new_file.txt","w") as file:
    file.write("I love Python! ")

#append to a file using absolute path
with open("C:/Users/Edie/Desktop/my_file.txt","a") as file:
    file.write("\nMy name is Edward!")

#append to a file using relative path
with open("../../../my_file.txt","a") as file:
    file.write("\nMy name is Edward!")

#create a file in existing directories
with open("Input/Letter/starting_letter.txt","w") as file:
    file.write("Dear [NAME],\n\nYou're invited to my birthday tomorrow.\n"
               "\nHope you can make it!\n\nEdward ")

#create names  to a new text file
with open("Input/Names/invited_names.txt","w") as file:
    file.write("Israel\nGrace\nAndrew\nFaith\nHope\nRogers")

#read names from a file using readlines() method
with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()

PLACEHOLDER = "[NAME]"

#Write to a new created file
with open("Input/Letter/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        #replace "[NAME]" in the starting_letter.txt with each name
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.docx", "w") as completed_letter:
            completed_letter.write(new_letter)


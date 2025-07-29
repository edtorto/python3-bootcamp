#Read a file
with open("my_file.txt") as file:
    content = file.read()
    print(content)

#Write to existing file
with open("my_file.txt","w") as file:
    file.write("I love Python :) ")

#append to a file
with open("my_file.txt","a") as file:
    file.write("\nMy name is Edward!")

#Write to a new created file
with open("new_file.txt","w") as file:
    file.write("I love Python :) ")

list1 = [" "," "," "]
list2 = [" "," "," "]
list3 = [" "," "," "]
map = [list1, list2,list3]
position = input("Where do you want to put the treasure? e.g B1: \n")
letter = position[0].upper()
ABC = ["A", "B","C"]
letter_index = ABC.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"
print(f"{list1}\n{list2}\n{list3}") 


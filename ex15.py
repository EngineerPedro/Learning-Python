#Pedro Lebron Guzman III
#Learning Python the Hard Way
#April 6  2019
#PURPOSE: reading from a .txt file
#Lesson Program #15

from sys import argv #argv allows user to pass imput from comand to execution

script, filename = argv #this designates how many imputs at the command line can be taken

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Typed the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

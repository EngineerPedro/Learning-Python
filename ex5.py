#Pedro Lebron Guzman III
#Learning Python the Hard Way
#April 4 2019
#PURPOSE: more variables with strings implanted in them and printing
#Lesson Program #5

#variable establishment
my_name = 'Pedro Lebron Guzman III'
my_age = 26
my_height = 69 #inches
my_WEIGHT = 215 #puonds
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'


#string construction
print(f"Let's talk about {my_name}.")
print(f"he is {my_height} inches tall.  "    )
print(f"he is {my_WEIGHT} pounds heavy")
print("Actuallly thats a big boy")
print(f"Hes got {my_eyes} eyes and {my_hair} hair. ")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

#must be very careful
total = my_age + my_height + my_WEIGHT
print(f"If I add {my_age}, {my_height}, and {my_WEIGHT} I get a {total}.")

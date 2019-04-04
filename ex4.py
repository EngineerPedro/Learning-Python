#Pedro Lebron Guzman III
#Learning Python the Hard Way
#April 4 2019
#PURPOSE: variables
#Lesson Program #4

#variables being set to equal etc.
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven  = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers /cars_driven

#displaying results
print("There are ", cars, " cars available.")
print("There are only ", drivers, " drivers available.")
print("There will be ", cars_not_driven," empty cars today")
print("We can transport ", carpool_capacity," people today")
print("We have", passengers," to carpool today")
print("We need to put about ", average_passengers_per_car," in each car.")

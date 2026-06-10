#assignment 1:
#creating a tuple:
location = ("Hyderabad", "Telangana", "India")

print(location)

#assignment 2:
#creating a two sets:
# Students in Cricket Club
cricket_club = {"Rahul", "Vamshi", "Arjun", "Kiran", "Ravi"}
# Students in Football Club
football_club = {"Vamshi", "Ravi", "Sai", "Kiran", "Ajay"}

# finding Common students
common_students = cricket_club.intersection(football_club)

# finding Total unique students
total_unique_students = cricket_club.union(football_club)

print("Common Students:", common_students)
print("Total Unique Students:", total_unique_students)
print("Number of Unique Students:", len(total_unique_students)) 

#assignment 3:
#creating a dictionary onject for your mobile phone:
mobile = {
    "brand": "Samsung",
    "model": "Galaxy A54",
    "price": 35000,
    "storage": "128GB"
}

print(mobile) 

#assignment 4:
#creating a function to calculate the square of a number:
def calculate_square(number):
    return number * number


result = calculate_square(5)
print("Square:", result) 



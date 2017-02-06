#CONDITIONS (15PTS TOTAL)

# PROBLEM 1 (GPA - 4pts)
# Grades are values between 0 and 100
# We will translate grades to letters using:
# http://www.collegeboard.com/html/academicTracker-howtoconvert.html
# Make a variable for your percentage grade.
# Make a series of if/elif/else statements to print the letter grade.
# If the user enters a grade lower than zero or higher than 100, just give an error message.
# Don't worry about making an exception for these right now.
grade = int(input("What is your grade, dummy? "))

grades = [["A+", 97], ["A", 94], ["A-", 90], ["B+", 87], ["B", 84], ["B-", 80], ["C+", 77], ["C", 74], ["C-", 70], ["D+", 67], ["D", 64], ["D-", 60], ["F", 59]]

for i in range(len(grades)):
    if grade > 100:
        print("That's a lot of extra credit, dummy.")
        break
    elif grade >= grades[i][1]:
        grade = grades[i][0]
        print(grade)
        break
    elif 0 < grade < 59:
        print("You failin', dummy.")
        break


# PROBLEM 2 (Vowels - 5pts)
# Ask the user to supply a string.
# Print how many different vowels there are in the string.
# The capital version of a lower case vowel is considered to be the same vowel.
# y is not considered a vowel.
# Try to print proper output (e.g., printing “There are 1 different vowels in the string” is ugly).
# Example: When the user enters the string “It’s Owl Stretching Time,”
# the program should say that there are 3 different vowels in the string.
vowels = ["A","a","E","e","I","i","O","o","U","u"]
text = input("Tell me something: ")
unique_vowels = 0

for letter in text:
    for i in range(len(vowels)):
        if letter == vowels[i]:
            unique_vowels += 1
            vowels.pop(i)
            '''
            if letter == vowels[0]:
                vowels.pop(1)
            if letter == vowels[2]:
                vowels.pop(3)
            if letter == vowels[4]:
                vowels.pop(5)
            if letter == vowels[6]:
                vowels.pop(7)
            if letter == vowels[8]:
                vowels.pop(9)
            '''
            break

print("There are", unique_vowels, "unique vowels in your string.")

# PROBLEM 3 (Quadratic Equation - 6pts)
# You can solve quadratic equations using the quadratic formula.
# Quadratic equations are of the form Ax2 + Bx + C = 0.
# Such equations have zero, one or two solutions.
# The first solution is (−B + sqrt(B^22 − 4AC))/(2A).
# The second solution is (−B − sqrt(B^2 − 4AC))/(2A).
# There are no solutions if the value under the square root is negative.
# There is one solution if the value under the square root is zero.
# Write a program that asks the user for the values of A, B, and C,
# then reports whether there are zero, one, or two solutions,
# then prints those solutions.
# Note: Make sure that you also take into account the case that A is zero,
# and the case that both A and B are zero.

a = int(input("What is a? "))
b = int(input("What is b? "))
c = int(input("What is C? "))

val = (b**2 - 4 * a * c)
if val < 0:
    print("There are no solutions.")
elif val == 0:
    solution = -b/(2*a)
else:
    first_solution = (-b + val**(1/2))/(2*a)
    second_solution = (-b - val**(1/2))/(2*a)
    print("First solution: ", first_solution)
    print("Second solution: ", second_solution)

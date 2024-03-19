# Prompt users to enter their age
age = int(input("Enter your age: "))

# Check if age is greater than or equal to 18
if age >= 18:
    # If age is 18 or older, print eligibility message
    print("You are eligible to vote")
else:
    # If age is younger than 18, print ineligibility message
    print("You are not eligible to vote, wait and reach 18 years for you to vote!")
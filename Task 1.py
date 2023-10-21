import random
import string

def generate_password(length=12):

  # Select the characters to include in the password
  characters = string.ascii_letters + string.digits + string.punctuation

  # Create the password using random.choices()
  password = ''.join(random.choices(characters, k=length))
  return password

print("Welcome to the Password Generator!")
# Get user input, for the number of passwords and length
num_passwords = int(input("Please enter the number of passwords you'd like to generate : "))
length = int(input("Please enter the desired length, for each password : "))
# Generate and display the passwords
for i in range(num_passwords):
  password = generate_password(length)
  print(f"Password {i+1}: {password}")



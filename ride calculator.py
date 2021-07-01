# taking input of age
age = int(input("What is your age (i.e.12) :-"))
height = int(input("what is your height in cm (i.e. 170) :-" ))
if height>=120:
  if age<12:
    bill=5
    print("Your bill will be $5")
  elif age<18:
    bill=12
    print("Your bill will be $12")
  elif age>18:
    bill = 15
    print("Your bill will be $15")
  
  # if they want to take a photo
  wants_photo=input("Do you want to take a photo (y or n) :-")
  if wants_photo == "y":
    bill += 3
  
  print(f"Your total bill will be ${bill}")
else:
  print("You are not eligible to ride the roolercoster, Try next Year XD")

input()

# Take the input temperature from user in celcius

Temperature = input("Enter your temperature:")

# Convert the temperature into the floating point number because Python take input as a string so we first convert into numeric

temperature = float(Temperature)

#  Insert the conditions

Status = "Fridge broken"
Status_Cold = "Fridge is too cold"
Status_Ok = "Fridge Ok"
Status_Warm = "Fridge is too Warm"

if temperature < 0:
    Status = Status_Cold
elif (temperature <= 4):
    Status = Status_Ok
elif (temperature>4 and temperature<=6):
    Status = Status_Warm

print(Status)


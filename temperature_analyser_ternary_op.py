temperature = int(input("What is the temperature in your room: "))
message = ("Its warm." if temperature > 30 else "Its nice." if temperature > 20 else "Its cold.")
print(message)
print("Temperature analysis completed with ternary operator")
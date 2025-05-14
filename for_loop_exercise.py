successful = False
for i in range(1, 4):
    print("Attempt", i, i * ".")
    if successful:
        print("Successful")
        break
else:
    print("attempted 3 times but failed to send the message.")
            
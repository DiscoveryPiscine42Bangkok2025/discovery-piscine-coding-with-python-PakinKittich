num = int(input("Enter a number less than 25\n"))

if num > 25:
    print("Error")
else:
    i = num
    while i <= 25:
        print(f"Inside the loop, my variable is {i}")
        i += 1
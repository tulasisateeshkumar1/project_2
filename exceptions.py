
try:
    a = int(input("Enter a number to which divide:"))
    b = int(input("Enter a number to which divide by:"))
    print("Resource open")
    k=a/b
    print(k)

except ZeroDivisionError as e:
    print("you can't divide by zero")
except ValueError as e:
    print("Invalid input")
except exception as e:
    print("Something went wrong")

finally:
    print("Resource closed")
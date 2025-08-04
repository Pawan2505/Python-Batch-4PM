
# try:
#     num1 = 10
#     num2 = 2
#     result = num1/num2
#     print(f"Result : {result}")

# except:
#     print("Something worng!!")
# finally:
#     print("Cleanup unwanted memory!!")


# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ValueError:
#     print("Please enter a valid number!")
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# else:
#     print("Result is:", result)


# try:
#     f = open("data.txt", "r")   
# except ValueError:
#     print("Please enter a valid number!")
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# except FileNotFoundError:
#     print("File Not Found!!")
# else:
#     print(f.read())

try:
    f = open("data.txt", "r")   
except ValueError:
    print("Please enter a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
except FileNotFoundError:
    print("File Not Found!!")
else:
    print(f.read())
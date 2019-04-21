"""
Ask the user for a number. Depending on whether the number is even or odd,
 print out an appropriate message to the user. Hint:
 how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num)
and one number to divide by (check). If check divides evenly into num,
 tell that to the user. If not, print a different appropriate message.

"""

user_Number = int(input("Please add a number! "))
user_Number2 = int(input("Please add another number! "))

if user_Number % 2 == 0 and user_Number2 % 2 == 0:
    print("this number \"", user_Number,"\" is even")
    print("this anthor \"", user_Number2, "\" is even")
elif user_Number % 2 != 0 and user_Number2 % 2 != 0:
    print("this number \"", user_Number, "\" is odd")
    print("this anthor \"", user_Number2, "\" is odd")
elif user_Number % 2 == 0 and user_Number2 % 2 != 0:
    print("this number \"", user_Number, "\" is even")
    print("this anthor \"", user_Number2, "\" is odd")
elif user_Number % 2 != 0 and user_Number2 % 2 == 0:
    print("this number \"", user_Number, "\" is odd")
    print("this anthor \"", user_Number2, "\" is even")
else:
    print("this number \"", user_Number, "\" is odd")
    print("this anthor \"", user_Number2, "\" is odd")
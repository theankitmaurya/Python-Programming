try:
    a = int(input("Enter a number: "))
    print(a)

except Exception as e:
    print(e)

finally:
    print("I'm inside of finally")

# Python offers a 'finally' clause which ensures execution of a piece of code inspective of the exception.

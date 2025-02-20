def myFunction():
    print("This is a module block.")


if __name__ == "__main__":
    # If this this code is present in the main file then execute the code otherwise not
    print("We are running this code when we are in main file.")
    myFunction()
    print(__name__)

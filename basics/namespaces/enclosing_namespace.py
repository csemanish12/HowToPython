def welcome():
    x = "python"   # x is considered to be in enclosing scope as it resides in a method which encloses the nested method

    def nested_welcome():
        print("Welcome from nested method:", x)

    nested_welcome()


welcome()

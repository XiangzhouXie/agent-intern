try:
    number = int(input("please enter a number:"))
    result = 10 / number
    print(result)
except Exception as e:
    print("error")
    print(e)
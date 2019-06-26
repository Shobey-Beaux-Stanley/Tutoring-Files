def add(num1, num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - 2

def mult(num1,num2):
    return num1 * num2

def div(num1,num2):
    return num1/num2
def main():
    try:
        userInput = input("Enter what kind of operation you want to perform:\n" +
                          "type add to add two numbers\n"+
                          "type subtract to subtract two numbers\n"+
                          "type mult to multiply two numbers\n" +
                          "type div to divide two numbers\n")
        number1 = int(input("enter the first number"))
        number2 = int(input("enter the second number"))

        if(userInput == "add"):
            print(add(number1,number2))
        elif(userInput == "sub"):
            sub(number1,number2)
        elif(userInput == "mult"):
            mult(number1,number2)
        elif(userInput == "div"):
            div(number1,number2)
    except:
        print("There was an error")
if __name__ == "__main__":
    main()
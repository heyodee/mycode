class calculate:
    def __init__(self,num1,num2):
        while (num1 != "q"):
            print("\nWhat is the first operator? Or, enter q to quit: ")
            num1 = input().lower()
            lcase=num1.lower()
            if lcase == "q":
                break
            elif len(num1) == 0:
                print("\n cannot be blank. Restarting...")
                continue
            else:
                num1 = float(num1)

            print("\nWhat is the second operator? Or, enter q to quit: ")
            num2 = input()
            lcase=num2.lower()
            if lcase == "q":
                break
            elif len(num2) == 0:
                print("\n cannot be blank. Start over...")
                continue
            else:
                num2 = float(num2)

        
        #self.num1=num1
        #self.num2=num2
        #self.operator=""

calculate(1,21)

#print("Enter an operation to perform on the two operators (+ or -): ")
#num1 = input("Please enter an IPv4 IP address:")

#print("Enter an operation to perform on the two operators (+ or -): ")
#num2 = input("Please enter an IPv4 IP address:")

#print("Enter an operation to perform on the two operators (+ or -): ")
#operation = input()

#if operation == "+":
#    print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))
#elif operation == '-':
#    print("\n" + str(calc1) + " - " + str(calc2) + " = " + str(calc1 - calc2))
#else:
#    print("\n Not a valid entry. Restarting...")
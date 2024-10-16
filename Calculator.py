print("Which of the following calculations would you like to perform?")
print("1- Basic Arithmetic Operation")
print("2- Converter")
print("3- Currency Converter")
print("4- Number Converter")
print("5- Weight Converter")
option = int(input("Choose any calculation: "))

if option == 1:
    print("Which operation would you like?")
    print("1- Addition")
    print("2- Subtraction")
    print("3- Multiplication")
    print("4- Division")
    option2 = int(input("Choose an operation: "))
    
    if option2 in [1, 2, 3, 4]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if option2 == 1:
            result = num1 + num2
            print("The answer is", result)
        elif option2 == 2:
            result = num1 - num2
            print("The answer is", result)
        elif option2 == 3:
            result = num1 * num2
            print("The answer is", result)
        elif option2 == 4:
            if num2 != 0:
                result = num1 / num2
                print("The answer is", result)
            else:
                print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation choice.")
if option == 2:
    print("Which converter would you like?")
    print("1-meter(m) to kilometer(km)")
    print("2- kilometer(km) to meter(m)")
    option3 = int(input("Choose a converter: "))

    if option3 == 1:
            meter = float(input("Enter length in meter: "))
            km = meter/1000
            print("The length in kilometer is",km)
    elif option3 == 2 :
            kmeter = float(input("Enter length in kilometer: "))
            m = kmeter*1000
            print("The length in meter is",m)
    else:
        print("Invalid converter choice.")

        
if option == 3:
    print("Which currency converter would you like?")
    print("1-nepali to indian")
    print("2- nepali to dollar")
    print("3- indian to nepali")
    print("4- indian to dollar")
    print("5- dollar to nepali)")
    print("6- dollar to indian)")
    option4 = int(input("Choose a converter: "))

    if option4 == 1:
            nepali = float(input("Enter currency in rupees: "))
            indian = nepali*0.63
            print("The currency in Indian Rupee (INR)  is",indian )
    elif option4 == 2:
            nepali2 = float(input("Enter currency in rupees: "))
            dollar = nepali2*0.0074
            print("The currency in dollar is",dollar)
    elif option4 == 3:
            indian = float(input("Enter currency in Indian Rupee (INR): "))
            nepali = indian*1.60
            print("The currency in rupees is",nepali)
    elif option4 == 4:
            indian2 = float(input("Enter currency in Indian Rupee (INR): "))
            dollar = indian2*0.012
            print("The currency in dollar is",dollar)
    elif option4 == 5:
            dollar = float(input("Enter currency in dollar: "))
            nepali = dollar*134.48
            print("The currency in rupees is",nepali)
    elif option4 == 6:
            dollar2 = float(input("Enter currency in dollar: "))
            indian = dollar2*84.05
            print("The currency in Indian Rupee (INR) is",indian )        
            
    else:
          print("Invalid currency converter choice.")
          
def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:  
        decimal = decimal * 2 + int(digit)  
    return decimal
def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"  
    binary = ""
    
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2
    
    return binary
def quinary_to_decimal(quinary):
    decimal = 0
    for digit in quinary:  
        decimal = decimal * 5 + int(digit)  
    return decimal
def decimal_to_quinary(decimal):
    if decimal == 0:
        return "0"  
    quinary = ""
    
    while decimal > 0:
        remainder = decimal % 5
        quinary = str(remainder) + quinary
        decimal = decimal //5
    
    return quinary

if option == 4:
        print("Which number converter would you like?")
        print("1- Binary to Decimal")
        print("2- Decimal to Binary")
        print("3- Quinary to Decimal")
        print("4- Decimal to Quinary")  
        option3 = int(input("Choose a converter: "))

        if option3 == 1:
            binary_number = input("Enter the binary number: ")  
            if all(char in "01" for char in binary_number): 
                decimal_number = binary_to_decimal(binary_number)  
                print("The decimal number of", binary_number, "is", decimal_number)
            else:
                print(binary_number, "contains characters not used in binary numbers.")
        elif option3 == 2:
            number = int(input("Enter a decimal number: "))
            binary_result = decimal_to_binary(number)
            print("Binary representation:", binary_result)
        elif option3 == 3:
            quinary_number = input("Enter the quinary number: ")  
            if all(char in "1,2,3,4,5" for char in quinary_number): 
                decimal_number = quinary_to_decimal(quinary_number)  
                print("The decimal number of", quinary_number, "is", decimal_number)
            else:
                print(binary_number, "contains characters not used in binary numbers.")
        elif option3 == 4:
            number = int(input("Enter a decimal number: "))
            quinary_result = decimal_to_quinary(number)
            print("Quinary representation:", quinary_result)
    
else:
            print("Invalid number converter choice.")


if option == 5:
    print("Welcome to the Weight Converter!")
    print("Which conversion would you like to perform?")
    print("1- Pounds to Kilograms")
    print("2- Kilograms to Pounds")
    choice = int(input("Choose a conversion option (1 or 2): "))

    if choice == 1:
        pounds = float(input("Enter weight in pounds: "))
        kilograms = pounds / 2.205
        print(pounds, "pounds is equal to", kilograms, "kilograms.")
    elif choice == 2:
        kilograms = float(input("Enter weight in kilograms: "))
        pounds = kilograms * 2.205
        print(kilograms, "kilograms is equal to", pounds, "pounds.")
    else:
        print("Invalid choice. Please select either 1 or 2.")

else:
    print("Invalid calculation option.")            

           
    

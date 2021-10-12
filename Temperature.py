try:
    temperature = float(input("input temperatur in figures: "))
    unit =  input("input C for celsius and F for fahrenheit: ").upper()
    if (unit == 'C'):
        print("Temperature in Fahrenheit: " + str((temperature - 32)*5/9) + " F")
    elif (unit == 'F'):
        print ("Temperature in Celsius: " + str((temperature * 9/5)+32) + " C")
    else:
        print ("include an integer value")
except ValueError:
    print(" Please input an integer value")

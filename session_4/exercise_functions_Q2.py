degrees_f = input("Enter the temperature in Farenheit")

def celcius_convert():
    result = (float(degrees_f) - 32) * 5/9
    return float(result)

degrees_c = celcius_convert()
print(degrees_c)
#8. Implement a python function to Convert Celsius to Fahrenheit and Fahrenheit to
#Celsius.

def cel_to_fah(cel_0030) :
    fah_0030 = ((cel_0030*9)/5)+32
    print("Temperature in Fahrenheit : ", fah_0030)
    
def fah_to_cel(fah_0030):
    cel_0030 = (fah_0030-32)/1.8
    print("Temperature in Celcius : ", cel_0030)
    
cel_0030 = 37
cel_to_fah(cel_0030)

fah_0030 = 100
fah_to_cel(fah_0030)    
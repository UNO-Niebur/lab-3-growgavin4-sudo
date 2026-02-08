#TempConvert.py
#Name:Gavin Grow
#Date:2/8/26
#Assignment:TempConv


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF= float(input("Give me a temperature:"))
  
 

  tempC=round( (tempF-32) *(5/9), 1)

  print(tempF, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()

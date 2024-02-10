import os #to clear screen
num1=int(input("Enter the first number: "))#asks for first number
def calculation():#defines the calculation function
  result=0#sets result to 0
  mode=input("Enter the mode of operation:\n+\t-\t*\t/\t")#asks for the mode of operation
  if mode == "+" or mode == "-" or mode == "*" or mode == "/":#checks if the mode is valid
    num2=int(input("Enter the next number: "))#asks for the second number
    if mode == "+":
      result=num1+num2
      print(num1,mode,num2,"=",result)
    elif mode == "-":
      result=num1-num2
      print(num1,mode,num2,"=",result)
    elif mode == "*":
      result=num1*num2
      print(num1,mode,num2,"=",result)
    elif mode == "/":
      result=num1/num2
      print(num1,mode,num2,"=",round(result,2))
  else:
    print("Invalid mode of operation")#if the mode is not valid, it prints an error message
  repeat=calling()#calls the calling function
  return result ,repeat#returns the result and repeat
def calling():#defines the calling function
  repeat = input("enter 'y' to continue calculation with the result\n"
  "enter 'n' to start a new calculation\n"
  "enter 'e' to exit\n")#asks if the user wants to continue
  return repeat#returns the repeat
repeat="y"
while repeat=="y" or "n": #while the repeat is y or n
  if repeat == "y":
    num1,repeat=calculation()#calls the calculation function and sets the result and repeat to the values returned
  elif repeat=="n":
    os.system('clear')
    num1=int(input("Enter the first number: "))#asks for the first number
    num1,repeat=calculation()#calls the calculation function and sets the result and repeat to the values returned
  else: #if the repeat is not y or n
    print("Thank you for using the calculator")
    break
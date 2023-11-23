while True:
  try:
    x = float(input("What is the first number "))
  except ValueError:
     print("Please enter a number")
  way = input("What is the symbol: ")
  if way == "*":
      y = float(input("What is the second number: "))
      answer = x * y
      print ("The answer is ",answer)
      ex = input("Do you want to exit: ")
      if ex == "yes" or ex == "Yes":
          exit()
      else:
          exit
  elif way == "+":
      y = float(input("What is the second number: "))
      answer = x + y
      print ("The answer is ",answer)
      ex = input("Do you want to exit: ")
      if ex == "yes" or ex == "Yes":
          exit()
      else:
          exit
  elif way == "-":
      y = float(input("What is the second number: ")) 
      answer = x - y
      print ("The answer is ",answer)
      ex = input("Do you want to exit: ")
      if ex == "yes" or ex == "Yes":
          exit() 
      else:
          exit  
  elif way == "/":
      y = float(input("What is the second number: "))
      answer = x / y
      print ("The answer is ",answer)
      ex = input("Do you want to exit: ")
      if ex == "yes" or ex == "Yes":
          exit()
      else:
          exit
  elif way == "**":
      y = float(input("What is the second number: "))
      answer = x ** y
      print ("The answer is ",answer)
      ex = input("Do you want to exit: ")
      if ex == "yes" or ex == "Yes":
          exit()
      else:
          exit
  elif way == "//":
      y = float(input("What is the second number: "))
      answer = x // y
      print ("The answer is ",answer)
      ex = input("Do you want to exit: ")
      if ex == "yes" or ex == "Yes":
          exit()
      else:
          exit
          
          
  else:
      print("Thats not a symbol for math")
      exit
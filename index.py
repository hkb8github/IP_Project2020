
while True:
  print("-"*60)
  print(" "*20, "Welcome to Students Project")
  print("-"*60)
  print("1. Add Student")
  print("2. Search Student")
  print("3. Updation")
  print("0. Exit")
  print("-"*60)
  choice = int(input("Enter your choice"))
  if choice==0:
    break
  elif choice == 1:
    pass  
  elif choice == 2:
    pass
  elif choice == 3:
    while True:
      print("-"*60)
      print("Home->Updation")
      print("-"*60)
      print("1. Update")
      print("2. Delete")
      print("0. Go Back")
      choice = int(input("Enter your choice"))
      if choice == 0:
        break
      elif choice == 1:
        print("-"*60)
        print("Home->Updation->Delete")
        print("-"*60)
      elif choice == 2:
        print("-"*60)
        print("Home->Updation->Delete")
        print("-"*60)      
      else:
        print("\n\n\t\tWrong choice entered......!!!")
  else:
    print("\n\n\t\tWrong choice entered......!!!")
    

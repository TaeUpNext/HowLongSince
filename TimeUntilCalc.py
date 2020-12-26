import datetime
starting = True #Starting loop 
while starting == True:
  #*Starting Date
  startingDate_Entry = input('\nEnter the starting date in YYYY-MM-DD format: ')
  sMonth,sDay,sYear= map(int, startingDate_Entry.split('-'))
  startingDate = datetime.date(sMonth, sDay, sYear)
  formattedStartDate = (startingDate.strftime("\nStaring Date: %B/%d/%Y"))

  #*Ending Date
  endingDate_Entry = input('\nEnter the ending date in YYYY-MM-DD format: ')
  eMonth,eDay,eYear= map(int, endingDate_Entry.split('-'))
  endingDate = datetime.date(eMonth, eDay, eYear)
  formattedEndDate = (endingDate.strftime("\nEnding Date: %B/%d/%Y"))

  print(formattedStartDate)
  print(formattedEndDate)

    
  determineTime = input("\nWould You like to find the time until a date or the time from a date, Enter a 1 for time from or a 2 for time until") #Determines if a user is finding out how long its been since a date or how long it will take to get to a date
    
  #if determineTime == 1:


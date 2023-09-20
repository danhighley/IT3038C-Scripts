import datetime, re
from datetime import date


# capture current date time
currentDate = datetime.datetime.now()

# get user input - birthday
print()
print("          How old are you?")

# validate correct date input
while True:
    birthDay = input("Please enter your date of birth [mm/dd/yyyy] ")
    month = birthDay[0:2]
    day = birthDay[3:5]
    year = birthDay[6:10]
    if int(month) <= 0 or int(month) > 12:
        print("Invalid Month, please try again.")
    elif int(day) <= 0 or int(day) > 31:
        print("Invalid Day, please try again.")
    elif int(month) == 2 and int(day) > 29:
        print("Invalid Day, please try again.")
    elif (int(month) == 4 or int(month) == 6 or int(month) == 9 or int(month) == 11) and int(day) > 30:
        print("Invalid Day, please try again.")
    else:
        break

# Display and confirm bithday
birthDayDate = datetime.datetime.strptime(birthDay,'%m/%d/%Y').date()
print()
print("Your birthday is on " + birthDayDate.strftime("%d") + " of " + birthDayDate.strftime("%B, %Y"))

# Choose age output format - validate input
print()
print("   Please choose how to display your age:")
while True:
    menuChoice = input("[S]econds, [M]inutes, [H]ours, [D]ays, [Y]ears ")
    if not re.match("[SsMmHhDdYy]", menuChoice):
        print("Error! Please select from the Menu.")
    elif len(menuChoice) > 1:
        print("Error! Please use only one character.")
    else:
        break

# Calculations
birthDayFull = datetime.datetime.strptime(birthDay,'%m/%d/%Y')
daysLeft = currentDate - birthDayFull
seconds = daysLeft.total_seconds()
minutes = seconds / 60
hours = seconds / 3600
days = hours / 24
years = currentDate.year - birthDayFull.year - ((currentDate.month, currentDate.day) < (birthDayFull.month, birthDayFull.day))

# Disply age base on user format selection
print()
if menuChoice.casefold().__eq__("s"):
   print("You must realy want to feel old..")
   print("You are %s seconds old." % format(int(seconds), ',d'))  
elif menuChoice.casefold().__eq__("m"):
   print("You must realy want to feel old..")
   print("You are %s minutes old." % format(int(minutes), ',d')) 
elif menuChoice.casefold().__eq__("h"):
   print("You must realy want to feel old..")
   print("You are %s hours old." % format(int(hours), ',d')) 
elif menuChoice.casefold().__eq__("d"):
   print("You must realy want to feel old..")
   print("You are %s days old." % format(int(days), ',d')) 
else:
   if years == 0:
        print("You are not 1 year old yet.")
        yearsToAdd = birthDayDate.year +1
        newDate = birthDayDate.replace(year = yearsToAdd).strftime('%m/%d/%Y')
        print("You will be 1 year old on " + newDate)
   else:
        print("You are %s years old." % format(int(years), ',d')) 
print()

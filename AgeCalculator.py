import datetime
Running_year = datetime.datetime.now().year
birth_year = int(input("Enter your birthday year: "))
age = (Running_year - birth_year)
print("You are now %i years old" % (age))

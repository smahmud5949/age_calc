import datetime
#import arrow
#utc = arrow.utcnow()

date_in = int(input("Input date : "))
month_in = int(input("Input Month : "))
year_in = int(input("Input year : "))

year = datetime.datetime.now().year
#month = datetime.datetime.now().month
#date = datetime.datetime.now().date()

print ("You're "+ str(year-int(year_in))+" old")
print("Enter to exit")
#print(month-int(month_in))







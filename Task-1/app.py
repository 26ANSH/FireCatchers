from datetime import datetime
from weather import get_data, get_dates, get_weather, get_wind_speed, get_pressure

MENU= '''1. Get weather
2. Get Wind Speed
3. Get Pressure
0. Exit'''

CITY = "London,uk"
URL = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q={CITY}&appid=b6907d289e10d714a6e88b30761fae22"

data = get_data(URL)

def valid_date_function(date, function):
         try:
            # date = date.split('-')[2]+'-'+date.split('-')[1]+'-'+date.split('-')[0]
            date_obj = datetime.strptime(date, '%Y-%m-%d')
         except:
            print("Wrong Date Format, Date Should be YYYY-MM-DD\n")
            date = input("Enter date in format(YYYY-MM-DD): ")
            valid_date_function(date, function)
         else:
            if date in get_dates(data):
               function(data, date)
            else:
               print("data unavailable for date "+date)


while True:
   print(MENU)
   try:
      choice = int(input("Choose form the above menu: "))
      if choice not in [1,2,3,0]:
         raise TypeError
   except:
      print("Invalid Choice, Choose again from the Menu")
   else:
      print('\n'+'-'*100+'\n')

      if choice == 0:
          print("BYE")
          break
      elif choice == 1:
         date = input("Enter date in format(YYYY-MM-DD): ")
         valid_date_function(date, get_weather)
      elif choice == 2:
         date = input("Enter date in format(YYYY-MM-DD): ")
         valid_date_function(date, get_wind_speed)
      elif choice == 3:
         date = input("Enter date in format(YYYY-MM-DD): ")
         valid_date_function(date, get_pressure)
  
   print('\n'+'-'*100+'\n')
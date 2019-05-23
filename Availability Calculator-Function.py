'''
Availability Calculator
6/29/17
by Jeff Moy

Directions:
Click on the 'Run" option at the top of the page
Select "Run Module"
This should bring up the Python Shell
Call the function by typing in: Availability()
'''

def Availability():
    while True:
        try:
            Product_MTBF = float(input('What is the Product\'s Mean Time Between Failure(MTBF)(In Hours)?: '))
        except ValueError:
            print("Sorry, I didn't understand that. Please provide MTBF value in numeric form")
            continue
        else:
            break


    while True:
        try:
            Product_MTTR = float(input("What will be the Mean Time to Repair (MTTR) value to get the product in working order (In Hours)?: "))
        except ValueError:
            print("Sorry, I didn't understand that. Please provide MTTR value in numeric form")
        else:
            break

    print('\n')

    Product_Availability = round((Product_MTBF / (Product_MTBF + Product_MTTR)),3)
    print('Availability for this product is: ' + str(100*Product_Availability) + '%')

    print('\n')

    Downtime_Per_Year_in_Days= float(round((1-Product_Availability) * 364.25,2))
    Downtime_Per_Year_in_Hours= float(round((1-Product_Availability) * 8760,2))
    Downtime_Per_Year_in_Minutes= float(round((1-Product_Availability) * 525600, 2))
    Downtime_Per_Year_in_Seconds= int(round((1-Product_Availability) * 3.154e+7,0))

    if Downtime_Per_Year_in_Days > 1:
        Notation_Days = 'Days'
    else:
        Notation_Days = 'Day'

    if Downtime_Per_Year_in_Hours > 1:
        Notation_Hours = 'Hours'
    else:
        Notation_Hours = 'Hour'
    
    if Downtime_Per_Year_in_Minutes > 1:
        Notation_Minutes = 'Minutes'
    else:
        Notation_Minutes = 'Minute'

    if Downtime_Per_Year_in_Seconds > 1:
        Notation_Seconds = 'Seconds'
    else:
        Notation_Seconds = 'Second'
    
    print('Downtime information per year as follows:'
     +'\n In Days: '+ str(Downtime_Per_Year_in_Days) +' ' + str(Notation_Days)
     +'\n In Hours: '+ str(Downtime_Per_Year_in_Hours) +' ' + str(Notation_Hours)
     +' \n In Minutes: '+ str(Downtime_Per_Year_in_Minutes) + ' ' + str(Notation_Minutes)
     +' \n In Seconds: '+ str(Downtime_Per_Year_in_Seconds) + ' ' + str(Notation_Seconds))

    Downtime_Per_Month_in_Days= float(round(((1-Product_Availability) * 364.25)/12,2))
    Downtime_Per_Month_in_Hours= float(round(((1-Product_Availability) * 8760)/12,2))
    Downtime_Per_Month_in_Minutes= float(round(((1-Product_Availability) * 525600)/12, 2))
    Downtime_Per_Month_in_Seconds= int(round(((1-Product_Availability) * 3.154e+7)/12,0))

    print('\n')

    if Downtime_Per_Year_in_Days > 1:
        Notation_Days = 'Days'
    else:
        Notation_Days = 'Day'

    if Downtime_Per_Year_in_Hours > 1:
        Notation_Hours = 'Hours'
    else:
        Notation_Hours = 'Hour'
    
    if Downtime_Per_Year_in_Minutes > 1:
        Notation_Minutes = 'Minutes'
    else:
        Notation_Minutes = 'Minute'

    if Downtime_Per_Year_in_Seconds > 1:
        Notation_Seconds = 'Seconds'
    else:
        Notation_Seconds = 'Second'


    print('Downtime information per month as follows:'
     +'\n In Days: '+ str(Downtime_Per_Month_in_Days) +' ' + str(Notation_Days)
     +'\n In Hours: '+ str(Downtime_Per_Month_in_Hours) +' ' + str(Notation_Hours) 
     +' \n In Minutes: '+ str(Downtime_Per_Month_in_Minutes) + ' ' + str(Notation_Minutes)
     +' \n In Seconds: '+ str(Downtime_Per_Month_in_Seconds) + ' ' + str(Notation_Seconds))




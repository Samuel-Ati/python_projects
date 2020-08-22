#1

month = int(input('month'))
day = int(input("day"))
if month == 3 or 6 and day == 20:
    print('True')
else:
     print("False")


#2

current_balance = 500
time_in_years = 1
annual_rate = 20/100
annual_interest = (current_balance*time_in_years*annual_rate)
print(annual_interest)

new_current_balance = annual_interest + current_balance
print(new_current_balance)
total_time_in_years = 5 
compound_interest = annual_interest* total_time_in_years + new_current_balance*5
print(compound_interest)


#3 and 4

T_in_Fahrenheit = 35.5
T_in_celcius = T_in_Fahrenheit - 32*5/9
print(T_in_celcius)
v_in_miles_per_hour = 50
v_in_km = v_in_miles_per_hour *1.609344
w = 35.74 + 0.6215*T_in_celcius + (0.4275*T_in_celcius-35.75)*v_in_km


#5

import math
x = 4.5
y = 5.8

r = math.sqrt(x+y)**2
print(r)
o = math.atan2(y,x)
print(o)



#7

x=1.5
y=2.5
z=3.5
if x < y < z:
    print(True)
else:
    print(False)






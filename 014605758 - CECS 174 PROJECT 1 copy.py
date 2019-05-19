# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 13:20:47 2017

@author: Dominique Oyco dominickoyco@gmail.com
Estimate how much the user has lived in terms of minutes and seconds, heartbeat, sneeze, calories, and other health related statistics
"""

import time

current_time = time.localtime()

#ask the user to input age then calculate it in minutes & seconds
birthMonth = int(input('Please enter your month of birth in the format of 1 to 12: '))
birthDay = int(input('Please enter your day of birth in the format of 1 to 31: '))
birthYear = int(input('Please enter your year of birth that is past or currently at 2017: '))

diff_months = current_time[1] - birthMonth
diff_days = current_time[2] - birthDay
diff_years = current_time[0]- birthYear

minutes_per_year = diff_years * 365 * 24 * 60
minutes_per_month = diff_months * 30 * 24 * 60
minutes_per_day = diff_days * 24 * 60

seconds = current_time[5]

total_minutes = minutes_per_month + minutes_per_day + minutes_per_year
total_days = diff_days + (diff_years * 365) + (diff_months * 30)

print("You've been alive for about", total_minutes, "minutes and", seconds, "seconds.")

#2. calculate the user's heart beat in his/her lifetime
user_heartbeat = total_days * 72 * (24 * 60)
print("Your heart has beaten for over", user_heartbeat, "times.")

#3. calculate how much the user has sneezed in his/her lifetime
user_sneezed = int(total_days * 1.2) #no decimals so int is used to get the exact number
print("You have sneezed about", user_sneezed, "times.")

#4a. calculate the amount of calories the user has consumed in his/her lifetime
user_calories_m = total_days * 2640
user_calories_f = total_days * 1785
print("If you're a guy, you have consumed about", user_calories_m, "calories. Otherwise, you have consumed about", user_calories_f, " calories if you're a girl.")

#4b. calculate the amount of calories in terms of a food item
chicken_nuggets_calories_m = int(user_calories_m / 20 )
chicken_nuggets_calories_f = int(user_calories_f / 20 )
print("That is about", chicken_nuggets_calories_m, "chicken nuggets if you are a guy or about", chicken_nuggets_calories_f, "chicken nuggets if you are a girl.")

#5a. calculate how much the user blinks in his/her lifetime
user_blink = total_days * 21600
print("You have blinked for about", user_blink, "times.")

#5b. calculate how much glasses of water the user drinks per day
user_drink = total_days * 8
print("You have drank over", user_drink, "glasses of water.")
















    
    
    

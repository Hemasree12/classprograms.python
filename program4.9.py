month = input("Input the month: ")
day = int(input("Input the day: "))
if month in ('March'):
	season = 'summer'
elif month in ('june', 'july'):
	season = 'spring'
elif month in ('August', 'September'):
	season = 'fall'	
elif month in ('december'):
        season='winter'
else:
	season = 'autumn'
if (month == 'March') and (day > 19):
	season = 'summer'
elif (month == 'June') and (day > 20):
	season = 'spring'
elif (month == 'September') and (day > 21):
	season = 'fall'
elif (month == 'December') and (day > 20):
	season = 'winter'
print("Season is",season)





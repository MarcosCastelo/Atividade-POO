from datetime import *

def week_day_today():


def week_day(date):
	return datetime.weekday(date)


def week_day_name(week_day:int):
	if week_day == 0:
		return "Monday"
	if week_day == 1:
		return "Tuesday"
	if week_day == 2:
		return "Wednesday"
	if week_day == 3:
		return "Thursday"
	if week_day == 4:
		return "Friday"
	if week_day == 5:
		return "Saturday"
	if week_day == 6:
		return "Sunday"


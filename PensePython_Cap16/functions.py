from classes import *
from copy import copy

def print_time(time):
	hour = "%.2d" % time.hour
	minute = "%.2d" % time.minute
	second = "%.2d" % time.second

	s_time = hour + ":" + minute + ":" + second

	print("\nHour -> ", s_time)


def  is_after(time1, time2):
	return (time1.hour, time1.minute, time1.second) > (time2.hour, time2.minute, time2.second)


def add_time(time1, time2):
	assert valid_time(time1) and valid_time(time2)

	seconds = time_to_int(time1) + time_to_int(time2)
	return int_to_time(seconds)


def increment(time, seconds):
	assert valid_time(time)

	total_time = int_to_time(time_to_int(time) + seconds)

	time.second = total_time.second
	time.minute = total_time.minute
	time.hour = total_time.hour


def pure_increment(time, seconds):
	assert valid_time(time)
	inc_time = copy(time)
	increment(inc_time, seconds)

	return inc_time


def time_to_int(time):
	minutes = time.hour * 60 + time.minute
	seconds = minutes * 60 + time.second

	return seconds


def int_to_time(seconds):
	time = Time()
	minutes, time.second = divmod(seconds, 60)
	time.hour, time.minute = divmod(minutes, 60)

	return time


def valid_time(time):
	if time.hour < 0 or time.minute < 0 or time.second < 0:
		return False
	if time.hour > 60 or time.minute > 60 or time.second > 60:
		return False

	return True


def mul_time(time, multiply):
	total_time = int_to_time(time_to_int(time) * multiply)

	return total_time


def median_step(time, distance):
	mile = 1600
	time_to_step =  mul_time(time, 1/distance)

	return mul_time(time_to_step, mile)

def week_day_today():
	from datetime import datetime
	today = datetime.today()
	week_day = datetime.weekday(today)

	return week_day_name(week_day)


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


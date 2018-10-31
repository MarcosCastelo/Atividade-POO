from classes import *
from functions import *

def main():
	start = Time()
	start.hour = 9
	start.minute = 45
	start.second = 0

	duration = Time()
	duration.hour = 1
	duration.minute = 35
	duration.second = 0

	done = add_time(start, 	duration)
	print_time(done)


if __name__ == '__main__':
	main()
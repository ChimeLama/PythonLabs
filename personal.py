def organizer():
	eventName = []
	eventMonth = []
	eventDay = []
	eventYear = []
	month_names = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
	def addEvent():
		event_name = input("What is the event: ")
		eventName.append(event_name)
		event_year = int(input("What is the year: "))
		while event_year < 1:
			event_year = int(input("Invalid year. Please enter a valid year: "))
		eventYear.append(event_year)
		event_month = int(input("What is the month (number): "))
		event_month = validateMonth(event_month)
		eventMonth.append(event_month)
		event_day = int(input("What is the date: "))
		event_day = validateDay(event_month, event_day, event_year)
		eventDay.append(event_day)
	def validateMonth(month):
		while month < 1 or month > 12:
			month = int(input("Invalid month. Please enter value from 1-12: "))
			return month
	def validateDay(month, day, year):
		if month == 2:
			if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
				days_in_month = 29
			else:
				days_in_month = 28
		elif month in [4, 6, 9, 11]:
			days_in_month = 30
		else:
			days_in_month = 31
		while day < 1 or day > days_in_month:
			day = int(input("Invalid day. Please enter value from 1-" + str(days_in_month) + ": "))
			return day
	def printEvents():
		print("******************** List of Events ********************")
		for i in range(len(eventName)):
			print(eventName[i])
			print("Date:", month_names[eventMonth[i]]+" "+ str(eventDay[i])+",", eventYear[i])
	if __name__ == "__main__":
		add_more_event = True
		while add_more_event:
			addEvent()
			repeat = input("Do you want to enter another date? NO to stop: ")
			if repeat.lower() != "yes":
				add_more_event = False
				printEvents()

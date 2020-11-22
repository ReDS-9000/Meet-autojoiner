import os, time, csv
from datetime import datetime as dt
import webFunctions as web
import PySimpleGUI as sg


def readSchedule():
	lun, mar, mer, gio, ven = ([], ) * 5  #week length
	week=[lun, mar, mer, gio, ven]

	with open('schedule.csv', 'r') as file:
		reader = csv.reader(file)
		i=0
		for row in reader:
			week[i].append(row[1:7])
			i+=1
		return week

def warning():
	layout = [[sg.Text("Joining next class in 10 seconds")], [sg.Button("Switch class")], [sg.Button("Stay Here")] ]
	window = sg.Window('MeetManager', layout)
	event, values = window.Read(timeout = 10000)
	if event == "Stay Here":
		window.close()
		return True
	else: 
		window.close()
		return False



sg.theme('DarkAmber')
schedule = readSchedule()  #schedule[0][day]
web.Glogin("EMAIL HERE","PASSWORD HERE")

previousCode=None
previousHour=None
while True:
	now=dt.now()
	hour=int(str(now).split(" ")[1].split(":")[0])
	#hour=int(input("[!Debug] hour >")) #DEBUG
	min=int(str(now).split(" ")[1].split(":")[1])
	day=dt.today().weekday()	
	#day=int(input("[!Debug] day >"))	#DEBUG

	#print("hour:", hour, " Day: ", day) #DEBUG


	if (day > 5):	#Week length
		print( "No lessons today!")
		break
	if (hour < 9):	#Start hour
		print("Lessons not started yet!")
		web.go("https://www.nayuki.io/res/full-screen-clock-javascript/full-screen-clock-24hr.html")
		time.sleep(3)
		web.fullScreen()
		time.sleep(10)
		continue
	if (hour > 13):	#End hour
		print("Lessons ended!")
		break


	if (hour != previousHour):
		previousHour=hour
		if(warning()==False):
			lessons = schedule[0][day]
			print(day)
			print("Today lessons", lessons)

			
			code=lessons[hour-8]
			if (code != previousCode):
				previousCode = code
				print("Now: ", code)

				if ("-" in code):	#direct Meet code
					print("Joining via direct code")
					web.joinMeetCall(code)

				elif ("ND" in code): #No Meet code
					print("No lessons now!")
					web.go("https://classroom.google.com/")

				elif ("NE" in code): #New code everytime
					print("Check your email!")
					web.go("https://www.gmail.com")

				else:	#Meet lookup code
					print("Joining via lookup code")
					web.joinMeetCall("lookup/" + code)






import pyttsx3
import wikipedia
import speech_recognition as sr
import datetime
import webbrowser
import os
import smtplib
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishme():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak("good morning mister kumar!")
	elif hour>=12 and hour<18:
		speak("good afternoon mister kumar!")
	else:
		speak("good evening mister kumar!")

	speak("I am a jarvis program, how may i help you ")

def takecommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio)
		print(f"User said : {query}\n")

	except Exception as e:
		speak("I didn't understand, can you say that again")
		return "None"

	return query

def sendEmail(to, content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login('bchandora60@gmail.com', 'Bh@ve$H60')
	server.sendmail('bchandora60@gmail.com', to, content)
	server.close() 

if __name__ == '__main__':
	wishme()
	while True:
	# if 1:
		query = takecommand().lower()

		# logic for task in query for jarvis
		if 'wikipedia' in query:
			speak("searching wikipedia...")
			query = query.replace("wikipedia", "")
			result = wikipedia.summary(query, sentences=2)
			speak("According to wikipedia")
			speak(result)

		elif 'open youtube' in query:
			webbrowser.open("youtube.com")

		elif 'open google' in query:
			webbrowser.open("google.com")

		elif 'open stackoverflow' in query:
			webbrowser.open("stackoverflow.com")

		elif 'play music' in query:
			music_dir = 'E:\\music'
			songs = os.listdir(music_dir)
			print(songs)
			os.startfile(os.path.join(music_dir, songs[0]))

		elif 'time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			speak(f"Sir! the time is {strTime}")

		elif 'email to bhavesh' in query:
			try:
				speak("what should I say")
				content = takecommand()
				to = "akshitvaishnav321@gmail.com"
				sendEmail(to, content)
				speak("Email has been sent successfully!")
			except Exception as e:
				speak("Sorry mister bhavesh, I am not able to send this email")

		elif 'quit' in query:
			speak("Okay mister bhavesh! Have a good day")
			exit()
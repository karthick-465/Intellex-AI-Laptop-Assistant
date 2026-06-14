import re
import pyttsx3
import pyautogui
import webbrowser
import os
from datetime import datetime
import speech_recognition as sr
import screen_brightness_control as pct
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import pywhatkit
import requests
from bs4 import BeautifulSoup
from time import sleep
import winsound
from pynput.keyboard import Key,Controller
import time
import pygame
import datetime
import requests
import speedtest
import random
import threading
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pyttsx3



keyboard=Controller()

for i in range(3):
    a=input("ENTER SECURITY PASSWORD TO ACCESS Mechion:")
    pw_file=open("password.txt","r")
    pw=pw_file.read()
    pw_file.close()
    if(a==pw):
        print("WELCOME USER")
        break
    elif(i==2 and a!=pw):
        exit()
    elif(a!=pw):
        print("ACCESS DENIED TRY AGAIN!")




def speak(text):
    
    engine = pyttsx3.init("sapi5")
    voices=engine.getProperty("voices")
    engine.setProperty("voice",voices[0].id)
    engine.say(text)
    engine.runAndWait()

def listen(language="en-US"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Can you please repeat?")
        return listen(language)
    except sr.RequestError as e:
        speak(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def open_file_explorer():
    speak("Opening File Explorer")
    os.system("explorer")

def close_file_explorer():
    speak("Closing File Explorer")
   
    

def open_paint():
    speak("Opening Paint")
    

def close_paint():
    speak("Closing Paint")
    pyautogui.hotkey('alt', 'f4')

def open_browser():
    speak("Opening Browser")
    webbrowser.open("http://www.google.com")

def close_browser():
    
    speak("Closing Browser")
    pyautogui.hotkey("ctrl", "w")

def open_youtube():
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")
    print("Opening YouTube")
    

def close_youtube():
    speak("Closing YouTube")
    pyautogui.hotkey("ctrl", "w")

def search_in_google(query):
    speak(f"Searching for {query} on YouTube")
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)


def search_in_youtube(query):
    speak(f"Searching for {query} on YouTube")
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

def adjust_volume(direction, amount=0.1):
   
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume_control = cast(interface, POINTER(IAudioEndpointVolume))

    current_volume = volume_control.GetMasterVolumeLevelScalar()

    if direction == 'increase':
        speak("Increasing volume")
        new_volume = min(1.0, current_volume + amount)
    elif direction == 'decrease':
        speak("Decreasing volume")
        new_volume = max(0.0, current_volume - amount)
    else:
        raise ValueError("Invalid direction. Use 'increase' or 'decrease'.")

    volume_control.SetMasterVolumeLevelScalar(new_volume, None)

def increase_brightness():
    print("Brightness value now:",pct.get_brightness())
    speak("enter the brightness level you want")
    level=input("enter the brightness level you want:")
    pct.set_brightness(level)
    speak("Increasing Brightness")
    print("Brightness value now:",pct.get_brightness())

def decrease_brightness():
    print("Brightness value now:",pct.get_brightness())
    speak("enter the brightness level you want")
    level=input("enter the brightness level you want:")
    pct.set_brightness(level)
    print("Brightness value now:",pct.get_brightness())
    speak("decreasing Brightness")

def set_alarm_from_text(time_text):
    def _alarm_worker():
        while True:
            current_time = time.localtime()
            if current_time.tm_hour == alarm_time[0] and current_time.tm_min == alarm_time[1]:
                play_alarm_sound()
                break
            time.sleep(10)  # Check every 10 seconds

    def play_alarm_sound():
        """Play the alarm sound."""
        speak("Wake up")
        pygame.mixer.init()
        pygame.mixer.music.load("alarm_tune.mp3") 
        # Load the alarm sound file
        pygame.mixer.music.play()  # Play the alarm sound
        

    def parse_time(time_text):
        try:
            hour, minute = map(int, time_text.split(':'))
            if 0 <= hour < 24 and 0 <= minute < 60:
                return hour, minute
            else:
                print("Invalid time format. Please provide valid hour and minute values.")
                return None
        except ValueError:
            print("Invalid time format. Please provide time in 'hour:minute' format.")
            return None

    alarm_time = parse_time(time_text)
    if alarm_time:
        print(f"Alarm set for {alarm_time[0]:02d}:{alarm_time[1]:02d}.")
        alarm_thread = threading.Thread(target=_alarm_worker)
        alarm_thread.start()

    



def set_reminder(hour, minute, message):
    """Set the reminder for the specified hour, minute, and message."""
    reminder_time = f"{hour:02d}:{minute:02d}:00"
    print(f"Reminder set for {reminder_time}: {message}")
    return reminder_time

def play_reminder_sound(message):
    """Play the reminder sound."""
    frequency = 2500  # Set frequency to 2500 Hertz
    duration = 4000  # Set duration to 1000 milliseconds (1 second)
    winsound.Beep(frequency, duration)
    speak(message)  # Play a beep sound

def check_reminder(reminder_time, message):
    """Check if the current time matches the reminder time."""
    current_time = time.strftime("%H:%M:%S", time.localtime())
    if current_time == reminder_time:
        print(f"Reminder: {message}")
        play_reminder_sound(message)

def add_song(playlist, song):
    playlist.append(song)
    speak(f"Added '{song}' to the playlist.")
    print(f"Added '{song}' to the playlist.")


def play_playlist(playlist):
    if not playlist:
        speak("Playlist is empty Add some songs first")
        print("Playlist is empty. Add some songs first.")
        return
   
    pygame.init()
    speak("Playing Playlist.")
    print("Playing Playlist.")
    stopped = False
    paused = False
    for song in playlist:
        print(f"Now playing: {song}")
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            if stopped:
                pygame.mixer.music.stop()
                speak("Music stopped.")
                print("Music stopped.")
                return
            else:
            
                while True:
                    choice = input("PRESS 'p' to PAUSE, 's' to STOP, 'r' to RESUME : ")
                    if choice.lower() == 'p':
                        paused = True
                        pygame.mixer.music.pause()
                        speak("Music paused.")
                        print("Music paused.")
                        
                    elif choice.lower() == 's':
                        stopped = True
                        break
                    elif choice.lower() == 'r':
                        paused = False
                        pygame.mixer.music.unpause()
                        print("Music resumed.")
                        
                    else:
                        speak("invalid choice")
                        print("Invalid choice.")
        if stopped:
            break
    print("Playlist Finished")
    speak("Playlist Finished")





def create_file():
    # Get file path and name from user
    speak("tell me the file name")
    print("Tell the file name you want to create:")
    file_name = listen().strip()
    
    speak("Enter the file path")
    file_path = input("Enter the file path: ")
    

# Combine the path and name to create the complete file path
    complete_path = os.path.join(file_path, file_name)
    allowed_path = "D:\\"  # Replace with your allowed path

    # Check if the specified path is allowed
    if not complete_path.startswith(allowed_path):
        speak("Access is restricted")
        print("Folder creation is restricted to a specific path.You can only work within D: drive")
        return


# Open the file in write mode ('w') and write content if needed
    with open(complete_path, 'w') as file:
       file.write("Hello, this is a new file!")
    speak("File is created successfully")
    print(f"File '{file_name}' created at '{file_path}'.")
    


def delete_file():
    speak("tell me the file name")
    print("Tell the file name you want to delete:")
    file_name = listen().strip()
    speak("Enter the path of the file you want to delete")
    file_path=input("Enter the file path:")
    
# Concatenate file path and name to create the full file path
    full_file_path = os.path.join(file_path, file_name)
    allowed_path = "D:\\"  # Replace with your allowed path

    # Check if the specified path is allowed
    if not full_file_path.startswith(allowed_path):
        speak("Access Denied")
        print("Folder deletion is restricted to a specific path.You can only work within D: drive")
        return

    try:
    # Attempt to remove the file
      os.remove(full_file_path)
      speak(f'The file {file_name} has been successfully deleted.')
      print(f'The file {file_name} has been successfully deleted.')
    except OSError as e:
    # Handle the case where the file cannot be removed
      speak(f"Error: {file_name} - {e}")
      print(f"Error: {file_name} - {e}")





def who_are_you():
    speak("I'm Mechion AI Assitant. I'm here to provide you some help")
    print("I'm Mechion AI Assitant. I'm here to provide you some help")

def current_time():
    current_hour = datetime.now().hour

    if 5 <= current_hour < 12:
        greeting = "Good morning"
    elif 12 <= current_hour < 17:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    time_to_tell = datetime.now().strftime("%H:%M")

    # Combine greeting and time
    message = f"{greeting}. The current time is {time_to_tell}"
    speak(message)
  
def listen_withoutCMD():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Can you please repeat?")
        return listen()

def create_folder_with_user_input():
    speak("tell me the folder name you want to create")
    print("tell me the folder name you want to create")
    folder_name = listen().strip() 
    print("you said:".folder_name)
    folder_path = input("Enter the folder path: ")

    # Validate if the entered path is a valid directory
    while not os.path.isdir(folder_path):
        speak("Enter correct path")
        print("Invalid folder path. Please enter a valid directory.")
        folder_path = input("Enter the folder path: ")

    full_path = os.path.join(folder_path, folder_name)

    try:
        os.makedirs(full_path)
        speak("folder created successfully")
        print(f"Folder created successfully: {full_path}")
        
    except FileExistsError:
        speak("Folder already exists")
        print(f"Folder already exists: {full_path}")
        
    except Exception as e:
        speak("An error occured")
        print(f"Error creating folder: {e}")
        
    

     # Restrict folder creation to a specific path
    allowed_path = "D:\\"  # Replace with your allowed path

    # Check if the specified path is allowed
    if not folder_path.startswith(allowed_path):
        speak("Access Denied")
        print("Folder creation is restricted to a specific path.You can only work within D: drive")
        
        return

def delete_folder():
    speak("tell me the name of folder you want to delete")
    print("tell me the name of folder you want to delete")
    folder_name = listen().strip() 
    print("you said:",folder_name)
    folder_path = input("Enter the folder path: ")

    # Validate if the entered path is a valid directory
    while not os.path.isdir(folder_path):
        speak("Enter correct path")
        print("Invalid folder path. Please enter a valid directory.")
        speak("Enter folder path")
        folder_path = input("Enter the folder path: ")

    full_path = os.path.join(folder_path, folder_name)
    try:
        # Remove the folder and its contents
        os.rmdir(full_path)
        speak(f"Folder '{folder_name}' deleted successfully.")
        print(f"Folder '{folder_name}' deleted successfully.")
    except OSError as e:
        speak("An error occured")
        print(f"Error: {e}")
        print(f"Failed to delete the folder '{folder_name}'.")

      # Restrict folder creation to a specific path
    allowed_path = "D:\\"  # Replace with your allowed path

    # Check if the specified path is allowed
    if not folder_path.startswith(allowed_path):
        speak("Access denied")
        print("Folder creation is restricted to a specific path.You can only work within D: drive")
        return

def temperature():
    search="temperature in chennai"
    url=f"https://www.google.com/search?q={search}"
    r=requests.get(url)
    data=BeautifulSoup(r.text,"html.parser")
    temp=data.find("div",class_="BNeawe").text
    print(temp)
    speak(f"current{search}is {temp}")


def rename_folder():
    # Get folder path from the user
    folder_path = input("Enter the folder path: ")

    # Verify if the folder path exists
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        print(f"Folder path '{folder_path}' does not exist.")
        return

    # Get existing folder name from the user
    speak(" tell me existing name of the folder you want to rename")
    print("tell me existing name of the folder you want to rename ")
    old_name = listen().strip()
    print("you said:",old_name)

    # Verify if the existing folder exists
    old_path = os.path.join(folder_path, old_name)
    if not os.path.exists(old_path) or not os.path.isdir(old_path):
        print(f"Folder '{old_name}' does not exist in the specified path.")
        return

    # Get new folder name from the user
    speak(" tell me the new name")
    print("tell me the new name")
    new_name = listen().strip()
    print("you said:",new_name)

    try:
        # Construct the full paths for the old and new folder names
        new_path = os.path.join(folder_path, new_name)

        # Rename the folder
        os.rename(old_path, new_path)
        speak("Folder has been renamed successfully")
        print(f"Folder '{old_name}' in path '{folder_path}' renamed to '{new_name}' successfully.")
    except Exception as e:
        speak("An error occured")
        print(f"Error renaming folder: {e}")
    
    allowed_path = "D:\\"  # Replace with your allowed path

    # Check if the specified path is allowed
    if not folder_path.startswith(allowed_path):
        speak("Access denied")
        print("Folder creation is restricted to a specific path.You can only work within D: drive")
        return


def google_search(query):
    if "google" in query:
        import wikipedia as googleScrap
    
        speak("This is what I found on google")
        try:
            pywhatkit.search(query)
            result=googleScrap.summary(query,2)
            speak(result)
        except:
            speak("No speakable output available")


def search_in_youtube(query):
    if "youtube" in query:
        speak("This is what I found on youtube")
        print("This is what I found on youtube")

        web="https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done")


def search_in_wikipedia(query):
    if "wikipedia" in query:
        import wikipedia
        results=wikipedia.summary(query,sentences=2)
        print("This is what I found on wikipedia")
        print(results)
        speak(results)

def volumeup():
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)

def volumedown():
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)


def fetch_news(api_key, topic='general', country='us'):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&category={topic}&apiKey={api_key}'
    response = requests.get(url)
    data = response.json()
    if data['status'] == 'ok':
        articles = data['articles']
        return articles
    else:
        print("Failed to fetch news:", data['message'])
        return []

def speak_news(articles):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    for index, article in enumerate(articles):
        headline = article['title']
        description = article['description']
        engine.say(f"News {index + 1}: {headline}")
        print(description)
        engine.say(headline)
       
    engine.runAndWait()

def jarvis_tell_news(api_key, topic='entertainment'):
    articles = fetch_news(api_key, topic)
    if articles:
        speak_news(articles)    
    else:
        print("No news available.")


    
def send_whatsapp_message(phone_number, message ,time_hour, time_minute):
       time.sleep(20)
       pywhatkit.sendwhatmsg(phone_number, message,time_hour, time_minute)
       time.sleep(3)  # Wait for 3 seconds to ensure the chat window is focused
       pyautogui.press('enter')
def shutdown_system():
    # Execute the shutdown command based on the operating system
    
    if os.name == 'nt':  # Windows
        os.system('shutdown /s /t 0')


activities = []

def add_activity(name, date_time):
    activity = {"name": name, "date_time": date_time}
    activities.append(activity)
    print("Activity added successfully!")

def display_activities():
    if not activities:
        print("No activities scheduled.")
    else:
        for index, activity in enumerate(activities, start=1):
            print(f"{index}. {activity['name']} - {activity['date_time']}")

        
def check_internet_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1e+6  # Convert to Mbps
    upload_speed = st.upload() / 1e+6  # Convert to Mbps
    ping = st.results.ping

    print("Download Speed: {:.2f} Mbps".format(download_speed))
    print("Upload Speed: {:.2f} Mbps".format(upload_speed))
    print("Ping: {} ms".format(ping))
    
def fetch_cricket_scores(api_key):
    url = "https://unofficial-cricbuzz.p.rapidapi.com/matches/get-hscorecard?matchId=43781"
    headers = {
        "X-RapidAPI-Key": "9b4a805180msh7bde5c0f7ab5d77p1d3c7ejsn92fed90b2679",
        "X-RapidAPI-Host": "unofficial-cricbuzz.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to retrieve data.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)
        return

    data = response.json()
    print("Raw JSON Response:", data)

    # Check if the response is a list of matches
    if isinstance(data, list):
        for match in data:
            # Print each match to understand its structure
            print("Match Data:", match)
            # Assuming the match dictionary contains keys 'team_1', 'team_2', 'match_status', and 'score'
            if 'team_1' in match and 'team_2' in match:
                print(f"{match['team_1']} vs {match['team_2']}")
                print(f"Match Status: {match['match_status']}")
                print(f"Score: {match['score']}\n")
    else:
        print("Unexpected data format:", data)

# Replace 'your_api_key' with your actual RapidAPI key
api_key = 'your_api_key'
fetch_cricket_scores(api_key)


# Function to check if the current player has won
def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full (tie)
def check_tie(board):
    return all(cell != ' ' for row in board for cell in row)

# Function for Mechion to make a move in Tic Tac Toe
def jarvis_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(empty_cells) if empty_cells else None

# Function to play Tic Tac Toe
def play_tic_tac_toe():
    print("Let's play Tic Tac Toe!")
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    while True:
        print_board(board)
        if player == 'X':
            row, col = map(int, input("Enter row and column to place your 'X' (e.g., 1 2): ").split())
            if board[row - 1][col - 1] != ' ':
                print("Invalid move. That cell is already occupied.")
                continue
            board[row - 1][col - 1] = 'X'
        else:
            row, col = jarvis_move(board)
            if row is None:
                print("It's a tie!")
                break
            board[row][col] = 'O'
        if check_win(board, player):
            print_board(board)
            print(f"{player} wins!")
            break
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break
        player = 'X' if player == 'O' else 'O'

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 5)

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_tie(board):
    return all(cell != ' ' for row in board for cell in row)

def jarvis_move(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                return row, col
    return None, None

# Function to play the dice game
def play_dice_game():
    print("Let's play the Dice Game!")
    user_score = random.randint(1, 6)
    jarvis_score = random.randint(1, 6)
    print(f"You rolled: {user_score}")
    print(f"Jarvis rolled: {jarvis_score}")
    if user_score > jarvis_score:
        print("You win!")
    elif user_score < jarvis_score:
        print("Jarvis wins!")
    else:
        print("It's a tie!")

# Function to play Rock-Paper-Scissors
def play_rock_paper_scissors():
    speak("Let's play Rock-Paper-Scissors!")
    print("Let's play Rock-Paper-Scissors!")
    options = ['rock', 'paper', 'scissors']
    jarvis_choice = random.choice(options)
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    if user_choice not in options:
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
        return
    print("Jarvis chose:", jarvis_choice)
    if user_choice == jarvis_choice:
        speak("It's a tie!")
        print("It's a tie!")

    elif (user_choice == 'rock' and jarvis_choice == 'scissors') or \
         (user_choice == 'paper' and jarvis_choice == 'rock') or \
         (user_choice == 'scissors' and jarvis_choice == 'paper'):
        speak("You win!")
        print("You win!")
    else:
        speak("Mechion wins!")
        print("Mechion wins!")


def get_location():
    try:
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        return data.get('city'), data.get('region'), data.get('country')
    except Exception as e:
        print("Error fetching location:", e)
        return None, None, None

def speak_location(city, region, country):
    engine = pyttsx3.init()
    engine.say(f"You are currently in {city}, {region}, {country}.")
    print(f"You are currently in {city}, {region}, {country}.")
    engine.runAndWait()


def perform_basic_arithmetic_operations():
    speak("Please select operation:")
    print("Please select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1/2/3/4): ")
    if choice not in ['1', '2', '3', '4']:
        speak("Invalid input")
        print("Invalid input")
        return

    speak("tell me the first number:")
    num1 = float(input("Enter first number:"))
    
    speak("tell me the second number:")
    
    num2 = float(input("Enter second number:"))

    if choice == '1':
        result = num1 + num2
    elif choice == '2':
        result = num1 - num2
    elif choice == '3':
        result = num1 * num2
    elif choice == '4':
        if num2 == 0:
            speak("Division by zero is not allowed")
            print("Division by zero is not allowed")
            return
        result = num1 / num2

    print("The result is:", result)
    speak("The result is: " + str(result))


def perform_geometrical_calculations():
    speak("Please select operation:")
    print("Please select operation:")
    print("1. Calculate Area")
    print("2. Calculate Perimeter")

    choice =input("Enter choice (1/2): ")
    if choice not in ['1', '2']:
        speak("Invalid input")
        print("Invalid input")
        return

    if choice == '1':  # Area calculation
        speak("Please select shape:")
        print("Please select shape:")
        print("1. Rectangle")
        print("2. Circle")
        
        shape_choice = input("Enter your choice:")
        if shape_choice == '1':
            speak("Enter length of the rectangle:")
            length =float(input("Enter length of the rectangle "))
            speak("Enter width of the rectangle:")
            width = float(input("Enter width of the rectangle:"))
            area = length * width
            print("The area of the rectangle is:", area)
            speak("The area of the rectangle is: " + str(area))
        elif shape_choice == '2':
            speak("Enter radius of the circle:")
            
            radius = float(input("Enter radius of the circle:"))
            area = 3.14159 * radius ** 2
            print("The area of the circle is:", area)
            speak("The area of the circle is: " + str(area))
        else:
            speak("Invalid input")
            print("Invalid input")
    elif choice == '2':  # Perimeter calculation
        speak("Please select shape:")
        print("Please select shape:")
        print("1. Rectangle")
        print("2. Circle")
        
        
        shape_choice = input("Enter your choice:")
        if shape_choice == '1':
            speak("Enter length of the rectangle:")
            length = float(input("Enter length of the rectangle:"))
            speak("Enter width of the rectangle:")
            width = float(input("Enter width of the rectangle:"))
            perimeter = 2 * (length + width)
            print("The perimeter of the rectangle is:", perimeter)
            speak("The perimeter of the rectangle is: " + str(perimeter))
        elif shape_choice == '2':
            speak("Enter radius of the circle:")
            radius = float(input("Enter radius of the circle:"))
            perimeter = 2 * 3.14159 * radius
            print("The perimeter of the circle is:", perimeter)
            speak("The perimeter of the circle is: " + str(perimeter))
        else:
            speak("Invalid input")
            print("Invalid input")


def send_email(to_email, subject, message):
    from_email = "sakthipriya4428@gmail.com"
    app_password="stks ijok hsrk uzew"
    
    
    # Setting up the MIME
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # Adding the message body
    msg.attach(MIMEText(message, 'plain'))
    
    try:
        # Connect to the server and send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Replace with your SMTP server details
        server.starttls()
        server.login(from_email, app_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")


def fetch_definition(api_key, word):
    url = f"https://dictionary-by-api-ninjas.p.rapidapi.com/v1/dictionary?word=bright"
    
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "api.dictionaryapi.dev"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to retrieve data.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)
        return

    data = response.json()

    # Check if the word exists in the dictionary
    if isinstance(data, list):
        if len(data) == 0:
            print("Word not found in the dictionary.")
            return

        # Extract and print the definition
        print(f"Definition of '{word}':")
        for entry in data:
            for meaning in entry['meanings']:
                print(f"- {meaning['definitions'][0]['definition']}")


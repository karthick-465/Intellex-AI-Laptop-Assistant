import pickle
import nltk
nltk.download('punkt_tab')
from sklearn.base import ClassifierMixin
from NBC import preprocess_text
from functions import *
from nltk.classify import NaiveBayesClassifier
import sys
import datetime
import speedtest
import requests
import time
import keyboard




if __name__ == "__main__":
    print('app started ')
    speak("Hello, I am your AI assistant. How can I assist you today?")
    with open('naive_bayes_model.pkl', 'rb') as model_file:
            trained_classifier = pickle.load(model_file)
    # trained_classifier.classify(preprocess_text(command))
    while True:
        command = listen()
        
        # with open('naive_bayes_model.pkl', 'rb') as model_file:
        #     trained_classifier = pickle.load(model_file)
        trained_classifier.classify(preprocess_text(command))
        # classifier.classify(preprocess_text(user_command))
        predicted_action = trained_classifier.classify(preprocess_text(command))
        

        if predicted_action:
            if "open file explorer" in predicted_action:
                open_file_explorer()
            elif "close file explorer" in predicted_action:
                close_file_explorer()
            elif "open paint" in predicted_action:
                open_paint()
            elif "close paint" in predicted_action:
                close_paint()
            elif "open browser" in predicted_action:
                open_browser()
            elif "close browser" in predicted_action:
                close_browser()
            elif "search in google" in predicted_action:
                query = command.replace("search in google", "").strip()
                google_search(query)
            elif "search in wikipedia" in predicted_action:
                query = command.replace("search in wikipedia", "").strip()
                search_in_wikipedia(query)   
            elif "temperature" in predicted_action:
                temperature()
            
            
            
            elif "shut down" in predicted_action:
                shutdown_system()

            
            elif "whatsapp" in predicted_action:
                speak("You can now send messages in whatsapp using Mechion")
                print("You can now send messages in whatsapp using Mechion")
                speak("enter phone number")
                phone_number=input("enter phone number with recipitent code ")
                speak("what is the message you want to send")
                message = listen().strip()
                print("you said:",message)
                time_hour = int(input("Enter the hour to send the message (0-23): "))
                time_minute = int(input("Enter the minute to send the message (0-59): "))
                whatsapp_thread = threading.Thread(target=send_whatsapp_message, args=(phone_number, message, time_hour, time_minute))
                whatsapp_thread.start()

               
           
                
            elif "alarm" in predicted_action:
               current_time = time.localtime()
               print("current time",current_time)
               time_text = input("Enter the alarm time (format: hour:minute): ")
               set_alarm_from_text(time_text)         
               

            elif "remainder" in predicted_action:
                hour = int(input("Enter the hour for the reminder (0-23): "))
                minute = int(input("Enter the minute for the reminder (0-59): "))
                message = input("Enter the reminder message: ")
                reminder_time = set_reminder(hour, minute, message)
                
                while True:
                    check_reminder(reminder_time, message)
                    time.sleep(1)

            elif "playlist" in predicted_action:
                playlist = []

                while True:
                   speak("Create a playlist and enjoy songs you like")
                   print("YOUR PLAYLIST!")
                   print("1. Add song to playlist")
                   print("2. Play playlist")
                   print("3. Exit")
                   speak("enter your choice")
                   choice = input("Enter your choice: ")

                   if choice == "1":
                      speak("enter the name of the song")
                      song = input("Enter the name of the song: ") 
                      add_song(playlist, song)
                   elif choice == "2":
                        play_playlist(playlist)
                   elif choice == "3":
                      speak("visit again thank you")
                      print("visit again thank you")
                      break
                   else:
                      speak("Invalid choice. Please try again.")
                      print("Invalid choice. Please try again.")
            
            
     
            elif "schedule" in predicted_action:

                speak("Welcome to Mechion Scheduler")
                print("Welcome to Mechion Scheduler!")
                while True:
                   print("\n1. Add Activity")
                   print("2. View Activities")
                   print("3. Exit")

                   speak("Enter your choice")
                   choice = input("Enter your choice")

                   if choice == "1":
                      name = input("Enter the activity:")
                      date_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
                      try:
                         date_time = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                         add_activity(name, date_time)
                      except ValueError:
                         print("Invalid date/time format. Please try again.")

                   elif choice == "2":
                      display_activities()

                   elif choice == "3":
                      print("Exiting...")
                      break

                   else:
                     print("Invalid choice! Please try again.")
                     
            elif "latest news" in predicted_action:
                api_key = "cf7e260f1f5445618c66eb426b86c526"  # Replace "YOUR_API_KEY" with your News API key
                topic = 'entertainment'  # Change the topic if needed

                jarvis_tell_news(api_key, topic)

                
                

            elif "internet speed" in predicted_action:
                speed = check_internet_speed()
                if speed is not None:
                   print(f"Internet Speed: {speed:.2f} Mbps")
                else:
                   print("Failed to check internet speed.")

               
            elif "cricket score" in predicted_action:
                speak("This is cricket score I have fetched")
            elif "games" in predicted_action:
                speak("Welcome to Mechion Game Center!")
                print("Welcome to Mechion Game Center!")
                while True:
                    speak("\nChoose a game to play:")
                    print("\nChoose a game to play:")
                    print("1. Tic Tac Toe")
                    print("2. Dice Game")
                    print("3. Rock-Paper-Scissors")
                    print("4. Quit")
                    choice = input("Enter your choice (1-4): ")

                    if choice == '1':
                       play_tic_tac_toe()
                    elif choice == '2':
                       play_dice_game()
                    elif choice == '3':
                      play_rock_paper_scissors()
                    elif choice == '4': 
                      print("Goodbye!")
                      speak("Goodbye!")
                      break
                    else:
                      speak("Invalid choice. Please enter a number between 1 and 4.")
                      print("Invalid choice. Please enter a number between 1 and 4.")

            elif "location" in predicted_action:
                city, region, country = get_location()
                if city and region and country:
                     speak_location(city, region, country)
                else:
                     print("Unable to determine location.")
            elif "calculator" in predicted_action:
                while True:
                    speak("Welcome to Mechion calculator. Please select operation:")
                    print("Welcome to Mechion calculator. Please select operation:")
                    print("1. Basic Arithmetic Operations")
                    print("2. Geometrical Calculations")
                    print("3. Quit!")
    
                    choice = input("Enter choice (1/2): ")
                    if choice == '1':
                       perform_basic_arithmetic_operations()
                    elif choice == '2':
                       perform_geometrical_calculations()
    
                    elif choice == '3':
                       print("Good Bye")
                       break
                    else:
                       speak("Invalid input")
                       print("Invalid input")

                
            elif "open youtube" in predicted_action:
                open_youtube()
            elif "close youtube" in predicted_action:
                close_youtube() 
            elif "search in youtube" in predicted_action:
                query = command.replace("search in youtube", "").strip()
                search_in_youtube(query)
            elif "increase volume" in predicted_action:
                adjust_volume('increase',1.0)
            elif "decrease volume" in predicted_action:
                adjust_volume('decrease',1.0)
            elif "time" in predicted_action:
                current_time()
            
            elif "increase brightness" in predicted_action:
                increase_brightness()
            elif "decrease brightness" in predicted_action:
                decrease_brightness()
            elif "create file" in predicted_action:
                create_file()
            elif "delete file" in predicted_action:
                delete_file()
            
            elif "who are you" in predicted_action:
                who_are_you()
            elif "create folder" in predicted_action:
                create_folder_with_user_input()
            elif "delete folder" in predicted_action:
                delete_folder()
            elif "rename folder" in predicted_action:
                rename_folder()
            elif "pause video" in predicted_action:
                pyautogui.press("k")
                speak("video has been paused")

            elif "play video" in predicted_action:
                pyautogui.press("k")
            elif "mute video" in predicted_action:
                pyautogui.press("m")
                speak("video muted")

            elif "video volume up" in predicted_action:
                volumeup()
                speak("Turning volume up")
            elif "video volume down" in predicted_action:
                volumedown()
                speak("Turning volume down")
            elif "mail" in predicted_action:
                 speak("Please say the recipient's email address.")
                 to_email = input("Please say the recipient's email address:")
                 if to_email:
                    speak("Please say the subject of the email")
                    subject = listen("Please say the subject of the email.")
                 if subject:
                    speak("Please dictate your message.")
                    message = listen("Please dictate your message.")
                 if message:
                     send_email(to_email, subject, message)
            
            elif "dictionary" in predicted_action:
                api_key = 'your_api_key'
                word = input("Enter a word: ")
                fetch_definition(api_key, word)


                
            elif "exit" in predicted_action or "bye" in predicted_action:
                speak("Goodbye!")
                break
            else:
                speak("I'm sorry, I don't understand that command. Can you please repeat?")
           
           
            
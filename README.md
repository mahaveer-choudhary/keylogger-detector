
# KEYLOGGER DETECTOR 

warns the user when a malicious program or keylogger tries to send data from your device.

## Description 

This keylogger detector is a python script designed to identify and locate potential keyloggers running on a system. It scans specific Directories for python scripts exhibiting keylogger patterns, providing users with the ability to take actions against detecting keylogger in your system. 

Keylogger detector aims to provide extra layer of security by providing a montoring tool that monitors the common ways keylogger send the information from the computer to the hacker and warns the user for the same. 

This tool is useful for users who want to ensure the security of their system and protect against potential threats posed by keyloggers. 
It offers the flexibility to block, or remove or investigate the location of the identified keylogger script. 

### Email monitoring 
keyloggers work by logging all the keystrokes and storing the file locally for a fixed period of time, after which they send the log file to the hacker through a email.
Keylogger Detector monitors most used SMTP ports to detect the processes trying to communicate using 
#### Popular SMTP servers monitored by keylogger detector 
```smtp.gmail.com          ssl             465
   smtp.gmail.com          StartTLS        587
   smtp.live               StartTLS        587
   smtp.office365.com      StartTLS        587
   smtp.mail.yahoo.com     StartTLS        587
```

## Installation 

To use the Keylogger detector, use these steps : 

Clone the repository in your local machine 

  ```bash
git clone https://github.com/mahaveer-choudhary/keylogger-detector

  ```
navigate to the directory 
  ```bash
 cd keylogger-detector
  ```

run the script 
  ```bash
sudo python keylogger-detector.py
```
This will setup keylogger detector in your machine. Make sure that you have installed python's latest version in your machine.

## Usage 

1. Run the script
   ```bash
   sudo python keylogger-detector.py
   ```

   1. Choose your option from menu:
      option 1 : Scan for a particular location
      option 2 : Detect keylogger automatically
      option 3 : Exit

   2. Depending on your choice, follow the on-screen instructions.
      * For scanning a particular location, Enter the directory or drive path to scan.
      * To detect the keyloggers, follow the prompts and take necessary actions.
      * Use option 3 to exit the program.

      The keylogger detector provide feedback based on your actions you choose, helping you identify and handle potential keylogger on your system.


!(https://drive.google.com/file/d/1tYl4sIZIH2Kfm8UbI1wZPpaQTLBAWk8G/view?usp=sharing)

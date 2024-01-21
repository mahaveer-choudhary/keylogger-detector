#!/usr/bin/env python

import os
import re
import shlex
import subprocess
from os.path import exists
import getopt
import sys
import os.path
import psutil
from rich.console import Console
from colorama import Fore, Style
import time as mahi
import shutil
console = Console()


logo = """

   \033[91m▄█   ▄█▄    ▄████████ ▄██   ▄    ▄█        ▄██████▄     ▄██████▄     ▄██████▄     ▄████████    ▄████████ 
  \033[91m███ ▄███▀   ███    ███ ███   ██▄ ███       ███    ███   ███    ███   ███    ███   ███    ███   ███    ███ 
  \033[91m███▐██▀     ███    █▀  ███▄▄▄███ ███       ███    ███   ███    █▀    ███    █▀    ███    █▀    ███    ███ 
 \033[91m▄█████▀     ▄███▄▄▄     ▀▀▀▀▀▀███ ███       ███    ███  ▄███         ▄███         ▄███▄▄▄      ▄███▄▄▄▄██▀ 
\033[91m▀▀█████▄    ▀▀███▀▀▀     ▄██   ███ ███       ███    ███ ▀▀███ ████▄  ▀▀███ ████▄  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
  \033[91m███▐██▄     ███    █▄  ███   ███ ███       ███    ███   ███    ███   ███    ███   ███    █▄  ▀███████████ 
  \033[91m███ ▀███▄   ███    ███ ███   ███ ███▌    ▄ ███    ███   ███    ███   ███    ███   ███    ███   ███    ███ 
  \033[91m███   ▀█▀   ██████████  ▀█████▀  █████▄▄██  ▀██████▀    ████████▀    ████████▀    ██████████   ███    ███ 
  \033[91m▀                                ▀                                                             ███    ███ 


                \033[91m████████▄     ▄████████     ███        ▄████████  ▄████████     ███      ▄██████▄     ▄████████ 
                \033[91m███   ▀███   ███    ███ ▀█████████▄   ███    ███ ███    ███ ▀█████████▄ ███    ███   ███    ███ 
                \033[91m███    ███   ███    █▀     ▀███▀▀██   ███    █▀  ███    █▀     ▀███▀▀██ ███    ███   ███    ███ 
                \033[91m███    ███  ▄███▄▄▄         ███   ▀  ▄███▄▄▄     ███            ███   ▀ ███    ███  ▄███▄▄▄▄██▀ 
                \033[91m███    ███ ▀▀███▀▀▀         ███     ▀▀███▀▀▀     ███            ███     ███    ███ ▀▀███▀▀▀▀▀   
                \033[91m███    ███   ███    █▄      ███       ███    █▄  ███    █▄      ███     ███    ███ ▀███████████ 
                \033[91m███   ▄███   ███    ███     ███       ███    ███ ███    ███     ███     ███    ███   ███    ███ 
                \033[91m████████▀    ██████████    ▄████▀     ██████████ ████████▀     ▄████▀    ▀██████▀    ███    ███ 
                                                                                    

"""
print(logo)

# Extra functions of stopping keylogger....

def block_keylogger():
    # implementing blocking of keylogger code...!
    print("blocking keylogger...!")

    # rest code here ....

    print("Thank you ..")



def center(message):
    terminal_width = os.get_terminal_size().columns
    padding = (terminal_width - len(message)) // 2
    return " " * padding + message

color = """ \033[91m """


# ------------------------------progress bar ----------
def run_command(command):
    try:
        
        result=subprocess.run(command,shell=True,check=True, stdout=subprocess.PIPE, text=True)
	
        #print("output: ")
        #print(result.stdout)
	
    except subprocess.CalledProcessError as e:
        print(f"Error : {e}")


# -------------1st function ---------------------------
def find_location(pid):
    # implementing find of location of keylogger ...!
    print("finding location...!")

    # rest code here ....

    try:
      process = psutil.Process(pid)
      executable_path = process.exe()
      command_line = " ".join(process.cmdline())
      file_name = command_line.split()[-1]
      #return file_name

      # using locate command to find the file 
      file_paths = locate_file(file_name)
      print(f"The name of the file is : {file_name}")

      if file_paths :
        print(f"The name of the file is : {file_name}")
        for path in file_paths:
          print("The location of file is :",path)
          print("We successfully detected the location of the process ..")

          # returning the path to other function 
          return path

      else :
        #print(f"File {file_name} not found.")
        print(f"Sorry we can't find location of {file_name}")
        print("But no worries, you can run your custom command here ")
        print()
        #print("Sorry we can't detect the location of the file !")
        
        user_command = input("Enter the command to run : ")
        run_command(user_command)

    except psutil.NoSuchProcess:
      print("Process not found.")


    
    print("Thank you ..")



def locate_file(file_name):
    try:
        #result = subprocess.run(["locate", file_name], check=True, capture_output=True, text=True)
        result = subprocess.run(["find / {file_name} | grep {file_name}", file_name], check=True, capture_output=True, text=True)
        return result.stdout.strip().split('\n')
    except subprocess.CalledProcessError:
        return None



# ---------------------------------------------------
def remove_file(file_path):
  try:
    os.remove(file_path)
    print(f"File removed successfully : {file_path}")

  except OSError as e:
    print(f"Error removing file {file_path}: {e}")

  except Exception as ex:
    print(f"An unexcepted error occured : {ex}")
# --------------1st function complete -----------------

# --------------2nd function for option3----------------------------------
def find_location2(pid):
    # implementing find of location of keylogger ....!

    try:
        process = psutil.Process(pid)
        executable_path = process.exe()
        command_line = " ".join(process.cmdline())
        file_name = command_line.split()[-1]

        # using locate command to find the file 
        file_paths = locate_file(file_name)

        if file_paths:
            #print(file_name)
            for path in file_paths:
                print(path)
                return path 
        else :
            print("file not found")

    except psutil.NoSuchProcess:
        print("process not found")

def locate_file(file_name):
    try:
        result = subprocess.run(["locate",file_name], check=True, capture_output=True, text=True)
        return result.stdout.strip().split('\n')
    except subprocess.CalledProcessError:
        return None

def remove_file2(file_path):
    try:
        os.remove(file_path)
        print(f"File removed successfully : {file_path}")
    except OSError as e:
        print(f"Error removing file {file_path}: {e}")
    except Exception as ex:
        print(f"An unexcepted error occured : {ex}")


# ---------------2nd function close ---------------------------

def exit():
    # code of exiting from the script ...!
    print("Bye ... ")
    print("We are Signing Off ...")

    # rest code here ....

    print("Thank you for using this application ..")


def exit2():
    print("we are going back to main menu ... ")


def center1(text, width=40):
  left_padding = (width - len(text)) // 2
  centered_text = " " * left_padding + text
  return centered_text

# ----------------------------------------------------------------------------
console.print(center("[bold green]welcome to keylogger detector...![/bold green]"))
print()
print(color)   

# running command for updating the database 
upcommand = "sudo updatedb"
run_command(upcommand)
while True:
    

    # short_options = "har"
    # long_options = ["help","add-to-startup","remove-from-startup"]
    
    print("choose you want to do : ")
    print("1. Scan for a particular location : ")
    print("2. Detect keylogger : ")
    print("3. Exit")
    
    user_input = input("Choose your option : ")

    if not user_input:
      print("Invalid input. Please enter a value.")
      continue

    opt = int(user_input)


    #opt = int(input("Choose your option : "))

    if (opt == 1):
        print("you choose for a particular location ..")
        # loc = str(input("Enter your location : "))

        # --------------------------------------------------------------

        def detect_keylogger(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                script_content = file.read()

                # checking for common keylogger patterns ...
                keylogger_patterns = [
                    r'pynput\.keyboard\.Listener',
                    r'logging\.basicConfig\(',
                    r'on_press\(',
                    r'logging\.info\('
                ]

                for pattern in keylogger_patterns:
                    if re.search(pattern, script_content):
                        return True

                return False

        def scan_directory(directory_path):
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    if file_path.endswith('.py') and detect_keylogger(file_path):
                        print(f'Keylogger successfully detected in: {file_path}')

                        # new code --------- xxxx --------------------------
                        print("Options :")
                        print("1. Block ")
                        print("2. Remove ")
                        print("3. Exit")

                        choice = input("Enter your choice (1/2) :")

                        if choice == '1':
                            block_keylogger()
                        elif choice == '2':
                            remove_keylogger()
                        if choice == '3':
                            exit()
                        else:
                            print("Invalid .. Try again !")

            # code finish ------------- xxxx -----------------------------

        # location = input("Enter your location : ")

        # scanning for location ....
        if __name__ == "__main__":
            scan_location = input("Enter the directory or drive path to scan : ")
            scan_directory(scan_location)

        print("Scan complete ")
# ------------------------------------------------------

    elif (opt == 2):
        print("you choose for detecting keylogger ..")

        time = 1
        black_list = []
        white_list = []

        # ----------

        detected = False

        # -------------

        short_options = "har"
        long_options = ["help", "add-to-startup", "remove-from-startup"]

        # remove 1st argument from the list of arguments
        argumentList = sys.argv[1:]

        # autostart directory
        autostart_path = os.path.expanduser('~/.config.autostart/')

        # arguments dealt with here
        if argumentList:
            try:
                arguments, values = getopt.getopt(argumentList, short_options, long_options)
                for opt, arg in arguments:
                    if opt in ('-h', "--help"):
                        print("Available arguments:\n"
                              "-h/--help shows this menu\n"
                              "-a/ --add-to-startup Adds program to startup directory\n"
                              "-r/--remove-from-startup remove from startup directory.")

                    elif opt in ('a', "--add-to-startup"):

                        # create autostart directory if it does not exist
                        start_directory = exists(autostart_path)
                        if not start_directory:
                            os.makedirs(autostart_path, mode=0o77, exist_ok=False)

                        # check if file already exists in startup
                        program_path = exists(os.path.join(autostart_path, 'Keylogger-detector'))
                        if program_path:
                            print("Error: Program already exists in startup. ")

                        else:
                            # create .desktop file to place in the startup folder
                            with open(os.path.join(autostart_path, 'Keylogger-detector'), "w") as file1:
                                toFile = ('[Desktop Entry]\n'
                                          'Version=v0.1\n'
                                          'Type=Applocation\n'
                                          'Name=Keylogger-detector\n'
                                          f'Exec=python3{os.getcwd()}/Keylogger-detector\n'
                                          'Terminal=True')
                                file1.write(toFile)

                            # give permissions to launch
                            st = os.stat(os.path.join(autostart_path, 'Keylogger-detector'))

                            # only file owner can write to file, others can read - 664
                            os.chmod(os.path.join(autostart_path, 'Keylogger-detector'), 0o664)
                            check_exists = exists(autostart_path)
                            if check_exists:
                                print("Program successfully added to startup...")
                            else:
                                print("Program was not added to startup. Please try again.")

                    elif opt in ('r', "--remove-from-startup"):
                        program_path = exists(os.path.join(autostart_path, 'Keylogger-detector'))
                        if program_path:
                            os.remove(os.path.join(autostart_path, 'Keylogger-detector'))
                            if not program_path:
                                print("File removed successfully...")

                            else:
                                print("Error: Program does not exist in the startup directory. ")

            except getopt.error as err:
                # output error and return error code
                print(str(err))

        else:
            while True:
                if time == 1:
                    print("\nScanning in progress.....")

# _---------------------progress bar ----------------------------------------------------------
                    def get_terminal_width():
                        return shutil.get_terminal_size().columns

                    def rolling_progress_bar(total, bar_length=70):
                        for i in range(total):
                            progress = i / total
                            bar_progress = int(bar_length * progress)
                            bar_str = "█" * bar_progress + "-" * (bar_length - bar_progress)
                            percentage_str = f"{int(progress * 100)}%"
        
                            colored_progress = f"\r[{Fore.GREEN}{bar_str}{Style.RESET_ALL}] Progress: {percentage_str}"
                            print(colored_progress, end='', flush=True)

                            mahi.sleep(0.1)
        
                    rolling_progress_bar(50)
                    print()
                    print()
                    print(color)
# _---------------------progress bar ----------------------------------------------------------

                command = shlex.split('lsof -nP -iTCP:587 -iTCP:465 -iTCP:2525')
                proc = subprocess.Popen(command, stdout=subprocess.PIPE)
                out, err = proc.communicate()
                output = out.decode()
                time += 1

                if "ESTABLISHED" in output:
                    output = output.split(" ")

                    # delete empty array elements
                    my_list = list(filter(None, output))

                    # full IP address with port number
                    port_num = my_list[-2]

                    # split at the ':' to get port number at the last index of the array
                    get_port = port_num.split(":")
                    port = get_port[-1]
                    process_name = my_list[8]
                    process_n = process_name.split("\n")
                    process_name = process_n[-1]
                    pid = my_list[9]
                    p = psutil.Process(int(pid))

                    if process_name not in white_list:
                        print("KEYLOGGER DETECTED SUCCESSFULLY !!")
                        time = 1
                        detected = True

                        # new code ----------------------- xxxx --------------------------
                        while True:
                            print("Options :")
                            print("1. Find location ")
                            print("2. Terminate process ")
                            print("3. Remove file")
                            print("4. Add to list")
                            print("5. Exit ")
                            print("6. Main Menu")

                            choice = input("Enter your choice (1/2/3/4/5/6) :")
                    
    #                    while True :
                        # -------- complete ----------
                            if not choice:
                                continue 

                            if choice == '1':
                              print("We are finding location....")
                              print("Please wait a minute.. ")
                              print("Thank you for your time..")
                              try :
                                find_location(int(pid))
                              except ValueError:
                                print("Invalid PID")

                              #print("We successfully detected the location of the process ..")

                              #break
                              continue

                            # -------- complete ----------

                            elif choice == '2':
                              print("We are Terminating the process.. ")
                              print("Please wait a minute ")
                              p.kill()
                              print("Process successfully terminated..")
                              print("Thank you ..")

                              #break
                              continue

                            # ---------- complete -----------

                            elif choice == '3':
                                # print("options : ")
                                # print("1. Enter manual location " )
                                # print("2. Detect automatic location ")

                                # while True :
                                #     opts = input("Enter your choice (1/2) : ")
                                #     if opts == '1':
                                #         command = input("Enter the location " )
                                #         print("Wait... we are going to the location !")
                                #         print("wait we are removing the file ... ")

                              print("We are finding location ......")
                              print("location successfully found ")
                              try:
                                file_path = find_location2(int(pid))

                                if file_path:
                                    print("wait ... we are removing the file ...")
                                    remove_file2(file_path)
                                    p.kill()
                                    print("File removed successfully ...")

                                else :
                                    print("File location not found. ")
                              except ValueError:
                                print("Invalid pid")
                                print("Thank you..")

                              break
                              #continue

                            # ----------- complete ----------------------------

                            elif choice == '5':
                              print("We are shutting down the program..")
                              print("Thank you for using this...")
                              sys.exit()

                              #break
                              #continue
                              

                            # -------------complete-----------------

                            elif choice == '4':
                              print("In which list you want to add this program..")
                              print("showing lists :")
                              print("(i).  White list")
                              print("(ii). Black list")
                              print("(iii).Exit ")

                              choose = input("Choose list (i/ii/iii) : ")

                      

                              if choose == 'i':
                                while True :
                                    option = input("You wanna add this program to white list (Y/N) :").lower()
                                    if option == 'y':
                                      print("Resuming process .. ")
                                      p.resume()
                                      print("Adding program to white list ...")
                                      white_list.append(process_name)

                                      print("White list programs are : ", white_list)

                                      selected = True
                                      break
                                      #continue

                                      #print("White list programs are : ",white_list)
                                    elif option == 'n':
                                        while True :
                                            option2 = input("would you like to add in black list ? (YES(y)/NO(n)/SKIP(s)) : ").lower()
                                            if option2 == 'y' or option2 == 'yes':
                                                print("Ok adding to black list ...")

                                                print("Terminating process .. .. ..")
                                                p.kill()

                                                print(" Successfully added to black list ")

                                                print("Black list programs : ",black_list)
                                                break
                                                
                                            elif option2 == 'n'or option2 == 'no':
                                                print("no problem ...")
                                                print("Thank you ...")
                                                break

                                            elif option2 == 's' or option2 == 'skip':
                                                print("you are skipping this ...")
                                                print("Think about it again !")
                                                break

                                            else :
                                                print("Invalid option. Try again. ")
                                        break
                                        #continue
                              
                        
                                    else:
                                        print("Invalid option .. please try again .. ")
                                        continue
                                
                                break
                                

                          


                              elif choose == 'ii' :
                                while True :
                                    option = input("You wanna add this program to black list (Y/N) :").lower()
                                    if option == 'y':
                                        print("killing the process fist ..")
                                        p.kill()
                                        print("Adding to Black list ")
                                        black_list.append(process_name)

                                        print("Black list programs are : ",black_list)
                                        break

                                    elif option == 'n':
                                        print("Ok no problem..")
                                        print("Once check again please ..")
                                        print("Thank you ...")
                                        break

                                    else :
                                        print("Invalid options. Try again. ")
                                break

                              elif choose == 'iii':
                                exit2()
                                continue

                              else :
                                print("Invalid option. Try again. ")

                            elif choice == '6':
                               print("Returning to the main menu ...")
                               break
                            #break 


                            else : 
                                print("Invalid option.. Try again. ")
                        #break
                        #continue
                    break
                                

    elif (opt == 3):
        #exit()
       print("We are shutting down this menu")
       print("Thank you for using this ... ")
       break                  

    else:
        print("You chose an invalid option ..")
        print("Thanks ")
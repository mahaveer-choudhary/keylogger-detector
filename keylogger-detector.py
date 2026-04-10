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
from rich.panel import Panel
from rich.prompt import Prompt
from colorama import Fore, Style
import time as mahi
import shutil
console = Console()


logo = """

   \033[96m▄█   ▄█▄    ▄████████ ▄██   ▄    ▄█        ▄██████▄     ▄██████▄     ▄██████▄     ▄████████    ▄████████ 
  \033[96m███ ▄███▀   ███    ███ ███   ██▄ ███       ███    ███   ███    ███   ███    ███   ███    ███   ███    ███ 
  \033[96m███▐██▀     ███    █▀  ███▄▄▄███ ███       ███    ███   ███    █▀    ███    █▀    ███    █▀    ███    ███ 
 \033[96m▄█████▀     ▄███▄▄▄     ▀▀▀▀▀▀███ ███       ███    ███  ▄███         ▄███         ▄███▄▄▄      ▄███▄▄▄▄██▀ 
\033[96m▀▀█████▄    ▀▀███▀▀▀     ▄██   ███ ███       ███    ███ ▀▀███ ████▄  ▀▀███ ████▄  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
  \033[96m███▐██▄     ███    █▄  ███   ███ ███       ███    ███   ███    ███   ███    ███   ███    █▄  ▀███████████ 
  \033[96m███ ▀███▄   ███    ███ ███   ███ ███▌    ▄ ███    ███   ███    ███   ███    ███   ███    ███   ███    ███ 
  \033[96m███   ▀█▀   ██████████  ▀█████▀  █████▄▄██  ▀██████▀    ████████▀    ████████▀    ██████████   ███    ███ 
  \033[96m▀                                ▀                                                             ███    ███ 


                \033[96m████████▄     ▄████████     ███        ▄████████  ▄████████     ███      ▄██████▄     ▄████████ 
                \033[96m███   ▀███   ███    ███ ▀█████████▄   ███    ███ ███    ███ ▀█████████▄ ███    ███   ███    ███ 
                \033[96m███    ███   ███    █▀     ▀███▀▀██   ███    █▀  ███    █▀     ▀███▀▀██ ███    ███   ███    ███ 
                \033[96m███    ███  ▄███▄▄▄         ███   ▀  ▄███▄▄▄     ███            ███   ▀ ███    ███  ▄███▄▄▄▄██▀ 
                \033[96m███    ███ ▀▀███▀▀▀         ███     ▀▀███▀▀▀     ███            ███     ███    ███ ▀▀███▀▀▀▀▀   
                \033[96m███    ███   ███    █▄      ███       ███    █▄  ███    █▄      ███     ███    ███ ▀███████████ 
                \033[96m███   ▄███   ███    ███     ███       ███    ███ ███    ███     ███     ███    ███   ███    ███ 
                \033[96m████████▀    ██████████    ▄████▀     ██████████ ████████▀     ▄████▀    ▀██████▀    ███    ███ 
                                                                                    

"""
print(logo)

# Extra functions of stopping keylogger....

def block_keylogger():
    # implementing blocking of keylogger code...!
    console.print("[bold green]blocking keylogger...![/bold green]")
    # rest code here ....

    console.print("[bold green]Thank you ..[/bold green]")
def center(message):
    terminal_width = os.get_terminal_size().columns
    padding = (terminal_width - len(message)) // 2
    return " " * padding + message

color = """ \033[0m """


# ------------------------------progress bar ----------
def run_command(command):
    try:
        
        result=subprocess.run(command,shell=True,check=True, stdout=subprocess.PIPE, text=True)
	
        #print("output: ")
        #print(result.stdout)
	
    except subprocess.CalledProcessError as e:
        console.print(f"[bold green]Error : {e}[/bold green]")
# -------------1st function ---------------------------
def find_location(pid):
    # implementing find of location of keylogger ...!
    console.print("[bold green]finding location...![/bold green]")
    # rest code here ....

    try:
      process = psutil.Process(pid)
      executable_path = process.exe()
      command_line = " ".join(process.cmdline())
      file_name = command_line.split()[-1]
      #return file_name

      # using locate command to find the file 
      file_paths = locate_file(file_name)
      console.print(f"[bold green]The name of the file is : {file_name}[/bold green]")
      if file_paths :
        console.print(f"[bold green]The name of the file is : {file_name}[/bold green]")
        for path in file_paths:
          print("The location of file is :",path)
          console.print("[bold green]We successfully detected the location of the process ..[/bold green]")
          # returning the path to other function 
          return path

      else :
        #print(f"File {file_name} not found.")
        console.print(f"[bold green]Sorry we can't find location of {file_name}[/bold green]")
        console.print("[bold green]But no worries, you can run your custom command here [/bold green]")
        print()
        #print("Sorry we can't detect the location of the file !")
        
        user_command = console.input("[bold cyan]Enter the command to run : [/bold cyan]")
        run_command(user_command)

    except psutil.NoSuchProcess:
      console.print("[bold green]Process not found.[/bold green]")
    console.print("[bold green]Thank you ..[/bold green]")
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
    console.print(f"[bold green]File removed successfully : {file_path}[/bold green]")
  except OSError as e:
    console.print(f"[bold green]Error removing file {file_path}: {e}[/bold green]")
  except Exception as ex:
    console.print(f"[bold green]An unexcepted error occured : {ex}[/bold green]")
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
            console.print("[bold green]file not found[/bold green]")
    except psutil.NoSuchProcess:
        console.print("[bold green]process not found[/bold green]")
def locate_file(file_name):
    try:
        result = subprocess.run(["locate",file_name], check=True, capture_output=True, text=True)
        return result.stdout.strip().split('\n')
    except subprocess.CalledProcessError:
        return None

def remove_file2(file_path):
    try:
        os.remove(file_path)
        console.print(f"[bold green]File removed successfully : {file_path}[/bold green]")
    except OSError as e:
        console.print(f"[bold green]Error removing file {file_path}: {e}[/bold green]")
    except Exception as ex:
        console.print(f"[bold green]An unexcepted error occured : {ex}[/bold green]")
# ---------------2nd function close ---------------------------

def exit():
    # code of exiting from the script ...!
    console.print("[bold green]Bye ... [/bold green]")
    console.print("[bold green]We are Signing Off ...[/bold green]")
    # rest code here ....

    console.print("[bold green]Thank you for using this application ..[/bold green]")
def exit2():
    console.print("[bold green]we are going back to main menu ... [/bold green]")
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
    
    menu_text = "[bold yellow]1. Scan for a particular location[/bold yellow]\n" \
                "[bold yellow]2. Detect keylogger[/bold yellow]\n" \
                "[bold yellow]3. Exit[/bold yellow]"
    console.print(Panel(menu_text, title="[bold cyan]Main Menu[/bold cyan]", border_style="cyan", expand=False))
    
    user_input = console.input("[bold cyan]Choose your option : [/bold cyan]")

    if not user_input:
      console.print("[bold green]Invalid input. Please enter a value.[/bold green]")
      continue

    opt = int(user_input)


    #opt = int(input("Choose your option : "))

    if (opt == 1):
        console.print("[bold green]you choose for a particular location ..[/bold green]")
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
                        console.print("[bold green]Options :[/bold green]")
                        console.print("[bold green]1. Block [/bold green]")
                        console.print("[bold green]2. Remove [/bold green]")
                        console.print("[bold green]3. Exit[/bold green]")
                        choice = console.input("[bold cyan]Enter your choice (1/2) :[/bold cyan]")
                        if choice == '1':
                            block_keylogger()
                        elif choice == '2':
                            remove_keylogger()
                        if choice == '3':
                            exit()
                        else:
                            console.print("[bold green]Invalid .. Try again ![/bold green]")
            # code finish ------------- xxxx -----------------------------

        # location = input("Enter your location : ")

        # scanning for location ....
        if __name__ == "__main__":
            scan_location = console.input("[bold cyan]Enter the directory or drive path to scan : [/bold cyan]")
            scan_directory(scan_location)

        console.print("[bold green]Scan complete [/bold green]")
# ------------------------------------------------------

    elif (opt == 2):
        console.print("[bold green]you choose for detecting keylogger ..[/bold green]")
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
                            console.print("[bold green]Error: Program already exists in startup. [/bold green]")
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
                                console.print("[bold green]Program successfully added to startup...[/bold green]")
                            else:
                                console.print("[bold green]Program was not added to startup. Please try again.[/bold green]")
                    elif opt in ('r', "--remove-from-startup"):
                        program_path = exists(os.path.join(autostart_path, 'Keylogger-detector'))
                        if program_path:
                            os.remove(os.path.join(autostart_path, 'Keylogger-detector'))
                            if not program_path:
                                console.print("[bold green]File removed successfully...[/bold green]")
                            else:
                                console.print("[bold green]Error: Program does not exist in the startup directory. [/bold green]")
            except getopt.error as err:
                # output error and return error code
                print(str(err))

        else:
            while True:
                if time == 1:
                    console.print("[bold green]\nScanning in progress.....[/bold green]")
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
                        console.print(f"[bold green]{Fore.RED}KEYLOGGER DETECTED SUCCESSFULLY !!{Style.RESET_ALL}[/bold green]")
                        time = 1
                        detected = True

                        # new code ----------------------- xxxx --------------------------
                        while True:
                            options_text = "[bold yellow]1. Find location[/bold yellow]\n" \
                                           "[bold yellow]2. Terminate process[/bold yellow]\n" \
                                           "[bold yellow]3. Remove file[/bold yellow]\n" \
                                           "[bold yellow]4. Add to list[/bold yellow]\n" \
                                           "[bold yellow]5. Exit[/bold yellow]\n" \
                                           "[bold yellow]6. Main Menu[/bold yellow]"
                            console.print(Panel(options_text, title="[bold cyan]Action Options[/bold cyan]", border_style="red", expand=False))

                            choice = console.input("[bold cyan]Enter your choice (1/2/3/4/5/6) : [/bold cyan]")
                    
    #                    while True :
                        # -------- complete ----------
                            if not choice:
                                continue 

                            if choice == '1':
                              console.print("[bold green]We are finding location....[/bold green]")
                              console.print("[bold green]Please wait a minute.. [/bold green]")
                              console.print("[bold green]Thank you for your time..[/bold green]")
                              try :
                                find_location(int(pid))
                              except ValueError:
                                console.print("[bold green]Invalid PID[/bold green]")
                              #print("We successfully detected the location of the process ..")

                              #break
                              continue

                            # -------- complete ----------

                            elif choice == '2':
                              console.print("[bold green]We are Terminating the process.. [/bold green]")
                              console.print("[bold green]Please wait a minute [/bold green]")
                              p.kill()
                              console.print("[bold green]Process successfully terminated..[/bold green]")
                              console.print("[bold green]Thank you ..[/bold green]")
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

                              console.print("[bold green]We are finding location ......[/bold green]")
                              console.print("[bold green]location successfully found [/bold green]")
                              try:
                                file_path = find_location2(int(pid))

                                if file_path:
                                    console.print("[bold green]wait ... we are removing the file ...[/bold green]")
                                    remove_file2(file_path)
                                    p.kill()
                                    console.print("[bold green]File removed successfully ...[/bold green]")
                                else :
                                    console.print("[bold green]File location not found. [/bold green]")
                              except ValueError:
                                console.print("[bold green]Invalid pid[/bold green]")
                                console.print("[bold green]Thank you..[/bold green]")
                              break
                              #continue

                            # ----------- complete ----------------------------

                            elif choice == '5':
                              console.print("[bold green]We are shutting down the program..[/bold green]")
                              console.print("[bold green]Thank you for using this...[/bold green]")
                              sys.exit()

                              #break
                              #continue
                              

                            # -------------complete-----------------

                            elif choice == '4':
                              list_text = "[bold yellow](i). White list[/bold yellow]\n" \
                                          "[bold yellow](ii). Black list[/bold yellow]\n" \
                                          "[bold yellow](iii). Exit[/bold yellow]"
                              console.print(Panel(list_text, title="[bold cyan]Select List To Add[/bold cyan]", border_style="magenta", expand=False))

                              choose = console.input("[bold cyan]Choose list (i/ii/iii) : [/bold cyan]")

                      

                              if choose == 'i':
                                while True :
                                    option = console.input("[bold cyan]You wanna add this program to white list (Y/N) :[/bold cyan]").lower()
                                    if option == 'y':
                                      console.print("[bold green]Resuming process .. [/bold green]")
                                      p.resume()
                                      console.print("[bold green]Adding program to white list ...[/bold green]")
                                      white_list.append(process_name)

                                      print("White list programs are : ", white_list)

                                      selected = True
                                      break
                                      #continue

                                      #print("White list programs are : ",white_list)
                                    elif option == 'n':
                                        while True :
                                            option2 = console.input("[bold cyan]would you like to add in black list ? (YES(y)/NO(n)/SKIP(s)) : [/bold cyan]").lower()
                                            if option2 == 'y' or option2 == 'yes':
                                                console.print("[bold green]Ok adding to black list ...[/bold green]")
                                                console.print("[bold green]Terminating process .. .. ..[/bold green]")
                                                p.kill()

                                                console.print("[bold green] Successfully added to black list [/bold green]")
                                                print("Black list programs : ",black_list)
                                                break
                                                
                                            elif option2 == 'n'or option2 == 'no':
                                                console.print("[bold green]no problem ...[/bold green]")
                                                console.print("[bold green]Thank you ...[/bold green]")
                                                break

                                            elif option2 == 's' or option2 == 'skip':
                                                console.print("[bold green]you are skipping this ...[/bold green]")
                                                console.print("[bold green]Think about it again ![/bold green]")
                                                break

                                            else :
                                                console.print("[bold green]Invalid option. Try again. [/bold green]")
                                        break
                                        #continue
                              
                        
                                    else:
                                        console.print("[bold green]Invalid option .. please try again .. [/bold green]")
                                        continue
                                
                                break
                                

                          


                              elif choose == 'ii' :
                                while True :
                                    option = console.input("[bold cyan]You wanna add this program to black list (Y/N) :[/bold cyan]").lower()
                                    if option == 'y':
                                        console.print("[bold green]killing the process fist ..[/bold green]")
                                        p.kill()
                                        console.print("[bold green]Adding to Black list [/bold green]")
                                        black_list.append(process_name)

                                        print("Black list programs are : ",black_list)
                                        break

                                    elif option == 'n':
                                        console.print("[bold green]Ok no problem..[/bold green]")
                                        console.print("[bold green]Once check again please ..[/bold green]")
                                        console.print("[bold green]Thank you ...[/bold green]")
                                        break

                                    else :
                                        console.print("[bold green]Invalid options. Try again. [/bold green]")
                                break

                              elif choose == 'iii':
                                exit2()
                                continue

                              else :
                                console.print("[bold green]Invalid option. Try again. [/bold green]")
                            elif choice == '6':
                               console.print("[bold green]Returning to the main menu ...[/bold green]")
                               break
                            #break 


                            else : 
                                console.print("[bold green]Invalid option.. Try again. [/bold green]")
                        #break
                        #continue
                    break
                                

    elif (opt == 3):
        #exit()
       console.print("[bold green]We are shutting down this menu[/bold green]")
       console.print("[bold green]Thank you for using this ... [/bold green]")
       break                  

    else:
        console.print("[bold green]You chose an invalid option ..[/bold green]")
        console.print("[bold green]Thanks [/bold green]")

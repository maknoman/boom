import os
import smtplib
import sys
import getpass
import time

os.system('clear')
print(''' 
 ____   ___   ___  __  __ 
| __ ) / _ \ / _ \|  \/  |
|  _ \| | | | | | | |\/| |
| |_) | |_| | |_| | |  | |
|____/ \___/ \___/|_|  |_|
                          Made by:MAK
''')

time.sleep(1)
print("\033[95mLoading", flush=True, end='')
for i in range(3):
    time.sleep(1)
    print('.', flush=True, end='')
print("\n\n")
file = open("email_list.txt", "a")
print("\033[96mFirst you have to make your Email list whom you want to send your Mail. Once you made list next time you don't need to repeat it. But you can add new mail in your list. If you don't want to add new mail just enter no.\nIf you want to remove particular email from your list just edit \033[91mmail_list.txt \033[96mfile in this location.\n\n")
choice = input('\033[92mDo you want to add mail address in your list?\033[93m\n[1] Yes\n[2] No\n[?] ')
if choice == '1':
    print("\033[91m[e] Type 'e' as mail to exit entering email\033[93m")
    while True:
        mail = input('\033[94m[-] \033[97mEnter recipient mail:\033[93m')
        if mail != 'e':
            file.write(mail)
            file.write('\n')
        else:
            break
file.close()
print('\033[97mYour Email list:\033[93m')
f = open("email_list.txt", "r")
email = f.read()
print(email)
email_list = open("email_list.txt").read().splitlines()
print('\033[91mCheck your mail list.\nYour password or any information never store anywhere.\n\033[96mLog in information loading in few second', flush=True, end='')
for i in range(10):
    time.sleep(1)
    print('.', flush=True, end='')
os.system('clear')

user = input('\033[94m[?] \033[97mYour \033[92mGmail\033[97m :\033[93m ')
password = getpass.getpass('\033[94m[?]\033[97m Your \033[91mPassword\033[97m :\033[93m ')
print(" ")
subject = input('\033[94m[?]\033[97m Subject of your mail: \033[93m')
message = input('\033[94m[?]\033[97m Your \033[92mMessage\033[97m : \033[93m')

print(" ")

print("\033[94m[*] \033[97mSending : ")

smtp_server = 'smtp.gmail.com'
port = 587

try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user, password)

    for i in range(len(email_list)):
        msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + message
        server.sendmail(user, email_list[i], msg)
        print("\033[94m[-]\033[97m Email \033[92mSENT to\033[97m  :\033[93m"+str(email_list[i]))
        sys.stdout.flush()
    server.quit()
    print('\033[93m[-]\033[97m All \033[97mMessage\033[92m sent\033[97m ')
except KeyboardInterrupt:
    print('[x] Canceled')
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print(" ")
    print("\033[94m[x] \033[91mError \033[97m:")
    print('\033[94m[x] \033[91mYour email or password may incorrect. Or you need to do the action below.')
    print("\033[94m[!] \033[96mCheck if the Options of 'Applications are less secure' is enabled in your account setting. Check it at https://myaccount.google.com/lesssecureapps")
    sys.exit()

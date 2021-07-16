##############################
#    iMessage Sender Code    #
#  created by Brad Campbell  #
#       06 / 10 / 2020       #
##############################



import subprocess

# Put service ID here
serviceID = ""
# Message to be sent
fullMessage = input("Message you wish to send: \n")
# Declare phone number EXACTLY as is is stored in the user's address book
phoneNumber = input("Phone number of intended target (exactly as it is stored in address book: \n")



# Deploys the text message
def sendToTarget():
    global fullMessage, phoneNumber

    # Script is written in Apple Script language, executable in Script application
    script = 'tell application "Messages" get every service send "' + fullMessage + '" to buddy "' + phoneNumber + '" of service id "' + serviceID + '" end tell'
    proc = subprocess.Popen(['osascript', '-'], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, universal_newlines = False)
    stdout_output, stderr_output = proc.communicate(script)
    print(stdout_output)
    print(stderr_output)



# Runs both mentioned methods and has "print()" check points for console verification
def main():
    try: 
        sendToTarget()
        print("The below message has been successfully sent.")
        print(fullMessage)
    except:
        print("Something has gone wrong. Message failed to send.")



if __name__ == "__main__":
    main()



# Script reference code below for getting service ID
"""
tell application "Messages"
	get every account
end tell
"""

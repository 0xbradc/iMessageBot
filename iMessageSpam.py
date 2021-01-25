##############################
#   iMessage Spammer Code    #
#  created by Brad Campbell  #
#       06 / 10 / 2020       #
##############################


import subprocess

# This message will be split up by spaces
fullMessage = "Test Message. Ignore."
# Declare phone number EXACTLY as they are inputted into the address book
phoneNumber = +1 (111) 111-1111
# The array of words split up by words
eachWordArray = []


# Takes the inputted string (variable named "fullMessage") and splits up each word into an array (variable "eachWordArray")
def splitWords():
    global fullMessage, eachWordArray
    temp = ""
    fullMessage += " " # Ensures the last word is printed effectively

    for x in range(0, len(fullMessage), 1):
        if (fullMessage[x] == " "):
            #temp += "\n" # Adds line for printing individually
            eachWordArray.append(str(temp))
            temp = ""
        elif (fullMessage[x] == "," or fullMessage[x] == "."):
            temp += ""
        else:
            temp += fullMessage[x]

# Deploys a separate text message for each word of the "eachWordArray"
def spamTarget():
    global eachWordArray, phoneNumber
    
    for x in range(0, len(eachWordArray), 1):
        # Script is written in Apple Script language, executable in Script application
        script = '''tell application "Messages"
            get every service #prints the service number to print in line below
            send "''' + str(eachWordArray[x]) + '''" to buddy "''' + str(phoneNumber) + '''" of service id "700D7248-40A4-40E0-8387-0254B2CE75A7"
        end tell
        '''
        proc = subprocess.Popen(['osascript', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        stdout_output = proc.communicate(script)[0]
        print ("Completed word " + str(x) + "\t" + str(stdout_output)) #gives running word count and tells error words

# Runs both mentioned methods and has "print()" check points for console verification
def main():
    splitWords()
    print("Completed initial \"splitWords()\" method.") # Checkpoint
    spamTarget()
    print("Completed whole \"spamTarget()\" method.") # Checkpoint


# Final Method Run
main()


# Script reference code below
"""
import subprocess
script = '''tell application "Messages"
    get every service #prints the service number to print in line below
    send "Test Message" to buddy "+15555555555" of service id "PRINTED-BY-LINE-ABOVE"
end tell
'''

proc = subprocess.Popen(['osascript', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
stdout_output = proc.communicate(script)[0]

print (stdout_output)
"""

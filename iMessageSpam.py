##############################
#   iMessage Spammer Code    #
#  created by Brad Campbell  #
#         enjoy!             #
##############################


import subprocess

#this is what will be split up by each word
#fullMessage = "This is for Rachel you big fat white nasty smelling fat bitch Why you took me off the motherfuking schedule With your trifling dirty white racist ass big fat bitch Oompa Loompa body ass bitch I\'m coming up there and I\'m gonna beat the fuck Out of you bitch"
fullMessage = "Fuckers in school were telling me, always in the barber shop Chief Keef ain't bout this, Chief Keef ain't bout that My boy a BD on fucking Lamron and them They say that nigga don't be putting in no work Shut the fuck up! Y'all niggas ain't know shit, all ya motherfuckers talk about Chief Keef ain't no hitta, Chief Keef ain't this, Chief Keef a fake Shut the fuck up! Y'all don't live with that nigga Y'all know that nigga got caught with a ratchet shootin' at the police and shit Nigga been on probation since fuckin', I don't know when! Motherfuckers stop fuckin' playin' him like that! Them niggas savages out there If I catch another motherfucker talking sweet about Chief Keef I'm fucking beating they ass! I'm not fucking playing no more, you know those niggas role with Lil' Reese and THESE BITHCES LOVE SOSA"
#declare phone number EXACTLY as they are inputted into the address book
phoneNumber = +14795951038
#the array of words split up by elements without spaces
eachWordArray = []


#this method takes the inputted paragraph (variable named "fullMessage") and splits up each word into an array (variable "eachWordArray")
def splitWords():
    global fullMessage, eachWordArray
    temp = ""
    fullMessage += " " #this ensures the last word is printed effectively

    for x in range(0, len(fullMessage), 1):
        if (fullMessage[x] == " "):
            #temp += "\n" #adds line for printing individually
            eachWordArray.append(str(temp))
            temp = ""
        elif (fullMessage[x] == "," or fullMessage[x] == "."):
            temp += ""
        else:
            temp += fullMessage[x]

#this method deploys a separate text message for each word of the "eachWordArray"
def spamTarget():
    global eachWordArray, phoneNumber
    
    for x in range(0, len(eachWordArray), 1):
        #below script is written in Apple Script language, executable in Script application
        script = '''tell application "Messages"
            get every service #prints the service number to print in line below
            send "''' + str(eachWordArray[x]) + '''" to buddy "''' + str(phoneNumber) + '''" of service id "700D7248-40A4-40E0-8387-0254B2CE75A7"
        end tell
        '''
        proc = subprocess.Popen(['osascript', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        stdout_output = proc.communicate(script)[0]
        print ("Completed word " + str(x) + "\t" + str(stdout_output)) #gives running word count and tells error words

#this method runs both mentioned methods and has "print()" check points for console verification
def main():
    splitWords()
    print("Completed initial \"splitWords()\" method.") #checkpoint
    spamTarget()
    print("Completed whole \"spamTarget()\" method.") #checkpoint


#FINAL METHOD RUN
main()





#reference code below that sends one individual message
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
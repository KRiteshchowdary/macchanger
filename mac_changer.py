### Program for MAC changer for a specific interface using python3

### For manual run python3 mac_changer.py -h


### single # = comments , double # = code



#For running commands in shell we use an module called subprocess

import subprocess
import optparse
import re

#To run an command we use 
#subprocess.call("command",shell=True)

#To see network interfaces on our system

# subprocess.call("sudo ifconfig",shell=True)


# To change MAC address we run the following commands in our terminal usually

# 1. ifconfig <interface> down                      :- Shutdown the interface initially
# 2. ifconfig <interface> hw ether <New MAC addr>   :- Change the MAC address
# 3. ifconfig <interface> up                        :- Start the interface again

# Now lets see how to implememnt the same using python
# In this program we will ask the users to give new MAC address and interace that they want to change 


##### METHOD - 1 #########

## CODE

## interface = input("[+] Enter Interface > ")
## new_MAC = input("[+] Enter new MAC address > ")


## print("[+] Changing MAC address to " + new_MAC + " for the " + interface + " interface .....")

## subprocess.call("sudo ifconfig " + interface + " down",shell=True)
## subprocess.call("ifconfig " + interface + " hw ether "+new_MAC,shell=True)
## subprocess.call("ifconfig " + interface + " up",shell=True)







##### METHOD - 2 #########

# By using the above method-1 the user can use our script to insert malicious code into the program 
# i.e Giving an command through the input which is very dangerous 


## CODE

# So we use another way to call the subprocess call method which can avoid this .
# We enter the command as a list of words with a space after each word .

## print("[+] Changing MAC address to " + new_MAC + " for the " + interface + " interface .....")

## subprocess.call(["sudo", ifconfig", interface, "down"])
## subprocess.call(["ifconfig", interface, "hw", "ether", new_MAC])
## subprocess.call(["ifconfig", interface, "up"])

## subprocess.call(["ifconfig ", interface])





##### METHOD - 3 ##########

# Let us change the method-2 a little bit to give the inputs as arguments in the run code itself
# We do so beacause thats how usually an programs runs . But you can use both Method 2 and 3, but 1 is dangerous(but works) .


# optparse is a module that helps us to get arguments (Usually Comand-line arguments) and use them in our code .
# we often see codes that take input as arguments while running the code itself parser helps us to do this

# For this we import optparse module
# OptionParser is a class in optparse that we use to create a child "parser" which is an object that we use .

## parser = optparse.OptionParser()

# Now we add arguments to the parser object and tell it how to use them using add_option() method

# Arguments of this method are :
#   1. options i.e arguments names - enter these as strings in the begining, you can add any number of options
#   2. dest - variable to which the value must be assigned
#   3. help - message to show when user asks for help using -h or --help

# parser.add_option("option1","option2","option3",dest="Variable to store value",help="Help message to show")

## parser.add_option("-i","--interface",dest="interface",help="Enter Interface to which changes are to be maid .")
## parser.add_option("-m","--new_MAC",dest="new_MAC",help="Enter new MAC address to be changed .")

# parse_args() method returns the values captured by parser object as 2 sets of data (options,argument values)
# In order to use these values we assign them to some other variables or directly

## (options,argumets) = parser.parse_args()

# To use the values of arguments stored in options we use options.<argument_name>

## inteface = options.interface
## new_MAC = options.new_MAC

## print("[+] Changing MAC address to " + new_MAC + " for the " + interface + " interface .....")

## subprocess.call(["sudo", ifconfig", interface, "down"])
## subprocess.call(["ifconfig", interface, "hw", "ether", new_MAC])
## subprocess.call(["ifconfig", interface, "up"])

## subprocess.call(["ifconfig ", interface])







# SIMPLYFING ALL THE ABOVE CODE INTO FUNCTIONS AND IMPLEMENTING IT IN THE BEST WAY

#CODE

def get_inputs():
    parser = optparse.OptionParser()

    parser.add_option("-i","--interface",dest="interface",help="Enter Interface to which changes are to be maid .")
    parser.add_option("-m","--new_MAC",dest="new_MAC",help="Enter new MAC address to be changed .")

    (options,arguments) = parser.parse_args()
    
    # Making sure that all required arguments are entered .
    if not options.interface:
        parser.error("[+] Please enter proper interface name use --help or -h for more info . ")
    else:
        if not options.new_MAC:
            parser.error("[+] Please enter proper interface name use --help or -h for more info . ")
        else:
            user_inputs=options 
            return user_inputs


    
def change_MAC(interface,new_MAC):
    print("[+] Changing MAC address to " + new_MAC + " for the " + interface + " interface .....")

    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_MAC])
    subprocess.call(["sudo", "ifconfig", interface, "up"])



#### CHECKING IF MAC ADDRESS REALLY CHANGED TO USER INPUT ###############



# For this we use a method from subprocess module called check_output
# check_ouput() returns the result of the command run as text
# syntax :- subprocess.check_output([<command as list of strings and variables(if any)>])


def Check_Result(options):
    Output =str(subprocess.check_output(["sudo", "ifconfig", options.interface]))
    Output_MAC = re.findall(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", Output)
    if Output_MAC:
        current_MAC = Output_MAC[0]
        if current_MAC == options.new_MAC:
            print("[+] MAC address changed for " + options.interface + " changed to " + current_MAC + ".")
        else:
            print("Failed to change MAC address for " + options.interface + " to " + options.new_MAC + ".")
    else:
        print("[+] Can not find MAC address for the interface specified .")



# Calling all Functions

user_inputs=get_inputs()
change_MAC(user_inputs.interface,user_inputs.new_MAC)
Check_Result(user_inputs)



# *please do not re-use this code, it is not for redistribution without permission*

# the opening screen (aka the most print functions you will ever see in a simple password brute-force tool)
print("P    A    S    S    W    O    R    D")
print("S    T    R    E    N    G    T    H")
print("T    E    S    T    E    R")
print('       _--------------_')
print('          By Formula')
print('       _--------------_')
print("This process will attempt to brute force your password, it could take more than 45 minutes, you can leave"
      " the process to run in the background if you need to.")
print("")
print("If the process takes too long, (Over 2 Hours), your password exceedingly strong and essentially "
      "uncrackable, well done.")
print("To end the process prematurely, press CTRL-C")
print("")
print("Source-Code available upon request, please email max.6688@icloud.com for access. ")
print("")
print("*Your password will not be seen, saved or taken by any person, this is an offline program*")
print("")

# the actual code begins!

import random

character_list = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyz1234567890!@#$%^&*()<>?:{}|+_~`"
password = input("Enter Password: ")
guess = ""
while guess != password:
    guess = random.choices(character_list, k=len(password))
    print(guess)
    guess = "".join(guess)
    print(guess)
# and then it ends... this is a really short program isn't it.

# more unnecessary print functions, I guess it makes the program a bit prettier?
print("Password cracked! Your password is: " + guess)
print("")
print("Password Strength Is Well Above Standard,"
      " if you need help choosing a new and strong password; use a password generator such"
      " as https://passwordsgenerator.net/")
print("")
print("Please Press ENTER to close the program.")
print("")
print("Thank You")
input()

# and the whole program ends, just as it began, what a shame... I was just starting to enjoy myself.

#             ______________
# |  ___|                       | |
# | |_ ___  _ __ _ __ ___  _   _| | __ _
# |  _/ _ \| '__| '_ ` _ \| | | | |/ _` |
# | || (_) | |  | | | | | | |_| | | (_| |
# \_| \___/|_|  |_| |_| |_|\__,_|_|\__,_|
#             -------------
#             get formulated
#              ------------

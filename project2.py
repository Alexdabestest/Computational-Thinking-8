Yes_PJO = 0
No_PJO = 0
print(r" _    _                                                              _     _____     _  ____ ___  ")
print(r"| |  | |                                                            | |   |  __ \   | |/ __ \__ \ ")
print(r"| |__| | __ ___   _____     _   _  ___  _   _     _ __ ___  __ _  __| |   | |__) |  | | |  | | ) |")
print(r"|  __  |/ _` \ \ / / _ \   | | | |/ _ \| | | |   | '__/ _ \/ _` |/ _` |   |  ___/   | | |  | |/ /")
print(r"| |  | | (_| |\ V /  __/   | |_| | (_) | |_| |   | | |  __/ (_| | (_| |   | |  | |__| | |__| |_|  ")
print(r"|_|  |_|\__,_| \_/ \___|    \__, |\___/ \__,_|   |_|  \___|\__,_|\__,_|   |_|   \____/ \____/(_)  ")
print(r"                             __/ |                                                            ")
print(r"                            |___/                                                             ")
input ("")
print("Please answer all questions with the word not the letter")
print("and with the first letter uppercase.")
input("")
print("Who is the main villain in Percy Jackson and the lightning thief?")
answer = input("A) Luke B) Kronos")
if answer == "Kronos":
    No_PJO += 1
elif answer == "Kronos" or answer == "Luke":
    Yes_PJO += 1
input("")
print("Who is Percy's girlfriend?")
answer = input("A) Annabeth B) Rachel")
if answer == "Annabeth":
    Yes_PJO += 1
elif answer == "Rachel":
    No_PJO += 1
input("")
print("Who is Percy's best friend?")
answer = input ("A) Grover B) Clarisse")
if answer == "Grover":
    Yes_PJO += 1
elif answer == "Clarisse":
    No_PJO += 1
input("")
print("Who stole Zeus's lightning bolt? ")
answer = input("A) Percy B) Luke")
if answer == "Luke":
    Yes_PJO += 1
elif answer == "Percy":
    No_PJO += 1
input("")
print("Who wins the battle of Manhattan?")
answer = input("A) Percy B) Kronos")
if answer == "Percy":
    Yes_PJO += 1
elif answer == "Kronos":
    No_PJO += 1
input("")
print ("What is the name of Percy's brother?")
answer = input ("A) Tyson B) Nobody")
if answer == "Tyson":
    Yes_PJO += 1
elif answer == "Nobody":
    No_PJO += 1
#end of quiz:
if Yes_PJO > No_PJO:
    print("You have read Percy Jackson.")
elif No_PJO > Yes_PJO:
    print("You have not read Percy Jackson.")
elif No_PJO == Yes_PJO and Yes_PJO > 0:
    print("you've read at least one of the books.")
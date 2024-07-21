import random

blackPin = 0
whitePin = 0

colors = ["B", "W", "Bl", "R", "G", "Y"]
comCol1 = random.choice(colors)
comCol2 = random.choice(colors)
comCol3 = random.choice(colors)
comCol4 = random.choice(colors)
comRow = [comCol1, comCol2, comCol3, comCol4]

row1 = "[ ] [ ] [ ] [ ]"
print(row1)
print(f"What colors would you like to guess?\n B for black \n W for white \n Bl for blue \n R for red \n G for green \n Y for yellow")
col1 = input("Color 1")
col2 = input("Color 2")
col3 = input("Color 3")
col4 = input("Color 4")
choice = [col1, col2, col3, col4]
print(choice)

if choice[0] == comRow[0]:
    blackPin += 1
    choice[0] = None
    comRow[0] = None
elif choice[0] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[0] == comRow[2]:
    whitePin += 1
    comRow[2] = None
elif choice[0] == comRow [3]:
    whitePin += 1
    comRow[3] = None
    
if choice[1] == comRow[1]:
    blackPin += 1
    choice[1] = None
    comRow[1] = None
elif choice[1] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[1] == comRow[2]:
    whitePin += 1
    comRow[2] = None
elif choice[1] == comRow[3]:
    whitePin += 1
    comRow[3] = None
    
if choice[2] == comRow[2]:
    blackPin += 1
    choice[2] = None
    comRow[2] = None
elif choice[2] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[2] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[2] == comRow[3]:
    whitePin += 1
    comRow[3] = None

if choice[3] == comRow[3]:
    blackPin += 1
    choice[3] = None
    comRow[3] = None
elif choice[3] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[3] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[3] == comRow[2]:
    whitePin += 1
    comRow[2] = None   

if blackPin == 4:
    print("You win!")
    exit()

print(f"Black pins: {blackPin}")
print(f"White pins: {whitePin}")
whitePin = 0
blackPin = 0

print("Number of guesses: 2/12")
print("Next guess")
col1 = input("Color 1")
col2 = input("Color 2")
col3 = input("Color 3")
col4 = input("Color 4")
choice = [col1, col2, col3, col4]
print(choice)

if choice[0] == comRow[0]:
    blackPin += 1
    choice[0] = None
    comRow[0] = None
elif choice[0] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[0] == comRow[2]:
    whitePin += 1
    comRow[2] = None
elif choice[0] == comRow [3]:
    whitePin += 1
    comRow[3] = None
    
if choice[1] == comRow[1]:
    blackPin += 1
    choice[1] = None
    comRow[1] = None
elif choice[1] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[1] == comRow[2]:
    whitePin += 1
    comRow[2] = None
elif choice[1] == comRow[3]:
    whitePin += 1
    comRow[3] = None
    
if choice[2] == comRow[2]:
    blackPin += 1
    choice[2] = None
    comRow[2] = None
elif choice[2] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[2] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[2] == comRow[3]:
    whitePin += 1
    comRow[3] = None

if choice[3] == comRow[3]:
    blackPin += 1
    choice[3] = None
    comRow[3] = None
elif choice[3] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[3] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[3] == comRow[2]:
    whitePin += 1
    comRow[2] = None   

if blackPin == 4:
    print("You win!")
    exit()
    
print(f"Black pins: {blackPin}")
print(f"White pins: {whitePin}")
whitePin = 0
blackPin = 0    
    
print("Number of guesses: 3/12")
print("Next guess")
col1 = input("Color 1")
col2 = input("Color 2")
col3 = input("Color 3")
col4 = input("Color 4")
choice = [col1, col2, col3, col4]
print(choice)

if choice[0] == comRow[0]:
    blackPin += 1
    choice[0] = None
    comRow[0] = None
elif choice[0] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[0] == comRow[2]:
    whitePin += 1
    comRow[2] = None
elif choice[0] == comRow [3]:
    whitePin += 1
    comRow[3] = None
    
if choice[1] == comRow[1]:
    blackPin += 1
    choice[1] = None
    comRow[1] = None
elif choice[1] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[1] == comRow[2]:
    whitePin += 1
    comRow[2] = None
elif choice[1] == comRow[3]:
    whitePin += 1
    comRow[3] = None
    
if choice[2] == comRow[2]:
    blackPin += 1
    choice[2] = None
    comRow[2] = None
elif choice[2] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[2] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[2] == comRow[3]:
    whitePin += 1
    comRow[3] = None

if choice[3] == comRow[3]:
    blackPin += 1
    choice[3] = None
    comRow[3] = None
elif choice[3] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[3] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[3] == comRow[2]:
    whitePin += 1
    comRow[2] = None   

if blackPin == 4:
    print("You win!")
    exit()
    
print(f"Black pins: {blackPin}")
print(f"White pins: {whitePin}")
whitePin = 0
blackPin = 0

print("Number of guesses: 4/12")
print("Next guess")
col1 = input("Color 1")
col2 = input("Color 2")
col3 = input("Color 3")
col4 = input("Color 4")
choice = [col1, col2, col3, col4]
print(choice)

if choice[0] == comRow[0]:
    blackPin += 1
    choice[0] = None
    comRow[0] = None
elif choice[0] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[0] == comRow[2]:
    whitePin += 1
    comRow[2] = None
elif choice[0] == comRow [3]:
    whitePin += 1
    comRow[3] = None
    
if choice[1] == comRow[1]:
    blackPin += 1
    choice[1] = None
    comRow[1] = None
elif choice[1] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[1] == comRow[2]:
    whitePin += 1
    comRow[2] = None
elif choice[1] == comRow[3]:
    whitePin += 1
    comRow[3] = None
    
if choice[2] == comRow[2]:
    blackPin += 1
    choice[2] = None
    comRow[2] = None
elif choice[2] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[2] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[2] == comRow[3]:
    whitePin += 1
    comRow[3] = None

if choice[3] == comRow[3]:
    blackPin += 1
    choice[3] = None
    comRow[3] = None
elif choice[3] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[3] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[3] == comRow[2]:
    whitePin += 1
    comRow[2] = None   

if blackPin == 4:
    print("You win!")
    exit()
    
print(f"Black pins: {blackPin}")
print(f"White pins: {whitePin}")
whitePin = 0
blackPin = 0
    
print("Number of guesses: 5/12")
print("Next guess")
col1 = input("Color 1")
col2 = input("Color 2")
col3 = input("Color 3")
col4 = input("Color 4")
choice = [col1, col2, col3, col4]
print(choice)

if choice[0] == comRow[0]:
    blackPin += 1
    choice[0] = None
    comRow[0] = None
elif choice[0] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[0] == comRow[2]:
    whitePin += 1
    comRow[2] = None
elif choice[0] == comRow [3]:
    whitePin += 1
    comRow[3] = None
    
if choice[1] == comRow[1]:
    blackPin += 1
    choice[1] = None
    comRow[1] = None
elif choice[1] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[1] == comRow[2]:
    whitePin += 1
    comRow[2] = None
elif choice[1] == comRow[3]:
    whitePin += 1
    comRow[3] = None
    
if choice[2] == comRow[2]:
    blackPin += 1
    choice[2] = None
    comRow[2] = None
elif choice[2] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[2] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[2] == comRow[3]:
    whitePin += 1
    comRow[3] = None

if choice[3] == comRow[3]:
    blackPin += 1
    choice[3] = None
    comRow[3] = None
elif choice[3] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[3] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[3] == comRow[2]:
    whitePin += 1
    comRow[2] = None   

if blackPin == 4:
    print("You win!")
    exit()
    
print(f"Black pins: {blackPin}")
print(f"White pins: {whitePin}")
whitePin = 0
blackPin = 0    
    
print("Number of guesses: 6/12")
print("Next guess")
col1 = input("Color 1")
col2 = input("Color 2")
col3 = input("Color 3")
col4 = input("Color 4")
choice = [col1, col2, col3, col4]
print(choice)

if choice[0] == comRow[0]:
    blackPin += 1
    choice[0] = None
    comRow[0] = None
elif choice[0] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[0] == comRow[2]:
    whitePin += 1
    comRow[2] = None
elif choice[0] == comRow [3]:
    whitePin += 1
    comRow[3] = None
    
if choice[1] == comRow[1]:
    blackPin += 1
    choice[1] = None
    comRow[1] = None
elif choice[1] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[1] == comRow[2]:
    whitePin += 1
    comRow[2] = None
elif choice[1] == comRow[3]:
    whitePin += 1
    comRow[3] = None
    
if choice[2] == comRow[2]:
    blackPin += 1
    choice[2] = None
    comRow[2] = None
elif choice[2] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[2] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[2] == comRow[3]:
    whitePin += 1
    comRow[3] = None

if choice[3] == comRow[3]:
    blackPin += 1
    choice[3] = None
    comRow[3] = None
elif choice[3] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[3] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[3] == comRow[2]:
    whitePin += 1
    comRow[2] = None   

if blackPin == 4:
    print("You win!")
    exit()

print(f"Black pins: {blackPin}")
print(f"White pins: {whitePin}")
whitePin = 0
blackPin = 0

print("Number of guesses: 7/12")
print("Next guess")
col1 = input("Color 1")
col2 = input("Color 2")
col3 = input("Color 3")
col4 = input("Color 4")
choice = [col1, col2, col3, col4]
print(choice)

if choice[0] == comRow[0]:
    blackPin += 1
    choice[0] = None
    comRow[0] = None
elif choice[0] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[0] == comRow[2]:
    whitePin += 1
    comRow[2] = None
elif choice[0] == comRow [3]:
    whitePin += 1
    comRow[3] = None
    
if choice[1] == comRow[1]:
    blackPin += 1
    choice[1] = None
    comRow[1] = None
elif choice[1] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[1] == comRow[2]:
    whitePin += 1
    comRow[2] = None
elif choice[1] == comRow[3]:
    whitePin += 1
    comRow[3] = None
    
if choice[2] == comRow[2]:
    blackPin += 1
    choice[2] = None
    comRow[2] = None
elif choice[2] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[2] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[2] == comRow[3]:
    whitePin += 1
    comRow[3] = None

if choice[3] == comRow[3]:
    blackPin += 1
    choice[3] = None
    comRow[3] = None
elif choice[3] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[3] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[3] == comRow[2]:
    whitePin += 1
    comRow[2] = None   

if blackPin == 4:
    print("You win!")
    exit()

print(f"Black pins: {blackPin}")
print(f"White pins: {whitePin}")
whitePin = 0
blackPin = 0

print("Number of guesses: 8/12")
print("Next guess")
col1 = input("Color 1")
col2 = input("Color 2")
col3 = input("Color 3")
col4 = input("Color 4")
choice = [col1, col2, col3, col4]
print(choice)

if choice[0] == comRow[0]:
    blackPin += 1
    choice[0] = None
    comRow[0] = None
elif choice[0] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[0] == comRow[2]:
    whitePin += 1
    comRow[2] = None
elif choice[0] == comRow [3]:
    whitePin += 1
    comRow[3] = None
    
if choice[1] == comRow[1]:
    blackPin += 1
    choice[1] = None
    comRow[1] = None
elif choice[1] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[1] == comRow[2]:
    whitePin += 1
    comRow[2] = None
elif choice[1] == comRow[3]:
    whitePin += 1
    comRow[3] = None
    
if choice[2] == comRow[2]:
    blackPin += 1
    choice[2] = None
    comRow[2] = None
elif choice[2] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[2] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[2] == comRow[3]:
    whitePin += 1
    comRow[3] = None

if choice[3] == comRow[3]:
    blackPin += 1
    choice[3] = None
    comRow[3] = None
elif choice[3] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[3] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[3] == comRow[2]:
    whitePin += 1
    comRow[2] = None   

if blackPin == 4:
    print("You win!")
    exit()

print(f"Black pins: {blackPin}")
print(f"White pins: {whitePin}")
whitePin = 0
blackPin = 0

print("Number of guesses: 9/12")
print("Next guess")
col1 = input("Color 1")
col2 = input("Color 2")
col3 = input("Color 3")
col4 = input("Color 4")
choice = [col1, col2, col3, col4]
print(choice)

if choice[0] == comRow[0]:
    blackPin += 1
    choice[0] = None
    comRow[0] = None
elif choice[0] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[0] == comRow[2]:
    whitePin += 1
    comRow[2] = None
elif choice[0] == comRow [3]:
    whitePin += 1
    comRow[3] = None
    
if choice[1] == comRow[1]:
    blackPin += 1
    choice[1] = None
    comRow[1] = None
elif choice[1] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[1] == comRow[2]:
    whitePin += 1
    comRow[2] = None
elif choice[1] == comRow[3]:
    whitePin += 1
    comRow[3] = None
    
if choice[2] == comRow[2]:
    blackPin += 1
    choice[2] = None
    comRow[2] = None
elif choice[2] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[2] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[2] == comRow[3]:
    whitePin += 1
    comRow[3] = None

if choice[3] == comRow[3]:
    blackPin += 1
    choice[3] = None
    comRow[3] = None
elif choice[3] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[3] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[3] == comRow[2]:
    whitePin += 1
    comRow[2] = None   

if blackPin == 4:
    print("You win!")
    exit()

print(f"Black pins: {blackPin}")
print(f"White pins: {whitePin}")
whitePin = 0
blackPin = 0

print("Number of guesses: 10/12")
print("Next guess")
col1 = input("Color 1")
col2 = input("Color 2")
col3 = input("Color 3")
col4 = input("Color 4")
choice = [col1, col2, col3, col4]
print(choice)

if choice[0] == comRow[0]:
    blackPin += 1
    choice[0] = None
    comRow[0] = None
elif choice[0] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[0] == comRow[2]:
    whitePin += 1
    comRow[2] = None
elif choice[0] == comRow [3]:
    whitePin += 1
    comRow[3] = None
    
if choice[1] == comRow[1]:
    blackPin += 1
    choice[1] = None
    comRow[1] = None
elif choice[1] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[1] == comRow[2]:
    whitePin += 1
    comRow[2] = None
elif choice[1] == comRow[3]:
    whitePin += 1
    comRow[3] = None
    
if choice[2] == comRow[2]:
    blackPin += 1
    choice[2] = None
    comRow[2] = None
elif choice[2] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[2] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[2] == comRow[3]:
    whitePin += 1
    comRow[3] = None

if choice[3] == comRow[3]:
    blackPin += 1
    choice[3] = None
    comRow[3] = None
elif choice[3] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[3] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[3] == comRow[2]:
    whitePin += 1
    comRow[2] = None   

if blackPin == 4:
    print("You win!")
    exit()

print(f"Black pins: {blackPin}")
print(f"White pins: {whitePin}")
whitePin = 0
blackPin = 0

print("Number of guesses: 11/12")
print("Next guess")
col1 = input("Color 1")
col2 = input("Color 2")
col3 = input("Color 3")
col4 = input("Color 4")
choice = [col1, col2, col3, col4]
print(choice)

if choice[0] == comRow[0]:
    blackPin += 1
    choice[0] = None
    comRow[0] = None
elif choice[0] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[0] == comRow[2]:
    whitePin += 1
    comRow[2] = None
elif choice[0] == comRow [3]:
    whitePin += 1
    comRow[3] = None
    
if choice[1] == comRow[1]:
    blackPin += 1
    choice[1] = None
    comRow[1] = None
elif choice[1] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[1] == comRow[2]:
    whitePin += 1
    comRow[2] = None
elif choice[1] == comRow[3]:
    whitePin += 1
    comRow[3] = None
    
if choice[2] == comRow[2]:
    blackPin += 1
    choice[2] = None
    comRow[2] = None
elif choice[2] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[2] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[2] == comRow[3]:
    whitePin += 1
    comRow[3] = None

if choice[3] == comRow[3]:
    blackPin += 1
    choice[3] = None
    comRow[3] = None
elif choice[3] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[3] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[3] == comRow[2]:
    whitePin += 1
    comRow[2] = None   

if blackPin == 4:
    print("You win!")
    exit()

print(f"Black pins: {blackPin}")
print(f"White pins: {whitePin}")
whitePin = 0
blackPin = 0

print("Number of guesses: 12/12")
print("Final guess!")
col1 = input("Color 1")
col2 = input("Color 2")
col3 = input("Color 3")
col4 = input("Color 4")
choice = [col1, col2, col3, col4]
print(choice)

if choice[0] == comRow[0]:
    blackPin += 1
    choice[0] = None
    comRow[0] = None
elif choice[0] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[0] == comRow[2]:
    whitePin += 1
    comRow[2] = None
elif choice[0] == comRow [3]:
    whitePin += 1
    comRow[3] = None
    
if choice[1] == comRow[1]:
    blackPin += 1
    choice[1] = None
    comRow[1] = None
elif choice[1] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[1] == comRow[2]:
    whitePin += 1
    comRow[2] = None
elif choice[1] == comRow[3]:
    whitePin += 1
    comRow[3] = None
    
if choice[2] == comRow[2]:
    blackPin += 1
    choice[2] = None
    comRow[2] = None
elif choice[2] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[2] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[2] == comRow[3]:
    whitePin += 1
    comRow[3] = None

if choice[3] == comRow[3]:
    blackPin += 1
    choice[3] = None
    comRow[3] = None
elif choice[3] == comRow[0]:
    whitePin += 1
    comRow[0] = None
elif choice[3] == comRow[1]:
    whitePin += 1
    comRow[1] = None
elif choice[3] == comRow[2]:
    whitePin += 1
    comRow[2] = None   

if blackPin == 4:
    print("You win!")
    exit()
    
print("You lose!")
exit()
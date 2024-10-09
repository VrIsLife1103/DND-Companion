#import Lines
import random
import sys
from termcolor import colored, cprint
import pygame 
import json 
import tkinter as tk
from tkinter import scrolledtext
import re 

#Functions

def importFiles():
    global characterName
    global characterSpecies
    global attackList
    global characterInventory

    with open('character_data.json', 'r') as file:
        data = json.load(file)
    characterName = data['Character']['Name']
    # print('Name is',characterName)
    characterSpecies = data['Character']['Species']
    # print('Species is',characterSpecies)
    attackList = data['Weapon Attacks & Cantrips']
    # print('Attacks are',attackList)
    characterInventory = data['Inventory']
    # print('inventory Test 1: ',characterInventory)


def rollDice(howMany,diceType):

    global diceTotal
    global rollCount
    global PlayerName    
    # diceType = input('what dice type do you wanna roll? \n'  'd4, d6, d8, d10, d12, d20, d100: ')

    # diceAmount = int(input("How many dice would you like to roll?: "))
    # diceAmount = int(diceAmount)
    global diceAmount
    global showAllDiceRolls

    importFiles()


    #gets the users input

    showAllDiceRolls = input('Show all dice rolls?  \n Answer: True or False: ')
    

    rollCount = 0
    diceTotal = 0
    print(characterName, "Is rolling")
    for x in range (int(howMany)):
        if diceType == 'd4':
            Roll = random.randint(1,4)
            diceTotal = diceTotal + Roll
            rollCount += 1
            if showAllDiceRolls == 'True':
                print('roll count is ',colored(rollCount,'red'),'\n' 'the rolled number is', colored(Roll,'red'), '\n''the rolled total is ', colored(diceTotal,'red'))
                playDiceRoll() 
        elif diceType == 'd6':
            Roll = random.randint(1,6)
            diceTotal = diceTotal + Roll
            rollCount += 1
            if showAllDiceRolls == 'True':
                print('roll count is ',colored(rollCount,'red'),'\n' 'the rolled number is', colored(Roll,'red'), '\n''the rolled total is ', colored(diceTotal,'red'))
                playDiceRoll() 
        elif diceType == 'd8':
            Roll = random.randint(1,8)
            diceTotal = diceTotal + Roll
            rollCount += 1
            if showAllDiceRolls == 'True':
                print('roll count is ',colored(rollCount,'red'),'\n' 'the rolled number is', colored(Roll,'red'), '\n''the rolled total is ', colored(diceTotal,'red'))
                playDiceRoll() 
        elif diceType == 'd10':
            Roll = random.randint(1,10)
            diceTotal = diceTotal + Roll
            rollCount += 1
            if showAllDiceRolls == 'True':
                print('roll count is ',colored(rollCount,'red'),'\n' 'the rolled number is', colored(Roll,'red'), '\n''the rolled total is ', colored(diceTotal,'red'))
                playDiceRoll() 
        elif diceType == 'd12':
            Roll = random.randint(1,12)
            diceTotal = diceTotal + Roll
            rollCount += 1
            if showAllDiceRolls == 'True':
                print('roll count is ',colored(rollCount,'red'),'\n' 'the rolled number is', colored(Roll,'red'), '\n''the rolled total is ', colored(diceTotal,'red'))
                playDiceRoll() 
        elif diceType == 'd20':
            Roll = random.randint(1,20)
            diceTotal = diceTotal + Roll
            rollCount += 1
            if showAllDiceRolls == 'True':
                print('roll count is ',colored(rollCount,'red'),'\n' 'the rolled number is', colored(Roll,'red'), '\n''the rolled total is ', colored(diceTotal,'red'))
                playDiceRoll() 
        elif diceType == 'd100':
            Roll = random.randint(1,100)
            diceTotal = diceTotal + Roll
            rollCount += 1
            if showAllDiceRolls == 'True':
                print('roll count is ',colored(rollCount,'red'),'\n' 'the rolled number is', colored(Roll,'red'), '\n''the rolled total is ', colored(diceTotal,'red'))
                playDiceRoll()
    print('Number of dice rolled:',colored(howMany,'red'),'\n Dice type rolled:', colored(diceType,'red'),'\n Total amount rolled:',colored(diceTotal,'red'))
    playDiceRoll()


def mainAttackFunction():
    # Load the character data (Weapon Attacks & Cantrips) from the JSON file
    with open('character_data.json', 'r') as file:
        data = json.load(file)

    #Prints Inventory Legibly.
    printAttacks(data)
    choosenAttack = str(chooseAttack(data))  # Return dice roll string
    whatType = choosenAttack[1:]
    howManyDice = choosenAttack[:-2]
    print(howManyDice)
    print(whatType)
    rollDice(str(howManyDice),whatType)


def printAttacks(data):
    print(colored('----------Weapon Attacks & Cantrips----------','red'))
    for item in data['Weapon Attacks & Cantrips']:
        print(f'Name: {item['Name']}')
        print(f'Damage Type: {item['Damage/Type']}')
        print(f'Damage: {item['Dice Roll']}')
        print(f'Notes: {item['Notes']}')

        #Cleanly Seperates The Text
        print(colored('-' * 30,'red'))


def chooseAttack(data):
    choice = input('Please name the Weapon/Cantrip of choice: ')
    global choosenAttack
    for item in data['Weapon Attacks & Cantrips']:
        if f'{item['Name']}' == choice:
            print(f'Your weapon choice is {item['Name']}')
            print(f'You deal {item['Dice Roll']}')
            choosenAttack = f'{item['Dice Roll']}'
    return(choosenAttack)


def userMenue():
    #import File

    importFiles()

    #Setting Global Variables

    global PlayerChoice
    global areYouDone

    #Getting players Choice information
    playerChoice = input('What do you wanna do? \nRoll, Attack, Open Inventory, Take Notes, or Exit: ')
    
    #Setting the control variable
    areYouDone = 'No'

    #Starting the while loop(Needs Work)
    while areYouDone == 'No':
        areYouDone = 'No'
        if playerChoice == 'Roll':
            diceChoosen = input('what dice type do you wanna roll? \n'  'd4, d6, d8, d10, d12, d20, d100: ')
            amountToRoll = int(input('How many dice do you wish to roll'))
            rollDice(amountToRoll,diceChoosen)
            doneRolling = input('Are you done roling\nYes,No: ')
            if doneRolling == 'Yes':
                userMenue()
            else:
                diceType = input('what dice type do you wanna roll? \n'  'd4, d6, d8, d10, d12, d20, d100: ')
                rollDice(diceChoosen)
        elif playerChoice == 'Attack':
            mainAttackFunction()
        elif playerChoice == 'Open Inventory':
            mainInventoryFunction()
        elif playerChoice == 'Take Notes':
            open_notes_window()
        elif playerChoice == 'Exit':
            print('Exiting!?')
            break
        areYouDone = input('Are You Done?: \n Yes, No?: ')
        if areYouDone == 'No':
            userMenue
        else:
            print('Bye', characterName, ', have a wonderful rest of your day!')
            break


def playDiceRoll():
    # Initialize the mixer module in pygame
    pygame.mixer.init()

    # Load an audio file
    pygame.mixer.music.load('diceSFX.mp3')

    # Play the audio file
    pygame.mixer.music.play()

    # Keep the program running to listen to the audio
    while pygame.mixer.music.get_busy():  # Check if the music is still playing
        continue



def open_notes_window():
    # Create the main window
    root = tk.Tk()
    root.title("Edit Your Notes")

    # Create a scrolled text widget for the user to enter notes
    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20, font=("Times New Roman", 12))
    text_area.pack(padx=10, pady=10)
    
    # Load existing notes from a file (if available)
    try:
        with open('notes.txt', 'r') as file:
            notes = file.read()
            text_area.insert(tk.INSERT, notes)  # Insert the existing notes
    except FileNotFoundError:
        pass  # If no file, leave the text area empty

    def save_and_close():
        # Get the text from the text area
        user_notes = text_area.get(1.0, tk.END)

        # Save the notes to a file
        with open('notes.txt', 'w') as file:
            file.write(user_notes)

        # Close the window
        root.destroy()

        # Print the notes to the terminal
        print("User Notes:\n")
        print(user_notes)

    # Create a Save button that will save the notes and close the window
    save_button = tk.Button(root, text="Save & Close", command=save_and_close)
    save_button.pack(pady=10)

    # Start the Tkinter main loop (this will keep the window open)
    root.mainloop()


def print_inventory(data):
    """Displays the inventory in a readable format."""
    print("Inventory:")
    print("=" * 30)
    
    for item in data["Inventory"]["Items"]:
        print(f"Name: {item['Name']}")
        print(f"  Quantity: {item['Quantity']}")
        print(f"  Weight: {item['Weight']}")
        print(f"  Notes: {item['Notes']}")
        print("-" * 30)  # Separator between items


def add_item_to_inventory(data):
    """Prompts the user for item details and adds it to the inventory."""
    print("\n--- Add a New Item ---")
    
    # Get the details for the new item
    name = input("Enter the item name: ")
    quantity = input("Enter the item quantity: ")
    weight = input("Enter the item weight (or 'None' if unknown): ")
    notes = input("Enter any notes about the item: ")
    
    # Create a new item dictionary
    new_item = {
        "Name": name,
        "Quantity": quantity,
        "Weight": weight if weight.lower() != 'none' else None,
        "Notes": notes
    }
    
    # Append the new item to the inventory
    data["Inventory"]["Items"].append(new_item)
    print(f"Item '{name}' added to the inventory!")


def save_inventory(data, filename='character_data.json'):
    """Saves the updated inventory back to the JSON file."""
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Inventory saved to {filename}!")


def mainInventoryFunction():
    # Load the character data (inventory) from the JSON file
    with open('character_data.json', 'r') as file:
        data = json.load(file)
    
    # Display the current inventory
    print_inventory(data)
    
    # Ask the user if they want to add a new item
    while True:
        choice = input("Do you want to add a new item to the inventory? (yes/no): ").lower()
        if choice == 'yes':
            add_item_to_inventory(data)
        elif choice == 'no':
            break
        else:
            print("Please enter 'yes' or 'no'.")
    
    # Save the updated inventory back to the JSON file
    save_inventory(data)
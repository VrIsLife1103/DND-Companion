#import Lines
import random
import sys
from termcolor import colored, cprint
import pygame 

#Functions

def importFiles():
    with open('character.json', 'r') as file:
    data = json.load(file)



def rollDice():

    global diceTotal
    global rollCount
    global PlayerName
    global diceType
    global diceAmount
    global showAllDiceRolls


    #gets the users input

    PlayerName = colored(input('Please enter your character Name: '),'red')

    diceType = input('what dice type do you wanna roll? \n'  'd4, d6, d8, d10, d12, d20, d100: ')

    diceAmount = int(input("How many dice would you like to roll?"))
    diceAmount = int(diceAmount)

    showAllDiceRolls = input('Show all dice rolls?  \n Answer: True or False')



    rollCount = 0
    diceTotal = 0
    print(PlayerName, "Is rolling")
    for x in range (diceAmount):
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
    print('Number of dice rolled:',colored(diceAmount,'red'),'\n Dice type rolled:', colored(diceType,'red'),'\n Total amount rolled:',colored(diceTotal,'red'))
    playDiceRoll()


def Attack(name):
    if name == 'WrkYaBitch':
        print('it fkn works')



def userMenue():
    #import files

    attacksFile = open('attacks.txt','r')
    readAttacks = attacksFile.readlines()
    Attacks = []
    for line in readAttacks:
        if line[-1] == '\n':
            Attacks.append(line[:-1])
        else:
            Attacks.append(line)

    spellsFile = open('Spells.txt','r')
    readSpells = spellsFile.readlines()
    Spells = []
    for line in readSpells:
        if line[-1] == '\n':
            Spells.append(line[:-1])
        else:
            Spells.append(line)

    userInventoryFile = open('playerInventory.txt','r')
    readInventory = userInventoryFile.readlines()
    Inventory = []
    for line in readInventory:
        if line[-1] == '\n':
            Inventory.append(line[:-1])
        else:
            Inventory.append(line)

    userNotesFile = open('userNotes.txt','r')
    readNotes = userNotesFile.readlines()
    Notes = []
    for line in readNotes:
        if line[-1] == '\n':
            Notes.append(line[:-1])
        else:
            Notes.append(line)

    global PlayerChoice
    global areYouDone
    playerChoice = input('What do you wanna do? \nRoll, Attack, Open Inventory, Take Notes, or Exit: ')
    areYouDone = 'No'
    while areYouDone == 'No':
        areYouDone = 'No'
        if playerChoice == 'Roll':
            rollDice()
        elif playerChoice == 'Attack':
            spellOrWeapon = input('Weapon or Spell?:')
            if spellOrWeapon == 'Weapon':
                userWeapon = input('What weapon do you use?:')
                if userWeapon == 'Fists':
                    print('Finish Later')
            else:
                userSpell = input('what spell do you cast?:')
                if userSpell == 'WildShape':
                    print('Finish Later')
        elif playerChoice == 'Open Inventory':
            print(colored(Inventory,'red'))
            inventoryManage = input('Exit, Add, Remove?: ')
            if inventoryManage == 'Exit':
                break
            elif inventoryManage == 'Add':
                print('Finsih Later')
            elif inventoryManage == 'Remove':
                print('Finish Later')
        elif playerChoice == 'Take Notes':
            print(colored(Notes,'red'))
            manageNotes = input('Add, Remove, Exit:')
            if manageNotes == 'Add':
                addToNotes = input('Line To Add: ')
                userNotesFile = open('userNotes.txt','a')
                userNotesFile.writelines('\n' + addToNotes)
                print(colored(Notes),'red')
                userNotesFile.close()
            elif manageNotes == 'Remove':
                removeFromNotes = input('Text Letter By letter to remove: ')
                userNotesFile.close()
                print('Finish Later')
            elif manageNotes == 'Exit':
                userNotesFile.close()
                break 
        elif playerChoice == 'Exit':
            print('Exiting!?')
            break
        areYouDone = input('Are You Done?: \n Yes,No?: ')
        userNotesFile.close()


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
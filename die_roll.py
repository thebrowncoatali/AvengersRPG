"""
deals with the die rolls in the MainPRG program 
"""
import random

def DiceRoll(roll):
    """
    deals with rolling the dice 
    args:
        roll: the roll of the dice
    """

    roll_sum = random.randint(2,12)

    return(roll_sum)#returns the sum of the dice rolls 

def RollStatements(rolls):
    """
    returns statemetns that correspond with loss, critloss, win and critwin statements
    args:
        rolls: the sum of the die with stat bonus
    return:
        challenge_state: returns a statement based on the sum of the die. 
    """
    if(rolls <= 4):
        challenge_state = "***you recieved a critical loss, associated stats are decreased***\n***you've been damaged severely, and you run away***"
        return(challenge_state)
    elif(rolls >= 5 and rolls <=7):
        challenge_state = "***you recieved a loss, associated stats stay the same***\n***you run away ***"
        return(challenge_state)
    elif(rolls >=8 and rolls <=11):
        challenge_state = "***you recieved a win, associated stats stay the same***\n***you beat the challenge***"
        return(challenge_state)
    elif(rolls >=12):
        challenge_state = '***you recieved a critical win, associated stats increase***\n***you beat the challenge and sharpen your skills*** '
        return(challenge_state)
        
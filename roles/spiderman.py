"""
	deals with creating the character Spiderman
"""
def Spiderman(STR, INT, AGL):
    """
    determines Spiderman Traits/ attributes
    Args:
        STR: Spiderman strength
        INT: Spiderman intelligence 
        HP: Spiderman health
    return:
        Spiderman stats
    """
    SPIDERMANSTR = STR
    SPIDERMANINT = INT
    SPIDERMANAGL = AGL

    

    return(SPIDERMANSTR, SPIDERMANINT, SPIDERMANAGL)#returns Spiderman stats

def Agility(bonus, AGL):
    """
    determins what agility stats are lost or gained
    args:
        bonus: the sum of the die with stat multiplier.
    return:
        AGL: Spiderman remaining agility
    """
    if(bonus <= 4):
        AGL = AGL - 1
        return(AGL)
    elif(bonus >= 5 and bonus <=7):
        AGL = AGL + 0
        return(AGL)
    elif(bonus >=8 and bonus <=11):
        AGL = AGL + 0
        return(AGL)
    elif(bonus >=12):
        AGL = AGL + 1
        return(AGL)
        
def Strength(bonus, STR):
    """
    determins what Strength stats are lost or gained
    args:
        bonus: the sum of the die with stat multiplier.
    return:
        STR: Spiderman remaining strength
    """
    if(bonus <= 4):
        STR = STR - 1
        return(STR)
    elif(bonus >= 5 and bonus <=7):
        STR = STR + 0
        return(STR)
    elif(bonus >=8 and bonus <=11):
        STR = STR + 0
        return(STR)
    elif(bonus >=12):
        STR = STR + 1
        return(STR)

def Intelligence(bonus, INT):
    """
    determins what intelligence stats are lost or gained
    args:
        bonus: the sum of the die with stat multiplier.
    return:
        INT: Spiderman remaining intelligence
    """
    if(bonus <= 4):
        INT = INT - 1
        return(INT)
    elif(bonus >= 5 and bonus <=7):
        INT = INT + 0
        return(INT)
    elif(bonus >=8 and bonus <=11):
        INT = INT + 0
        return(INT)
    elif(bonus >=12):
        INT = INT + 1 
        return(INT)

def WinLossStatements(count,special):
    """
    Determines if Spiderman has won or lost the game
    args:
        count: how many losses Spiderman has gotten on his journey 
        special: how many critical wins Spiderman has gotten
    return:
        winloss: win or loss statement
    """
    if(special == 2):
    	#PERFECT WIN two critical wins(impossible to have 3 critwins since Spiderman has a -2 intellegence and you need a 12 for a critwin)
        win_or_loss = "***You have stolen the infinity gauntlet from Thanos\nyou have given it to Tony Stark and he has used it to eliminate the entire chitauri army. Iron Man resists the power unleashed by the Infinity Gauntlet and he lives. CONGRATULATIONS! You've beat the game.***"
        return(win_or_loss)
    elif(count == 0):#no loss win 
        win_or_loss = "******You have stolen the infinity gauntlet from Thanos\nyou have given it to Tony Stark and he has used it to eliminate the entire chitauri army. CONGRATULATIONS! You've beat the game.***"
        return(win_or_loss)
    elif(count == 1):#one loss win 
        win_or_loss = "***Thanos and his army are gone.\nCONGRATULATIONS! You've beat the game.***"
        return(win_or_loss)
    elif(count >= 2):#lose game/ game over
        win_or_loss = "***You did not get the mission done\nThanos snapped his fingers\nGAME OVER***"
        return(win_or_loss)
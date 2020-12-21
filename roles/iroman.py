"""
	deals with creating the character Iroman
"""
def Iroman(STR, INT, AGL):
    """
    determines Iroman Traits/ attributes
    Args:
        STR: Iroman strength
        INT: Iroman intelligence 
        HP: Iroman health
    return:
        Iroman stats
    """
    IROMANSTR = STR
    IROMANINT = INT
    IROMANAGL = AGL

    

    return(IROMANSTR, IROMANINT, IROMANAGL)#returns Iroman stats

def Agility(bonus, AGL):
    """
    determins what agility stats are lost or gained
    args:
        bonus: the sum of the die with stat multiplier.
    return:
        AGL: Iroman remaining agility
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
        STR: Iroman remaining strength
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
        INT: Iroman remaining intelligence
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
    Determines if Iroman has won or lost the game
    args:
        count: how many losses Iroman has gotten on his journey 
        special: how many critical wins Iroman has gotten
    return:
        winloss: win or loss statement
    """
    if(special == 2):
    	#PERFECT WIN
        win_or_loss = "***You have snatched the infinity gauntlet from thanos' hand and snapped your fingers to eliminate him along with his entire army. you resisted the snap CONGRATULATIONS! You've beat the game.***"
        return(win_or_loss)
    elif(count == 0):#no loss win 
        win_or_loss = "***You have snatched the infinity gauntlet from thanos' hand and snapped your fingers to eliminate him along with his entire army. your life has saved many CONGRATULATIONS! You've beat the game.***"
        return(win_or_loss)
    elif(count == 1):#one loss win 
        win_or_loss = "***Thanos and his army are gone.\nCONGRATULATIONS! You've beat the game.***"
        return(win_or_loss)
    elif(count >= 2):#lose game/ game over
        win_or_loss = "***You did not get the mission done\nThanos snapped his fingers\nGAME OVER***"
        return(win_or_loss)
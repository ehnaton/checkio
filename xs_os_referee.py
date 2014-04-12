def checkio(game_result):
    
    output, finallist = [], []
    
    for i in range(0,3):
	#check each vertical column, output - 3 list elements
        output.append(''.join([(val[i]) for val in game_result]))
	#check one of the 2 diagonal options, output - 1
        output.append(''.join([(val[key]) for key,val in enumerate(reversed(game_result))]))
	#check the remaining diagonal option, output - 1
        output.append(''.join([(val[key]) for key,val in enumerate(game_result)]))
    #final list consists of 3 given + 5 items from above, total 8 probable outcome 
    finallist = output + game_result
    
    if 'X'*3 in finallist:
        return 'X'
    elif 'O'*3 in finallist:
        return 'O'
    return 'D'
        
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"
    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"
    assert checkio([
        u"O.X",
        u"XX.",
        u"XOO"]) == "X", "Xs wins again"



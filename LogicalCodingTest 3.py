def countOff(numberOfPlayers: int) -> int:
    '''
    This function is for finding out the index of the last survivor in a 
    "1, 2, 3" count-off game.
    The man counting number 3 will left the game while the others keep counting off.
    The game will be continue until only one player remaining.
    
    e.g. input: 3
         output: 2
    '''
    
    if numberOfPlayers < 0 or numberOfPlayers > 100:
        raise Exception("The number of players should be in range 0-100.")
    if numberOfPlayers == 0:
        raise Exception("There's no players in this game.")
    # If there's only one winner, return index 0
    if numberOfPlayers == 1:
        return 0

    # The number of each player.
    players = [n for n in range(numberOfPlayers)]
    # The index that will be first removed in the next round.
    indexToBeRemoved = 2
    
    while len(players) > 1:
        while indexToBeRemoved < len(players):
            # Remove the player.
            players.pop(indexToBeRemoved)
            # After removal, the remaining elements move forward and the indices
            # change.
            indexToBeRemoved += 2
        
        # Before last removal: [a, b, c, d, e], indexToBeRemoved = 2
        # After last removal: [a, b, d, e], indexToBeRemoved = 4
        #
        # If (indexToBeRemoved - arraySize) = 0, the next index to be removed should
        # be 0.
        #
        #
        # Before last removal: [a, b, c, d], indexToBeRemoved = 2
        # After last removal: [a, b, d], indexToBeRemoved = 4
        #
        # If (indexToBeRemoved - arraySize) = 1, the next index to be removed should
        # be 1.
        #
        #
        # Before last removal: [a, b, d, e, f], indexToBeRemoved = 4
        # After last removal: [a, b, d, e], indexToBeRemoved = 6
        #
        # If (indexToBeRemoved - arraySize) = 2, the next index to be removed should
        # be 2(will be index 0 if arraySize == 2).
        #
        indexToBeRemoved = (indexToBeRemoved - len(players)) % len(players)
    
    # Return the number of the remaining player.
    return players[0]


#input1 = 0
input2 = 1
input3 = 2
input4 = 3
input5 = 4
input6 = 5
input7 = 6
input8 = 100
#input9 = -1

#print("\nTestcase1:", input1)
#print(countOff(input1))
print("\nTestcase2:", input2)
print(countOff(input2))
print("\nTestcase3:", input3)
print(countOff(input3))
print("\nTestcase4:", input4)
print(countOff(input4))
print("\nTestcase5:", input5)
print(countOff(input5))
print("\nTestcase6:", input6)
print(countOff(input6))
print("\nTestcase7:", input7)
print(countOff(input7))
print("\nTestcase8:", input8)
print(countOff(input8))
#print("\nTestcase9:", input9)
#print(countOff(input9))

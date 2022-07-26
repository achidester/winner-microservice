#############################################################################################
# Winner.py microservice
#   Reads dealers hand (line 0) and users hand (line 1) from a text file
#   Evaluates winner and loser (Or tie) based on the rules of blackjack
#   Currently prints the results directly to screen (can be modified to record to txt file)
#
#############################################################################################


with open('hands.txt', 'r') as hands:
    hands.seek(0)                   #sets readline's "cursor" to the first line of file
    dealers_hand = int(hands.readline()) #reads 0'th line 
    users_hand = int(hands.readline())   #reads 1st line

    if dealers_hand < 22 and users_hand < 22: 
        if dealers_hand > users_hand and dealers_hand < 22:
            print("\nDealers hand: %s\nYour hand: %s \n\nDealer Wins" %(dealers_hand, users_hand))
        elif users_hand > dealers_hand and users_hand < 22:
            print("\nDealers hand: %s\nYour hand: %s \n\nYou Win" %(dealers_hand, users_hand))
        else:
            print("\nDealers hand: %s\nYour hand: %s \n\nIt's a Tie" %(dealers_hand, users_hand))
    elif dealers_hand >= 22 and users_hand < 22:
        print("\nDealers hand: %s\nYour hand: %s \n\nDealer bust, you win" %(dealers_hand, users_hand))
    elif users_hand >=22 and dealers_hand < 22:
        print("\nDealers hand: %s\nYour hand: %s \n\nYou bust, dealer wins" %(dealers_hand, users_hand))
    elif dealers_hand >=22 and users_hand >=22:
        print("\nDealers hand: %s\nYour hand: %s \n\nBoth bust, It's a Tie" %(dealers_hand, users_hand))
    


    hands.close()
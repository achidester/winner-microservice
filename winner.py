#############################################################################################
# Winner.py microservice
#   Reads dealers hand (line 0) and users hand (line 1) from a text file
#   Evaluates results based on the rules of blackjack, writes them to results.txt
#   
#############################################################################################


with open('hands.txt', 'r') as hands, open('results.txt', 'w') as results:

    dealers_hand = int(hands.readline()) #reads 0'th line
    users_hand = int(hands.readline())   #reads 1st line

    if dealers_hand < 22 and users_hand < 22: 
        if dealers_hand > users_hand:
            results.write("Dealers hand: %s\nYour hand: %s \n\nDealer Wins" %(dealers_hand, users_hand))
        elif users_hand > dealers_hand:
            results.write("Dealers hand: %s\nYour hand: %s \n\nYou Win" %(dealers_hand, users_hand))
        else:
            results.write("Dealers hand: %s\nYour hand: %s \n\nIt's a Tie" %(dealers_hand, users_hand))
    elif dealers_hand >= 22 and users_hand < 22:
        results.write("Dealers hand: %s\nYour hand: %s \n\nDealer bust, you win" %(dealers_hand, users_hand))
    elif users_hand >=22 and dealers_hand < 22:
        results.write("Dealers hand: %s\nYour hand: %s \n\nYou bust, dealer wins" %(dealers_hand, users_hand))
    elif dealers_hand >=22 and users_hand >=22:
        results.write("Dealers hand: %s\nYour hand: %s \n\nBoth bust, It's a Tie" %(dealers_hand, users_hand))
    else:
        results.write("Error: readHands unable to parse data.")

    hands.close()
    results.close()
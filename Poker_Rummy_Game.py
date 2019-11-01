#####################################
#             Rummy Game            #
#####################################
import random


def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
        input("\nPress enter to continue. ")
        print()
    except SyntaxError:
        pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck = []
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663')  # remove a queen as the game requires
    return deck


def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)



def deal_cards(deck):
    '''(list of str)-> tuple of (list of str,list of str)

    Returns two lists representing two decks that are obtained
    after the dealer deals the cards from the given deck.
    The first list represents dealer's i.e. computer's deck
    and the second represents the other player's i.e user's list.
    '''
    dealer = deck[1::2]
    other = deck[::2]

    return (dealer, other)


def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs = []
    l.sort()

    count = 1
    for i in range(len(l)-1):
        if l[i][:-1] == l[i+1][:-1]:
            count += 1
        else:
            if count % 2 != 0:
                no_pairs.append(l[i])
            count = 1
    if len(l) > 0 and count % 2 != 0:
        no_pairs.append(l[-1])

    random.shuffle(no_pairs)
    return no_pairs


def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''
    print()
    for i in deck:
        print(i, end=' ')
    print()
    print()

def get_valid_input(n):
    '''
    (int)->int
    Returns an integer given by the user that is at least 1 and at most n.
    Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]

    Precondition: n>=1
    '''
    get = True
    user_input = int(input("Give me an integer between 1 and "+str(n)+": "))
    while(get):
        if user_input >= 1 and user_input <= n:
            get = False
        else:
            user_input = int(
                input("Invalid number. Please enter integer between 1 and "+str(n)+": "))

    return user_input


def play_game():
    '''()->None
    This function plays the game'''

    deck = make_deck()
    shuffle_deck(deck)
    tmp = deal_cards(deck)

    dealer = tmp[0]
    human = tmp[1]

    print("Hello. My name is Robot and I am the dealer.")
    print("Welcome to my card game!")
    print("Your current deck of cards is:")
    print_deck(human)
    print("Do not worry. I cannot see the order of your cards")

    print("Now discard all the pairs from your deck. I will do the same.")
    wait_for_player()

    dealer = remove_pairs(dealer)
    human = remove_pairs(human)

    while (len(human) > 0 and len(dealer) > 0):
        print("Your turn.")
        print()
        print("Your current deck of cards is:")
        print_deck(human)
        print("I have "+str(len(dealer))+" cards. If 1 stands for my first card and " +
              str(len(dealer))+" stands for my last card, which of my cards would you like?")

        k = get_valid_input(len(dealer))
        if k == 1:
            print("You asked for my 1st card.")
        elif k == 2:
            print("You asked for my 2nd card.")
        elif k == 3:
            print("You asked for my 3rd card.")
        else:
            print("You asked for my "+str(k)+"th card.")

        added = dealer[k-1]
        print("Here it is. It is "+added)
        human.append(added)
        dealer.remove(added)
        print()
        print("With "+added+" added, your current deck of cards is:")
        print_deck(human)
        human = remove_pairs(human)
        print("And after discarding pairs and shuffling, your deck is: ")
        print_deck(human)
        wait_for_player()

        print("My turn.")
        print()
        robot_input = random.randint(1, len(human))
        if robot_input == 1:
            print("I took your 1st card.")
        elif robot_input == 2:
            print("I took your 2nd card.")
        elif robot_input == 3:
            print("I took your 3rd card.")
        else:
            print("I took your "+str(robot_input)+"th card.")
        robot_added = human[robot_input-1]
        dealer.append(robot_added)
        human.remove(robot_added)
        wait_for_player()
    if len(human) == 0:
        print("Ups. You do not have any more cards.")
        print("Congulatulations! You, Human, win!")
    else:
        print("Ups. I do not have any more cards.")
        print("You lost! I, Robot, win!")


# main
play_game()

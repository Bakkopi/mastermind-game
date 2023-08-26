import random

# Returns a list of 4 random colours from the possible selections.
def randomizer(colours):
    codemaster = []
    for i in range(4):
        choose = random.choice(colours)
        codemaster.append(choose)
    return codemaster

# Prints a divider line between sections.
def divider():
    print("-" * 55)
    print()

# Compares user's colour inputs w/ computer generated colours.
# Returns the number of partial and perfect matches.
def comparator(codemaster, user_result):
    matched = ["", "", "", ""]
    one_correct = 0
    both_correct = 0
    for u in range(4):
        match = 0
        for c in range(4):
            if user_result[u] == codemaster[c] and u == c:      # Conditional for perfect match.
                if match == 1:
                    match = 0
                if matched[c] == codemaster[c]:
                    one_correct -= 1
                matched[c] = "X"
                break
            elif user_result[u] == codemaster[c] and u != c:    # Conditional for partial match.
                if matched[c] != "X" and matched[c] != user_result[u] and match == 0:
                    matched[c] = user_result[u]
                    match = 1
        if match == 1:
            one_correct += 1
    for m in matched:
        if m == "X":
            both_correct += 1
    return one_correct, both_correct

# Converts list into board format.
def unwrap(listo):
    for e in listo:
        print("(%s)" % e, end=" ")
    print()

# Outputs a unique string for different num of attempts taken.
def end_remark(score):
    if score == 1:
        print("You finished it in 1 attempt! What a prodigy! (^ o ^   )")
    elif score > 1 and score <= 5:
        print("You finished it in %s attempts. Amazing!" % score)
    elif score > 5 and score <= 20:
        print("You finished it in %s attempts. Good job!" % score)
    elif score > 20:
        print("You finished it in %s attempts. What a battle that was!" % score)

# Returns the second element of a list.
def sortbysecond(lst):
    return lst[1]

# Creates a leaderboard entry in the form of a list.
def add_lb(username, attempts):
    lb = []
    lb.append(username)
    lb.append(attempts)
    return lb

# Sorts leaderboard entries by num of attempts.
def sort_lb(lb):
    lb.sort(key=sortbysecond)
    return lb

# Displays leaderboard in an orderly format.
def show_lb(lb):
    print((" " * 15) + "LEADERBOARD")
    print()
    print(" #              Username        Attempts")
    ranking = 1
    leaderboard = sort_lb(lb)
    for sublist in leaderboard:
        name = sublist[0]
        attempts = sublist[1]
        print("%2d  %20s %15s" % (ranking, name, attempts))
        ranking += 1

# Possible colour selections.
colours = ["R", "Y", "G", "B", "V", "C"]

# Initializing assignments and flags.
codemaster = []
leaderboard = []
keep_looping = 1
end_prompt = ""
keep_playing = "y"

print()
print("WELCOME TO MASTERMIND!  \('o' )/")
print()
print("Crack the secret 4-colour code to win!")
print("Enter the first letter for each colour (Colours can be repeated!)")
print()
print()

# Loop allows user to start a new game after completion.
while keep_playing == "y":
    codemaster = randomizer(colours)        # Sets up randomly generated colour list.
    attempts = 1
    username = ""

    # Loop ensures username is entered and is not >20 characters.
    while len(username) == 0 or len(username) > 20:
        username = str(input("Enter USERNAME (<20 char): ")).upper()
        if len(username) == 0:
            print("Please enter a username.")
        elif len(username) > 20:
            print("Username too long!")
        print()

    # Loop allows user to continue retrying combinations until code is broken.
    keep_looping = 1
    while keep_looping == 1:
        user_combo = []

        divider()
        print("Pick a combination of 4: ")
        print("Red(R), Yellow(Y), Green(G), Blue(B), Violet(V), Cyan(C)")
        print()
        print("Attempt %s" % attempts)

        # Iterative for user to enter 4-colour code guess.
        for x in range(1, 5):
            entry = str(input("Colour " + str(x) + " : ").upper())
            while (entry in colours) == False:              # Checks if entry is a valid colour.
                entry = str(input("Re-enter colour " + str(x) + ": ").upper())
            user_combo.append(entry)

        oneCorrect, bothCorrect = comparator(codemaster, user_combo)     # Retrieves num of partial and perfect matches.

        # Displays user combination and results.
        print()
        print("Your combination:", end=" ")
        unwrap(user_combo)
        if bothCorrect < 4:             # Output for incorrect combination.
            print("Colour RIGHT, position WRONG: " + str(oneCorrect))
            print("Colour RIGHT, position RIGHT: " + str(bothCorrect))
            print()
            if bothCorrect == 3:
                print("So close! Try again. q(^-^q)")
                print()
            else:
                print("It's alright! Try again. q(^-^q)")
                print()
            attempts += 1
        else:                           # Output for correct combination.
            print()
            print("CODE BROKEN")
            print()
            end_remark(attempts)            # Unique output based on num of attempts.
            keep_looping = 0
            print()
            leaderboard.append(add_lb(username, attempts))          # Adds result to leaderboard list.
            print()
            print()
            show_lb(leaderboard)        # Displays leaderboard.
            print()
            print()

    # Choice for user to start a new game.
    keep_playing = ""
    while keep_playing != "y" and keep_playing != "n":
        keep_playing = str(input("Wanna play again? (y/n) ")).lower()
        if keep_playing != "y" and keep_playing != "n":
            print("Sorry, didn't quite catch that.")
            print()
    print()
    divider()

print("Good Game!")





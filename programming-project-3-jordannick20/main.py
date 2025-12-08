import csv
def load_story():
    # Reads the CSV file and returns a 2D list 
    try:
        infile = open("story.csv","r",)
        csvreader = csv.reader(infile)
        story_data = []
        # row is a list of strings
        for row in csvreader:
            story_data.append(row)
        infile.close()
    except FileNotFoundError:
        print("ERROR: csv file not found WOMP WOMP.")
        return False

    return story_data

def display_menu():
    # Shows the main game menu and returns a number 1 2 or 3 once validated 
    print("****** Text Adventure Game v1.0 ******")
    print("*                                    *")
    print("*           1 - New Game             *")
    print("*           2 - Load Game            *")
    print("*           3 - Quit                 *")
    print("*                                    *")
    print("**************************************")

    while True:
        choice = input("> ")

        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("wrong choice bucko. Please enter 1, 2, or 3.")

def get_saved_progress():
    # Returns saved line number if saved.txt exists
    try:
        infile = open("saved.txt","r") 
        value = infile.read()
        infile.close()
        # returns the number in the txt file
        return int(value)   
    except:
        return False

def save_progress(line_number):
    # Saves the player’s current story position in file open creates the txt file
    infile = open("saved.txt","w")
    infile.write(str(line_number))
    infile.close()
    print("Game Saved")

def play_game(story_data, zero):
    current = zero
    while True:
        # story_data is a 2D list and current is 0 because row = the first row in the csv row must have [0] or else it would print this row ['Should I add a database to my app?', 'Use MS Access', 'No way - databases suck', '2', '3']
        row = story_data[current]
        # plot text = row 0 column 0
        plot_text = row[0]
       
        # option 1 uses greater than operator and uses len to return the ammount of items and if row has more then one row in it and the column does not equal an empty string option 1 equals row 0 column 1
        if len(row) > 1 and (row[1] != ""):
            option1 = row[1]
        else:
            option1 = False
   
        # option 2
        if len(row) > 1 and (row[2] != ""):
            option2 = row[2]
        else:
            option2 = False

        # destination 1 if column 3 = 2 for example 2 - 1 = 1 dest1 = 1
        if len(row) > 1 and (row[3] != ""):
            dest1 = int(row[3]) - 1
        else:
            dest1 = False 

        # destination 2
        if len(row) > 1 and (row[4] != ""):
            dest2 = int(row[4]) - 1
        else:
            dest2 = False

        print(plot_text)

        # Ends story if both are false
        if (option1 == False) and (option2 == False):
            print("The story ends here.")
            break
            
        print("What do you want to do?")
        if (option1 != False):
            print(f"1 - {option1}")
        if (option2 != False):
            print(f"2 - {option2}")
        print("3 - Save Game")

        while True:
            choice = input("> ")
            # if the user inputs one the next row they will go to is the int value in dest1
            if (choice == "1") and (dest1 != False):
                current = dest1
                break
            elif (choice == "2") and (dest2 != False):
                current = dest2
                break
            elif (choice == "3"):
                # saves the current row the player is on to a txt file
                save_progress(current)
                break
            else:
                print("Invalid input. Please enter 1, 2, or a 3.")

def main():
    zero = 0
    story_data = load_story()
    if (story_data == False):
        # if csv file can not be found main program shuts down
        return

    while True:
        choice = display_menu()
        # New Game if user inputs 1
        if (choice == "1"):  
            play_game(story_data, zero)
        # Load Game if user inputs 2 if no save start new game
        elif (choice == "2"):
            # if txt file cant be found saved = false
            saved = get_saved_progress()
            if (saved == False):
                print("No saved game found a new game will be started.")
                play_game(story_data, zero)
            else:
                print("Loading saved game")
                # load row on csv depending on the int value in saved so if saved = 2 zero = 2 witch means current = 2
                play_game(story_data, saved)
        # quit if input is 3
        elif (choice == "3"):
            break
main()
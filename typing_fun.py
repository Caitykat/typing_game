#Welcome to my game! Thanks for taking
#A look at the code. 
#Made by Caitlyn Trail
#Github: Caitykat
#Repository: Typing_game
#Finished: 05/12/2026 (May 12th)
#Enjoy!

#Imports
import pgzrun, random as r

#Global variables
WIDTH = 800
HEIGHT = 200
score = 0
lives = 5
difficulty = "None"
#Feel free to edit this list! (list_of_words)
#This is all the words that the game could spawn
#If you have specific words you want to practice
#Spelling with, make your own list and play!
list_of_words = ["anthropomorphize",  
                "simplification",
                "questionnaire",
                "mathematizing",
                "representatives",
                "satisfactorily",
                "hubristically",
                "incandescence",
                "cardiopulmonary",
                "insurmountable",
                "huckleberries",
                "confederation",
                "personification",
                "accreditation",
                "contingencies",
                "suffrutescent",
                "constitutional",
                "justification",
                "insectivorous",
                "autocephalous",
                "qualifications",
                "baccalaureate",
                "encouragement",
                "exceptionally",
                "accomplishment",
                "parenthetical",
                "mathematician",
                "uncomfortable",
                "absorbefacient",
                "automatically",
                "infinitesimal",
                "unforeseeable",
                "extemporaneous",
                "inconsiderate",
                "antihistamine",
                "parliamentary",
                "affectionately",
                "inexpressible",
                "ichthyosaurus",
                "knowledgeable",
                "unconscionable",
                "zoopraxiscope",
                "establishment",
                "perfectionism",
                "septuagenarian",
                "incarceration",
                "quadrilateral",
                "comparatively",
                "correspondence",
                "consciousness",
                "thermodynamic",
                "approximately",
                "circumnavigate",
                "indescribable",
                "entertainment",
                "concatenation",
                "reconciliation",
                "indefatigable",
                "animadversion",
                "gravitational",
                "transportation",
                "circumference",
                "uncooperative",
                "hieroglyphics",
                "ichthyophagist",
                "preternatural",
                "impulsiveness",
                "ventriloquist",
                "sanctification",
                "paraphernalia",
                "assassination",
                "mediterranean",
                "superintendent",
                "daguerreotype",
                "scintillation",
                "circumstances",
                "responsibility",
                "horripilation",
                "pusillanimous",
                "accoutrements",
                "manageability",
                "administrator",
                "recrimination",
                "amelioration",
                "efflorescence",
                "dischargeable",
                "international",
                "inefficiency",
                "perspicacious",
                "contradictory",
                "procrastinate",
                "suspiciously",
                "multitudinous",
                "configuration",
                "comprehensive",
                "imponderable",
                "inexperienced",
                "petrochemical",
                "transference",
                "coincidental"]
x_pos = 20
y_pos = 20
number_words = []
#Easter egg: procompsagnathus is my fav dino
text_choice = "procompsagnathus"
y_pos_list = []
x_pos_list = []
number = 0
typed_text = ""
screen_choice = "Start"
error = "None"
max_words = 0
spawn_timer = 0
high_score = 0

#This function makes sure the words dont spawn 
#Too close together (so you can actually read them)
def get_valid_y():
    while True:
        new_y = r.randint(20, 130)
        if all(abs(new_y - y) > 10 for y in y_pos_list):
            return new_y
        
#All the key bindings!! Calculates what to do based on
#what you press
def on_key_down(key):
    global typed_text, number_words, y_pos_list
    global screen_choice, error, difficulty, score, x_pos_list

    #If you are at the end game and you press back
    #takes you to the start screen + resets score
    if screen_choice == "Death" and key == keys.BACKSPACE:
        score = 0
        number_words.clear()
        x_pos_list.clear()
        y_pos_list.clear()
        screen_choice = "Start"

    #If you are at the end of the game and you press return
    #Restarts the game immideately with same difficulty
    if screen_choice == "Death" and key == keys.RETURN:
        score = 0
        number_words.clear()
        x_pos_list.clear()
        y_pos_list.clear()
        typed_text = ""
        screen_choice = "Play"
    
    #If you try to start the game but you havent
    #Selected a difficulty it will error 
    if key == keys.RETURN and difficulty != "None":
        screen_choice = "Play"
        typed_text = ""
    if key == keys.RETURN and difficulty == "None":
        error = "Select" 

    #If you press E it makes it easy
    if screen_choice == "Start" and key == keys.E:
        difficulty = "Easy"
        error = "None"

    #If you press M it makes it medium difficulty
    if screen_choice == "Start" and key == keys.M:
        difficulty = "Medium"
        error = "None"
    
    #If you press H it makes it hard
    if screen_choice == "Start" and key == keys.H:
        difficulty = "Hard"
        error = "None"

    #Backspace for typing
    if key == keys.BACKSPACE:
        typed_text = typed_text[:-1]
    
    #Actual typing 
    else:
        if key.name is not None and len(key.name) == 1:
            typed_text += key.name.lower()

#Update runs every second, updates the game 
def update():
    global x_pos, y_pos, number_words, text_choice 
    global y_pos_list, typed_text, score, screen_choice
    global max_words, difficulty, spawn_timer, high_score

    #Timer, makes it to where not all words spawn at once
    spawn_timer += 1

    #Chooses a random word in list
    choice = r.randint(0,len(list_of_words) - 1)

    #Saves the choice
    text_choice = list_of_words[choice]

    #Updates high score if score is the same or greater
    if high_score <= score:
        high_score = score

    #Calculates number of words to spawn based on difficulty
    if difficulty == "Easy":
        max_words = 1
    if difficulty == "Medium":
        max_words = 3
    if difficulty == "Hard":
        max_words = 5
    
    #Delays word spawn and spawns them until max is reached (spawns words)
    if spawn_timer >= 120 and len(number_words) < max_words:
        number_words.append(text_choice)
        x_pos_list.append(0)
        new_y = get_valid_y()
        y_pos_list.append(new_y)
        spawn_timer = 0
    
    #Calculates if a word on screen and your typing is same,
    #If so gets rid of word and gives you a point
    if typed_text in number_words:
            index = number_words.index(typed_text)
            number_words.pop(index)
            y_pos_list.pop(index)
            x_pos_list.pop(index)
            typed_text = ""
            score += 1
    
    #Calculates moving words and if they hit the other side
    #goes to death screen
    if screen_choice == "Play":
        for i, word in enumerate(number_words):
                if x_pos_list[i] < 680:
                    x_pos_list[i] += 1
                if x_pos_list[i] >= 680:
                    x_pos_list[i] = 0
                    screen_choice = "Death"


#Draw, actually draws everything as text in the game.
def draw():
    global x_pos, y_pos, text_choice, number_words
    global number, x_pos_list,score, screen_choice
    global difficulty, error, score, high_score

    #resets the screen
    screen.clear()

    #If its the start screen it draws start
    if screen_choice == "Start":

        #Text for the start screen
        screen.draw.text("Press enter to start", 
                         (WIDTH/2 - 120, HEIGHT/2 - 40), color = "white")
        screen.draw.text(f"Current difficulty is:" + difficulty ,
                         (WIDTH/2 - 120, HEIGHT/2 - 20), color = "white")
        screen.draw.text("Press E to change difficulty to easy", 
                         (WIDTH/2 -120, HEIGHT/2), color = "white")
        screen.draw.text("Press M to change difficulty to medium",
                          (WIDTH/2 -120, HEIGHT/2 + 20), color = "white")
        screen.draw.text("Press H to change difficulty to hard", 
                         (WIDTH/2 - 120, HEIGHT /2 + 40))
        
        #Only appers if you dont have a difficulty
        if error == "Select":
            screen.draw.text("ERROR: No game difficulty selected", 
                             (WIDTH/2 - 120, HEIGHT/2 +60) , color ="red")
            
        #Draws over the error to get rid of it once gone
        if error != "Select":
            screen.draw.text("ERROR: No game difficulty selected", 
                             (WIDTH/2 - 120, HEIGHT/2 +60) , color ="black")
            
    #Draws the play screen
    if screen_choice == "Play":

        #Goes through each word on the screen and draws them
        for i, word in enumerate(number_words):
            screen.draw.text(word, (x_pos_list[i], y_pos_list[i]))

        #Draws your text
        screen.draw.text(typed_text, (20, 170), color="white")

        #Scores
        screen.draw.text(f"High score :"+ str(high_score), (650, 150), color = "white")
        screen.draw.text(f"Score :"+ str(score), (650, 170), color = "white")

    #Draws the death screen
    if screen_choice == "Death":
        screen.draw.text("Game Over", (WIDTH/2 -80, HEIGHT/2 -40), color = "white")

        #F strings to display your score and high score
        screen.draw.text(f"Score :"+ str(score), (WIDTH/2 -80, (HEIGHT/2 -20)), color = "white")
        screen.draw.text(f"High score :"+ str(high_score), (WIDTH/2 -80, (HEIGHT/2)), color = "white")

        screen.draw.text("Press enter to restart the game", (WIDTH/2 - 80, HEIGHT/2 +20), color = "white")
        screen.draw.text("Press backspace to return to the start screen", (WIDTH/2 - 80, HEIGHT/2 +40), color = "white")

        
#Runs the game! Have fun!
pgzrun.go()
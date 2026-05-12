import pgzrun, random as r

#Global variables
WIDTH = 800
HEIGHT = 200
score = 0
lives = 5
difficulty = "None"
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
speed_of_words = 1
x_pos = 20
y_pos = 20
number_words = []
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


def get_valid_y():
    while True:
        new_y = r.randint(20, 130)
        if all(abs(new_y - y) > 10 for y in y_pos_list):
            return new_y
        
def on_key_down(key):
    global typed_text, number_words, y_pos_list, screen_choice, error, difficulty, score, x_pos_list

    if screen_choice == "Death" and key == keys.BACKSPACE:
        score = 0
        screen_choice = "Start"
    if screen_choice == "Death" and key == keys.RETURN:
        score = 0
        number_words.clear()
        x_pos_list.clear()
        y_pos_list.clear()
        typed_text = ""
        screen_choice = "Play"
    if key == keys.RETURN and difficulty != "None":
        screen_choice = "Play"
        typed_text = ""
    if key == keys.RETURN and difficulty == "None":
        error = "Select" 
    if key == keys.BACKSPACE:
        typed_text = typed_text[:-1]
    if screen_choice == "Start" and key == keys.E:
        difficulty = "Easy"
        error = "None"

    if screen_choice == "Start" and key == keys.M:
        difficulty = "Medium"
        error = "None"
    if screen_choice == "Start" and key == keys.H:
        difficulty = "Hard"
        error = "None"
    else:
        if key.name is not None and len(key.name) == 1:
            typed_text += key.name.lower()
            
def update():
    global x_pos, y_pos, number_words, text_choice, y_pos_list, typed_text, score, screen_choice, max_words, difficulty, spawn_timer, high_score
    spawn_timer += 1
    choice = r.randint(0,99)
    text_choice = list_of_words[choice]
    if high_score <= score:
        high_score = score
    if difficulty == "Easy":
        max_words = 1
    if difficulty == "Medium":
        max_words = 3
    if difficulty == "Hard":
        max_words = 5
    if spawn_timer >= 120 and len(number_words) < max_words:
        number_words.append(text_choice)
        x_pos_list.append(0)
        new_y = get_valid_y()
        y_pos_list.append(new_y)
        spawn_timer = 0
    if typed_text in number_words:
            index = number_words.index(typed_text)
            number_words.pop(index)
            y_pos_list.pop(index)
            x_pos_list.pop(index)
            typed_text = ""
            score += 1
    if screen_choice == "Play":
        for i, word in enumerate(number_words):
                if x_pos_list[i] < 680:
                    x_pos_list[i] += speed_of_words
                if x_pos_list[i] >= 680:
                    x_pos_list[i] = 0
                    screen_choice = "Death"


def draw():
    global x_pos, y_pos, text_choice, number_words, number, x_pos_list,score, screen_choice, difficulty, error, score, high_score
    screen.clear()
    if screen_choice == "Start":
        screen.draw.text("Press enter to start", (WIDTH/2 - 120, HEIGHT/2 - 40), color = "white")
        screen.draw.text(f"Current difficulty is:" + difficulty ,(WIDTH/2 - 120, HEIGHT/2 - 20), color = "white")
        screen.draw.text("Press E to change difficulty to easy", (WIDTH/2 -120, HEIGHT/2), color = "white")
        screen.draw.text("Press M to change difficulty to medium", (WIDTH/2 -120, HEIGHT/2 + 20), color = "white")
        screen.draw.text("Press H to change difficulty to hard", (WIDTH/2 - 120, HEIGHT /2 + 40))
        if error == "Select":
            screen.draw.text("ERROR: No game difficulty selected", (WIDTH/2 - 120, HEIGHT/2 +60) , color ="red")
        if error != "Select":
            screen.draw.text("ERROR: No game difficulty selected", (WIDTH/2 - 120, HEIGHT/2 +60) , color ="black")
    if screen_choice == "Play":
        for i, word in enumerate(number_words):
            screen.draw.text(word, (x_pos_list[i], y_pos_list[i]))
        screen.draw.text(typed_text, (20, 170), color="white")
        screen.draw.text(f"High score :"+ str(high_score), (650, 150), color = "white")
        screen.draw.text(f"Score :"+ str(score), (650, 170), color = "white")
    if screen_choice == "Death":
        screen.draw.text("Game Over", (WIDTH/2 -80, HEIGHT/2 -40), color = "white")
        screen.draw.text(f"Score :"+ str(score), (WIDTH/2 -80, (HEIGHT/2 -20)), color = "white")
        screen.draw.text(f"High score :"+ str(high_score), (WIDTH/2 -80, (HEIGHT/2)), color = "white")
        screen.draw.text("Press enter to restart the game", (WIDTH/2 - 80, HEIGHT/2 +20), color = "white")
        screen.draw.text("Press backspace to return to the start screen", (WIDTH/2 - 80, HEIGHT/2 +40), color = "white")

        

pgzrun.go()
import random

hardy = []
quirky = []
calm = [] 
lonely = []
brave = []
quiet = []
impish = []
docile = []
rash = []
bold = []
timid = []
jolly = []

def main():

    gender_question = input("Are you a boy or a girl? ")
    print()
    question_1 = get_questions_1()
    user_1 = input(f"{question_1}\nAnswer with a, b, c or d: ")
    print()
    question_2 = get_questions_2()
    user_2 = input(f"{question_2}\nAnswer with a, b, c or d: ")
    print()
    question_3 = get_questions_3()
    user_3 = input(f"{question_3}\nAnswer with a, b, c or d: ")
    print()
    question_4 = get_questions_1()
    user_4 = input(f"{question_4}\nAnswer with a, b, c or d: ")
    print()
    question_5 = get_questions_2()
    user_5 = input(f"{question_5}\nAnswer with a, b, c or d: ")
    print()
    question_6 = get_questions_3()
    user_6 = input(f"{question_6}\nAnswer with a, b, c or d: ")
    print()
    question_7 = get_questions_1()
    user_7 = input(f"{question_7}\nAnswer with a, b, c or d: ")
    print()
    question_8 = get_questions_2()
    user_8 = input(f"{question_8}\nAnswer with a, b, c or d: ")
    print()
    question_9 = get_questions_3()
    user_9 = input(f"{question_9}\nAnswer with a, b, c or d: ")
    print()
    question_10 = get_questions_1()
    user_10 = input(f"{question_10}\nAnswer with a, b, c or d: ")
    print()
    question_11 = get_questions_2()
    user_11 = input(f"{question_11}\nAnswer with a, b, c or d: ")
    print()
    question_12 = get_questions_3()
    user_12 = input(f"{question_12}\nAnswer with a, b, c or d: ")
    print()

    calculate_traits(user_1, hardy, quirky, calm, lonely)
    calculate_traits_1(user_4, hardy, quirky, calm, lonely)
    calculate_traits_2(user_7, hardy, quirky, calm, lonely)
    calculate_traits_3(user_10, hardy, quirky, calm, lonely)
    calculate_traits(user_2, brave, quiet, impish, docile)
    calculate_traits_1(user_5, brave, quiet, impish, docile)
    calculate_traits_2(user_8, brave, quiet, impish, docile)
    calculate_traits_3(user_11, brave, quiet, impish, docile)
    calculate_traits(user_3, rash, bold, timid, jolly)
    calculate_traits_1(user_6, rash, bold, timid, jolly)
    calculate_traits_2(user_9, rash, bold, timid, jolly)
    calculate_traits_3(user_12, rash, bold, timid, jolly)

    # print()
    # I put this here to see how much got added to each list.

    # print(f"Hardy: {hardy}, Quirky: {quirky}, Calm: {calm}, lonely: {lonely},")
    # print(f"Brave: {brave}, Quiet: {quiet}, Impish: {impish}, Docile: {docile},")
    # print(f"Rash: {rash}, Bold: {bold}, Timid: {timid}, Jolly: {jolly}")
    print()
    tot_hardy = sum(hardy)
    tot_quirky = sum(quirky)
    tot_calm = sum(calm)
    tot_lonely = sum(lonely)
    tot_brave = sum(brave)
    tot_quiet = sum(quiet)
    tot_impish = sum(impish)
    tot_docile = sum(docile)
    tot_rash = sum(rash)
    tot_bold = sum(bold)
    tot_timid = sum(timid)
    tot_jolly = sum(jolly)

    # print()
    # I put this here to see which trait got the highest number.
    # print(f"Hardy: {tot_hardy}, Quirky: {tot_quirky}, Calm: {tot_calm}, lonely: {tot_lonely},")
    # print(f"Brave: {tot_brave}, Quiet: {tot_quiet}, Impish: {tot_impish}, Docile: {tot_docile},")
    # print(f"Rash: {tot_rash}, Bold: {tot_bold}, Timid: {tot_timid}, Jolly: {tot_jolly}")
    # print()

    traits = {"hardy":tot_hardy, "quirky":tot_quirky, "calm":tot_calm, "lonely":tot_lonely, "brave":tot_brave, "quiet":tot_quiet, "impish":tot_impish, "docile":tot_docile, "rash":tot_rash, "bold":tot_bold, "timid":tot_timid, "jolly":tot_jolly}
    winner = max(traits, key=traits.get)
    
    if winner == "hardy" and gender_question.lower() == "girl":
        print("Your Pokemon is: Squirtle")
    elif winner == "hardy" and gender_question.lower() == "boy":
        print("Your Pokemon is: Turtwig")
    elif winner == "quirky" and gender_question.lower() == "girl":
        print("Your Pokemon is: Bidoof")
    elif winner == "quirky" and gender_question.lower() == "boy":
        print("Your Pokemon is: Cacnea")
    elif winner == "calm" and gender_question.lower() == "girl":
        print("Your Pokemon is: Oddish")
    elif winner == "calm" and gender_question.lower() == "boy":
        print("Your Pokemon is: seedot")
    elif winner == "lonely" and gender_question.lower() == "girl":
        print("Your Pokemon is: Sobble")
    elif winner == "lonely" and gender_question.lower() == "boy":
        print("Your Pokemon is: Mimikyu")
    elif winner == "brave" and gender_question.lower() == "girl":
        print("Your Pokemon is: Vulpix")
    elif winner == "brave" and gender_question.lower() == "boy":
        print("Your Pokemon is: Charmander")
    elif winner == "quiet" and gender_question.lower() == "girl":
        print("Your Pokemon is: Whismur")
    elif winner == "quiet" and gender_question.lower() == "boy":
        print("Your Pokemon is: Cyndaquil")
    elif winner == "impish" and gender_question.lower() == "girl":
        print("Your Pokemon is: Aipom")
    elif winner == "impish" and gender_question.lower() == "boy":
        print("Your Pokemon is: Chimchar")
    elif winner == "docile" and gender_question.lower() == "girl":
        print("Your Pokemon is: Surskit")
    elif winner == "docile" and gender_question.lower() == "boy":
        print("Your Pokemon is: Magnemite")
    elif winner == "rash" and gender_question.lower() == "girl":
        print("Your Pokemon is: Ponyta")
    elif winner == "rash" and gender_question.lower() == "boy":
        print("Your Pokemon is: Riolu")
    elif winner == "bold" and gender_question.lower() == "girl":
        print("Your Pokemon is: Chikorite")
    elif winner == "bold" and gender_question.lower() == "boy":
        print("Your Pokemon is: Totodile")
    elif winner == "timid" and gender_question.lower() == "girl":
        print("Your Pokemon is: Mareep")
    elif winner == "timid" and gender_question.lower() == "boy":
        print("Your Pokemon is: Marill")
    elif winner == "jolly" and gender_question.lower() == "girl":
        print("Your Pokemon is: Eevee")
    elif winner == "jolly" and gender_question.lower() == "boy":
        print("Your Pokemon is: Scorbunny")

    print()
    input("that is the whole test.")

def get_questions_1():
    """Return a random question from the first section
    of the questions."""

    questions_1 = ["What do you do with your spending money? \nA. Save it. \nB. Spend it, \nC. Spend half save half. \nD. I don’t make money", 
    "What is you studying style? \nA. working hard every day. \nB. If I remember to. \nC. I just cover what I need to. \nD. I can’t really do it alone", 
    "Which of these qualities is best in a friend? \nA. Honesty. \nB. Humor. \nC. Trust. \nD. Generosity.", 
    "Which season is your favorite? \nA. Fall. \nB. Spring. \nC. Summer. \nD. Winter.",
    "Which of these colors do you most associate with? \nA. Red. \nB. Green. \nC. Blue. \nD. Black.",
    "Your idea of good weather is? \nA. Fair day, maybe partly cloudy, warm temperature, at night its quiet. \nB. Sun is out day is hot at night the moon is full and the stars are bright and twinkling. \nC. Bitter cold day, maybe snowy. At night you notice nothing but the starts twinkling. \nD. Cool day, a little sunlight, mostly cloudy, at night no stars moonless and drizzy.",
    "Is your tone of voice usually… \nA. mellow. \nB. High pitched. \nC. Gentle. \nD. Gruff."]

    # Randomly choose the question for the user.
    question = random.choice(questions_1)
    return question

def get_questions_2():
    """Return a random question from the second section
    of the questions."""

    questions_2 = ["Someone is hassling a stranger in a busy street what will you do? \nA. Help without hesitation. \nB. Do nothing out of fear. \nC. Hassle them back. \nD. Call the police.",
    "Do you think its important to be fashionably late? \nA. no. \nB. I don’t go to parties. \nC. yes. \nD. I Don't know.", 
    "Everyone is laughing at something you think is pretty boring what do you do? \nA. Nothing. \nB. It depends on the situation. \nC. Change the subject. \nD. Laugh along.",
    "Your phone is ringing what do you do? \nA. Answer right away. \nB. Wait a bit before answering. \nC. Make someone else answer it. \nD. Ignore it and let it ring.",
    "You would most enjoy spending a vacation… \nA. Diving deep into a cave. \nB. Camping in a deep quiet forest. \nC. Site seeing on a wildlife reserve. \nD. Climbing mountains.",
    "Which of these do you wish for the most? \nA. Power. \nB. World peace. \nC. Money. \nD. Love.",
    "Your told to wait in a big empty room what do you do? \nA. Search for something to do. \nB. Cradle my knees and sit in the corner. \nC. Wonder outside. \nD. Wait quietly."] 

    # Randomly choose the questions for the user.
    question = random.choice(questions_2)
    return question

def get_questions_3():
    """Retrun a random question from the third section
    of the questions."""

    questions_3 = ["THERE IS SOMEONE BEHIND YOU! Did you look? \nA. Okay I admit it you tricked me. \nB. No way I didn't fall for it. \nC. Don’t do that is sacred me. \nD. Huh what.",
    "You want to confess your feeling to someone what do you do? \nA. Play a prank. \nB. State it clearly for all to hear. \nC. Keep it to myself. \nD. Play together.",
    "You’ve been handed a large bag for a souvenir what do you do? \nA. Open it. \nB. Point out it is smaller then everyone else’s. \nC. Wait until I get home to open it. \nD. Shake it.",
    "Do you think you have good study habits? \nA. Yes. \nB. No. \nC. Sometimes. \nD. Well I never lose at sports.",
    "How are your mornings? \nA. Always in a rush. \nB. Always perfect. \nC. They are okay. \nD. Full of fun.",
    "When angry what do you most often do? \nA. Fight with whomever or whatever made you angry. \nB. Talk it out with the person who made you angry. \nC. Ignore the situation until things have simmered down. \nD. Apologize and be friends again.",
    "Everyone is sharing a desert there is one extra piece what do you do? \nA. let everyone know. \nB. Don’t tell anyone. \nC. Didn’t even notice it. \nD. First come first serve."]

    # Randomly choose the question for the user
    question = random.choice(questions_3)
    return question

def calculate_traits(user, trait_1, trait_2, trait_3, trait_4):
    """This will calculate the answers the user picked and add them into 
    catagories to figure out which pokemon they are."""

    if user.lower() == "a":
        trait_1.append(4)
    elif user.lower() == "b":
        trait_2.append(4)
    elif user.lower() == "c":
        trait_3.append(4)
    elif user.lower() == "d":
        trait_4.append(4)

    return trait_1, trait_2, trait_3, trait_4

def calculate_traits_1(user, trait_1, trait_2, trait_3, trait_4):
    """This will calculate the answers the user picked and add them into 
    catagories to figure out which pokemon they are."""

    if user.lower() == "a":
        trait_1.append(3)
    elif user.lower() == "b":
        trait_2.append(3)
    elif user.lower() == "c":
        trait_3.append(3)
    elif user.lower() == "d":
        trait_4.append(3)

    return trait_1, trait_2, trait_3, trait_4

def calculate_traits_2(user, trait_1, trait_2, trait_3, trait_4):
    """This will calculate the answers the user picked and add them into 
    catagories to figure out which pokemon they are."""

    if user.lower() == "a":
        trait_1.append(2)
    elif user.lower() == "b":
        trait_2.append(2)
    elif user.lower() == "c":
        trait_3.append(2)
    elif user.lower() == "d":
        trait_4.append(2)

    return trait_1, trait_2, trait_3, trait_4 

def calculate_traits_3(user, trait_1, trait_2, trait_3, trait_4):
    """This will calculate the answers the user picked and add them into 
    catagories to figure out which pokemon they are."""

    if user.lower() == "a":
        trait_1.append(1)
    elif user.lower() == "b":
        trait_2.append(1)
    elif user.lower() == "c":
        trait_3.append(1)
    elif user.lower() == "d":
        trait_4.append(1)

    return trait_1, trait_2, trait_3, trait_4   



# Call main to start this program.
if __name__ == "__main__":
    main()    
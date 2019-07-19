import random
bank_simple = {"asd": ["as", "sas", "das", "saad", "ssaa"],
               "kip": ["ki", "kkip", "ip", "ik", "kkpik", "ikik"],
               "qol": ["qo", "qqq", "oqqo", "qllqq", "llll"]}
bank_moderate = {"ghik": ["gi", "ki", "kik", "hih", "ghi", "gki", "ghiki", "ggii", "kikiki"],
                 "wxaz": ["wa", "waw", "xax", "zaz", "wawaz", "wazaw", "wzzzaa", "aaww", "zzz"],
                 "triu": ["tri", "rii", "tuii", "rrtii", "trt", "irtr"]}
bank_hard = {"oplyt": ["op", "lyt", "lll", "ytyt", "lyly", "opttt", "lytttt", "lypllll", "pplyttt", "ololtpt", "plyplyt", "plooo"],
             "jfcvx": ["jfj", "fxj", "cvjf", "cvxxxj", "xjfxvvv", "cxvcxv", "fcjx", "jjjxxx", "cvvjffxx", "fxfx", "cfvfcfc", "vvvv"],
             "dsnim": ["dsn", "dss", "nimd","min", "das", "nimmm","nimdsd", "msiiind", "siidnm", "minmind", "nnn", "mnisnd", "dnd"]}


def input_evaluation(input_):
    try:
        if len(input_) > 1:
            return False
        elif 49 <= ord(str(input_)) <= 51:
            return True
    except (ValueError, TypeError, NameError):
            return False
flag_1 = True
while flag_1:
    user_input = input("Enter NUMBER of game level ? (1:simple), (2:moderate), (3:hard): ")
    if input_evaluation(user_input):
        input_level = int(user_input)
        flag_1 = False
    else:
        print("please enter one number between 1 to 3: ")


def target_word(number):  # specify char and words depend on game level
    if number == 1:
        target_key = random.sample(bank_simple.keys(), 1)
        targetwords = bank_simple.get(target_key[0])
        targetchar = set("".join(bank_simple.get(target_key[0])))
    elif number == 2:
        target_key = random.sample(bank_moderate.keys(), 1)
        targetwords = bank_moderate.get(target_key[0])
        targetchar = set("".join(bank_moderate.get(target_key[0])))
    elif number == 3:
        target_key = random.sample(bank_hard.keys(), 1)
        targetwords = bank_hard.get(target_key[0])
        targetchar = set("".join(bank_hard.get(target_key[0])))
    else:
        print("please enter a number between 1 to 4")
    return targetwords, targetchar

target_wordss = target_word(input_level)[0]
target_chars = target_word(input_level)[1]


def lenght_words(lst): # to explain number of words based on number of characters
    mylist = []
    for i in lst:
        mylist.append(len(i))
    rep_char = [mylist.count(i) for i in range(2, 7)]
    for i, j in enumerate(rep_char):
        if j:
            print(j, " Word with ", i+2, " characters ")
    return "*************************"


def word_evaluation(word, lst): # to check whether char is in list or not
    if word in lst:
        return True
    else:
        return False

print("Here are your characters: ", target_chars)
print("you should guess: ")
print(lenght_words(target_wordss))
print("You have unlimited chance to guess the words, Let's get started...!")
temp_target_words = target_wordss
guess_lst = []   # to check duplicate answers
while len(temp_target_words) > 0:  # main check
    user_word = str(input("guess a word:"))
    if word_evaluation(user_word, temp_target_words) and user_word not in guess_lst:
        guess_lst.append(user_word)
        print("True")
        temp_target_words.remove(user_word)
        if len(temp_target_words) == 0:
            print("You win!")
        else:
            print("these are left: ")
            print(lenght_words(temp_target_words))
    elif user_word in guess_lst:
        print("You have said it before!")
    elif not word_evaluation(user_word, target_wordss) and user_word not in guess_lst:
        print("NOT True")

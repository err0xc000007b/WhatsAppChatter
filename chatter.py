# chatter.py
# Instructions:
# 1. Remember to add path-to-chromedriver.exe in line 16
# 2. Remember to pip install -r requirements.txt
# 3. Remember to read the README file!
# ~ err0xc000007b, with ❤️

import os, time, datetime, random
import threading
import keyboard
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

os.system('cls')
print(f"[!] Machine started at {datetime.datetime.now()}")

driver = webdriver.Chrome("<PATH TO CHROMEDRIVER.EXE>")
driver.get("https://web.whatsapp.com/")

keyboard.wait('esc')
print("#Clearing Screen")                             
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[3]").click()
time.sleep(.5);driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[3]/span/div/ul/li[4]/div").click()
time.sleep(.5);driver.find_element_by_xpath("/html/body/div[1]/div/span[2]/div/div/div/div/div/div/div[2]/div[2]").click()
keyboard.wait('esc')
print("#fetching...")

RecentlySent = ""
        
def send(message):
    print(f">{message}")
    global RecentlySent
    RecentlySent = message
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]").send_keys(message+Keys.ENTER) 


#Analyzing catalysts#############################################################################
greetings = ['hi', 'hello', 'hey']
positiveAdverbs = ['good', 'great', 'fantastic', 'cool', 'nice', 'awesome']
verbs = ["play", "run", "exercis", "cook", "watch", "read"]
#################################################################################################

#Replies Based on feelings#######################################################################
Bad = ["I am sorry to hear that", "Sorry to hear", "My condolences", "Too bad", "thats not good"]
Good = ["That's amazing", "That's great", "That's fantastic", "That's cool", "That's nice", "That's awesome"]
Sympathy = ["I understand", "I feel you", "Its ok", "dont stree on it"]
Agreeing = ["I agree", "ok", "alright", "good with me", "sure"]
Disagreeing = ["no", "I am sorry but no", "Dont count on it", "nope", "no can do", "I am afraid not"]
Apology = ["I am sorry", "please forgive me for that", "my apologies", "I am really sorry for that"]
AboutMe = ["nothing much", "just relaxing", "just laying around", "I was staring at the wall", "I was playing dead"]
HowAmI = ["I am all good, you?", "all good", "alive and kickin'", "I am doing great"]
HowAreOthers = ["They're great", "They're fine", "They're doing great", "They're good"]
NotFound = ["right", "ok", "I see"]
Endings = ["Bye", "Goodbye"]
Emotes = [":)", ":3", ":-)", ":>"] 
##################################################################################################


def analyze(data):
    feeling = ""

    for guess in greetings:
        if guess in data:
            feeling = greetings  
    
    for adv in positiveAdverbs:
        if adv in data:
            feeling = Emotes
    
    if 'bye' in data or 'gtg' in data or 'see you later' in data or 'catch you later' in data:
        feeling = Endings

    if "what" in data:
        if "doing" in data:
            feeling = AboutMe
        
    if "how" in data:
        if "are" in data and "you" in data:
            feeling = HowAmI
        if "your" in data:
            if "mum" in data or "mom" in data or "mother" in data or "ma" in data or "parents" in data or "grand" in data or "dad" in data or "father" in data or "brother" in data or "uncle" in data or "mousi" in data or "aunt" in data:
                feeling = HowAreOthers
        
    if "i" in data:
        if 'hurt' in data or 'fell' in data or 'crashed' in data or 'burn' in data or 'broke' in data or 'cut' in data or "bad" in data or 'not well' in data:
            feeling = Bad

        if 'feel' in data:
            if 'down' in data or 'ill' in data:
                feeling = Bad
            for adverb in positiveAdverbs:
                if adverb in data:
                    feeling = Good

        for adverb in positiveAdverbs:
            if adverb in data:
                if "am" in data:
                    feeling = Good
                if "had" in data:
                    feeling = Good
                    
        if "was" in data or 'am' in data:
            for verb in verbs:
                if verb+'ing' in data:
                    if 'and' in data and 'hurt' in data or 'fell' in data or "didn't like" in data or 'hate' in data or 'crashed' in data or 'burn' in data:
                        feeling = Bad
                    else:
                        feeling = Good
                        
        for verb in verbs:
            if verb+'ed' in data or 'read' in data:
                feeling = Good
    
    if not feeling:
        feeling = NotFound 
    send(feeling[random.randint(0, len(feeling)-1)])

def fetch():
    index = 4
    while(True):
        try:    
            data = driver.find_element_by_xpath(f"/html/body/div[1]/div/div/div[4]/div/div[3]/div/div/div[2]/div[{index}]/div/div/div/div[1]/div/span[1]/span").text
            if data == RecentlySent:
                index += 1 
                continue
            print("//"+data, f"[{index}]")
            analyze(data.lower())
            index += 1
        except:
            continue
                    

fetch()


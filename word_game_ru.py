from bs4 import BeautifulSoup
import requests
from googletrans import Translator

def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        translator = Translator()

        english_words=soup.find("div",id="random_word").text.strip()
        english_words=translator.translate(english_words,dest="ru").text
        word_definition=soup.find("div",id="random_word_definition").text.strip()
        word_definition = translator.translate(word_definition, dest="ru").text
        return{
            "english_words":english_words,
            "word_definition":word_definition

        }

    except:
        print("Failed to connect to the website")
        return
def word_game():
    print("Welcome to the game")
    while True:
        word_dict=get_english_words()
        word=word_dict.get("english_words")
        word_definition=word_dict.get("word_definition")
        print(f"Значение слова-{word_definition}")
        user=input("Что это за слово?")
        if user==word:
            print("Вы угадали!")
        else:
            print(f"Неверно! Правильное слово - {word}")
        play_again=input("Хотите сыграть еще раз? y/n")
        if play_again!='y':
            print("Спасибо за игру!")
            break
word_game()







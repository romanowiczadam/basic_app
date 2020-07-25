import json
import difflib
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(w):
    global w_1
    w = w.lower()
    if w in data:
        w_1 = w
        return data[w]
    elif w.capitalize()in data: #nazwy wlasne
        w_1 = w.capitalize()
        return data[w.capitalize()]
    elif w.upper() in data: # wszystkie z duzej np:USA
        w_1 = w.upper()
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        print('Ups! Chyba cos zle wpisales...')
        possib = get_close_matches(w, data.keys())
        y_n = input(f'Czy chodzilo Ci moze o slowo "{possib[0]}"\n'
                    f'jesli tak wcisnij klawisz: "Y", jesli nie: "N"  (Y/N): ')
        if y_n == 'y' or y_n =='Y':
            w_1 = get_close_matches(w, data.keys())[0]
            return data[get_close_matches(w, data.keys())[0]]
        elif y_n == 'n' or y_n =='N':
            return print('Sprobuj wpisac szukane slowo jeszcze raz.')
        else:
            return 'Wcisnij klawisz: Y/N'
    else:
        print('Przykro mi, ale nie umiem znalesc takiego slowa\n')


while True:
    word = input('Proszę wpisać szukane słowo: ')
    output = translate(word)
    # stała wykorzystana w pętli do podania numeru definicji
    l = 0

    if type(output) == list:
        print(f'\n{w_1}:')
        for i in output:
            l += 1
            print(f'def {l}. {i}\n')
    else:
        print(output)



from tkinter import Tk, Entry, Button, Label, StringVar

window = Tk()
window.geometry('400x400')
window.title('Language translator')

entry_text = Entry(window)
entry_text.pack()

result = StringVar()
result_label = Label(window, textvariable=result)
result_label.pack()

french_dictionary = {'good':'bon',
                     'hour':'heure',
                     'thank you':'merci',
                     'yes':'oui',
                     'no':'non',
                     'meet':'rencontrer',
                     'shout':'crier',
                     'kill':'tuer',
                     'split':'diviser',
                     'scatter':'dispersion',
                     'happy':'heureuse',
                     'sad':'triste',
                     'confused':'confus',
                     'cut':'couper',
                    'slice':'tranche',
                    'serious':'sérieuse',
                    'inspect':'inspecter',
                    'pour':'verser',
                    'speak':'parler',
                    'lie':'mensonge'}

def search(word):
    if word in french_dictionary:
        result.set(french_dictionary[word])
        print(french_dictionary[word])
    else:
        result.set('Not found')
        print('Not found')
      
search_btn = Button(window, text='French', command=lambda: search(entry_text.get()))
search_btn.pack(padx=10,pady=10)

gbagyi_dictionary={'god gift':'shegiza',
                  'there is god':'sheyilo',
                  'there is time':'sayilo',
                  'know':'kpeoye',
                  'see':'gyeoye',
                  'fly':'seafnu',
                  'star':'kpasi',
                  'say':'gna',
                  'rain':'ogma',
                  'you':'oho',
                  'two':'mba',
                  'man':'zangbai',
                  'skin':'pata',
                  'tongue':'ntala',
                  'liver':'aye',
                  'fire':'ona',
                  'yellow':'olo',
                  'new':'woi',
                  'name':'oye',
                  'dry':'wo',}

def search34(word):
    if word in gbagyi_dictionary:
        result.set(gbagyi_dictionary[word])
        print(gbagyi_dictinary[word])
    else:
        result.set('Not found')
        print('Not found')

button=button (window,text= 'gbagyi', command=lambda:search34(entry_text.get()))
button.pack(padx=10,pady=10)


bura_dictionary={"good morning":"wokpinya",
                    "good afternoon":"kpuchirna",
                    "thank you":"usah",
                    "come":"sira",
                    "go" : "tira",
                    "sorry" :"sama",
                    "water":"yimi",
                    "food" :"susuma",
                    "shoe" : "mbabi",
                    "cloth": "liptu",
                    "head" :"karga",
                    "welcome": "maraba",
                    "book " : "karkadu",
                    "broom" : "shimtu",
                    "mother": "mi yana",
                    "soup" : "sukwar",
                    "school" : "makaranta",
                    "dog" : "kila"}



def search2(word):
    if word in bura_dictionary:
        result.set(bura_dictionary[word])
        print(bura_dictionary[word])
    else:
        result.set('Not found')
        print('Not found')

button=Button (window,text= 'bura', command=lambda: search2(entry_text.get()))
button.pack(padx=10,pady=10)

Spanish_Dictionary = {
    'destiny' : 'destino',
    'bottle' : 'botella',
    'classroom' : 'aula',
    'food' : 'alimento',
    'love' : 'amar',
    'culture' : 'cultura',
    'beautiful' : 'hermosa/hermoso',
    'research' : 'investigacion',
    'studio' : 'estudio',
    'heartbreak' : 'desamor',
    'friend' : 'amigo',
    'house' : 'casa',
    'cat' : 'gato',
    'dog' : 'perro',
    'water' : 'agua',
    'sun' : 'sol',
    'book' : 'libro',
    'happy' : 'feliz',
    'family' : 'familia',
    'city' : 'ciudad'}

def search1(word):
    if word in Spanish_Dictionary:
        result.set(Spanish_Dictionary[word])
        print(Spanish_Dictionary[word])
    else:
        result.set('not found')
        print('not found')

search_btn = Button(window, text='spanish', command=lambda: search1(entry_text.get()))
search_btn.pack(padx=10,pady=10)

window.mainloop()

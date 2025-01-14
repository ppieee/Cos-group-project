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

window.mainloop()


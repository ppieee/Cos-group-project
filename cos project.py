from tkinter import Tk, Entry, Button, StringVar, Label

window = Tk()
window.geometry('600x250')
window.title('Language translator')

entry_text = Entry(window)
entry_text.pack()

result = StringVar()
result_label = Label(window, textvariable=result)
result_label.pack()

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
    'city' : 'ciudad'
}

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
from tkinter import *
from tkinter import colorchooser
from PIL import ImageTk, Image
from tkinter import messagebox
from difflib import get_close_matches
from tkinter.ttk import Combobox
from textblob import TextBlob
import pyttsx3
import speech_recognition as sr
import json


engine = pyttsx3.init()


rate = engine.getProperty('rate')
engine.setProperty('rate',150)

def wordAudio():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(enterWordEntry.get())
    engine.runAndWait()

def meaningAudio():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(textarea.get(1.0,END))
    engine.runAndWait()

def translate():
    try:
        textarea.delete(1.0,END)
        word = TextBlob(variable1.get())
        lan = word.detect_language()
        lan_todict = language.get()
        lan_to = lang_dict[lan_todict]
        word = word.translate(from_lang=lan, to=lan_to)
        textarea.insert(END, word)
    except:
        messagebox.showerror("Error","Please double check the word you entered")


# def speaker():
#     while True:
#         r = sr.Recognizer()
#         with sr.Microphone() as source:
#             audio = r.listen(source)
#         try:
#             text = (r.recognize_google(audio), "\n")
#             enterWordEntry.insert(END,text)
#         except:
#             pass

    # s = sr.Recognizer()
    # with sr.Microphone() as m:
    #     # s.adjust_for_ambient_noise(m, duration=0.2)
    #     audio = s.record(m)
    #     try:
    #         wordentered = s.recognize_google(audio)
    #         wordentered = wordentered.lower()
    #         enterWordEntry.insert(END,wordentered)
    #     except:
    #         print("Sorry")

def exit():
    res = messagebox.askyesno('Confirm','Do you want to exit?')
    if res == True:
        root.destroy()
    else:
        pass

def clear():
    enterWordEntry.delete(0,END)
    textarea.config(state=NORMAL)
    textarea.delete(1.0,END)
    textarea.config(state=DISABLED)

def search():
    data = json.load(open('data.json'))
    wordEntered = enterWordEntry.get()

    wordEntered = wordEntered.lower()
    textarea.config(state=NORMAL)
    textarea.delete(1.0,END)

    if wordEntered in data:
        meaning = data[wordEntered]
        for item in meaning:
            textarea.insert(END,u'\u2192 '+item+'\n\n')
        textarea.config(state=DISABLED)

    elif len(get_close_matches(wordEntered,data.keys()))>0:
        close_match = get_close_matches(wordEntered,data.keys())[0]
        result = messagebox.askyesno('Confirm','Did you mean '+close_match+' instead?')
        if result == True:
            meaning = data[close_match]
            for item in meaning:
                textarea.insert(END,u'\u2192 '+item+'\n\n')
            textarea.config(state=DISABLED)

        else:
            messagebox.showinfo('Information','Entered word does not exist.')
            enterWordEntry.delete(0, END)

    else:
        messagebox.showerror('Error','Entered word does not exist. Please double check it.')
        enterWordEntry.delete(0,END)

root = Tk()
root.geometry('1270x750+0+0')
root.title("Talking Dictionary")
root.resizable(0,0)

image = Image.open("dict.png")
resized = image.resize((1270,750),Image.ANTIALIAS)
bgImage = ImageTk.PhotoImage(resized)
bgLabel = Label(root,image=bgImage)
bgLabel.place(x=0,y=0)

#####Combo Box#########
lang_dict = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}

language = StringVar()
font_box = Combobox(root,textvariable=language,state='readonly')
font_box['values'] = [e for e in lang_dict.keys()]
font_box.current(37)
font_box.place(x=1100,y=173)
# color = colorchooser.askcolor()
enterWordLabel = Label(root,text="Enter Word",font=('Copperplate Gothic Light',30,'bold'),fg="#c9363b",bg="#ebcead",borderwidth=5,relief="raised")
enterWordLabel.place(x=470,y=80)

variable1 = StringVar()
enterWordEntry = Entry(root,textvariable=variable1,font=('Arial Rounded MT Bold',25),fg="#cc9d68",borderwidth=8,relief=GROOVE,justify=CENTER)
enterWordEntry.place(x=400,y=180)
enterWordEntry.focus_set()

# old_searchImage = Image.open("search.png")
# resized_searchImage = old_searchImage.resize((50,50),Image.ANTIALIAS)
searchImage = PhotoImage(file="search.png")
searchButton = Button(root,image=searchImage,borderwidth=0,cursor="hand2",command=search)
# searchButton.place(x=540,y=250)
searchButton.place(x=820,y=170)

# old_micImage = Image.open("mic.png")
# resized_micImage = old_micImage.resize((50,50),Image.ANTIALIAS)
micImage = PhotoImage(file="mic.png")
micButton = Button(root,image=micImage,borderwidth=0,cursor="hand2",command=wordAudio)
# micButton.place(x=640,y=253)
micButton.place(x=900,y=173)

# speakerButton = Button(root,borderwidth=7,cursor="hand2",command = speaker)
# speakerButton.place(x=1000,y=173)

translateButton = Button(root,text="Translate",borderwidth=5,cursor="hand2",font=('Arial Rounded MT Bold',15),fg="#cc9d68",command=translate)
translateButton.place(x=980,y=173)

meaningLabel = Label(root,text="Meaning",font=('Copperplate Gothic Light',30,'bold'),fg="#c9363b",bg="#ebcead",borderwidth=5,relief="raised")
meaningLabel.place(x=510,y=280)

textarea = Text(root,font=('Arial Rounded MT Bold',20),fg="#cc9d68",borderwidth=8,relief=GROOVE,height=7,width=40,wrap="word")
textarea.place(x=280,y=350)

microphoneImage = PhotoImage(file="microphone.png")
microphoneButton = Button(root,image=microphoneImage,borderwidth=0,cursor="hand2",bg='#d6ae81',command=meaningAudio)
microphoneButton.place(x=450,y=600)

clearImage = PhotoImage(file="clear.png")
clearButton = Button(root,image=clearImage,borderwidth=0,cursor="hand2",bg='#d6ae81',command=clear)
clearButton.place(x=600,y=600)

exitImage = PhotoImage(file="exit.png")
exitButton = Button(root,image=exitImage,borderwidth=0,cursor="hand2",bg='#d6ae81',command=exit)
exitButton.place(x=750,y=600)


root.mainloop()
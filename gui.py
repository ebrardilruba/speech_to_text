import threading
from tkinter import *
import whisper
from pygame import *
from tkinter import font



import tkinter as tk
from analiz import get_analysis_data  # analiz.py dosyasından fonksiyonu import edin
from analiz import compare_texts

#  def update_text():
#      data = get_analysis_data()  # analiz.py'den veriyi alın
#     listbox2.delete('1.0', tk.END)  # Önceki metni temizle
#     listbox2.insert(tk.END, data)  # Yeni metni ekle


# def update_text():
#     data = get_analysis_data()  # analiz.py'den veriyi alın
#     listbox2.delete('1.0', tk.END)  # Önceki metni temizle
#     listbox2.insert(tk.END, data)  # Yeni metni ekle

# root = tk.Tk()
# root.geometry("400x300")

# text2 = tk.Text(root, height=10, width=40)
# text2.pack()

# button = tk.Button(root, text="Analiz Verilerini Getir", command=update_text)
# button.pack()

# root.mainloop()














root = Tk()

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
height = 600
width = 700
x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//4)-(height//4)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))



window = Frame(root)
window2 = Frame(root)
window3 = Frame(root)


for frame in (window, window2,window3):
    frame.grid(row=0, column=0, sticky='nsew')


def show_frame(frame):
    frame.tkraise()


show_frame(window)


# ============== Giris Sayfasi ==============================


window.config(background='#1f0a42')

#line nin eklenmesi
image_image_line = PhotoImage(
    file="C:/Users/ebrar/OneDrive/Masaüstü/Bitirme_projesi_gui/MusicPlayer/build/images/image_line.png")
image_line = Label(
    window,
    bg='#1f0a42',
    image=image_image_line
)
image_line.place(
    x=100,
    y=310,
    width=500,
    height=80.0
    
)

# play buttonunun eklenmesi

button_image_play = PhotoImage(
    file="C:/Users/ebrar/OneDrive/Masaüstü/Bitirme_projesi_gui/MusicPlayer/build/images/button_play.png")
button_play = Button(
    window,
    image=button_image_play,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: play(),
    relief="flat",
    background='#1f0a42'
   
)
button_play.place(
    x=250,
    y=410,
    width=80.0,
    height=80.0
     
)


# convert butonunun eklenmesi bu buton whispera bağlanıyor

button_image_convert = PhotoImage(
    file="C:/Users/ebrar/OneDrive/Masaüstü/Bitirme_projesi_gui/MusicPlayer/build/images/convert.png")


button_convert = Button(
    window,
    image=button_image_convert,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: start_transcription_thread(),
    relief="flat",
    background='#1f0a42'

    
)
button_convert.place(
    x=380,
    y=410,
    width=75.0,
    height=75.0
)

# front da bulunan resim 

image_image_front = PhotoImage(
    file="C:/Users/ebrar/OneDrive/Masaüstü/Bitirme_projesi_gui/MusicPlayer/build/images/image_front.png")
image_front = Label(
    window,
    bg='#1f0a42',
    image=image_image_front
)
image_front.place(
    x=187,
    y=140
)

# text butonu ekleniyor bu buton whisper in metnini aliyor

button_image_text = PhotoImage(
    file="C:/Users/ebrar/OneDrive/Masaüstü/Bitirme_projesi_gui/MusicPlayer/build/images/button_text.png")
button_text = Button(
    window,
    image=button_image_text,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(window2),
    relief="flat",
    activebackground='#1f0a42'
)
button_text.place(
    x=130,
    y=410,
    width=80.0,
    height=80.0
)

# bu kisim herhangi ekstra bir ses eklenirse ismini de yazdirabilmek icin konuldu liste ile baglanti yapilmali
''' 
playing_voice = Label(
    window,
    text="test3",
    bg='#1f0a42',
    fg='#000000',
    font=('Times New Roman', 12, 'bold')

)
playing_voice.place(
    x=150,
    y=360,
    height=20,
    width=300
)
'''

# =============== -önemli kisim -convert-pause play- text- ============================


# ikinci pencere

window2.config(background='#1f0a42')


# back butonu

button_back = Button(
    window2,
    text="""BACK""",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(window),
    relief="flat",
    activebackground='#362a57',
    bg='#362a57',
    fg='#ffffff',
)
button_back.place(
    x=26.0,
    y=25.0,
    width=54.0,
    height=33.0
) 

#listbox text ayarlari
listbox = Text(
    window2,
    
    #bg='#000000',
    bg='#362a57',
    fg='#000000',
    font=('Times New Roman', 12, 'bold'),
    bd=25,
    relief='flat'
)
listbox.place(
    x=50,
    y=80,
    height=450,
    width=600
   
)

scroll = Scrollbar(
    window2,
   
)
scroll.place(
    x=650,
    y=80,
    height=450
    
)

listbox.config(yscrollcommand=scroll.set)
scroll.config(command=listbox.yview)

# pause buttonu ekleniyor  
button_image_pause = PhotoImage(
    file="C:/Users/ebrar/OneDrive/Masaüstü/Bitirme_projesi_gui/MusicPlayer/build/images/button_pause.png")

#play ve pause tuşu 
def play():
   
    mixer.music.load("C:/Users/ebrar/OneDrive/Masaüstü/Bitirme_projesi_gui/MusicPlayer/build/songs/filtreli_test3_cpu.mp3")
    mixer.music.play()

    button_pause = Button(
        window,
        image=button_image_pause,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: pause_song(),
        relief="flat",
        activebackground='#1f0a42'
    )
    button_pause.place(
        x=250,
        y=410,
        width=80.0,
        height=80.0
    )


resume_pic = PhotoImage(
    file="C:/Users/ebrar/OneDrive/Masaüstü/Bitirme_projesi_gui/MusicPlayer/build/images/button_play.png")

# sesi duraklatma
def pause_song():
    mixer.music.pause()

    resume_button = Button(
        window,
        image=resume_pic,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: resume_song(),
        relief="flat",
        activebackground='#b2bdeb'
    )
    resume_button.place(
      
        x=250,
        y=410,
        width=80,
        height=80
    )
# devam ettirme

def resume_song():
    mixer.music.unpause()
    button_pause2 = Button(
        window,
        image=button_image_pause,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: pause_song(),
        relief="flat",
        activebackground='#1f0a42'
    )
    button_pause2.place(
        x=250,
        y=410,
        width=80,
        height=80
    )



## analiz butonu ve içeriği 

# Load the image for the 'Analyze' button
button_image_analyze = PhotoImage(file="C:/Users/ebrar/OneDrive/Masaüstü/Bitirme_projesi_gui/MusicPlayer/build/images/analizd1.png")

# Define the function to be called when the 'Analyze' button is clicked
def analyze():
    try:
        print("Analysis started...")  # Placeholder for analysis functionality
        show_frame(window3)  # Assuming window3 is set up to display analysis results
    except:
        print("an error occured")
    # This function will show the analysis results window (window3)
    # You can add more complex analysis logic here later
   
    

# Call the function and print the results
    data = compare_texts()
    
    listbox2.insert(END,data)

monospace_font = font.Font(family='Courier', size=10)
# Create the 'Analyze' button and place it on the main window
button_analyze = Button(
    window,
    image=button_image_analyze,
    borderwidth=0,
    highlightthickness=0,
    command=analyze,  # Set the command to the analyze function
    relief="flat",
    activebackground='#1f0a42',
    font= monospace_font
)
button_analyze.place(
    x=500, 
    y=410, 
    width=80, 
    height=80)


window3.config(background='#1f0a42')


# back2 butonu

button_back2 = Button(
    window3,
    text="""BACK""",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(window),
    relief="flat",
    activebackground='#362a57',
    bg='#362a57',
    fg='#ffffff',
)
button_back2.place(
    x=26.0,
    y=25.0,
    width=54.0,
    height=33.0
) 

listbox2 = Text(
    window3,
    
    #bg='#000000',
    bg='#362a57',
    fg='#000000',
    font=('Times New Roman', 12, 'bold'),
    bd=25,
    relief='flat'
)
listbox2.place(
    x=50,
    y=80,
    height=450,
    width=600
   
)

scroll2 = Scrollbar(
    window3,
   
)
scroll2.place(
    x=650,
    y=80,
    height=450
    
)

listbox2.config(yscrollcommand=scroll2.set)
scroll2.config(command=listbox2.yview)


# sesi whisper ile dinleyip yazdirma
def write():
    # pygame.init();
    model = whisper.load_model("tiny")
    #"C:\Users\ebrar\OneDrive\Masaüstü\Bitirme_projesi_gui\MusicPlayer\build\songs\filtreli_test3_cpu.wav"
    result = model.transcribe("C:/Users/ebrar/OneDrive/Masaüstü/Bitirme_projesi_gui/MusicPlayer/build/songs/filtreli_test3_cpu.mp3")
    
    listbox.insert(END,result["text"])

def transcribe_audio(model, file_path):
    # Dosyayı işle ve sonucu al
    result = model.transcribe(file_path)
    text = result['text']
    
    # Ana iş parçacığındaki GUI bileşenine erişmek için
    # güvenli bir yol kullan
    listbox.insert(END, text)

def start_transcription_thread():
    # Modeli yükle
    model = whisper.load_model("tiny")
    file_path = "C:/Users/ebrar/OneDrive/Masaüstü/Bitirme_projesi_gui/MusicPlayer/build/songs/filtreli_test3_cpu.mp3"
    # Yeni bir thread başlat ve transcribe_audio fonksiyonunu kullan
    thread = threading.Thread(target=transcribe_audio, args=(model, file_path))
    thread.start()

#####

#  def update_text():
#      data = get_analysis_data()  # analiz.py'den veriyi alın
#     listbox2.delete('1.0', tk.END)  # Önceki metni temizle
#     listbox2.insert(tk.END, data)  # Yeni metni ekle


#####


mixer.init()
songs_state = StringVar()

root.resizable(False, False)
root.mainloop()

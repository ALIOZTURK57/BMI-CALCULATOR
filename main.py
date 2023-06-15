#basic BMI calculator

from tkinter import *


window=Tk()
window.title=("BMI CALCULATOR")
window.minsize(width=250,height=250)
window.config(padx=15,pady=15)

my_label=Label(text="BMI CALC.",font=("Arial",7,"bold"))
my_label.config(bg="grey")
my_label.config(fg="white")
my_label.config(padx=15,pady=15)
my_label.pack()


boy_label=Label(text="Boyunuz",font=('Arial',7,"bold"))
boy_label.pack()
boy=Entry(width=14)

boy.pack()
kilo_label=Label(text="Kilonuz",font=('Arial',7,"bold"))
kilo_label.pack()
kilo=Entry(width=14)
kilo.pack()
sonuç=Label()
sonuç.pack()

def butonaBasıldı():

    boyunuz=boy.get()
    kilonuz=kilo.get()

    if boyunuz==""or kilonuz=="":
        sonuç.config(text="İkisini de giriniz")
    else:

        bmı= float(kilonuz)/(float(boyunuz)/100)**2

        if bmı<18.5:
            sonuç.config(text="bmı'nız {}" "\n" "düşük kilolusunuz".format(bmı))
        elif 18.5<bmı<24.9:
            sonuç.config(text="bmı'nız {}" "\n" "Normal kilolusunuz".format(bmı))
        elif 25<bmı<29.9:
            sonuç.config(text="bmı'nız {}" "\n" "Fazla kilolusunuz".format(bmı))
        elif 30<bmı<39.9:
            sonuç.config(text="bmı'nız {}" "\n" "Obezsiniz".format(bmı))
        else:
            sonuç.config(text="bmı'nız {}" "\n" "Süper obezsiniz".format(bmı))

    return bmı


my_button=Button(text="hesapla",command=butonaBasıldı)
my_button.pack()



window.mainloop()
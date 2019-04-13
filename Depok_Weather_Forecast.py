from bs4 import BeautifulSoup
import requests
from tkinter import *

class Weather:

    def __init__(self,master):
        self.master = master

        #Memanggil website cuaca depok
        page = requests.get('https://weather.com/id-ID/cuaca/5hari/l/IDJB8864:1:ID')

        #Dijadikan variable soup
        soup = BeautifulSoup(page.content, 'html.parser')
        
        #Mengubah div dengan id tersebut menjadi sebuah variable
        five_day = soup.find(id="twc-scrollabe")

        #Mendapatkan list 5 hari ke depan
        hari = five_day("span",{"class":"date-time"})

        self.list_hari = []
        for i in range (5):
            if hari[i].get_text() == "Matahari":
                self.list_hari.append('Min')
            else:
                self.list_hari.append(hari[i].get_text())

        #Mendapatkan tanggal 5 hari ke depan
        tanggal = five_day("span",{"class":"day-detail clearfix"})

        self.list_tanggal = []
        for i in range (5):
            self.list_tanggal.append(tanggal[i].get_text())

        #Mendapatkan Cuaca untuk 5 hari ke depan
        cuaca = five_day("td",{"class":"description"})

        self.list_cuaca = []
        for i in range (5):
            self.list_cuaca.append(cuaca[i].get_text())

        #Mendapatkan Suhu maksimum dan minimum untuk 5 hari ke depan
        suhu = five_day("td",{"class":"temp"})

        self.list_suhu = []
        for i in range (5):
            if suhu[i].get_text().count('°') == 2:
                self.list_suhu.append(suhu[i].get_text()[:3]+'/'+suhu[i].get_text()[-3:])
            else:
                self.list_suhu.append(suhu[i].get_text()[:2]+'/'+suhu[i].get_text()[-3:])
        
        #Mendapatkan curah hujan untuk 5 hari ke depan
        curah_hujan = five_day("td",{"class":"precip"})

        self.list_curah_hujan = []
        for i in range (5):
            self.list_curah_hujan.append(curah_hujan[i].get_text())
        
        #Mendapatkan arah dan kecepatan angin untuk 5 hari ke depan
        angin = five_day("td",{"class":"wind"})

        self.list_angin = []
        for i in range (5):
            self.list_angin.append(angin[i].get_text().strip())
        
        #Mendapatkan kelembapan untuk 5 hari ke depan
        kelembapan = five_day("td",{"class":"humidity"})

        self.list_kelembapan = []
        for i in range (5):
            self.list_kelembapan.append(kelembapan[i].get_text())
        
        #Mendapatkan rincian singkat untuk cuaca 5 hari ke depan
        deskripsi = soup.find_all(class_='description')

        self.list_deskripsi =[]
        for i in range(1,6):
            self.list_deskripsi.append(deskripsi[i].get('title'))
    ##---------------------------------------------------------------------------------##
        #Judul GUI
        master.title("Reynard's Depok Weather Forecast")

        #Hari ini di GUI
        self.day = Label(self.master,text=self.list_hari[0],font="helvetica 34 bold")
        self.day.grid(row=0,columnspan=5)

        #Tanggal hari ini di GUI
        self.date = Label(self.master,text="Tanggal: "+self.list_tanggal[0],font="helvetica 20 bold")
        self.date.grid(row=1,columnspan=5)

        #Cuaca hari ini di GUI
        self.the_weather = Label(self.master,text="Cuaca: "+self.list_cuaca[0],font="helvetica 20 bold")
        self.the_weather.grid(row=2,columnspan=5)

        #Suhu maksimum/minimum hari ini di GUI
        self.temp = Label(self.master,text="Suhu Maks/min: "+self.list_suhu[0]+" C",font="helvetica 20 bold")
        self.temp.grid(row=3,columnspan=5)

        #Curah hujan hari ini di GUI
        self.precip = Label(self.master,text="Curah Hujan: "+self.list_curah_hujan[0],font="helvetica 20 bold")
        self.precip.grid(row=4,columnspan=5)

        #arah dan kecepatan hari ini di GUI
        self.wind = Label(self.master,text="Angin: "+self.list_angin[0],font="helvetica 20 bold")
        self.wind.grid(row=5,columnspan=5)

        #kelembapan hari ini di GUI
        self.humid = Label(self.master,text="Kelembapan: "+self.list_kelembapan[0],font="helvetica 20 bold")
        self.humid.grid(row=5,columnspan=5)

        #rincian singkat cuaca hari ini di GUI
        self.desc = Label(self.master,text="\""+self.list_deskripsi[0]+"\"",font="helvetica 15 bold")
        self.desc.grid(row=5,columnspan=5)

        #Tombol untuk tiap hari
        self.btn0 = Button(self.master,text=self.list_hari[0],command=self.press0,width=25)
        self.btn0.grid(row=6,column=0)
        
        self.btn1 = Button(self.master,text=self.list_hari[1],command=self.press1,width=25)
        self.btn1.grid(row=6,column=1)
        
        self.btn2 = Button(self.master,text=self.list_hari[2],command=self.press2,width=25)
        self.btn2.grid(row=6,column=2)
        
        self.btn3 = Button(self.master,text=self.list_hari[3],command=self.press3,width=25)
        self.btn3.grid(row=6,column=3)
        
        self.btn4 = Button(self.master,text=self.list_hari[4],command=self.press4,width=25)
        self.btn4.grid(row=6,column=4)

    #Jika memencet tombol hari ini
    def press0(self):

        self.day['text'] = self.list_hari[0]
        self.date['text'] = "Tanggal: "+self.list_tanggal[0]
        self.the_weather['text'] ="Cuaca: "+self.list_cuaca[0]
        self.temp['text'] = "Suhu Maks/min: "+self.list_suhu[0]+" C"
        self.precip['text'] ="Curah Hujan: "+self.list_curah_hujan[0]
        self.wind['text'] = "Angin: "+self.list_angin[0]
        self.humid['text'] = "Kelembapan: "+self.list_kelembapan[0]
        self.desc['text'] = "\""+self.list_deskripsi[0]+"\""
        
    #Jika memencet tombol hari esok
    def press1(self):

        self.day['text'] = self.list_hari[1]
        self.date['text'] = "Tanggal: "+self.list_tanggal[1]
        self.the_weather['text'] ="Cuaca: "+self.list_cuaca[1]
        self.temp['text'] = "Suhu Maks/min: "+self.list_suhu[1]+" C"
        self.precip['text'] ="Curah Hujan: "+self.list_curah_hujan[1]
        self.wind['text'] = "Angin: "+self.list_angin[1]
        self.humid['text'] = "Kelembapan: "+self.list_kelembapan[1]
        self.desc['text'] = "\""+self.list_deskripsi[1]+"\""
        
    #Jika memencet tombol hari lusa
    def press2(self):

        self.day['text'] = self.list_hari[2]
        self.date['text'] = "Tanggal: "+self.list_tanggal[2]
        self.the_weather['text'] ="Cuaca: "+self.list_cuaca[2]
        self.temp['text'] = "Suhu Maks/min: "+self.list_suhu[2]+" C"
        self.precip['text'] ="Curah Hujan: "+self.list_curah_hujan[2]
        self.wind['text'] = "Angin: "+self.list_angin[2]
        self.humid['text'] = "Kelembapan: "+self.list_kelembapan[2]
        self.desc['text'] = "\""+self.list_deskripsi[2]+"\""

    #Jika memencet tombol hari ke-3
    def press3(self):

        self.day['text'] = self.list_hari[3]
        self.date['text'] = "Tanggal: "+self.list_tanggal[3]
        self.the_weather['text'] ="Cuaca: "+self.list_cuaca[3]
        self.temp['text'] = "Suhu Maks/min: "+self.list_suhu[3]+" C"
        self.precip['text'] ="Curah Hujan: "+self.list_curah_hujan[3]
        self.wind['text'] = "Angin: "+self.list_angin[3]
        self.humid['text'] = "Kelembapan: "+self.list_kelembapan[3]
        self.desc['text'] = "\""+self.list_deskripsi[3]+"\""

    #Jika memencet tombol hari ke-4
    def press4(self):

        self.day['text'] = self.list_hari[4]
        self.date['text'] = "Tanggal: "+self.list_tanggal[4]
        self.the_weather['text'] ="Cuaca: "+self.list_cuaca[4]
        self.temp['text'] = "Suhu Maks/min: "+self.list_suhu[4]+" C"
        self.precip['text'] ="Curah Hujan: "+self.list_curah_hujan[4]
        self.wind['text'] = "Angin: "+self.list_angin[4]
        self.humid['text'] = "Kelembapan: "+self.list_kelembapan[4]
        self.desc['text'] = "\""+self.list_deskripsi[4]+"\""
        
            
    
    
    
def main():
    window = Tk()
    my_window = Weather(window)
    window.mainloop()
    

if __name__ == "__main__":
    main()

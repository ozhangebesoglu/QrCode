#Kutupphaneleri ekledik
import tkinter as tk
from tkinter import filedialog
import pyqrcode as qr 
from pyqrcode import QRCode

#Fonksiyonlari tanimladik
def qr_code_olustur():
    url = url_girdi.get()
    
    if url:
        qr_url = qr.create(url)
        
        dosya_yolu = filedialog.asksaveasfilename(defaultextension=".svg", filetypes = [("SVG dosyalari", "*.svg")])
        
        if dosya_yolu:
            qr_url.svg(dosya_yolu, scale=10)
            durum_etiketi.config(text="QR kodu başarıyla oluşturuldu ve kaydedildi.", fg="green") 
    else:
        durum_etiketi.config(text="Lütfen bir URL girin.", fg="red")


# Tasarim kismi

uygulama = tk.Tk()
uygulama.title("QR Kod Oluşturucu")
etiket_url = tk.Label(uygulama, text="URL girin:",)
url_girdi = tk.Entry(uygulama,width=50)
qr_kodu_olustur_butonu = tk.Button(uygulama, text="QR Kodu Oluştur", command=qr_code_olustur)
durum_etiketi = tk.Label(uygulama, text="", fg="black")


# Yerlestirme Kismi
""" etiket_url.pack()
url_girdi.pack()
qr_kodu_olustur_butonu.pack()
durum_etiketi.pack()         """

etiket_url.grid(row=0, column=0,padx= 10,pady=10)
url_girdi.grid(row=0, column=1,padx= 10,pady=10)
qr_kodu_olustur_butonu.grid(row=1, column=0,columnspan=2,padx= 10,pady=10)
durum_etiketi.grid(row=2, column=0,columnspan=2,padx= 10,pady=10)





uygulama.mainloop()

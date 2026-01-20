import customtkinter as ctk

class Bayroq(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("300x120")
        [ctk.CTkFrame(self, fg_color=r, height=40, corner_radius=0).pack(fill="x") 
         for r in ["#0099B5", "white", "#1EB53A"]]

Bayroq().mainloop()


# 1. Merosxo‘rlik (Inheritance)
# Vazifasi: Kodni qayta ishlatish. 
# Ota klassdagi xususiyatlarni 
# bola klassga o‘tkazish.

class Mashina:
    ''' Ota klass: Barcha mashinalar uchun umumiy qolip.
    Vazifasi: Kod takrorlanishini oldini olish. '''
    def __init__(self, brend):
        self.brend = brend

    def yurish(self):
        print(f"{self.brend} harakatlanmoqda...")

class Toyota(Mashina):
    ''' Bola klass: Mashina klassidan meros oladi.
    Vazifasi: Ota klass xususiyatlarini ishlatib, yangi funksiya qo'shish. '''
    def signal(self):
        print("Beep-beep!")

# TAHLIL: Toyota-da 'yurish' yozilmagan, lekin u ota klassdan bu qobiliyatni meros olgan.

# 2. Inkapsulyatsiya (Encapsulation)

class Avtomobil:
    ''' Vazifasi: Ma'lumotni himoya qilish (yashirish).
    Tashqaridan to'g'ridan-to'g'ri o'zgartirishni cheklaydi. '''
    def __init__(self):
        self.__yoqilgi = 50  # __ (private) - faqat klass ichida ko'rinadi

    def yoqilgi_korsat(self):
        ''' Ichki ma'lumotni xavfsiz taqdim etish usuli. '''
        return f"Bokda {self.__yoqilgi} litr bor."

# TAHLIL: mashina.__yoqilgi deb unga buzib kirib bo'lmaydi, ma'lumot xavfsiz.


# 3. Polimorfizm (Polymorphism)

class Benzinli:
    def ovoz(self): return "Vrrr-vrrr!"

class Elektro:
    def ovoz(self): return "Shshsh..."

''' Vazifasi: Bir xil nomli buyruqqa har xil obyektning turlicha javob berishi.
'ovoz' bitta, lekin har xil dvigatel har xil tovush chiqaradi. '''

for m in [Benzinli(), Elektro()]:
    print(m.ovoz())



# 4. Abstraksiya (Abstraction)

from abc import ABC, abstractmethod

class Reja(ABC):
    ''' Vazifasi: Umumiy standart (shablon) o'rnatish.
    Nima qilish kerakligini aytadi, lekin qanday qilishni bola klassga qoldiradi. '''
    @abstractmethod
    def tormoz(self): pass

class Nexia(Reja):
    def tormoz(self): # Majburiy amalga oshirish
        print("Nexia to'xtadi.")

# TAHLIL: Reja-dan obyekt olib bo'lmaydi, u faqat yo'nalish beruvchi qolipdir.

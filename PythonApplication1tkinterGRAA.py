from tkinter import * 
import random
import time

class Gracze():
    def __init__(self, scale1, scale2, scale3, scale4, scale5, scale6, scale7, scale8, scale9, scale10, textBox):
        self.scale1 = scale1
        self.scale2 = scale2
        self.scale3 = scale3
        self.scale4 = scale4
        self.scale5 = scale5
        self.scale6 = scale6
        self.scale7 = scale7
        self.scale8 = scale8
        self.scale9 = scale9
        self.scale10 = scale10
        self.textBox = textBox
        print("definiowanie klasy Gracze")
    


    def test(self):
        self.textBox.delete("1.0", END) ### Czyści pole tekstowe z wynikami.
# TUTAJ PODAJEMY LICZBĘ GRACZY O RÓŻNYCH STYLACH GRY #
        self.liczba_wspolnikow = self.scale1.get()
        print(self.liczba_wspolnikow)
        self.liczba_oszustow = self.scale2.get()
        print(self.liczba_oszustow)
        self.liczba_przypadkow = self.scale3.get()
        print(self.liczba_przypadkow)
        self.liczba_papug = self.scale4.get()
        print(self.liczba_papug)
        self.liczba_papuzek = self.scale5.get()
        print(self.liczba_papuzek)
        self.liczba_mscicieli = self.scale6.get()
        print(self.liczba_mscicieli)
        self.liczba_detektywow = self.scale7.get()
        print(self.liczba_detektywow)



# TUTAJ TWORZYMY I WYŚWIETLAMY LISTĘ WSZYSTKICH GRACZY #
        self.lista_graczy = []
        for n in range(0, self.liczba_wspolnikow):
            self.lista_graczy.append("Wspólnik")
        for n in range(0, self.liczba_oszustow):
            self.lista_graczy.append("Oszust")
        for n in range(0, self.liczba_przypadkow):
            self.lista_graczy.append("Przypadek")
        for n in range(0, self.liczba_papug):
            self.lista_graczy.append("Papuga")
        for n in range(0, self.liczba_papuzek):
            self.lista_graczy.append("Papużka")
        for n in range(0, self.liczba_mscicieli):
            self.lista_graczy.append("Mściciel")
        for n in range(0, self.liczba_detektywow):
            self.lista_graczy.append("Detektyw")
        print("Lista graczy:", self.lista_graczy)

        # TUTAJ WYZNACZAMY I WYŚWIETLAMY LICZBĘ GRACZY #
        self.liczba_graczy = len(self.lista_graczy)
        print("Liczba graczy:", self.liczba_graczy)

        # TUTAJ PODAJEMY LICZBĘ TURNIEJÓW, JAKA ZOSTANIE ROZEGRANA #
        
        self.liczba_turniejow = self.scale8.get()

        # TUTAJ PODAJEMY LICZBĘ RUND, JAKĄ KAŻDY ZAGRA PRZECIWKO KAŻDEMU W KAŻDYM TURNIEJU #
        self.liczba_rund = self.scale9.get()


        ## Macierz WYPŁAT
        ## Pobieramy Macierz WYPŁAT
        # TUTAJ OKREŚLAMY WYPŁATY #
        # TUTAJ OKREŚLAMY WYPŁATY #

        self.wyplata_ww = int(self.box1g1.get())

        self.wyplata_zz = int(self.box4g1.get())

        self.wyplata_wz = int(self.box2g1.get())

        self.wyplata_zw = int(self.box2g2.get())

        # TUTAJ TWORZYMY PUSTE TABLICE, KTÓRE BĘDĄ PRZECHOWYWAĆ WYBIERANE PRZEZ GRACZY STRATEGIE #
        self.strategie_gracza_i = []
        for n in range(0, self.liczba_rund):
            self.strategie_gracza_i.append("nic")
        self.strategie_gracza_j = []
        for n in range(0, self.liczba_rund):
            self.strategie_gracza_j.append("nic")

        # TUTAJ TWORZYMY PUSTE TABLICE, KTÓRE BĘDĄ PRZECHOWYWAĆ ZDOBYWANE PRZEZ GRACZY WYPŁATY #
        self.wyplaty_gracza_i = []
        for n in range(0, self.liczba_rund):
            self.wyplaty_gracza_i.append(0)
        self.wyplaty_gracza_j = []
        for n in range(0, self.liczba_rund):
            self.wyplaty_gracza_j.append(0)

        # TUTAJ TWORZYMY PUSTĄ TABLICĘ, W KTÓREJ BĘDĄ SUMOWANE WYPŁATY GRACZY (OSTATECZNE WYNIKI) #
        self.sumy_wyplat = []
        for n in range(0, self.liczba_graczy):
            self.sumy_wyplat.append(0)

        # TUTAJ OKREŚLAMY PRAWDOPODOBIEŃSTWO, ŻE GRACZ ZAGRA NIEZGODNIE ZE SWOIM STYLEM GRY #
        self.prawd_pomylki = self.scale10.get()

        # TUTAJ TWORZYMY TABLICĘ POTRZEBNĄ DO OKREŚLANIA, CZY GRACZ SIĘ POMYLI W WYBORZE STRATEGII #
        self.pomylka = []
        for n in range(0, self.prawd_pomylki + 1):
            self.pomylka.append(n)

# TUTAJ ZACZYNAMY GRĘ #
        for t in range(0, self.liczba_turniejow):  # iterowanie turniejów

            for i in range(0, self.liczba_graczy - 1):  # iterowanie i-tego gracza (od pierwszego do przedostatniego)
                # STRATEGIA I-TEGO GRACZA #
                if self.lista_graczy[i] == "Wspólnik" or self.lista_graczy[i] == "Papuga" or self.lista_graczy[i] == "Papużka" or self.lista_graczy[i] == "Mściciel" or self.lista_graczy[i] == "Detektyw":
                    self.strategia_i = "współpraca"
                elif self.lista_graczy[i] == "Oszust":
                    self.strategia_i = "zdrada"
                else:  # lista_graczy[i] == "Przypadek":
                    self.strategia_i = "współpraca" if random.randint(0, 1) == 0 else "zdrada"

                for j in range(i+1, self.liczba_graczy):  # iterowanie j-tego gracza (od i+1 do ostatniego)
                    # STRATEGIA J-TEGO GRACZA #
                    if self.lista_graczy[j] == "Wspólnik" or self.lista_graczy[j] == "Papuga" or self.lista_graczy[j] == "Papużka" or self.lista_graczy[j] == "Mściciel" or self.lista_graczy[j] == "Detektyw":
                        self.strategia_j = "współpraca"
                    elif self.lista_graczy[j] == "Oszust":
                        self.strategia_j = "zdrada"
                    else:  # lista_graczy[j] == "Przypadek":
                        self.strategia_j = "współpraca" if random.randint(0, 1) == 0 else "zdrada"

                    for k in range(0, self.liczba_rund):  # iterowanie rund

                        if self.strategia_i == "współpraca" and random.randint(1, 100) in self.pomylka:  # (prawd_pomylki)%, że i-ty gracz pomyli się w wyborze strategii
                            self.strategia_i = "zdrada"
                        if self.strategia_i == "zdrada" and random.randint(1, 100) in self.pomylka:
                            self.strategia_i = "współpraca"

                        if self.strategia_j == "współpraca" and random.randint(1, 100) in self.pomylka:  # (prawd_pomylki)%, że j-ty gracz pomyli się w wyborze strategii
                            self.strategia_j = "zdrada"
                        if self.strategia_j == "zdrada" and random.randint(1, 100) in self.pomylka:
                            self.strategia_j = "współpraca"

                        self.strategie_gracza_i[k] = self.strategia_i  # zapisanie strategii i-tego gracza w k-tej rundzie
                        self.strategie_gracza_j[k] = self.strategia_j  # zapisanie strategii j-tego gracza w k-tej rundzie

                        # WYPŁATY #
                        if self.strategia_i == "współpraca" and self.strategia_j == "współpraca":
                            self.wyplaty_gracza_i[k] = self.wyplata_ww
                            self.sumy_wyplat[i] += self.wyplata_ww
                            self.wyplaty_gracza_j[k] = self.wyplata_ww
                            self.sumy_wyplat[j] += self.wyplata_ww
                        elif self.strategia_i == "zdrada" and self.strategia_j == "zdrada":
                            self.wyplaty_gracza_i[k] = self.wyplata_zz
                            self.sumy_wyplat[i] += self.wyplata_zz
                            self.wyplaty_gracza_j[k] = self.wyplata_zz
                            self.sumy_wyplat[j] += self.wyplata_zz
                        elif self.strategia_i == "współpraca" and self.strategia_j == "zdrada":
                            self.wyplaty_gracza_i[k] = self.wyplata_wz
                            self.sumy_wyplat[i] += self.wyplata_wz
                            self.wyplaty_gracza_j[k] = self.wyplata_zw
                            self.sumy_wyplat[j] += self.wyplata_zw
                        else:  # strategia_i == "zdrada" and strategia_j == "współpraca":
                            self.wyplaty_gracza_i[k] = self.wyplata_zw
                            self.sumy_wyplat[i] += self.wyplata_zw
                            self.wyplaty_gracza_j[k] = self.wyplata_wz
                            self.sumy_wyplat[j] += self.wyplata_wz

                        if self.lista_graczy[i] == "Przypadek":
                            self.strategia_i = "współpraca" if random.randint(0, 1) == 0 else "zdrada"
                        if self.lista_graczy[i] == "Papuga":          # jeśli i-ty gracz jest Papugą
                            self.strategia_i = self.strategie_gracza_j[k]  # to jego następny ruch będzie ruchem przeciwnika z obecnej rundy
                        if self.lista_graczy[i] == "Papużka" and (k == 0 or self.strategie_gracza_j[k] == "współpraca"):
                            self.strategia_i = "współpraca"
                        if self.lista_graczy[i] == "Papużka" and k > 0 and self.strategie_gracza_j[k] == "zdrada" and self.strategie_gracza_j[k-1] == "zdrada":
                            self.strategia_i = "zdrada"
                        if self.lista_graczy[i] == "Mściciel" and "zdrada" in self.strategie_gracza_j:  # jeśli i-ty gracz jest Mścicielem i został zdradzony
                            self.strategia_i = "zdrada"                                            # to teraz będzie on zdradzał
                        if self.lista_graczy[i] == "Detektyw" and k == 0:
                           self. strategia_i = "zdrada"
                        if self.lista_graczy[i] == "Detektyw" and (k == 1 or k == 2):
                            self.strategia_i = "współpraca"
                        if self.lista_graczy[i] == "Detektyw" and k > 2 and self.strategie_gracza_j[3] == "zdrada":
                            self.strategia_i = self.strategie_gracza_j[k]
                        if self.lista_graczy[i] == "Detektyw" and k > 2 and self.strategie_gracza_j[3] == "współpraca":
                            self.strategia_i = "zdrada"

                        if self.lista_graczy[j] == "Przypadek":
                            self.strategia_j = "współpraca" if random.randint(0, 1) == 0 else "zdrada"
                        if self.lista_graczy[j] == "Papuga":
                            self.strategia_j = self.strategie_gracza_i[k]
                        if self.lista_graczy[j] == "Papużka" and (k == 0 or self.strategie_gracza_i[k] == "współpraca"):
                            self.strategia_j = "współpraca"
                        if self.lista_graczy[j] == "Papużka" and k > 0 and self.strategie_gracza_i[k] == "zdrada" and self.strategie_gracza_i[k-1] == "zdrada":
                            self.strategia_j = "zdrada"
                        if self.lista_graczy[j] == "Mściciel" and "zdrada" in self.strategie_gracza_i:
                            self.strategia_j = "zdrada"
                        if self.lista_graczy[j] == "Detektyw" and k == 0:
                            self.strategia_j = "zdrada"
                        if self.lista_graczy[j] == "Detektyw" and (k == 1 or k == 2):
                            self.strategia_j = "współpraca"
                        if self.lista_graczy[j] == "Detektyw" and k > 2 and self.strategie_gracza_i[3] == "zdrada":
                            self.strategia_j = self.strategie_gracza_i[k]
                        if self.lista_graczy[j] == "Detektyw" and k > 2 and self.strategie_gracza_i[3] == "współpraca":
                            self.strategia_j = "zdrada"

                # WYNIKI ZE WSZYSTKICH RUND Z GIER 1 VS 1 #

            # OSTATECZNE WYNIKI WSZYSTKICH GRACZY #
            for n in range(0, self.liczba_graczy):
                print("Ostateczny wynik Gracza", n+1, "(", self.lista_graczy[n], "):", self.sumy_wyplat[n])
                self.ostatecznyWynik = "Ostateczny wynik Gracza" + str(n+1) + "(" + self.lista_graczy[n] + "):" + str(self.sumy_wyplat[n]) 
                self.textBox.insert(END, self.ostatecznyWynik + "\n")
            # SPRAWDZENIE, KTÓRY GRACZ MA NAJWYŻSZY WYNIK I PRZYPISANIE JEGO INDEKSU DO POMOCNICZEJ ZMIENNEJ #
            for n in range(0, self.liczba_graczy):
                if self.sumy_wyplat[n] == max(self.sumy_wyplat):
                    self.najlepszy_gracz = n
                    break

            # SPRAWDZENIE, KTÓRY GRACZ MA NAJNIŻSZY WYNIK I ZAMIANA JEGO STRATEGII NA NAJLEPSZĄ #
            for n in range(0, self.liczba_graczy):
                if self.sumy_wyplat[n] == min(self.sumy_wyplat):
                    self.lista_graczy[n] = self.lista_graczy[self.najlepszy_gracz]
                    break

            print("Nowa lista graczy: ", self.lista_graczy)
            

            # WYZEROWANIE ZDOBYTYCH WYPŁAT PRZED NASTĘPNYM TURNIEJEM #
            for n in range(0, self.liczba_graczy):
                self.sumy_wyplat[n] = 0




class Application(Gracze):
    def __init__(self):
        self.window = Tk()
        self.window.title("Aplikacja")
        self.window.geometry("1500x900")


        ## Ramki
        self.leftFrame = Frame(self.window, background = "black", height = 100, width = 600) #Lewa Ramka Frame
        self.leftFrame.pack(side = LEFT, fill = Y) # umiejscowienie ramki lewej

        self.rightFrame = Frame(self.window, background = "grey", height = 100, width = 300) #Prawa Ramka Frame
        self.rightFrame.pack(side = RIGHT, fill = Y) # umiejscowienie ramki prawej

        self.scaFrame = Frame(self.rightFrame, height = 100, width = 300) #Ramka na suwaki
        self.scaFrame.pack(side = RIGHT , fill = Y) # umiejscowienie ramki na suwaki

        self.spinBoxFrame = Frame(self.rightFrame, height = 100, width = 100) #Ramka SpinBoxy (macierz wypłat)
        self.spinBoxFrame.pack(side = RIGHT, fill = Y) # umiejscowienie ramki na SpinBoxy(macierz wyplat)

        ## Suwaki do wprowadzania wartości

        #Liczba wspólnków
        self.LabelScal1 = Label(self.scaFrame, text="Podaj Liczbę Wspólników ")
        self.LabelScal1.grid(row=0, sticky=SW)
        self.scale1 = Scale(self.scaFrame, from_=0, to=20,orient=HORIZONTAL)
        self.scale1.grid(row=0, column=1)
        self.LabelScal11 = Label(self.scaFrame, text="Wspólnik (zawsze współpracuje)")
        self.LabelScal11.grid(row=0, column=2, sticky=S)
        #Liczba Oszustów
        self.LabelScal2 = Label(self.scaFrame, text="Podaj liczbę Oszustów ")
        self.LabelScal2.grid(row=1, sticky=SW)
        self.scale2 = Scale(self.scaFrame, from_=0, to=20,orient=HORIZONTAL)
        self.scale2.grid(row=1, column=1)
        self.LabelScal22 = Label(self.scaFrame, text="Oszust (zawsze zdradza)")
        self.LabelScal22.grid(row=1, column=2, sticky=S)
        #Liczba  Przypadków
        self.LabelScal3 = Label(self.scaFrame, text="Podaj liczbę Przypadków ")
        self.LabelScal3.grid(row=2, sticky=SW)
        self.scale3 = Scale(self.scaFrame, from_=0, to=20,orient=HORIZONTAL)
        self.scale3.grid(row=2, column=1)
        self.LabelScal33 = Label(self.scaFrame, text="Przypadek (losowo współpracuje lub zdradza)")
        self.LabelScal33.grid(row=2, column=2, sticky=S)
        #Liczba  Papug
        self.LabelScal4 = Label(self.scaFrame, text="Podaj liczbę Papug ")
        self.LabelScal4.grid(row=3, sticky=SW)
        self.scale4 = Scale(self.scaFrame, from_=0, to=20,orient=HORIZONTAL)
        self.scale4.grid(row=3, column=1)
        self.LabelScal44 = Label(self.scaFrame, text="Papuga (zaczyna od współpracy,\n a następnie naśladuje ruchy przeciwnika")
        self.LabelScal44.grid(row=3, column=2, sticky=S)
        #Liczba  Papużek
        self.LabelScal5 = Label(self.scaFrame, text="Podaj liczbę Papużek ")
        self.LabelScal5.grid(row=4, sticky=SW)
        self.scale5 = Scale(self.scaFrame, from_=0, to=20,orient=HORIZONTAL)
        self.scale5.grid(row=4, column=1)
        self.LabelScal55 = Label(self.scaFrame, text="Papużka (gra jak Papuga, ale zdradza tylko wtedy, \n gdy zostanie zdradzony 2 razy z rzędu")
        self.LabelScal55.grid(row=4, column=2, sticky=S)
        #Liczba  Mścicieli
        self.LabelScal6 = Label(self.scaFrame, text="Podaj liczbę Mścicieli ")
        self.LabelScal6.grid(row=5, sticky=SW)
        self.scale6 = Scale(self.scaFrame, from_=0, to=20,orient=HORIZONTAL)
        self.scale6.grid(row=5, column=1)
        self.LabelScal66 = Label(self.scaFrame, text="Mściciel (zaczyna od współpracy, \n a od kiedy zostanie oszukany, gra do końca jak Oszust")
        self.LabelScal66.grid(row=5, column=2, sticky=S)
        #Liczba  Detektywów
        self.LabelScal7 = Label(self.scaFrame, text="Podaj liczbę Detektywów ")
        self.LabelScal7.grid(row=6, sticky=SW)
        self.scale7 = Scale(self.scaFrame, from_=0, to=20,orient=HORIZONTAL)
        self.scale7.grid(row=6, column=1)
        self.LabelScal77 = Label(self.scaFrame, text="Detektyw (zaczyna od: współpraca, zdrada, współpraca, współpraca; \n później, jeśli zostanie zdradzony, gra jak Papuga, \n w przeciwnym wypadku gra jak Oszust)")
        self.LabelScal77.grid(row=6, column=2, sticky=S)

        #Liczba Turniejów
        self.LabelScal8 = Label(self.scaFrame, text="Podaj liczbę Turniejów ")
        self.LabelScal8.grid(row=7, sticky=SW)
        self.scale8 = Scale(self.scaFrame, from_=0, to=20,orient=HORIZONTAL)
        self.scale8.grid(row=7, column=1)
        self.LabelScal88 = Label(self.scaFrame, text="Podaj liczbę turniejów w których każdy zagra z każdym")
        self.LabelScal88.grid(row=7, column=2, sticky=S)
        #Liczba Gier w turnieju
        self.LabelScal9 = Label(self.scaFrame, text="Podaj liczbę Gier ")
        self.LabelScal9.grid(row=8, sticky=SW)
        self.scale9 = Scale(self.scaFrame, from_=0, to=20,orient=HORIZONTAL)
        self.scale9.grid(row=8, column=1)
        self.LabelScal99 = Label(self.scaFrame, text="Podaj liczbę gier (ile razy zagrają z rzędu dwaj przeciwnicy)")
        self.LabelScal99.grid(row=8, column=2, sticky=S)
        #Prawdopodobieństwo zmiany decyzji
        self.LabelScal10 = Label(self.scaFrame, text="Podaj prawdopodobieństwo \n (%) zmiany decyzji ")
        self.LabelScal10.grid(row=9, sticky=SW)
        self.scale10 = Scale(self.scaFrame, from_=0, to=30,orient=HORIZONTAL)
        self.scale10.grid(row=9, column=1)
        self.LabelScal10 = Label(self.scaFrame, text="Podaj prawdopodobieństwo (%) zmiany decyzji danego gracza (Zmiana sposobu gry)")
        self.LabelScal10.grid(row=9, column=2, sticky=S)



        self.btn1 = Button(self.scaFrame, text = "Zacznij gre", fg = "green", command = self.tester)
        self.btn1.grid(row=10, column=0, sticky=S)



        #Tutaj określamy WYPŁATY
        self.LabelBox2 = Label(self.spinBoxFrame, text="Wyniki ") #Górny prawy napis
        self.LabelBox2.grid(row=0, column=0, sticky = W, padx =0, pady = 0) #Górny prawy napis

        self.LabelBox1 = Label(self.spinBoxFrame, text="Współpraca ") #Górny lewy napis
        self.LabelBox1.place( x = 60)  #Górny lewy napis
        self.box1g2 = Entry(self.spinBoxFrame, width=2) # Górny prawy SpinBox
        self.box1g2.grid(row=1, column=2, pady =5, padx=10) # Górny prawy SpinBox | 0 | X |   | 0 | 0 |
        self.box1g2.insert(0, "2")  #Przypisanie domyślnej wartości 2 
        self.box2g2 = Entry(self.spinBoxFrame, width=2) # Górny prawy SpinBox
        self.box2g2.grid(row=1, column=5, pady =5, padx=10) # Górny prawy SpinBox | 0 | 0 |   | 0 | X |
        self.box2g2.insert(0, "3") #Przypisanie domyślnej wartości 3

        self.LabelBox2 = Label(self.spinBoxFrame, text="Zdrada ") #Górny prawy napis
        self.LabelBox2.place(x=130) #Górny prawy napis
        self.box3g2 = Entry(self.spinBoxFrame, width=2) # Dolny prawy SpinBox
        self.box3g2.grid(row=2, column=2) # Dolny prawy SpinBox  | 0 | X |   | 0 | 0 |
        self.box3g2.insert(0, "-1") #Przypisanie domyślnej wartości -1
        self.box4g2 = Entry(self.spinBoxFrame, width=2) # Dolny prawy SpinBox
        self.box4g2.grid(row=2, column=5) # Dolny prawy SpinBox | 0 | 0 |   | 0 | X |
        self.box4g2.insert(0, "0") #Przypisanie domyślnej wartości 0


        self.LabelBox3 = Label(self.spinBoxFrame, text="Współpraca ") #Górny lewy LEWY napis
        self.LabelBox3.grid(row=1, sticky=SW) #Górny lewy LEWY napis
        self.box1g1 = Entry(self.spinBoxFrame, width=2) # Lewy górny SpinBox
        self.box1g1.grid(row=1, column=1) # Lewy górny SpinBox  | X | 0 |   | 0 | 0 |
        self.box1g1.insert(0, "2") #Przypisanie domyślnej wartości 2
        self.box4g1 = Entry(self.spinBoxFrame, width=2) # Lewy górny SpinBox
        self.box4g1.grid(row=2, column=4) # Lewy Dokny SpinBox  | 0 | 0 |   | X | 0 |
        self.box4g1.insert(0, "0") #Przypisanie domyślnej wartości 0

        
        self.LabelBox4 = Label(self.spinBoxFrame, text="Zdrada ") #Dolnylewy LEWY napis
        self.LabelBox4.grid(row=2, sticky=SW) #Dolnylewy LEWY napis
        self.box3g1 = Entry(self.spinBoxFrame, width=2) # Lewy dolny SpinBox
        self.box3g1.grid(row=2, column=1) # Lewy dolny SpinBox | X | 0 |   | 0 | 0 |
        self.box3g1.insert(0, "3") #Przypisanie domyślnej wartości 3
        self.box2g1 = Entry(self.spinBoxFrame, width=2) # Lewy dolny SpinBox
        self.box2g1.grid(row=1, column=4) # Lewy Górny SpinBox  | 0 | 0 |   | X | 0 |
        self.box2g1.insert(0, "-1") #Przypisanie domyślnej wartości -1



        

    
        
#        self.S = Scrollbar(self.textBox)
#        self.S.pack(side = RIGHT, fill = Y)       
        self.textBox = Text(self.leftFrame, width= 200, height=700)   ###, yscrollcommand = self.S.set
        
        self.textBox.place(x = 0,y = 0)


#        self.S.config( command = self.textBox.yview )

        

        self.window.mainloop()

    def tester(self):
        scale1 = self.scale1
        scale2 = self.scale2
        scale3 = self.scale3
        scale4 = self.scale4
        scale5 = self.scale5
        scale6 = self.scale6
        scale7 = self.scale7
        scale8 = self.scale8
        scale9 = self.scale9
        scale10 = self.scale10
        textBox = self.textBox
        start_time = time.time()
        Gracze.test(scale1, scale2, scale3, scale4, scale5, scale6, scale7, scale8, scale9, scale10, textBox)
        print("--- %s seconds ---" % ((time.time() - start_time))/60)

app = Application()
app()



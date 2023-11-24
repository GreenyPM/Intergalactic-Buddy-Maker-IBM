from tkinter import *
import aimake
import printer
import random

class mainEngine:
    def __init__(self):
        self.prnt = printer.printerC()
        self.AI = aimake.animeAI()
        self.root = Tk()
        self.root.title("Intergalactic Buddy Maker")
        self.root.geometry("1280x1000")
        self.root.config(background = '#2A2B2E')
        self.root.resizable(False,False)
        self.photo = PhotoImage(file="Images\\img{}.png".format(self.AI.counter))
        self.aiArtwork = Label(self.root, image=self.photo)
        self.aiArtwork.photo = self.photo
        self.photoCounter = 100
        self.premadeDescPrompts = ("Elegant and poised", "Sleek and modern", "Sharp and stylish", "Cool and edgy", "Bold and daring", "Chic and trendy", "Casual and chic", "Elegant and chic", "Sleek and classic", "Sharp and refined", "Retro and chic", "Modern and sleek", "Cool and trendy", "Sleek and bold", "Edgy and chic", "Chic and classic", "Stylish and chic", "Elegant and cool", "Sleek and edgy", "Sharp and modern", "Trendy and chic", "Modern and edgy", "Cool and refined", "Sleek and daring", "Chic and modern", "Elegant and bold", "Classic and cool", "Retro and sleek", "Edgy and bold", "Sharp and edgy", "Trendy and sleek", "Sleek and sharp", "Cool and classic", "Chic and edgy", "Modern and bold", "Elegant and sharp", "Retro and cool", "Edgy and modern", "Sleek and classic", "Chic and trendy", "Bold and chic", "Elegant and edgy", "Modern and sharp", "Cool and bold", "Classic and sleek", "Sleek and trendy", "Edgy and sharp", "Trendy and cool", "Chic and sharp", "Retro and edgy", "Bold and stylish", "Elegant and cool", "Sleek and refined", "Modern and trendy", "Cool and sleek", "Sharp and edgy", "Classic and bold", "Chic and modern", "Retro and sleek", "Elegant and chic", "Trendy and bold", "Sleek and classic", "Edgy and stylish", "Cool and sharp", "Sharp and chic", "Chic and edgy", "Bold and trendy", "Modern and chic", "Elegant and sleek", "Retro and bold", "Classic and edgy", "Sleek and cool", "Trendy and sharp", "Edgy and classic", "Chic and sharp", "Cool and modern", "Sleek and trendy", "Retro and chic", "Elegant and bold", "Modern and sharp", "Bold and sleek", "Chic and classic", "Edgy and trendy", "Cool and edgy", "Sleek and edgy", "Sharp and trendy", "Trendy and cool", "Elegant and modern", "Classic and sleek", "Retro and cool", "Sleek and chic", "Cool and stylish", "Edgy and bold", "Chic and refined", "Bold and sharp", "Trendy and edgy", "Elegant and sleek", "Modern and bold", "Sleek and classic", "Sharp and modern")

    def screen(self):
        print(len(self.premadeDescPrompts))
        creatortag = Label (self.root, text= 'Patrick Madonna 2024', font = ('MoolBoran',20), bg = '#A4C2A8', fg = '#2A2B2E')
        creatortag.place(x=10, y=955)
        versionNo = Label(self.root, text='V 1.0.0', font=('MoolBoran', 30), bg='#A4C2A8', fg='#2A2B2E')
        versionNo.place(x=1130, y=940)
        picsRemaining = Label (self.root, text= str(self.photoCounter), font = ('MoolBoran',20), bg = '#A4C2A8', fg = 'red')
        picsRemaining.place(x=1200, y=880)

        title = Label(self.root, text='   Intergalactic  \n Buddy Maker', font=('MoolBoran', 120), bg='#5A5A66',fg='#87FF65')
        subTitle = Label(self.root, text='Powered by AI.', font=('MoolBoran', 40), bg='#5A5A66', fg='#ACEB98')
        title.place(x=80, y=100)
        subTitle.place(x=460, y= 460)

        startButton = Button(self.root, text="Begin!", font=('MoolBoran', 30), height=2, width=30, bg='#A4C2A8', fg='#2A2B2E', command=lambda: genderSelect())
        startButton.place(x=300, y=600)

        Gallbutton = Button(self.root, text="Gallery", font=('MoolBoran', 30), height=2, width=15, bg='#A4C2A8', fg='#2A2B2E', command=lambda: exit())
        Gallbutton.place(x=475, y=750)

        #Items for genderSelect
        subtitle1 = Label(self.root, text='Choose One:', font=('MoolBoran', 100), bg='#5A5A66', fg='#ACEB98')
        aButton = Button(self.root, text="Alien", font=('MoolBoran', 20), height=4, width=40, bg='#A4C2A8', fg='#2A2B2E', command=lambda: alien())
        sButton = Button(self.root, text="Space Marine/Spartan", font=('MoolBoran', 20), height=4, width=40, bg='#A4C2A8', fg='#2A2B2E', command=lambda: spartan())
        dButton = Button(self.root, text="Droid", font=('MoolBoran', 20), height=4, width=40, bg='#A4C2A8', fg='#2A2B2E', command=lambda: droid())
        wButton = Button(self.root, text="Alien Waifu", font=('MoolBoran', 20), height=4, width=40, bg='#A4C2A8', fg='#2A2B2E', command=lambda: waifu())

        #Items for phrase
        subtitle2 = Label(self.root, text='Enter a Descriptor.', font=('MoolBoran', 100),  bg='#5A5A66', fg='#ACEB98')
        phraseEntry = Entry(self.root, font=('Arial', 55))
        pButton = Button(self.root, text = "Enter", font=('MoolBoran', 20), bg='#A4C2A8', fg='#2A2B2E',height= 2, width= 20, command=lambda: thingObjectE())
        divider1 = Button(self.root, text = " ", font=('MoolBoran', 30), height= 0, width= 70, bg = "black",state=DISABLED)
        uTitle = Label(self.root, text="Can't think of one? \n Choose one from below:", font=('MoolBoran', 50), fg='black')

        # Premade Items
        sugg1Val = self.premadeDescPrompts[random.randint(0,11)]
        sugg2Val = self.premadeDescPrompts[random.randint(11, 22)]
        sugg3Val = self.premadeDescPrompts[random.randint(22, 33)]
        sugg4Val = self.premadeDescPrompts[random.randint(33, 44)]
        sugg5Val = self.premadeDescPrompts[random.randint(44, 55)]
        sugg6Val = self.premadeDescPrompts[random.randint(55, 66)]
        sugg1 = Button(self.root, text=sugg1Val, font=('MoolBoran', 20), height=2, width=20, bg='#A4C2A8', fg='#2A2B2E', command=lambda: thingObject1())
        sugg2 = Button(self.root, text=sugg2Val, font=('MoolBoran', 20), height=2, width=20, bg='#A4C2A8', fg='#2A2B2E', command=lambda: thingObject2())
        sugg3 = Button(self.root, text=sugg3Val, font=('MoolBoran', 20), height=2, width=20, bg='#A4C2A8', fg='#2A2B2E', command=lambda: thingObject3())
        sugg4 = Button(self.root, text=sugg4Val, font=('MoolBoran', 20), height=2, width=20, bg='#A4C2A8', fg='#2A2B2E', command=lambda: generate1())
        sugg5 = Button(self.root, text=sugg5Val, font=('MoolBoran', 20), height=2, width=20,bg='#A4C2A8', fg='#2A2B2E', command=lambda: generate2())
        sugg6 = Button(self.root, text=sugg6Val, font=('MoolBoran', 20), height=2, width=20, bg='#A4C2A8', fg='#2A2B2E', command=lambda: generate3())


        #Items for thingsObject
        subtitle3 = Label(self.root, text='Give me Another!', font=('MoolBoran', 90), bg='#5A5A66', fg='#ACEB98')
        thingEntry = Entry(self.root, font=('Arial', 45))
        tButton = Button(self.root, text="Enter", font=('MoolBoran', 20), bg='#A4C2A8', fg='#2A2B2E', height=2, width=20, command=lambda: generateE())

        #Items for generate
        subtitle4 = Label(self.root, text='Click Below \n To Generate!!', font=('MoolBoran', 120),  bg='#5A5A66', fg='#ACEB98')
        shButton = Button(self.root, text="Generate", font=('MoolBoran', 20), height=4, width=45, bg='#A4C2A8', fg='#2A2B2E', command=lambda: showResult())

        #Items for restart/showResult
        subtitle5 = Label(self.root, text='Thanks and Enjoy!', font=('MoolBoran', 90),  bg='#5A5A66', fg='#ACEB98')
        prButton = Button(self.root, text="Print", font=('MoolBoran', 20), bg='#A4C2A8', fg='#2A2B2E',height=2, width=20, command=lambda: printOut())
        rButton = Button(self.root, text="Reset", font=('MoolBoran', 20), bg='#A4C2A8', fg='#2A2B2E', height=2, width=20, command=lambda: restart())


        def genderSelect():
            title.place(x=100000, y=100000)
            subTitle.place(x=100000, y =100000)
            startButton.place(x=100000, y=100000)
            Gallbutton.place(x=100000, y=100000)
            subtitle1.place(x=230, y=30)
            aButton.place(x=305, y=200)
            sButton.place(x=305, y=400)
            dButton.place(x=305, y=600)
            wButton.place(x=305, y=800)
        def alien():
            self.AI.typeEntry("Alien Creature")
            phrase()
        def spartan():
            self.AI.typeEntry("Master Chief")
            phrase()

        def droid():
            self.AI.typeEntry("Droid")
            phrase()

            aButton.place(x=100000, y=100000)
            sButton.place(x=100000, y=100000)
            wButton.place(x=100000, y=100000)
            dButton.place(x=100000, y=100000)

            subtitle2.place(x=100, y=40)
            phraseEntry.place(x=180, y=250)
            pButton.place(x=775, y=250)
            divider1.place(x=0, y=400)
            sugg1.place(x= 20, y=700)
            sugg2.place(x=380, y=750)
            sugg3.place(x=740, y=800)
            uTitle.place(x=100, y=500)

        def thingObjectE():
            self.AI.phraseEntry(phraseEntry.get())
            subtitle2.place(x=10000, y=10000)
            phraseEntry.place(x=10000, y=10000)
            pButton.place(x=100000, y=100000)
            sugg1.place(x=100000, y=100000)
            sugg2.place(x=10000, y=100000)
            sugg3.place(x=100000, y=100000)

            subtitle3.place(x=100, y=40)
            thingEntry.place(x=180, y=250)
            tButton.place(x=775, y=250)
            sugg4.place(x= 20, y=700)
            sugg5.place(x=380, y=750)
            sugg6.place(x=740, y=800)

        def thingObject1():
            self.AI.phraseEntry(sugg1Val)
            subtitle2.place(x=10000, y=10000)
            phraseEntry.place(x=10000, y=10000)
            pButton.place(x=100000, y=100000)
            sugg1.place(x=100000, y=100000)
            sugg2.place(x=10000, y=100000)
            sugg3.place(x=100000, y=100000)

            subtitle3.place(x=100, y=40)
            thingEntry.place(x=180, y=250)
            tButton.place(x=775, y=250)
            sugg4.place(x= 20, y=700)
            sugg5.place(x=380, y=750)
            sugg6.place(x=740, y=800)

        def thingObject2():
            self.AI.phraseEntry(sugg2Val)
            subtitle2.place(x=10000, y=10000)
            phraseEntry.place(x=10000, y=10000)
            pButton.place(x=100000, y=100000)
            sugg1.place(x=100000, y=100000)
            sugg2.place(x=10000, y=100000)
            sugg3.place(x=100000, y=100000)

            subtitle3.place(x=100, y=40)
            thingEntry.place(x=180, y=250)
            tButton.place(x=775, y=250)
            sugg4.place(x= 20, y=700)
            sugg5.place(x=380, y=750)
            sugg6.place(x=740, y=800)

        def thingObject3():
            self.AI.phraseEntry(sugg3Val)
            subtitle2.place(x=10000, y=10000)
            phraseEntry.place(x=10000, y=10000)
            pButton.place(x=100000, y=100000)
            sugg1.place(x=100000, y=100000)
            sugg2.place(x=10000, y=100000)
            sugg3.place(x=100000, y=100000)

            subtitle3.place(x=100, y=40)
            thingEntry.place(x=180, y=250)
            tButton.place(x=775, y=250)
            sugg4.place(x= 20, y=700)
            sugg5.place(x=380, y=750)
            sugg6.place(x=740, y=800)


        def generateE():
            self.AI.objEntry(thingEntry.get())
            subtitle3.place(x=10000, y=10000)
            thingEntry.place(x=10000, y=10000)
            divider1.place(x=100000, y=10000)
            uTitle.place(x=10000, y=10000)
            tButton.place(x=100000, y=100000)
            sugg4.place(x=100000, y=100000)
            sugg5.place(x=10000, y=100000)
            sugg6.place(x=100000, y=100000)

            subtitle4.place(x=80, y=150)
            shButton.place(x=380, y=600)

        def generate1():
            self.AI.objEntry(sugg4Val)
            subtitle3.place(x=10000, y=10000)
            thingEntry.place(x=10000, y=10000)
            tButton.place(x=100000, y=100000)
            sugg4.place(x=100000, y=100000)
            sugg5.place(x=10000, y=100000)
            sugg6.place(x=100000, y=100000)
            divider1.place(x=100000, y=10000)
            uTitle.place(x=10000, y=10000)

            subtitle4.place(x=80, y=150)
            shButton.place(x=380, y=600)

        def generate2():
            self.AI.objEntry(sugg5Val)
            subtitle3.place(x=10000, y=10000)
            thingEntry.place(x=10000, y=10000)
            tButton.place(x=100000, y=100000)
            sugg4.place(x=100000, y=100000)
            sugg5.place(x=10000, y=100000)
            sugg6.place(x=100000, y=100000)
            divider1.place(x=100000, y=10000)
            uTitle.place(x=10000, y=10000)

            subtitle4.place(x=80, y=150)
            shButton.place(x=380, y=600)

        def generate3():
            self.AI.objEntry(sugg6Val)
            subtitle3.place(x=10000, y=10000)
            thingEntry.place(x=10000, y=10000)
            tButton.place(x=100000, y=100000)
            sugg4.place(x=100000, y=100000)
            sugg5.place(x=10000, y=100000)
            sugg6.place(x=100000, y=100000)
            divider1.place(x=100000, y=10000)
            uTitle.place(x=10000, y=10000)

            subtitle4.place(x=90, y=150)
            shButton.place(x=300, y=600)

        def showResult():
            self.AI.finalPromptGenerator(["A", "High Quality Well Drawn", "with", "and", "in outerspace"])
            self.AI.generate()
            subtitle4.place(x=10000, y=100000)
            shButton.place(x=10000, y=100000)

            #Place picture file here.
            self.photo = PhotoImage(file="Images\\img{}.png".format(self.AI.counter))
            self.aiArtwork = Label(self.root, image=self.photo)
            self.aiArtwork.photo = self.photo
            self.aiArtwork.place(x=350, y=225)


            subtitle5.place(x=100, y=40)
            prButton.place(x= 100, y=800)
            rButton.place(x= 800, y=800)
            picsRemaining.destroy()
            self.photoCounter -= 1


        def restart():
            self.aiArtwork.place(x=10000, y=10000)
            subtitle5.place(x=10000, y=10000)
            prButton.place(x=10000, y=10000)
            rButton.place(x=10000, y=10000)
            mainEngine.screen(self)

        def printOut():
            self.prnt.printOut(self.AI.counter)

        mainloop() ##PUT THIS AT THE END OF EVERYTHING

#This is what Generates the picture, and can be used as a test prompt via code (No gui needed).
#AI.finalPromptGenerator(["A", "High Quality Well Drawn Anime", "with", "and"], "Waifu", "With Pink Hair", "Holding a Cake")



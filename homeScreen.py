from tkinter import *
import tkinter as tk
import matplotlib
from tkcalendar import Calendar
import NLP

'''def homeScreen():
    window = Tk()
    window.title("HackerTracker")
    window.geometry('1000x400')
    lbl = Label(window, text="Welcome to HackerTracker!", font=("Arial Bold", 50))
    lbl.grid(column=0, row=0)
    lbl.place(relx=.5, rely=.5, anchor="c")
    btn = Button(window, text="Click here to start!", bg="blue")
    btn.grid(column=0, row=1)
    btn.place(relx=.5, rely=.65, anchor="c")
    window.mainloop()'''


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

#home page
class HomePage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs, bg="black")
        lbl = Label(self, text="Welcome to HackerTracker!", font=("Comic Sans MS", 50, 'bold'), bg="black", fg="SpringGreen2")
        lbl.place(relx=0.5, rely=0.5, anchor ="c")

#Second page asking for date
class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs, bg="black")
        lbl = Label(self, text="Please select today's date:  ",font=("Comic Sans MS", 40, 'bold'), bg="black", fg='SpringGreen2')
        lbl.place(relx=.5, rely=.05, anchor="c")

        #cal = Calendar(self, selectmode="day", year=2021, month=6, day=21, selectforeground='pink', foreground='yellow', highlightcolor='pink', normalforeground='orange', font=("Comic Sans MS", 20))
        cal = Calendar(self, background="black", disabledbackground="black", bordercolor="black",
                 headersbackground="black", normalbackground="black", foreground='white',
                 normalforeground='white', headersforeground='white', font=("Comic Sans MS", 20))
        cal.place(relx=.5, rely=.5, anchor="c")
        self.calendar = cal

        #create spins to add date
        #month = Label(self, text="Month")
        #month.grid(column=0, row=1, sticky="")
        #spin = Spinbox(self, from_=1, to=12, width=5, format="%02.0f")
        #spin.grid(column=0, row=2, sticky="")

        #day = Label(self, text="Day")
        #day.grid(column=1, row=1, sticky="")
        #spin2 = Spinbox(self, from_=1, to=30, width=5, format="%02.0f")
        #spin2.grid(column=1, row=2, sticky="")

        #year = Label(self, text="Year")
        #year.grid(column=2, row=1, sticky="")
        #spin3 = Spinbox(self, from_=0000, to=9999, width=5, format="%04.0f")
        #spin3.grid(column=2, row=2, sticky="")        # spin3.grid(column=2, row=2, sticky="")

#Third page asking to select options
class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs, bg="black")                            #copy these 3 lines to make a new class
        self.date = ""
        #make checkbutton for multiselect
        lbl = Label(self, text="Select desired categories", font=("Comic Sans MS", 40, 'bold'), bg="black", fg='SpringGreen2')
        lbl.place(relx=.5, rely=.05, anchor="c")

        self.sleep_state = IntVar()
        sleep = Checkbutton(self, text="Sleep", variable=self.sleep_state, font=("Comic Sans MS", 20), bg="black",
                            fg='white', highlightbackground="SpringGreen2")
        sleep.place(relx=.28, rely=.2, anchor="c")

        self.exercise_state = IntVar()
        exercise = Checkbutton(self, text="Exercise", variable=self.exercise_state, font=("Comic Sans MS", 20), bg="black",
                               fg='white', highlightbackground="SpringGreen2")
        exercise.place(relx=.28, rely=.3, anchor="c")

        self.caffeine_state = IntVar()
        caffeine = Checkbutton(self, text="Caffeine", variable=self.caffeine_state, font=("Comic Sans MS", 20), bg="black",
                               fg='white', highlightbackground="SpringGreen2")
        caffeine.place(relx=.28, rely=.4, anchor="c")

        self.mood_state = IntVar()
        mood = Checkbutton(self, text="Mood", variable=self.mood_state, font=("Comic Sans MS", 20), bg="black", fg='white',
                           highlightbackground="SpringGreen2")
        mood.place(relx=.28, rely=.5, anchor="c")

        self.confidence_state = IntVar()
        confidence = Checkbutton(self, text="Confidence", variable=self.confidence_state, font=("Comic Sans MS", 20),
                                 bg="black", fg='white', highlightbackground="SpringGreen2")
        confidence.place(relx=.48, rely=.2, anchor="c")

        self.screenTime_state = IntVar()
        screenTime = Checkbutton(self, text="Screen Time", variable=self.screenTime_state, font=("Comic Sans MS", 20),
                                 bg="black", fg='white', highlightbackground="SpringGreen2")
        screenTime.place(relx=.48, rely=.3, anchor="c")

        self.socializing_state = IntVar()
        socializing = Checkbutton(self, text="Socializing", variable=self.socializing_state, font=("Comic Sans MS", 20),
                                  bg="black", fg='white', highlightbackground="SpringGreen2")
        socializing.place(relx=.48, rely=.4, anchor="c")

        self.productivity_state = IntVar()
        productivity = Checkbutton(self, text="Productivity", variable=self.productivity_state, font=("Comic Sans MS", 20),
                                   bg="black", fg='white', highlightbackground="SpringGreen2")
        productivity.place(relx=.48, rely=.5, anchor="c")

        self.hygiene_state = IntVar()
        hygiene = Checkbutton(self, text="Hygiene", variable=self.hygiene_state, font=("Comic Sans MS", 20), bg="black",
                              fg='white', highlightbackground="SpringGreen2")
        hygiene.place(relx=.68, rely=.2, anchor="c")

        self.categories = []

    def newCategories(self):
        self.categories = [self.sleep_state.get(), self.exercise_state.get(), self.caffeine_state.get(), self.mood_state.get(),
                      self.confidence_state.get(), self.screenTime_state.get(), self.socializing_state.get(), self.productivity_state.get(),
                      self.hygiene_state.get()]

    #https://likegeeks.com/python-gui-examples-tkinter-tutorial/

#Fourth Page prompting journaling input
class Page4(Page):
     def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs, bg="black")
        self.date = ""
        self.categories = []
        
        # choice_lbl = Label(self, text="Select Best Option", font=("Comic Sans MS", 40, 'bold'), bg="black", fg='SpringGreen2')
        # choice_lbl.place(relx=.5, rely=.05, anchor="c")

        # sleep
        sleep_label = Label(self, text="How many hours did you sleep last night?", font=("Comic Sans MS", 30, 'bold'),
                            bg="black", fg='white')
        # sleep_label.grid(row=0, column=0)
        sleepMenu = OptionMenu(self, StringVar(self), "0-3 hours", "3-5 hours", "6-8 hours", "9-11 hours", "11+ hours")
        # sleepMenu.grid(row=0, column=1)

        # exercise
        exercise_label = Label(self, text="How many hours did you exercise today?", font=("Comic Sans MS", 30, 'bold'),
                               bg="black", fg='white')
        # exercise_label.grid(row=1, column=0)
        exerciseMenu = OptionMenu(self, StringVar(self), "0-3 hours", "3-5 hours", "6-8 hours", "9-11 hours",
                                  "11+ hours")
        # exerciseMenu.grid(row=1, column=1)

        # caffeine
        caffeine_label = Label(self, text="How much caffeine did you have today?", font=("Comic Sans MS", 30, 'bold'),
                               bg="black", fg='white')
        # caffeine_label.grid(row=2, column=0)
        caffeineMenu = OptionMenu(self, StringVar(self), "0-100 mg", "101-200 mg", "201-300 mg", "301-400 mg",
                                  "400+ mg")
        # caffeineMenu.grid(row=2, column=1)

        # mood
        mood_label = Label(self, text="How would you describe your mood today?", font=("Comic Sans MS", 30, 'bold'),
                           bg="black", fg='white')
        # mood_label.grid(row=3, column=0)
        moodMenu = OptionMenu(self, StringVar(self), "Sad/Mad", "Tired", "Neutral", "Content", "Happy")
        # moodMenu.grid(row=3, column=1)

        # Confidence
        con_label = Label(self, text="How would you describe your confidence today, 5 being most confident?",
                          font=("Comic Sans MS", 30, 'bold'), bg="black", fg='white')
        # con_label.grid(row=4, column=0)
        conMenu = OptionMenu(self, StringVar(self), "1", "2", "3", "4", "5")
        # conMenu.grid(row=4, column=1)

        # screen time
        screen_label = Label(self, text="How many hours of screen time did you have today?",
                             font=("Comic Sans MS", 30, 'bold'), bg="black", fg='white')
        # screen_label.grid(row=5, column=0)
        screenMenu = OptionMenu(self, StringVar(self), "0-3", "3-6", "6-9", "9-11", "11+")
        # screenMenu.grid(row=5, column=1)

        # socializing
        social_label = Label(self, text="How many hours did you spend socializing today?",
                             font=("Comic Sans MS", 30, 'bold'), bg="black", fg='white')
        # social_label.grid(row=6, column=0)
        socialMenu = OptionMenu(self, StringVar(self), "0-3", "3-6", "6-9", "9-11", "11+")
        # socialMenu.grid(row=6, column=1)

        # productivity
        prod_label = Label(self, text="How would you describe your productivity today, 5 being most productive?",
                           font=("Comic Sans MS", 30, 'bold'), bg="black", fg='white')
        # prod_label.grid(row=7, column=0)
        prodMenu = OptionMenu(self, StringVar(self), "1", "2", "3", "4", "5")
        # prodMenu.grid(row=7, column=1)

        # hygiene
        hy_label = Label(self, text="How would you rate your hygeine today, 5 being best?",
                         font=("Comic Sans MS", 30, 'bold'), bg="black", fg='white')
        # hy_label.grid(row=8, column=0)
        hyMenu = OptionMenu(self, StringVar(self), "1", "2", "3", "4", "5")
        # hyMenu.grid(row=8, column=1)

        self.labelList = [sleep_label, exercise_label, caffeine_label, mood_label, con_label, screen_label, social_label, prod_label, hy_label]
        self.menuList = [sleepMenu, exerciseMenu, caffeineMenu, moodMenu, conMenu, screenMenu, socialMenu, prodMenu, hyMenu]

     def updatedCategories(self):
        iterr = 0
        counter = 0
        for i in self.categories:
            if i == 1:
                self.labelList[iterr].grid(row=counter, column=0)
                self.menuList[iterr].grid(row=counter, column=1)
                counter += 1
            iterr += 1

     def destroyGrid(self):
         for label in self.grid_slaves():
             label.grid_forget()

#Page 5 with plots
class Page5(Page):
     def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs, bg="black")
        self.date = ""
        self.categories = []
        graph_lab = Label(self, text="Plots",  font=("Comic Sans MS", 40, 'bold'), bg="black", fg='SpringGreen2')
        graph_lab.place(relx=.5, rely=.05, anchor="c")

#NLP prompting user for input
class Page6(Page):


    def __init__(self, *args, **kwargs):
        self.nlpList = []
        texts = ""
        Page.__init__(self, *args, **kwargs, bg="black")
        graph_lab = Label(self, text="How are you feeling today:", font=("Comic Sans MS", 40, 'bold'), bg="black", fg='SpringGreen2')
        graph_lab.pack(pady=10, padx=10)
        E1 = Entry(self, textvariable=texts)
        E1.pack(side=TOP)
        blueButton = Button(self, text="Submit", fg="blue", command=lambda : NLP.nlpFunc(str(E1.get())))
        counter = 0
        
        self.nlpList = NLP.nlpFunc(str(E1.get()))
        for i in self.nlpList:
            iterr = 0
            counter = 0
            for i in self.categories:
                if i == 1:
                    self.nlpList[iterr].grid(row=counter, column=0)
                counter += 1
            iterr += 1
        
        blueButton.pack(side=TOP)

        
class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        #objects for each of the screens
        home = HomePage(self)
        date = Page2(self)
        options = Page3(self)
        choices = Page4(self)
        plots = Page5(self)
        nlp = Page6(self)

        #global variables
        global screens
        screens = [home, date, options, choices, plots, nlp]
        global num
        num = 0

        #create menu
        menu = Menu(window)
        new_item = Menu(menu)
        new_item.add_command(label='Next', command=lambda: self.goNext(num))
        new_item.add_command(label='Back', command=lambda: self.goBack(num))
        new_item.add_command(label='Exit', command=lambda: self.close())
        menu.add_cascade(label='File', menu=new_item)
        window.config(menu=menu)

        #make frames
        button_frame = tk.Frame(self, bg="gray")
        container = tk.Frame(self, bg="black")
        button_frame.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)
        #create next button
        next_btn = Button(button_frame, text="Next", bg="blue", command=lambda: self.goNext(num))
        next_btn.pack(side="right")
        #create back button
        back_btn = Button(button_frame, text="Back", bg="blue", command=lambda: self.goBack(num))
        back_btn.pack(side="left")
        #place screens into a container
        home.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        date.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        options.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        choices.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        plots.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        nlp.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        screens[0].show()

    #moves to next screen
    def goNext(self, index):
        if index < len(screens)-1:
            global num
            if num == 1:
                screens[num + 1].date = screens[num].calendar.get_date()
            elif num == 2:
                screens[num + 1].date = screens[num].date
                screens[num].newCategories()
                screens[num + 1].categories = screens[num].categories
                print(screens[num + 1].categories)
                screens[num + 1].updatedCategories()
            elif num >= 2:
                screens[num + 1].date = screens[num].date
                screens[num + 1].categories = screens[num].categories

            num += 1
            screens[index+1].show()

    #move to prev screen
    def goBack(self, index):
        if index > 0:
            global num
            if num == 3:
                screens[num].destroyGrid()
            num -= 1
            screens[index-1].show()

    #exits GUI
    def close(self):
        window.destroy()
        exit()


if __name__ == "__main__":
    window = Tk()
    main = MainView(window)
    main.pack(side="top", fill="both", expand=True)
    window.title("HackerTracker")
    window.geometry('1200x600')
    window.mainloop()

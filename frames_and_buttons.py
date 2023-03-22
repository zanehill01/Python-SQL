
import tkinter
import tkinter.messagebox


class myGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        # create window

        self.main_window.geometry('500x200')
        self.main_window.title('Frames and Buttons')

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # create labels and pack

        self.label1 = tkinter.Label(self.top_frame, text='JJ')
        self.label2 = tkinter.Label(self.top_frame, text='Brendon')
        self.label3 = tkinter.Label(self.top_frame, text='Zane')

        self.label1.pack(side='left')
        self.label2.pack(side='left')
        self.label3.pack(side='left')

        self.label4 = tkinter.Label(self.bottom_frame, text='Zane')
        self.label5 = tkinter.Label(self.bottom_frame, text='Zane')
        self.label6 = tkinter.Label(self.bottom_frame, text='Zane')

        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

        # create buttons and pack

        self.my_button = tkinter.Button(
            self.main_window, text='click me', command=self.do_something)
        self.quit_button = tkinter.Button(
            self.main_window, text='Quit', command=self.main_window.destroy)

        #

        self.my_button.pack(side='left')
        self.quit_button.pack(side='right')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo(
            'Response', 'Thanks for clicking the button')


myinstance = myGUI()

print('Moving on...')

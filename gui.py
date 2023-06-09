import tkinter
import tkinter.messagebox
import pyodbc


class SQLGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        # create window

        self.main_window.geometry('275x75')
        self.main_window.title('SQL Server Login')

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.last_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame, text='Login:')
        self.entry1 = tkinter.Entry(self.top_frame, width=30)

        self.label2 = tkinter.Label(self.bottom_frame, text='Password:')
        self.entry2 = tkinter.Entry(self.bottom_frame, width=30, show='*')

        self.loginbutton = tkinter.Button(
            self.last_frame, text='Login', command=self.do_something)

        #

        self.top_frame.pack()
        self.bottom_frame.pack()
        self.last_frame.pack()

        self.label1.pack(side='left')
        self.entry1.pack(side='left')

        self.label2.pack(side='left')
        self.entry2.pack(side='left')

        self.loginbutton.pack()

        #

        tkinter.mainloop()

    def do_something(self):

        login = self.entry1.get()
        pw = self.entry2.get()

        self.main_window.destroy()

        login = 'zane_hill1'
        pw = 'MIS4322student'

        preList = {}
        courseList = []
        cn_str = (

        'Driver={SQL Server Native Client 11.0};'
        'Server=MIS-SQLJB;'
        'Database=School;'
        'UID='+login+';'
        'PWD='+pw+';'

        )

        # connect to server

        cn = pyodbc.connect(cn_str)

        cursor = cn.cursor()
        cursor.execute('select name, budget From school.dbo.Department')

        data = cursor.fetchall()

        for row in data:

            courseID = row[0]
            title = row[1]
            credit = row[2]
            deptID = row[3]

            preList = {'CourseID':courseID, 'Title':title, 'Credit':credit, 'DeptID':deptID}

            courseList.append(preList)

            print(preList)

        a = int(input('CourseID to Search: '))

        for dict in courseList:
            if dict['CourseID'] == a:
                print(f"Title of the course:{dict['Title']}")
                print(f"Credits for the course:{dict['Credit']}")
                print(f"DeptID of the course:{dict['DeptID']}")

        for row in cursor.fetchall():
            print(row)

myinstance = SQLGUI()
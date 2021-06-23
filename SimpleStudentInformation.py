from tkinter import *
from tkinter import messagebox, ttk
import csv

class Student:

    def __init__(self, root, filename):
        self.root = root
        self.root.title("Student Information System")
        self.root.geometry("1400x700+0+0",)
        self.data = []
        self.filename = filename
        self.read()

        title = Label(self.root, text="Simple Student Information System", bd=0, relief=GROOVE,
                      font=("Calibri", 60, "bold italic"), fg="Black")
        title.pack(side=TOP)

        # Functions
        def viewList():
            try:
                Student_table.delete(*Student_table.get_children())
                with open("SSIS.csv", "r") as file:
                    listStudents = csv.reader(file)
                    next(listStudents, None)
                    counter = 0
                    for student in listStudents:
                        Student_table.insert(parent='', index='end', iid=counter,
                                    values=(student[0], student[1], student[2], student[3], student[4]))
                        counter += 1
            except IndexError:
                pass

        def add():
            if txt_id.get() == "":
                messagebox.showerror("Error", "The entries are not complete")
                return
            x = [txt_id.get(), txt_name.get(), txt_course.get(), combo_year.get(), combo_gender.get()]
            self.create(x)
            viewList()
            clear()

        def update():
            if txt_id.get() == "":
                messagebox.showerror("Error", "The entries are not complete")
                return
            if self.search_index(txt_id.get()) == None:
                messagebox.showerror("Update error", "The Student does not exist.")
                return

            self.update([txt_id.get(), txt_name.get(), txt_course.get(), combo_year.get(), combo_gender.get()])
            viewList()
            clear()

        def delete():
            if txt_id.get() == "":
                messagebox.showerror("Error", "The ID number entry is empty.")
                return
            if self.search_index(txt_id.get()) == None:
                messagebox.showerror("Update error", "The Student does not exist.")
                return

            self.delete(txt_id.get())
            viewList()
            clear()

        def clear():
            txt_id.delete(0, END)
            txt_name.delete(0, END)
            txt_course.delete(0, END)
            combo_year.current(0)
            combo_gender.current(0)

        def search():
            x = self.search_index(txt_search.get())
            if x is None:
                messagebox.showerror("Error", "Student not found.")
                return

            student = self.data[x]
            Student_table.delete(*Student_table.get_children())
            Student_table.insert(parent='', index='end',
                                 values=(student[0], student[1], student[2], student[3], student[4]))

        #Manage Frame

        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="Red1")
        Manage_Frame.place(x=10, y=95, width=500, height=555)

        m_title = Label(Manage_Frame, text="Students Information", bg="Red1", fg="black",
                        font=("Calibri", 20, "bold italic"))
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_id = Label(Manage_Frame, text="I.D No.", bg="Red1", fg="black", font=("Calibri", 20,"italic" ))
        lbl_id.grid(row=1, column=0, pady=10, padx=15, sticky="w")

        txt_id = Entry(Manage_Frame, font=("Calibri", 16, ), bd=1, relief=GROOVE)
        txt_id.grid(row=1, column=2, pady=10, padx=20, sticky="w")

        lbl_course = Label(Manage_Frame, text="Course", bg="Red1", fg="black", font=("Calibri", 20, "italic"))
        lbl_course.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_course = Entry(Manage_Frame, font=("Calibri", 16, "bold"), bd=1, relief=GROOVE)
        txt_course.grid(row=2, column=2, pady=10, padx=20, sticky="w")

        lbl_name = Label(Manage_Frame, text="Name", bg="Red1", fg="black", font=("Calibri",20,"italic" ))
        lbl_name.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_name = Entry(Manage_Frame, font=("Calibri", 16, ), bd=1, relief=GROOVE)
        txt_name.grid(row=3, column=2, pady=10, padx=20, sticky="w")

        lbl_year = Label(Manage_Frame, text="Year Level", bg="Red1", fg="black", font=("Calibri", 20,"italic" ))
        lbl_year.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_year = ttk.Combobox(Manage_Frame,width=29, font=("Calibri", 10, "bold"), state='readonly')
        combo_year['values'] = ("", "1st Year", "2nd Year", "3rd Year", "4th Year")
        combo_year.grid(row=4, column=2, pady=10, padx=20)
        combo_year.current(0)

        lbl_gender = Label(Manage_Frame, text="Gender", bg="Red1", fg="black", font=("Calibri", 20, "italic"))
        lbl_gender.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        combo_gender = ttk.Combobox(Manage_Frame,width=29, font=("Calibri", 10, "bold"), state='readonly')
        combo_gender['values'] = ("", "Male", "Female", "Other")
        combo_gender.grid(row=5, column=2, pady=10, padx=20)
        combo_gender.current(0)

        #Button Frame

        btn_Frame = Frame(Manage_Frame, bd=5, relief=RIDGE, bg="Red1")
        btn_Frame.place(x=22, y=385, width=450 , height=135)

        Addbtn = Button(btn_Frame, text="Add", bg="Black", fg="white", width=27,height=2, command=add).grid(row=0, column=0, padx=10,
                                                                                       pady=10) 
        updatebtn = Button(btn_Frame, text="Update", bg="Black", fg="white", width=27,height=2, command= update).grid(row=1, column=0, padx=10,
                                                                                             pady=10)
        deletebtn = Button(btn_Frame, text="Delete", bg="black", fg="white", width=27,height=2, command=delete).grid(row=1, column=1, padx=10,
                                                                                             pady=10)
        Clearbtn = Button(btn_Frame, text="Clear", bg="Black", fg="white"
                                                                  "", width=27,height=2, command=clear).grid(row=0, column=1, padx=10,
                                                                                           pady=10)

        #Detail Frame

        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="Red1")
        Detail_Frame.place(x=520, y=95, width=795, height=555)


        txt_search = Entry(Detail_Frame, width=30, font=("Calibri", 15, "italic"), bd=2, relief=GROOVE)
        txt_search.grid(row=0, column=3, pady=10, padx=20, sticky="w")

        searchbtn = Button(Detail_Frame, text="Search", bg="black", fg="white", width=20, pady=5, command= search).grid(row=0, column=4,
                                                                                                        padx=10,
                                                                                                        pady=10)


        #Table Frame

        Table_Frame = Frame(Detail_Frame, bd=0, relief=RIDGE, bg="Red1")
        Table_Frame.place(x=20, y=65, width=740, height=440)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        Student_table = ttk.Treeview(Table_Frame, columns=("i.d no.", "name", "course", "year level", "gender"),
                                     xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=Student_table.xview)
        scroll_y.config(command=Student_table.yview)
        Student_table.heading("i.d no.", text="I.D No.")
        Student_table.heading("name", text="Name")
        Student_table.heading("course", text="Course")
        Student_table.heading("year level", text="Year Level")
        Student_table.heading("gender", text="Gender")
        Student_table['show'] = 'headings'
        Student_table.column("i.d no.", width=100)
        Student_table.column("name", width=100)
        Student_table.column("course", width=100)
        Student_table.column("year level", width=100)
        Student_table.column("gender", width=150)
        Student_table.pack(fill=BOTH, expand=1)

        # Display CSV
        viewList()

    def read(self):
        with open("SSIS.csv", newline="") as file:
            reader = csv.reader(file)
            data = list(reader)
            self.data = data

    def create(self, new):
        with open("SSIS.csv","w", newline="") as file:
            writer = csv.writer(file)
            for i in self.data:
                writer.writerow(i)
            writer.writerow(new)
        self.data.append(new)

    def search_index(self, id):
        x = [id in student for student in self.data]
        index = [i for i, y in enumerate(x) if y]
        if sum(x) > 1:
            pass
        elif sum(x)==1:
            return index[0]
        else:
            return None

    def update(self, update):
        index = self.search_index(update[0])
        self.data[index][0] = update[0]
        self.data[index][1] = update[1]
        self.data[index][2] = update[2]
        self.data[index][3] = update[3]
        self.data[index][4] = update[4]

        with open("SSIS.csv","w", newline="") as file:
            writer = csv.writer(file)
            for i in self.data:
                writer.writerow(i)

    def delete(self, id):
        index = self.search_index(id)
        del self.data[index]

        with open("SSIS.csv","w", newline="") as file:
            writer = csv.writer(file)
            for i in self.data:
                writer.writerow(i)


root = Tk()
ob = Student(root, "C:/Users/Rangaig/PycharmProjects\StudentIS/SSIS.csv")
root.mainloop()

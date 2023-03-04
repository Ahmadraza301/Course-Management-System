from tkinter import*
from PIL import Image, ImageTk #pip Install  
from course import courseclass
from student import StudentClass

class CMS:
    def __init__(self, root):
        self.root=root
        self.root.title("Course Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#ADEAEA")
        #=======icons=========
        self.logo_dash=ImageTk.PhotoImage(file="images/logo_p.png")
        #=======title=========
        title=Label(self.root, text="Course Management system", padx=10, compound=LEFT, image=self.logo_dash, font=("goudy old style",20, "bold"),bg="#033054", fg="white").place(x=0, y=0, relwidth=1, height=50)
        #=========Menu=========
        M_Frame=LabelFrame(self.root, text="Menus", font=("times new roman", 15), bg="white")
        M_Frame.place(x=10, y=70, width=250, height=500)
        
        btn_course=Button(M_Frame, text="Courses", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_course).place(x=20, y=5, width=200, height=40)
        btn_student=Button(M_Frame, text="Student", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_student).place(x=20, y=90, width=200, height=40)
        btn_result=Button(M_Frame, text="Results", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2").place(x=20, y=170, width=200, height=40)
        btn_view=Button(M_Frame, text="View Student Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2").place(x=20, y=260, width=200, height=40)
        btn_logout=Button(M_Frame, text="Logout", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2").place(x=20, y=340, width=200, height=40)
        btn_exit=Button(M_Frame, text="Exit", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2").place(x=20, y=420, width=200, height=40)
        # abc = Button(M_Frame,text="Raza",font=('Times New Roman',15,"italic"),fg='white').place(x=20,y=500,width=200,height=40)
        #============content_window==========
        self.bg_img=Image.open("images/bg.png")
        self.bg_img=self.bg_img.resize((950, 500), Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        
        self.lbl_bg=Label(self.root, image=self.bg_img).place(x=280, y=100, width=920, height=420)
        
        #=============Update_details=======
        self.lbl_bg=Label(self.root, image=self.bg_img).place(x=300, y=180, width=920, height=350)
        self.lbl_course=Label(self.root, text="Total Courses\n[0]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#033054", fg="white")
        self.lbl_course.place(x=950, y=100, width=300, height=100)
        
        self.lbl_student=Label(self.root, text="Total Student\n[0]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#033054", fg="white")
        self.lbl_student.place(x=950, y=280, width=300, height=100)
        
        self.lbl_result=Label(self.root, text="Total Result\n[0]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#033054", fg="white")
        self.lbl_result.place(x=950, y=460, width=300, height=100)
        
        
        #=============footer=============
        
        footer=Label(self.root, text="Course Management system\nContact Us for any Technical Issue: 9876543210", font=("goudy old style",12),bg="#262626", fg="white").pack(side=BOTTOM, fill=X)
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=courseclass(self.new_win)
        
    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=StudentClass(self.new_win)
        
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=CMS(root)
    root.mainloop()        
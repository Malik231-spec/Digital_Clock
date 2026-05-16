
# Digital Clock


from tkinter import *
import datetime

def date_time():
    time =datetime.datetime.now()
    hr =time.strftime('%I')
    mi =time.strftime('%M')
    sec =time.strftime('%S')
    am =time.strftime('%p')
    date =time.strftime('%d')
    mon =time.strftime('%m')
    yr =time.strftime('%y')
    da =time.strftime('%a')

    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)
    lab_ap.config(text=am)
    lab_day.config(text=date)
    lab_month.config(text=mon)
    lab_yr.config(text=yr)
    lab_dnam.config(text=da)

    lab_hr.after(200,date_time)

clock = Tk()
clock.title("#\|/*\|/#  Digital Clock   #\|/*\|/#")
clock.iconbitmap("logo/Watch5.ico")
clock.geometry("640x500")
clock.config(bg="yellow")
clock.resizable(False, False)

lab_hr =Label(clock,text="00",font=("time new roman",40,"bold"),bg="red",fg="white")
lab_hr.place(x=40,y=40,height=110,width=100)

lab_hr1 =Label(clock,text="Hour",font=("time new roman",15,"bold"),bg="Yellow",fg="black")
lab_hr1.place(x=50,y=160,height=25,width=70)

lab_min =Label(clock,text="00",font=("time new roman",40,"bold"),bg="red",fg="white")
lab_min.place(x=190,y=40,height=110,width=100)

lab_min1 =Label(clock,text="Mins",font=("time new roman",15,"bold"),bg="Yellow",fg="black")
lab_min1.place(x=200,y=160,height=25,width=70)

lab_sec =Label(clock,text="00",font=("time new roman",40,"bold"),bg="red",fg="white")
lab_sec.place(x=340,y=40,height=110,width=100)

lab_sec1 =Label(clock,text="Sec",font=("time new roman",15,"bold"),bg="Yellow",fg="black")
lab_sec1.place(x=350,y=160,height=25,width=70)

lab_ap =Label(clock,text="00",font=("time new roman",40,"bold"),bg="red",fg="white")
lab_ap.place(x=490,y=40,height=110,width=100)

lab_ap1 =Label(clock,text="Am/Pm",font=("time new roman",15,"bold"),bg="Yellow",fg="black")
lab_ap1.place(x=500,y=160,height=25,width=70)

lab_day =Label(clock,text="00",font=("time new roman",40,"bold"),bg="red",fg="white")
lab_day.place(x=40,y=200,height=110,width=100)

lab_day1 =Label(clock,text="Date",font=("time new roman",15,"bold"),bg="Yellow",fg="black")
lab_day1.place(x=50,y=320,height=25,width=70)

lab_month =Label(clock,text="00",font=("time new roman",40,"bold"),bg="red",fg="white")
lab_month.place(x=190,y=200,height=110,width=100)

lab_month1 =Label(clock,text="Month",font=("time new roman",15,"bold"),bg="Yellow",fg="black")
lab_month1.place(x=200,y=320,height=25,width=70)

lab_yr =Label(clock,text="00",font=("time new roman",40,"bold"),bg="red",fg="white")
lab_yr.place(x=340,y=200,height=110,width=100)

lab_yr1 =Label(clock,text="Year",font=("time new roman",15,"bold"),bg="Yellow",fg="black")
lab_yr1.place(x=350,y=320,height=25,width=70)

lab_dnam =Label(clock,text="00",font=("time new roman",40,"bold"),bg="red",fg="white")
lab_dnam.place(x=490,y=200,height=110,width=100)

lab_dnam1 =Label(clock,text="Day",font=("time new roman",15,"bold"),bg="Yellow",fg="black")
lab_dnam1.place(x=500,y=320,height=25,width=70)

lab =Label(clock,text="Malik's Digital Clock",font=("comsecmes",20,"bold"),fg="Blue",bg="yellow")
lab.place(x=190,y=350,height=135,width=290)

date_time()

clock.mainloop()
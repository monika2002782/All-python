####Registration form

# from tkinter import*
# root=Tk()
# root.title("Registration Form")
# root.geometry("400x600")
# lbl=Label(root,text="Registration Form",width=20,font=("bold",22))
# lbl.place(relx=0.1,rely=0.1)
# lbl2=Label(root,text="Name",width=20,font=("arial",10))
# lbl2.place(relx=0.1,rely=0.2)
# entry1=Entry(root)
# entry1.place(relx=0.2,rely=0.2)
# lbl3=Label(root,text="Age",width=20,font=("bold",10))
# lbl3.place(relx=0.1,rely=0.3)
# entry2=Entry(root)
# entry2.place(relx=0.2,rely=0.3)
# lbl4=Label(root,text="DOB",width=20,font=("bold",10))
# lbl4.place(relx=0.1,rely=0.4)
# entry3=Entry(root)
# entry3.place(relx=0.2,rely=0.4)
# lbl5=Label(root,text="Email",width=20,font=("bold",10))
# lbl5.place(relx=0.1,rely=0.5)
# entry4=Entry(root)
# entry4.place(relx=0.2,rely=0.5)
# lbl6=Label(root,text="phone no",width=20,font=("bold",10))
# lbl6.place(relx=0.1,rely=0.6)
# entry5=Entry(root)
# entry5.place(relx=0.2,rely=0.6)
# lbl7=Label(root,text="address",width=20,font=("bold",10))
# lbl7.place(relx=0.1,rely=0.7)
# entry6=Entry(root)
# entry6.place(relx=0.2,rely=0.7)
# lbl8=Label(text="Gender")
# lbl8.place(relx=0.143,rely=0.8)
# var=IntVar()
# Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(relx=0.2,rely=0.8)
# Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(relx=0.266,rely=0.8)
# def data():
#    a=entry1.get()
#    b=entry2.get()
#    c=entry3.get()
#    d=entry4.get()
#    e=entry5.get()
#    f1=entry6.get()
#    gen=" "
#    if(var==1):
#       gen="male"
#    else:
#       gen="female"
#    f=open("std detail.txt","a")
#    f.write("\n"+a+" "+b+" "+c+" "+d+" "+e+" "+f1+" "+gen)
#    login()
# but=Button(root, text="Submit",width=20,activeforeground="blue",activebackground="violet",command=data).place(relx=0.3,rely=0.9)
# # but1=Button(root,text="login",width=20,activeforeground="blue",activebackground="violet",command=login).place(relx=0.3,rely=0.9)
# def login():
#     from tkinter import messagebox
#     root=Tk()
#     root.title("Login Form")
#     root.geometry("500x500")
#     l1=Label(root,text="Login Form",width=10,font=("bold",10))
#     l1.place(relx=0.1,rely=0.1)
#     l2=Label(root,text="Username",width=10,font=("bold",10))
#     l2.place(relx=0.1,rely=0.2)
#     e1=Entry(root)
#     e1.place(relx=0.2,rely=0.2)
#     l3=Label(root,text="Password",width=10,font=("bold",10))
#     l3.place(relx=0.1,rely=0.3)
#     e2=Entry(root)
#     e2.place(relx=0.2,rely=0.3)
#     def click():
#         a=e1.get()
#         b=e2.get()
#         f=open("std detail.txt","r")
#         data=f.read()
#         lines=data.split("\n")
#         for line in lines:
#             info=line.split()
#             if info[0]==a and info[1]==b:
#                 print("logged in")
#                 messagebox.showinfo("hello","login successfully")
#                 break
#         else:
#             print("nothing")
#             messagebox.showinfo("invalid","login Failed")
#     b1=Button(root,text="Submit",width=10,font=("bold",10),command=click).place(relx=0.1,rely=0.4)
#     root.mainloop()
# root.mainloop()







###login form


# from tkinter import*
# from tkinter import messagebox
# root=Tk()
# root.title("Login Form")
# root.geometry("500x500")
# l1=Label(root,text="Login Form",width=10,font=("bold",10))
# l1.place(relx=0.1,rely=0.1)
# l2=Label(root,text="Username",width=10,font=("bold",10))
# l2.place(relx=0.1,rely=0.2)
# e1=Entry(root)
# e1.place(relx=0.2,rely=0.2)
# l3=Label(root,text="Password",width=10,font=("bold",10))
# l3.place(relx=0.1,rely=0.3)
# e2=Entry(root)
# e2.place(relx=0.2,rely=0.3)
# def click():
#     a=e1.get()
#     b=e2.get()
#     f=open("std detail.txt","r")
#     data=f.read()
#     lines=data.split("\n")
#     for line in lines:
#         info=line.split()
#         if info[3]==a and info[4]==b:
#             print("logged in")
#             messagebox.showinfo("hello","login successfully")
#             break
#     else:
#         print("nothing")
#         messagebox.showinfo("invalid","login Failed")
# b1=Button(root,text="Submit",width=10,font=("bold",10),command=click).place(relx=0.1,rely=0.4)
# b2=Button(root,text="Cancel",width=10,font=("bold",10),command=click,).place(relx=0.2,rely=0.4)
# root.mainloop()




"""
f=open("st.txt","a")
f.write("\nname   \t pswd\n")
f.close()
 username="name"
password="pswd"
f=open("st.txt","r")
data=f.read()
lines=data.split("\n")
for line in lines:
    info=line.split()
    if info[0]==username and info[1]==password:
        print("logged in")
        break
else:
    print("nothing")"""


# from tkinter import*
# def check():
#     if(n.get()>0):
#         print("hi")
#     elif(n1.get()>2):
#         print("hlo")
#     else:
#         print("hai")
        
# f=open("std detail.txt","r")
# data=f.read()
# r=Tk()
# n=IntVar()
# c=Checkbutton(r,text="hi",variable=n,command=check).pack()
# n1=IntVar()
# c1=Checkbutton(r,text="hlo",variable=n1,command=check).pack()
# n2=IntVar()
# c2=Checkbutton(r,text="hai",variable=n2,command=check).pack()
# f=open("std detail.txt","r")
# print(f.read())
# btn=Button(r,text="enter",command=check).pack()

# r.mainloop()


    

# from tkinter import*
# def sel():
#     if var.get()==1:
#         print("male")
#     elif var.get()==2:
#         print("female")
#     else:
#         print("other")
#     select="you selected the option"+str(var.get())
#     Label.config(text=select)
# r=Tk()
# var=IntVar()
# r1=Radiobutton(r,text="option1",variable=var,value=1,command=sel)
# r1.pack(anchor=W)
# r2=Radiobutton(r,text="option2",variable=var,value=2,command=sel)
# r2.pack(anchor=W)
# r3=Radiobutton(r,text="option3",variable=var,value=3,command=sel)
# r3.pack(anchor=W)
# Label=Label(r)
# Label.pack()
# r.mainloop()


# from tkinter import*
# from tkinter import ttk
# r=Tk()
# r.title("Registration form")
# r.geometry("300x300")
# l=Label(r,text="GENDER",width=10,font=("bold",15))
# l.place(relx=0.1,rely=0.1)
# var=IntVar()
# radio=Radiobutton(r,text="male",variable=var,value=1).place(relx=0.2,rely=0.1)
# radio1=Radiobutton(r,text="female",variable=var,value=2).place(relx=0.254,rely=0.1)
# radio2=Radiobutton(r,text="other",variable=var,value=3).place(relx=0.333,rely=0.1)
# l1=Label(r,text="COURSE",width=10,font=("bold",15))
# l1.place(relx=0.1,rely=0.2)
# var=IntVar()
# c=Checkbutton(r,text="b.sc(cs)",variable=var).place(relx=0.2,rely=0.2)
# var1=IntVar()
# c1=Checkbutton(r,text="b.sc(IT)",variable=var1).place(relx=0.2,rely=0.3)
# var2=IntVar()
# c2=Checkbutton(r,text="b.sc(BCA)",variable=var2).place(relx=0.2,rely=0.4)
# l2=Label(r,text="LANGUAGE",width=10,font=("bold",15))
# l2.place(relx=0.1,rely=0.5)
# combo=ttk.Combobox(r,values=["python","java","c","c++","database"]).place(relx=0.2,rely=0.5)
# b=Button(r,text="submit",bg="violet",fg="green").place(relx=0.2,rely=0.6)
# r.mainloop()

# from tkinter import*
# r=Tk()
# r.title("Bank Application")
# r.geometry("400x400")
# l=Label(r,text="CUSTOMER REGISTRATION",width=30,font=("bold",10),bg="violet",fg="blue")
# l.place(relx=0.1,rely=0.1)
# l1=Label(r,text="NAME",width=10,font=("bold",10),bg="red",fg="white")
# l1.place(relx=0.1,rely=0.2)
# e=Entry(r)
# e.place(relx=0.2,rely=0.2)
# l2=Label(r,text="AADHAR NO",width=10,font=("bold",10),bg="red",fg="white")
# l2.place(relx=0.1,rely=0.3)
# e1=Entry(r)
# e1.place(relx=0.2,rely=0.3)
# l3=Label(r,text="PAN CARD",width=10,font=("bold",10),bg="red",fg="white")
# l3.place(relx=0.1,rely=0.4)
# e2=Entry(r)
# e2.place(relx=0.2,rely=0.4)
# l4=Label(r,text="PHO NO",width=10,font=("bold",10),bg="red",fg="white")
# l4.place(relx=0.1,rely=0.5)
# e3=Entry(r)
# e3.place(relx=0.2,rely=0.5)
# b=Button(r,text="Register",width=10,font=("bold",10),bg="blue",fg="black").place(relx=0.2,rely=0.6)
# r.mainloop()



###speech recognition

# from tkinter import font
# import webbrowser as wb
# # import speech_recognition as sr
# # import pyttsx3

# def main1():
#      r=sr.Recognizer()
#      with sr.Microphone() as source:
#         print("say something....")
#         audio=r.listen(source)
#      try:
#       print("Recognizing Now...")
#       text=str(r.recognize_google(audio))
#       label_font = font.Font(weight="bold",family='Times New Roman',size=10)
#       Label(r1,text=text,font=label_font).place(relx=0.5,rely=0.35)
#      except Exception as e:
#         print("Error :"+str(e))

# def main2():
#     r=sr.Recognizer()
#     url="https://www.google.com/search?q="
#     with sr.Microphone() as source:
#         print("speak....., It is the Google Search..., what do you want to Search..")
#         audio=r.listen(source)
#         try:
#             get=r.recognize_google(audio)
#             print(get)
#             label_font = font.Font(weight="bold",family='Times New Roman',size=10)
#             Label(r1,text=get,font=label_font).place(relx=0.5,rely=0.45)
#             wb.get().open_new(url+get)
#         except sr.UnknownValueError:
#             print("error")
#         except sr.RequestError as e:
#             print('failed'.format(e))
#         except:
#             print("Microphone not detected")


# def main3():
#     r=sr.Recognizer()
#     url="https://www.youtube.com/results?search_query="
#     with sr.Microphone() as source:
#         print("speak....., It is the Youtube Search..., what do you want to Search..")
#         audio=r.listen(source)
#         try:
#             get=r.recognize_google(audio)
#             print(get)
#             label_font = font.Font(weight="bold",family='Times New Roman',size=10)
#             Label(r1,text=get,font=label_font).place(relx=0.5,rely=0.55)
#             wb.get().open_new(url+get)
#         except sr.UnknownValueError:
#             print("error")
#         except sr.RequestError as e:
#             print('failed'.format(e))
#         except:
#             print("Microphone not detected")

# def main4():
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 50)
#     engine.setProperty('volume',1.0) #o to 1
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', voices[1].id)
#     engine.say(a1.get("1.0",END))
#     engine.runAndWait()
#     engine.stop()
# #end


# from tkinter import *
# r1=Tk()
# r1.geometry("600x400")
# label_font = font.Font(weight="bold",family='Helvetica',size=30)
# l1=Label(r1,text="Speech Recognition",font=label_font, bg='#0052cc', fg='#ffffff')
# l1.place(anchor="center",relx=0.5,rely=0.1)

# label_font = font.Font(weight="bold",family='Times New Roman',size=20)
# l2=Label(r1,text="This is Example of Speech Recognition and GUI",font=label_font, bg='red', fg='#ffffff')
# l2.place(anchor="center",relx=0.5,rely=0.25)

# label_font = font.Font(weight="bold",family='Times New Roman',size=10)
# b=Button(r1,text="It's Just a print what you Say",command=lambda:main1(),font=label_font)
# b.place(relx=0.1,rely=0.35)

# label_font = font.Font(weight="bold",family='Times New Roman',size=10)
# b=Button(r1,text="It's Google Search what you Say",command=lambda:main2(),font=label_font)
# b.place(relx=0.1,rely=0.45)

# label_font = font.Font(weight="bold",family='Times New Roman',size=10)
# b=Button(r1,text="It's Youtube Search what you Say",command=lambda:main3(),font=label_font)
# b.place(relx=0.1,rely=0.55)

# a1 = Text(r1,height=2, width=30)
# a1.place(relx=0.1,rely=0.65)

# label_font = font.Font(weight="bold",family='Times New Roman',size=10)
# b=Button(r1,text="Text to Speak",command=lambda:main4(),font=label_font)
# b.place(relx=0.55,rely=0.65)



# r1.mainloop()
















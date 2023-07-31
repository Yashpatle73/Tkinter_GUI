from tkinter import  *
from tkinter import messagebox
from PIL import ImageTk, Image

def user():
    email=entry.get()
    password=pass_entry.get()

    if email=='yashpatle@gamil' and password=='1234':
        messagebox.showinfo('Login Sucsessfull')

    else:
        messagebox.showinfo('please enter correct Password')

         


root=Tk()
root.title('flipCart Login Form ')
root.iconbitmap('favicon.ico')
root.geometry('350x500')
root.configure(background='#0096DC')
img=Image.open(('images.jpg'))
resized_img=img.resize((50,50))
img = ImageTk.PhotoImage(resized_img)
img_label=Label(root,image=img)
img_label.pack(pady=(10,10))


text_label =Label(root,text='Flipcart',fg='white',bg='#0096DC')
text_label.pack()
text_label.config(font=('Robotic',24))

email_label=Label(root,text='Enter Your Email',fg='white',bg='#0096DC')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana',12))

entry=Entry(root,width=50)
entry.pack(ipady=6,pady=(1,15))


pass_label=Label(root,text='Enter Your Password',fg='White',bg='#0096DC')
pass_label.pack(pady=(20,5))
pass_label.config(font=('verdana',12))

pass_entry=Entry(root,width=50)
pass_entry.pack(ipady=6,pady=(1,15))


login_bnt=Button(root,text='Login here',fg='White',bg='black',height=2,width=20,command=user)
login_bnt.pack(pady=(10,20))
login_bnt.config(font=('verdana',10))





root.mainloop()
from twilio.rest import Client
import random
from tkinter import *
from tkinter import messagebox


class otp_verifier(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x550")
        self.resizable(True, True)
        self.n = random.randint(1000, 9999)
        self.client = Client("AC343e7570357ba769847f695f2c89d63a", "a5c5706200923411b3c6bf38c828b277")
        self.client.messages.create(to=["+919833xxxxxx"],
                                    from_="+19705985647",
                                    body=self.n)

    def Labels(self):
        self.c = Canvas(self, bg="white", width=400, height=280)
        self.c.place(x=100, y=60)

        self.Login_Title = Label(self, text="OTP Verification", font="bold,72", bg="yellow")
        self.Login_Title.place(x=230, y=90)

        self.Resend = Label(self, text="Press Resend OTP if you didn't receive an OTP", font="bold,72", )
        self.Resend.place(x=200, y=3200)

    def clear_text(self):
        self.User_Name.delete(1.0, END)

    def Entry(self):
        self.User_Name = Text(self, borderwidth=2, wrap="word", width=29, height=2)
        self.User_Name.place(x=190, y=150)

    def Buttons(self):
        self.btn2 = Button(self, text='RESEND OTP', bd=5,
                           command=lambda: [self.resendOTP(), self.clear_text(), update_time(20), self.callback()],
                           border=0, background='#25a5be', height=3, width=35)
        self.btn2.place(x=185, y=400)

        self.btn3 = Button(self, text='Submit', bd=5, command=self.checkOTP, border=0, background='#25a5be', height=3,
                           width=35)
        self.btn3.place(x=185, y=240)

    def callback(self):
        messagebox.showinfo("Resend OTP", "Your new OTP is sent on your SMS")

    def checkOTP(self):
        try:
            self.userInput = int(self.User_Name.get(1.0, "end-1c"))

            if self.userInput == self.n:
                messagebox.showinfo("showinfo", "Login Success")
                self.n = "done"
            elif self.n == "done":
                messagebox.showinfo("showinfo", "Already Login")
            else:
                messagebox.showinfo("showinfo", "Wrong OTP")
        except:
            messagebox.showinfo("showinfo", "Invalid OTP")

    def resendOTP(self):
        self.n = random.randint(1000, 9999)
        self.client = Client("AC343e7570357ba769847f695f2c89d63a", "a5c5706200923411b3c6bf38c828b277")
        self.client.messages.create(to=["+919833040673"],
                                    from_="+19705985647",
                                    body=self.n)


def update_time(t):
    l = Label(font=('calibri', 50, 'bold'), background='white', foreground='black')
    l.place(x=220, y=0)
    if t > -1:
        mins, secs = divmod(t, 60)
        string = '{:02d}:{:02d}'.format(mins, secs)
        l.config(text=string)
        l.after(1000, update_time, t - 1)
        if t == 0:
            messagebox.showwarning("OTP Verification", "OTP expired")
    else:
        string = '00:00'


if __name__ == "__main__":
    window = otp_verifier()
    window.Labels()
    window.Entry()
    window.Buttons()
    update_time(20)
    window.mainloop()

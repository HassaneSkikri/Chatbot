from tkinter import *
from chat import get_response, bot_name

#Dfinding some colors and fonts
#----------------------------------------------------------------

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

#----------------------------------------------------------------

class ChatApplication:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()
    
    def _setup_main_window(self):
        self.window.title("Chat application")
        self.window.resizable(width = False, height = False)
        self.window.config( width = 470, height = 550, bg=BG_COLOR)

        # head  label
        head_label = Label(self.window,
                            bg=BG_COLOR ,
                            fg=TEXT_COLOR,
                            text="Welcome",
                            font=FONT_BOLD,
                            pady=10
                           )
        head_label.place(relwidth=1) #to tack the whol window

        # tiny divider

        line = Label(self.window,width=450, bg =BG_COLOR)
        line.place(relwidth=1,rely = 0.07,relheight=0.012)

        # text widget
        self.text_widget = Text(self.window,
                                width=20,
                                height=2,
                                bg=BG_COLOR,
                                fg=TEXT_COLOR,
                                font=FONT,
                                padx=5,
                                pady=5,
                               )
        self.text_widget.place(relwidth=1,rely = 0.08,relheight=0.743)
        self.text_widget.configure(cursor="arrow",state=DISABLED)


        #Scroll bar 

        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1,relx = 0.974)
        scrollbar.configure(command=self.text_widget.yview)

        #bottom label
        bottom_label = Label(self.window,
                            bg=BG_COLOR ,
                            height=80
                           )
        bottom_label.place(relwidth=1,rely=0.825)

        # message entry box

        self.msg_entry = Entry(bottom_label,bg= "#2C3E50", fg =TEXT_COLOR,font=FONT)
        self.msg_entry.place(relwidth=0.78,relheight=0.06,rely=0.008,relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self.send_message)

        # send button
        send_button = Button(bottom_label,
                            text="Send",
                            font=FONT_BOLD,
                            bg=BG_GRAY,
                            fg=TEXT_COLOR,
                            command=lambda: self.send_message(None)
                           )
        send_button.place(relwidth=0.22,relx=0.77,rely=0.008,relheight=0.06)

    def send_message(self,event):
        msg = self.msg_entry.get()
        self._inset_message(msg,'You')
    def _inset_message(self, msg,sender):
        if not msg:
            return
        self.msg_entry.delete(0,END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END,msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END,msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)
        # self.text_widget.yview(END)

if __name__ == "__main__":
    app = ChatApplication()
    app.run()
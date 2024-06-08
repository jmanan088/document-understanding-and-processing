from tkinter import * 
import customtkinter
import os
import PyPDF2
from PIL import Image, ImageTk
from pdf2image import convert_from_path
from image_to_text.ocrimage import gettext

# filepath = '/code/src/test/'
# print(gettext(filepath))


bot_name = 'Sam'

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

def button_event():
    print("button pressed")
class chatbot:

    def __init__(self):
        self.window = Tk()
        self.setup_main_window()

    def run(self):
        self.window.mainloop()

    def setup_main_window(self) :
        self.window.title("Document QnA")
        self.window.resizable(width=False, height=False)
        self.window.config(width=600, height=450, bg=BG_COLOR)

        headlabel = Label(self.window, bg = BG_COLOR, fg=TEXT_COLOR, text="Welcome to Document QnA", font=FONT_BOLD, pady=5) 
        headlabel.place( relwidth=1)
        
        #tiny divider
        line= Label(self.window, width=500, bg=BG_GRAY)
        line.place( relwidth=1, rely=0.07, relheight=0.012)

        #scrollable ctk textbox
        self.tk_textbox = customtkinter.CTkTextbox(self.window, activate_scrollbars=False, width=30, height = 3,text_color= TEXT_COLOR, fg_color=BG_COLOR, font=(FONT, 14), corner_radius=0, border_width=2, border_color= TEXT_COLOR, border_spacing= 5)
        self.tk_textbox.place(relwidth=1, relheight=0.82, rely =0.08)
        self.tk_textbox.configure(cursor="arrow", state = DISABLED)

        # create CTk scrollbar
        ctk_textbox_scrollbar = customtkinter.CTkScrollbar(self.tk_textbox, command=self.tk_textbox.yview)
        ctk_textbox_scrollbar.place(relheight=0.96, relx=0.964, rely = 0.02)
        ctk_textbox_scrollbar.configure(command=self.tk_textbox.yview)

        # connect textbox scroll event to CTk scrollbar
        self.tk_textbox.configure(yscrollcommand=ctk_textbox_scrollbar.set)

        #bottomlabel
        botlabel = customtkinter.CTkLabel(self.window, fg_color="transparent", text = "")
        botlabel.place(relwidth= 1, relheight = 0.10,rely=0.895)

        botlabel.grid_columnconfigure((0,1,2,3,4,5), weight=1)
        botlabel.grid_rowconfigure(0)


        self.button = customtkinter.CTkButton(botlabel, text="Upload Document", command=button_event())
        self.button.grid(row=0, column=0, padx=6, pady=(5,5),  sticky="nsew")
        self.entry = customtkinter.CTkEntry(botlabel, placeholder_text="Ask Document QnA", font=(FONT,14), fg_color = "#2C3E50", text_color="#ffffff")
        self.entry.grid(row=0,column =1,padx=(0,6), pady=(5,5),columnspan=5,  sticky="nsew")
        self.entry.focus()
        self.entry.bind("<Return>",self._on_enter_pressed)

    def _on_enter_pressed(self, event):
        mssg = self.entry.get()
        self._insert_mssg(mssg, "YOU")

    def _insert_mssg(self, mssg, sender):
        if not mssg:
            return
        
        self.entry.delete(0,END)
        mssg1 = f"{sender}: {mssg}\n\n"
        self.tk_textbox.configure(state = NORMAL)
        self.tk_textbox.insert(END, mssg1)
        self.tk_textbox.configure(state = DISABLED)

        #response implementation
        # mssg2 = f"{bot_name}: {mssg}"
        # self.tk_textbox.configure(state = NORMAL)
        # self.tk_textbox.insert(END, mssg1)
        # self.tk_textbox.configure(state = DISABLED)



if __name__ == "__main__":
    app=chatbot()
    
    app.run()



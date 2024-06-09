from tkinter import * 
import customtkinter
from tkinter.filedialog import askopenfile
from pdf2image import convert_from_path
from pathlib import Path
from image_to_text.ocrimage import gettext

# filepath = '/code/src/test/'
# print(gettext(filepath))


bot_name = 'Sam'

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

def open_file(root, tkbox):
    
    text_file = '/code/src/out/out_text.txt'
    image_list = []

    #load a PDF file
    PDF_file = askopenfile(parent=root, mode='rb', filetypes=[("Pdf file", "*.pdf")])
    if PDF_file:
        #filename print
        
        file_path_components = PDF_file.name.split("/")
        # Get the filename
        filename = file_path_components[-1]
        mssg1 = f"{bot_name}: {filename}\n\n"
        tkbox.configure(state = NORMAL)
        tkbox.insert(END, mssg1)
        tkbox.configure(state = DISABLED)


        #Part #1 : Converting PDF to images
        # Read in the PDF file at 500 DPI
        pdf_pages = convert_from_path(PDF_file.name, 500)

        # Iterate through all the pages stored above
        # enumerate() "counts" the pages for us.
        for pagenp, page in enumerate(pdf_pages, start=1):
            image_list.append(page)

        
        #Part #2 - Recognizing text from the images using OCR

        with open(text_file, "w") as output_file:
            # Open the file in append mode so that
            # All contents of all images are added to the same file

            # Iterate from 1 to total number of pages
            for image in image_list:

                # Recognize the text as string in image using pytesserct
                text = gettext(image)

                # The recognized text is stored in variable text
                # Any string processing may be applied on text
                # Here, basic formatting has been done:
                # In many PDFs, at line ending, if a word can't
                # be written fully, a 'hyphen' is added.
                # The rest of the word is written in the next line

                text = text.replace("-\n", "")

                # Finally, write the processed text to the file.
                output_file.write(text)


class chatbot:

    def __init__(self):
        self.window = Tk()
        self.window.geometry('+%d+%d'%(450,150))
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


        self.button = customtkinter.CTkButton(botlabel, text="Browse", command=lambda : open_file(self.window, self.tk_textbox))
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

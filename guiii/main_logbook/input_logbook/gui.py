
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, StringVar, messagebox, filedialog
import controller as db_controller


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\py_code\pbo_uas\guiii\main_logbook\input_logbook\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def inputlgbk():
    InputLogbook()
#window = Tk()

#window.geometry("1005x623")
#window.configure(bg = "#303030")

class InputLogbook(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.data = {"nama": StringVar(), "npm": StringVar(), "tanggal": StringVar(), "nama_dosen": StringVar(), "tugas": StringVar(), "tujuan": StringVar(), "permasalahan_skripsi": StringVar(), "solusi": StringVar(), "tugas_minggu_depan": StringVar(), "status_validasi": StringVar()}
        self.progress_skripsi = None
        self.canvas = Canvas(
            self,
            bg = "#313131",
            height = 666,
            width = 1099,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_13.png"))
        entry_bg_1 = self.canvas.create_image(
            119.5,
            54.5,
            image=self.entry_image_1
        )
        entry_1 = Entry(
            self,
            textvariable=self.data["nama"],
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Inter BoldItalic", 14 * -1)
        )
        entry_1.place(
            x=32.0,
            y=32.0,
            width=175.0,
            height=43.0
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_12.png"))
        entry_bg_2 = self.canvas.create_image(
            160.0,
            207.5,
            image=self.entry_image_2
        )
        entry_2 = Text(
            self,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Inter BoldItalic", 14 * -1)
        )
        entry_2.place(
            x=27.0,
            y=114.0,
            width=266.0,
            height=189.0
        )
        
        entry_2.insert(tk.END, self.data["tugas"].get())
        entry_2.bind("<<Modified>>", lambda event: self.update_tujuan(event, "tugas"))


        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_12.png"))
        entry_bg_3 = self.canvas.create_image(
            507.0,
            433.5,
            image=self.entry_image_3
        )
        entry_3 = Text(
            self,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Inter BoldItalic", 14 * -1)
        )
        entry_3.place(
            x=374.0,
            y=340.0,
            width=266.0,
            height=189.0
        )
        entry_3.insert(tk.END, self.data["tugas_minggu_depan"].get())
        entry_3.bind("<<Modified>>", lambda event: self.update_tujuan(event, "tugas_minggu_depan"))

        #entry_image_4 = PhotoImage(
        #    file=relative_to_assets("entry_4.png"))
        #entry_bg_4 = canvas.create_image(
        #    829.0,
        #    436.0,
        #    image=entry_image_4
        #)
        #entry_4 = Text(
        #    bd=0,
        #    bg="#FFFFFF",
        #    fg="#000716",
        #    highlightthickness=0
        #
        #entry_4.place(
        #    x=670.0,
        #    y=328.0,
        #    width=318.0,
        #    height=214.0
        #)

        self.entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_12.png"))
        entry_bg_5 = self.canvas.create_image(
            503.0,
            207.5,
            image=self.entry_image_5
        )
        entry_5 = Text(
            self,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Inter BoldItalic", 14 * -1)
        )
        entry_5.place(
            x=370.0,
            y=114.0,
            width=266.0,
            height=189.0
        )

        entry_5.insert(tk.END, self.data["tujuan"].get())
        entry_5.bind("<<Modified>>", lambda event: self.update_tujuan(event, "tujuan"))

        self.entry_image_6 = PhotoImage(
            file=relative_to_assets("entry_12.png"))
        entry_bg_6 = self.canvas.create_image(
            825.0,
            207.5,
            image=self.entry_image_6
        )
        entry_6 = Text(
            self,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Inter BoldItalic", 14 * -1)
        )
        entry_6.place(
            x=692.0,
            y=114.0,
            width=266.0,
            height=189.0
        )
        entry_6.insert(tk.END, self.data["permasalahan_skripsi"].get())
        entry_6.bind("<<Modified>>", lambda event: self.update_tujuan(event, "permasalahan_skripsi"))

        self.entry_image_7 = PhotoImage(
            file=relative_to_assets("entry_12.png"))
        entry_bg_7 = self.canvas.create_image(
            160.0,
            433.5,
            image=self.entry_image_7
        )
        entry_7 = Text(
            self,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Inter BoldItalic", 14 * -1)
        )
        entry_7.place(
            x=27.0,
            y=340.0,
            width=266.0,
            height=189.0
        )
        entry_7.insert(tk.END, self.data["solusi"].get())
        entry_7.bind("<<Modified>>", lambda event: self.update_tujuan(event, "solusi"))

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            45.0,
            17.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            47.0,
            94.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(
            47.0,
            322.0,
            image=self.image_image_3
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.save,
            activebackground="#313131",
            relief="flat"
        )
        button_1.place(
            x=296.0,
            y=558.0,
            width=207.0,
            height=45.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.open_file_dialog,
            activebackground="#313131",
            relief="flat"
        )
        button_2.place(
            x=72.0,
            y=558.0,
            width=207.0,
            height=45.0
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        image_4 = self.canvas.create_image(
            447.0,
            322.0,
            image=self.image_image_4
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        image_5 = self.canvas.create_image(
            386.0,
            94.0,
            image=self.image_image_5
        )

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        image_6 = self.canvas.create_image(
            744.0,
            94.0,
            image=self.image_image_6
        )

        self.image_image_7 = PhotoImage(
            file=relative_to_assets("image_7.png"))
        image_7 = self.canvas.create_image(
            285.0,
            17.0,
            image=self.image_image_7
        )

        self.image_image_8 = PhotoImage(
            file=relative_to_assets("image_8.png"))
        image_8 = self.canvas.create_image(
            535.0,
            17.0,
            image=self.image_image_8
        )

        self.image_image_9 = PhotoImage(
            file=relative_to_assets("image_9.png"))
        image_9 = self.canvas.create_image(
            825.0,
            17.0,
            image=self.image_image_9
        )

        self.entry_image_8 = PhotoImage(
            file=relative_to_assets("entry_13.png"))
        entry_bg_8 = self.canvas.create_image(
            358.5,
            54.5,
            image=self.entry_image_8
        )
        entry_8 = Entry(
            self,
            textvariable=self.data["npm"],
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Inter BoldItalic", 14 * -1)
        )
        entry_8.place(
            x=271.0,
            y=32.0,
            width=175.0,
            height=43.0
        )

        self.entry_image_9 = PhotoImage(
            file=relative_to_assets("entry_13.png"))
        entry_bg_9 = self.canvas.create_image(
            597.5,
            54.5,
            image=self.entry_image_9
        )
        entry_9 = Entry(
            self,
            textvariable=self.data["tanggal"],
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Inter BoldItalic", 14 * -1)

        )
        entry_9.place(
            x=510.0,
            y=32.0,
            width=175.0,
            height=43.0
        )

        self.entry_image_10 = PhotoImage(
            file=relative_to_assets("entry_13.png"))
        entry_bg_10 = self.canvas.create_image(
            836.5,
            54.5,
            image=self.entry_image_10
        )
        entry_10 = Entry(
            self,
            textvariable=self.data["nama_dosen"],
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            font=("Inter BoldItalic", 14 * -1)
        )
        entry_10.place(
            x=749.0,
            y=32.0,
            width=175.0,
            height=43.0
        )
        self.button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.navigate("viewlgbk"),
            activebackground="#313131",
            relief="flat"
        )
        button_3.place(
            x=10.0,
            y=563.0,
            width=45.0,
            height=36.0
        )
        self.image_image_10 = PhotoImage(
            file=relative_to_assets("image_11.png"))
        image_9 = self.canvas.create_image(
            744.0,
            322.0,
            image=self.image_image_10
        )
        self.entry_image_11 = PhotoImage(
            file=relative_to_assets("entry_15.png"))
        entry_bg_11 = self.canvas.create_image(
            779.5,
            360.5,
            image=self.entry_image_11
        )
        entry_11 = Entry(
            self,
            textvariable=self.data["status_validasi"],
            bd=0,
            bg="#283948",
            fg="#000716",
            highlightthickness=0,
            font=("Inter BoldItalic", 14 * -1)

        )
        entry_11.place(
            x=692.0,
            y=336.0,
            width=175.0,
            height=43.0
        )
    def update_tujuan(self, event, key):
        widget = event.widget
        self.data[key].set(widget.get("1.0", tk.END).strip())
        widget.edit_modified(False)
        
    def open_file_dialog(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.progress_skripsi_path = file_path
            print(f"Selected file: {file_path}")
    
    
    
    def save(self):
        # check if any fields are empty
        for key, val in self.data.items():
            if not val.get():
                messagebox.showinfo("Error", "Please fill in all the fields")
                return

        if not self.progress_skripsi_path:
            messagebox.showinfo("Error", "Please select a file for progress_skripsi")
            return

        # Save the room
        result = db_controller.add_logbook(
            self.data["nama"].get(), self.data["npm"].get(), self.data["tanggal"].get(),
            self.data["nama_dosen"].get(), self.data["tugas"].get(), self.data["tujuan"].get(),
            self.data["permasalahan_skripsi"].get(), self.data["solusi"].get(),
            self.data["tugas_minggu_depan"].get(), self.progress_skripsi_path,
            self.data["status_validasi"].get()
        )


        if result:
            messagebox.showinfo("Success", "Logbook added successfully")
            self.parent.navigate("viewlgbk")
            self.parent.windows.get("viewlgbk").handle_refresh()
            # clear all fields
            for label in self.data.keys():
                self.data[label].set("")  
        else:
            messagebox.showerror("Error", "Unable to add logbook. Please ensure the data is valid.")

    
        
        
        

#window.resizable(False, False)
#window.mainloop()

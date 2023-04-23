from tkinter import *
from tkinter import filedialog as fido
from PIL import ImageTk, Image


class CanvasImage:
    def __init__(self, title="Watermarking App"):
        self.master = Tk()
        self.master.withdraw()
        self.master.title(title)
        self.canvas = Canvas(self.master)
        self.canvas.grid(row=0, column=0, sticky=NSEW)
        self.image_button = Button(
            self.master, font=('Helvetica', 12),
            text="Choose Image", command=self.choose_image)
        self.image_button.grid(row=1, column=0, sticky=NSEW)
        self.master.update()
        self.master.resizable(False, False)
        self.master.deiconify()

    def choose_image(self):
        image_name = fido.askopenfilename(title="Pick your image")
        print(image_name)
        if image_name:
            self.img = ImageTk.PhotoImage(Image.open(image_name))
            w, h = self.img.width(), self.img.height()
            self.canvas.config(width=w, height=h)
            self.canvas.create_image((0, 0), image=self.img, anchor=NW)
            self.canvas.create_text(
                (w-75, h-25), text="TAIR", fill="RED", font=('Arial', 50))


if __name__ == "__main__":
    loader = CanvasImage()
    loader.master.mainloop()
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter

def open_image():
    global img_path, img
    img_path = filedialog.askopenfilename()
    if img_path:
        img = Image.open(img_path)
        img = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor=NW, image=img)

def apply_filter(filter_type):
    global img
    if img_path:
        original_img = Image.open(img_path)
        if filter_type == "blur":
            img = original_img.filter(ImageFilter.BLUR)
        elif filter_type == "sharpen":
            img = original_img.filter(ImageFilter.SHARPEN)
        # Add more filters here as needed
        img = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor=NW, image=img)

def save_image():
    global img
    if img_path:
        save_path = filedialog.asksaveasfilename(defaultextension=".jpg")
        if save_path:
            img.write(save_path)

root = Tk()
root.title("Simple Photo Editor")

canvas = Canvas(root, width=500, height=500)
canvas.pack()

Button(root, text="Open Image", command=open_image).pack()
Button(root, text="Blur", command=lambda: apply_filter("blur")).pack()
Button(root, text="Sharpen", command=lambda: apply_filter("sharpen")).pack()
Button(root, text="Save Image", command=save_image).pack()
def draw(event):
    global file_path
    if file_path:
        x1, y1 = (event.x - pen_size), (event.y - pen_size)
        x2, y2 = (event.x + pen_size), (event.y + pen_size)
        canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline="", width=pen_size, tags="oval")
      canvas.bind("<B1-Motion>", draw)
root.mainloop()

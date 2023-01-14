"""
Photo Quiz: Ask a question about a photo and guess the answer!
"""
import tkinter as tk
from tkinter import simpledialog, messagebox

from PIL import Image, ImageTk

def create_image(filename, width, height):
    image_obj = None

    try:
        image = Image.open(filename)
        image = image.resize((width, height), Image.ANTIALIAS)
        image_obj = ImageTk.PhotoImage(image=image)
    except FileNotFoundError as fnf:
        print("ERROR: Unable to find file " + filename)

    return image_obj

# ======================= DO NOT EDIT THE CODE ABOVE =========================

# TODO 0) Find at least 3 interesting photos (2 are provided if you want
#  to use those)

# TODO 1) Create a new tkinter class
class PhotoQuiz(tk.Tk):
    # TODO 2) Create a constructor
    def __init__(self):
        # TODO 3) call Tk's constructor
        super().__init__()
        # TODO 4) Create a member variable for a label and place it.
        #  You do not need to add any text or images to the label.
        self.label = tk.Label()
        self.label.place(relx=0.1, rely=0.1, relwidth=1, relheight=1)

# TODO 5) Create an if __name__ == '__main__': block
if __name__ == "__main__":
    # TODO 6) Create an object of the tkinter class
    app = PhotoQuiz()
    # TODO 7) Set the app window width and height using geometry()
    app.geometry("1000x500")
    # TODO 8) Declare and initialize a score variable
    score = 0
    # TODO 9) Create an image object variable using the create_image function
    #  above and store it in a variable
    image_files = ["carrots.jpg", "fossil.jpg", "python.png"]
    answers = ["carrots", "fossil", "python"]
    for idx, image_file in enumerate(image_files):
        image = create_image(image_file, 1000, 500)
        app.label.configure(image=image)
        if simpledialog.askstring("Prompt", "What is this (one word)?").lower() == answers[idx]:
            messagebox.showinfo("Message", "Correct")
            score += 1
    # TODO 10) Set the image onto the class's label using the configure method,
    #  for example:
    #  app.photo_label.configure(image=image_object)

    # TODO 11) Use a pop-up (simpledialog) to ask the user a question
    #  relating to the image and tell them if they get the right answer.

    # TODO 12) If the answer is correct, increase the score by 1

    # TODO 13) Repeat the steps to show a different photo and ask a different
    #  question

    # TODO 14) Display the score to the user after asking the last question
    messagebox.showinfo("Message", "Score: " + str(score))

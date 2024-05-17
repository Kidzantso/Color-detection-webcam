# Import required Libraries
from tkinter import *
from PIL import Image, ImageTk
import cv2
import numpy as np
from tkinter import filedialog
# Create an instance of TKinter Window or frame
win = Tk()

# Set the size of the window
win.geometry("800x600")
win.title('Video Color detection')
win.resizable(width=False, height=False)
# Create a Label to capture the Video frames
label =Label(win)
label.grid(row=0, column=0)
options = [ 
			"Red", 
			"Yellow", 
			"Blue", 
			"Pink", 
			"Green", 
			"Black", 
			"White",
			"Purple"
		];clicked = StringVar();clicked.set( "Red" )
drop = OptionMenu(win , clicked , *options )
drop.grid(row=1,column=2,padx=10,pady=10)
cap= cv2.VideoCapture(0)
def arrayscolorsUP(text):
    if text=="Red":Upper=np.array([10, 255, 255])
    elif text =="Blue":Upper=np.array([130, 255, 255])
    elif text=="Yellow":Upper=np.array([30, 255, 255])
    elif text=="Pink":Upper=np.array([350, 255, 255])
    elif text=="Green": Upper=np.array([80, 255, 255])
    elif text=="Black":Upper=np.array([179, 255, 30])
    elif text=="White":Upper=np.array([179, 18, 255])
    elif text=="Purple":Upper=np.array([160, 255, 255])
    return Upper
def arrayscolorsDOWN(text):
    if text=="Red":Lower=np.array([0, 100, 100])
    elif text =="Blue":Lower=np.array([100, 50, 50])
    elif text=="Yellow":Lower=np.array([20, 100, 100])
    elif text=="Pink":Lower=np.array([160, 50, 170])
    elif text=="Green": Lower=np.array([40, 40, 40])
    elif text=="Black":Lower=np.array([0, 0, 0])
    elif text=="White":Lower=np.array([0, 0, 231])
    elif text=="Purple":Lower=np.array([130, 50, 50])
    return Lower 
# Define function to show frame
def show_frames():
   # Get the latest frame and convert into Image
   cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
   HSV_im_1 = cv2.cvtColor(cv2image,cv2.COLOR_BGR2HSV)
   mask = cv2.inRange(HSV_im_1,arrayscolorsDOWN(clicked.get()),arrayscolorsUP(clicked.get()))
   mask3 = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
   im_thresh_color = cv2.bitwise_and(cv2image, mask3)
   b,g,r = cv2.split(im_thresh_color)
   im_thresh_color = cv2.merge((r,g,b))
   im = Image.fromarray(im_thresh_color)
   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image = im)
   label.imgtk = imgtk
   label.configure(image=imgtk)
   # Repeat after an interval to capture continiously
   label.after(10, show_frames)   
show_frames()
win.mainloop()

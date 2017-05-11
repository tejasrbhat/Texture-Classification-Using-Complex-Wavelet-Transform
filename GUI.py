from Tkinter import *
from code1 import gaborKernel, refFeats, cfeats, match, topprint
import numpy as np
from genlist import find_img, find_img1
from PIL import ImageTk
import PIL.Image as pimg



class MyApp:
    def __init__(self, parent):
        
        self.myParent = parent  
        
        '''Some variables'''
        
        self.kernels = []
        self.rvm = np.zeros((112, 16, 4, 2), dtype=np.double)
        self.cfeats = np.zeros((4, 2), dtype=np.double)
        self.error = {}
        self.result = {}
        optionlist = list()
        
        '''----'''
        
        self.frame = Frame(parent)
        self.frame.pack(ipadx=5, ipady=3, padx=5, pady=3)
        
        self.frame2 = Frame(self.frame)
        self.frame2.grid(row = 0, columnspan = 6, sticky = N)
        
        self.frame3 = Frame(self.frame)
        self.frame3.grid(row = 1, column = 0, sticky = N+W)
        
        self.frame4 = Frame(self.frame)
        self.frame4.grid(row = 1, column = 1, sticky = N)
        
        self.frame5 = Frame(self.frame)
        self.frame5.grid(row = 1, column = 2, sticky = W)
        
        self.subframe1 = Frame(self.frame3)
        self.subframe1.grid(row = 3, sticky = N)
        
        self.label1 = Label(self.frame2, text = "Texture Image Retrieval Using Rotation Invariant Gabor Filter Bank", font=("Courier", 18, "bold"), fg = "darkslategray", pady = 40)
        self.label1.grid(row = 0, columnspan = 6, sticky = N)
        
        self.button1 = Button(self.frame3, command=self.button1Click)
        self.button1.configure(text="Create Gabor Kernels",font=("Courier", 10, "bold"),bd = 5, background= "lightsteelblue")
        self.button1.focus_force()       
        self.button1.configure( width=15, padx=30, pady=10)
        self.button1.grid(row = 1,pady = 15, sticky = W)    
        self.button1.bind("<Return>", self.button1Click_a)  
        
        self.button2 = Button(self.frame3, command=self.button2Click)
        self.button2.configure(text="Reference Features",font=("Courier", 10, "bold"),bd = 5, background="lightsteelblue")  
        self.button2.configure(width=15, padx=30, pady=10)
        self.button2.grid(row = 2, pady = 15, sticky = W)
        self.button2.bind("<Return>", self.button2Click_a)   
        
        '''optionlist = cl()
        sel
        self.menu1 = OptionMenu(self.frame, self.v, *optionlist)
        self.menu1.grid(row = 3, pady = 10, sticky = W)'''
        
        
        self.entry1 = Entry(self.subframe1, width = 10)
        self.entry1.grid(row = 3, pady = 10, sticky = W)
        
        self.button3 = Button(self.subframe1, command=self.button3Click)
        self.button3.configure(text="Input Texture",font=("Courier", 10, "bold"),bd = 5, background="lightsteelblue")  
        self.button3.configure(width=12, padx=10, pady=5)
        self.button3.grid(row = 3,column = 1, pady = 15, sticky = W)
        self.button3.bind("<Return>", self.button3Click_a)

        self.img1 = ImageTk.PhotoImage(pimg.open('blank.jpg'))
        self.label2 = Label(self.frame3, image = self.img1)
        self.label2.grid(row = 4, padx = 30, sticky = W)
                
        self.button4 = Button(self.frame3, command=self.button4Click)
        self.button4.configure(text="Compute Distance",font=("Courier", 10, "bold"),bd = 5, background="lightsteelblue")  
        self.button4.configure(width=15, padx=30, pady=10)
        self.button4.grid(row = 5, pady = 15, sticky = W)
        self.button4.bind("<Return>", self.button4Click_a)
        
        '''self.scrollbar = Scrollbar(self.frame, orient=VERTICAL)
        self.listbox1 = Listbox(self.frame, width = 31, yscrollcommand = self.scrollbar.set)
        self.listbox1.grid(row=6, column=0,sticky=W)
        self.scrollbar.config(command=self.listbox1.yview)
        self.scrollbar.grid(row = 6, column=1, sticky=N+S+W)'''
        
        self.button5 = Button(self.frame3, command=self.button5Click)
        self.button5.configure(text="Display",font=("Courier", 10, "bold"),bd = 5, background="lightsteelblue")  
        self.button5.configure(width=15, padx=30, pady=10)
        self.button5.grid(row = 6, pady = 15, sticky = W)
        self.button5.bind("<Return>", self.button5Click_a)
        
        self.button6 = Button(self.frame3, command=self.button6Click)
        self.button6.configure(text="Refresh",font=("Courier", 10, "bold"),bd = 5, background="lightsteelblue")  
        self.button6.configure(width=15, padx=30, pady=10)
        self.button6.grid(row = 7, pady = 10, sticky = W)
        self.button6.bind("<Return>", self.button6Click_a)
        
        self.labl = [None] * 20
        
        self.img = ImageTk.PhotoImage(pimg.open('blank.jpg'))
        self.labl[0] = Label(self.frame4, image = self.img)
        self.labl[0].grid(row = 0, column = 0, padx = 10, pady = 10, sticky = W)
        
        self.labl[1] = Label(self.frame4, image = self.img)
        self.labl[1].grid(row = 0, column = 1, padx = 10, pady = 10, sticky = W)
        
        self.labl[2] = Label(self.frame4, image = self.img)
        self.labl[2].grid(row = 0, column = 2, padx = 10, pady = 10, sticky = W)
        
        self.labl[3] = Label(self.frame4, image = self.img)
        self.labl[3].grid(row = 0, column = 3, padx = 10, pady = 10, sticky = W)
        
        self.labl[4] = Label(self.frame4, image = self.img)
        self.labl[4].grid(row = 0, column = 4, padx = 10, pady = 10, sticky = W)
        
        self.labl[5] = Label(self.frame4, image = self.img)
        self.labl[5].grid(row = 1, column = 0, padx = 10, pady = 10, sticky = W)
        
        self.labl[6] = Label(self.frame4, image = self.img)
        self.labl[6].grid(row = 1, column = 1, padx = 10, pady = 10, sticky = W)
        
        self.labl[7] = Label(self.frame4, image = self.img)
        self.labl[7].grid(row = 1, column = 2, padx = 10, pady = 10, sticky = W)
        
        self.labl[8] = Label(self.frame4, image = self.img)
        self.labl[8].grid(row = 1, column = 3, padx = 10, pady = 10, sticky = W)
        
        self.labl[9] = Label(self.frame4, image = self.img)
        self.labl[9].grid(row = 1, column = 4, padx = 10, pady = 10, sticky = W)
        
        self.labl[10] = Label(self.frame4, image = self.img)
        self.labl[10].grid(row = 2, column = 0, padx = 10, pady = 10, sticky = W)
        
        self.labl[11] = Label(self.frame4, image = self.img)
        self.labl[11].grid(row = 2, column = 1, padx = 10, pady = 10, sticky = W)
        
        self.labl[12] = Label(self.frame4, image = self.img)
        self.labl[12].grid(row = 2, column = 2, padx = 10, pady = 10, sticky = W)
        
        self.labl[13] = Label(self.frame4, image = self.img)
        self.labl[13].grid(row = 2, column = 3, padx = 10, pady = 10, sticky = W)
        
        self.labl[14] = Label(self.frame4, image = self.img)
        self.labl[14].grid(row = 2, column = 4, padx = 10, pady = 10, sticky = W)
        
        self.labl[15] = Label(self.frame4, image = self.img)
        self.labl[15].grid(row = 3, column = 0, padx = 10, pady = 10, sticky = W)
        
        self.labl[16] = Label(self.frame4, image = self.img)
        self.labl[16].grid(row = 3, column = 1, padx = 10, pady = 10, sticky = W)
        
        self.labl[17] = Label(self.frame4, image = self.img)
        self.labl[17].grid(row = 3, column = 2, padx = 10, pady = 10, sticky = W)
        
        self.labl[18] = Label(self.frame4, image = self.img)
        self.labl[18].grid(row = 3, column = 3, padx = 10, pady = 10, sticky = W)
        
        self.labl[19] = Label(self.frame4, image = self.img)
        self.labl[19].grid(row = 3, column = 4, padx = 10, pady = 10, sticky = W)
        
        self.button7 = Button(self.frame5, command=self.one)
        self.button7.configure(text="Info",font=("Courier", 10, "bold"),bd = 5, background="lightsteelblue")  
        self.button7.configure(width=15, padx=30, pady=10)
        self.button7.grid(row = 10, pady = 10, sticky = N)
        self.button7.bind("<Return>", self.button5Click_a)
        
    def button1Click(self):
        self.kernel = gaborKernel()      
        self.button1["background"] = "lightgreen"
        
    
    def button2Click(self): 
        self.rfm = refFeats(self.kernel)
        self.button2["background"] = "lightgreen"
    
    def button3Click(self):
        self.info = self.entry1.get()
        self.cfeats = cfeats(self.info,self.kernel)
        self.button3["background"] = "lightgreen"
        self.img = find_img(self.info)
        self.label2["image"] = self.img
        for i in range(20):
            self.labl[i]["image"] = "blank.png" 
    
    def button4Click(self):
        self.error = match(self.cfeats,self.rfm)
        self.button4["background"] = "lightgreen"
    
    def button5Click(self):
        i = 0
        self.imag1 = [None] * 20
        for key, value in sorted(self.error.iteritems(), key=lambda (k,v): (v,k)):
            if  i<20:
                self.imag1[i] = find_img1(key)
                self.labl[i]["image"] = self.imag1[i]
            i = i+1
        self.button5["background"] = "lightgreen"
        #self.label1["fg"] = "lightgreen"
        
    def button6Click(self):
        self.myParent.destroy()
        self.loop = Tk()
        self.loop.title("Texture Retrieval")
        myapp = MyApp(self.loop)
    
    """def button7Click(self):
        self.myParent.destroy()
        self.loop = Tk()
        self.loop.title("Texture Retrieval")
        myapp = MyApp(self.loop)"""
        
    def button1Click_a(self, event):  
        self.button1Click()
                
    def button2Click_a(self, event): 
        self.button2Click() 
  
    def button3Click_a(self, event):
        self.button3Click()
        
    def button4Click_a(self, event):
        self.button4Click()
    
    def button5Click_a(self, event):
        self.button5Click()
    
    def button6Click_a(self, event):
        self.button6Click()
        
    def button7Click_a(self, event):
        self.button7Click()
        
    def create_window(self):
        self.top = Toplevel(root)
        
    def one(self):
        #MessageBox.showinfo("one","this first.......")
        self.top=Toplevel(master=self.myParent)
        self.textb1 = Text(self.top, height=36, width=102) 
        self.textb1.pack()
        self.text = """            TEXTURE IMAGE RETRIEVAL USING ROTATION INVARIANT GABOR FILTER BANK

  Textures are psycho-physically perceived by the human visual system (HVS), particularly, on the
aspects of orientation and scale of texture patterns. Frequency and orientation representations of
Gabor filters are similar to those of the human visual system, and they have been found to be
particularly appropriate for texture representation and discrimination.

GABOR FILTER BANK:
        
  Gabor filtering is a widely adopted technique for texture analysis. A two-dimensional Gabor
filter consists of a sinusoidal wave modulated by a gaussian envelope. It performs a localized and
oriented frequency analysis of a two-dimensional signal.
Rotation- invariant Gabor representations are used, from which each representation only involves
a simple modification of the conventional Gabor filter family for achieving rotation invariance
individually.
  A bank of filters at different scales and orientations allows multichannel filtering of an image to
extract frequency and orientation information. This can then be used to decompose the image
into texture features.
        
FEATURE EXTRACTION
        
  The mean and standard deviation are used to for the feature vector. The outputs of filters at
different scales will be over differing ranges. For this reason each element of the feature vector is
normalized using the standard deviation of that element across the entire database.
        
SIMILARITY MEASUREMENTS:
        
  Euclidean distance is the most common metric for measuring the distance between two vectors
and is discussed and implemented in a number of CBIR approaches.
  Each image in the database is processed to generate a feature vector as its metadata for
performing similarity matching. The distance d(i, j) between two feature vectors according to is
computed (say, image i is the query image, and image j is one of the database images under
matching). Those images with the highest scores (i.e., shortest distances) are retrieved and
displayed according to their ranked scores. In the ideal case, the top 16 images being displayed
should be those images from the same class (i.e., the ground truth), including the query image
(supposed to be ranked as the top match)"""
        self.textb1.insert(END, self.text)
    
                
root = Tk()
root.title("Texture Retrieval")
myapp = MyApp(root)
root.mainloop()
import tkinter, PIL
from PIL import ImageTk
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from complexmethods import *

class GUI():
    def __init__(self):
        self.root = Tk()
        self.frame = Frame(self.root, bg='white')
        self.root.geometry('800x600')
        self.root.title('Steggy the Steganographer')
        self.mainscreen()

    def clearFrame(self):
        self.frame.destroy()
        self.frame = Frame(self.root, bg='pink')
        self.frame.pack(expand=True, fill=BOTH)
    def mainscreen(self):
        self.frame.destroy()
        self.frame = Frame(self.root, bg='white')
        self.frame.pack(expand=True, fill=BOTH)
        self.menubar = Menu(self.frame)
        self.encodemenu = Menu(self.menubar, tearoff=0)
        self.decodemenu = Menu(self.menubar, tearoff=0)
        self.encodemenu.add_command(label='Encode text to image', command=lambda: self.encodegui())
        self.encodemenu.add_command(label='Encode file to image', command=lambda: self.encodeFilegui())
        self.decodemenu.add_command(label='Decode text from image', command=lambda: self.decodegui())
        self.decodemenu.add_command(label='Decode file from image', command=lambda: self.decodeFilegui())
        self.menubar.add_cascade(label="Encode", menu=self.encodemenu)
        self.menubar.add_cascade(label="Decode", menu=self.decodemenu)
        self.root.config(menu=self.menubar)
        self.renderImage('stegpic.png',700,500).place(relx=0.5, rely=0.5, anchor=CENTER)
    def encodegui(self):
        self.clearFrame()
        self.menubar = Menu(self.frame)
        self.menubar.add_command(label='Back', command=lambda: self.mainscreen())
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='Upload', command=lambda: self.upload())
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.root.config(menu=self.menubar)
        self.t = Text(self.frame, height=8)
        self.t.pack(side=BOTTOM, fill=BOTH)
        self.t.focus_set()
        self.meslbl = Label(text='Message to encode')
        
    def renderImage(self,path,x,y):
        self.load = PIL.Image.open(path)
        self.load.thumbnail(
            (x,y),
            PIL.Image.ANTIALIAS)
        self.render = ImageTk.PhotoImage(self.load)
        self.img = Label(self.frame, image=self.render)
        self.img.image = self.render
        return self.img
        #self.img.place(relx=0.5, rely=0.35, anchor=CENTER)
    def encode(self):
        self.message = self.t.get('1.0',END)
        self.newpath = asksaveasfilename(
                    filetypes=(
                        ("PNG File", "*.png"),), title='Steggy says: SAVE YOUR FILE', initialdir='./')
        if encode(self.path,self.newpath+'.png',self.message) == 0:
            mainscreen()
    def decodegui(self):
        self.clearFrame()
        self.menubar = Menu(self.frame)
        self.menubar.add_command(label='Back', command=lambda: self.mainscreen())
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='Upload encoded file', command=lambda: self.doDecode())
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.root.config(menu=self.menubar)
        self.t = Text(self.frame, height=8)
        self.t.pack(side=BOTTOM, fill=BOTH)
        self.t.config(state=DISABLED)
    def encodeFilegui(self):
        self.clearFrame()
        self.menubar = Menu(self.frame)
        self.menubar.add_command(label='Back', command=lambda: self.mainscreen())
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='Upload image', command=lambda: self.encodeFilePicUpload())        
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.root.config(menu=self.menubar)

    def decodeFilegui(self):
        self.clearFrame()
        self.menubar = Menu(self.frame)
        self.menubar.add_command(label='Back', command=lambda: self.mainscreen())
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='Upload encoded file', command=lambda: self.decodeFileUploadPic())
        self.menubar.add_cascade(label="File",menu=self.filemenu)
        self.root.config(menu=self.menubar)
    def upload(self):
        self.path=askopenfilename(filetypes=(("PNG File", "*.png"),))
        print(self.path)
        if self.path:
            self.renderImage(self.path,700,350).place(relx=0.5, rely=0.35, anchor=CENTER)
            self.filemenu.add_command(label='Save encoded file', command=lambda: self.encode())
            self.filemenu.delete(0)
    def encodeFilePicUpload(self):
        self.path=askopenfilename(filetypes=(("PNG File", "*.png"),))
        print(self.path)
        if self.path:
            self.renderImage(self.path,700,500).place(relx=0.5, rely=0.5, anchor=CENTER)
            self.filemenu.add_command(label='Upload file to encode to image', command= lambda: self.pathToFileToEncode())
            self.filemenu.delete(0)
    def decodeFileUploadPic(self):
        self.path=askopenfilename(filetypes=(("PNG File", "*.png"),))
        if self.path:
            self.renderImage(self.path, 700, 500).place(relx=0.5, rely=0.5, anchor=CENTER)
            self.filemenu.add_command(label='Save decoded file', command = lambda: self.doDecodeFile())
            self.filemenu.delete(0)
    def doDecodeFile(self):
        self.filetype = encodedFileType(self.path)
        print(self.path,self.filetype[0])
        if self.filetype == 0:
            self.mainscreen()
        else:
            self.filepath = asksaveasfilename(filetypes=(("Decoded file","*"+self.filetype[0]),))
            try:
                var = self.filepath.index('.')
            except:
                self.filepath += self.filetype[0]
            
            decodeFile(self.path, self.filepath, self.filetype[1])
    def doDecode(self):
        self.path=askopenfilename()
        print(self.path)
        if self.path:
            self.renderImage(self.path,700,350).place(relx=0.5, rely=0.35, anchor=CENTER)
            self.t.config(state=NORMAL)
            self.t.insert(END, decode(self.path))
            self.t.config(state=DISABLED)
    def pathToFileToEncode(self):
        self.filepath=askopenfilename()
        if self.filepath:
            self.filemenu.add_command(label='Save encoded image', command=lambda: self.encodeFile())
    def encodeFile(self):
        self.newpath=asksaveasfilename(
                    filetypes=(
                        ("PNG File", "*.png"),), title='Steggy says: SAVE YOUR FILE', initialdir='./')
        if self.newpath[-4:]=='.png' or self.newpath[-4:]=='.PNG':
            pass
        else:
            self.newpath+='.png'
        if encodeFile(self.path,self.newpath,self.filepath) == 0:
            self.error()
    def error(self):
        self.clearFrame()
        self.urdumb = Label(self.frame,text="U caused error. Likely message/file too big", font=("Arial",30))
        self.urdumb.place(relx=0.5, rely=0.5, anchor=CENTER)
#try:
#    w=GUI()
#except:
#    w.root.destroy()
w=GUI()

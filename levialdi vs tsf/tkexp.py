import tkinter as tk
from tkinter.filedialog import *
from PIL import Image, ImageTk
from copy import copy, deepcopy
import numpy as np
import csv
import os



#GLOBAL VARIABLES
openedImage=None #Opened image
rowSize=0
columnSize=0
pix=None #Opened image as a pixel map
labelValue=None #Opened image as a labeled map according to siyah beyaz pixel map
pixelValue=None #Black and white pixel map
layerCount=0


levialdiLayerCounter = 0
tsfLayerCounter = 0
levialdiIter = 0


window = tk.Tk()



window.geometry("1100x900")
window.resizable(0,0)
window.title("Programing Studio")
window.configure(bg='white')

maxSize = 2000
titleSize = 25
arrayFont = 3
resultFont = 17

fileName = ""

for r in range(3):
    for c in range(3):
        if r==0:
            Label(window, text="test").grid(row=r, column=c, padx=160, pady=10)
        #elif c==0:
            #Label(window, text="test").grid(row=r, column=c, padx=160, pady=200)
        else:
            Label(window, text="test").grid(row=r, column=c, padx=160, pady=200)

#titles
imgTitleTitle = Label(window, text="Images", bg="white", fg="black", bd=3, relief="groove")
imgTitleTitle.grid(row=0, column=0, sticky=W+E+N+S)
binaryMapTitle = Label(window, text="Binary Map", bg="white", fg="black", bd=3, relief="groove")
binaryMapTitle.grid(row=0, column=1, sticky=W+E+N+S)
resultMapTitle = Label(window, text="Result", bg="white", fg="black", bd=3, relief="groove")
resultMapTitle.grid(row=0, column=2, sticky=W+E+N+S)


defImg = ImageTk.PhotoImage(file= "."+os.path.sep+"images"+os.path.sep+"logo.png")
img1 = Label(window, borderwidth=2, bg="white", fg="black", bd=3, relief="groove")
img1.config(image=defImg)
img1.image = defImg
img1.grid(row=1, column=0, sticky=W+E+N+S)


binStatic = Canvas(window, borderwidth=2, bg="white", bd=3, relief="groove", width=200, height=200)
binStatic.grid(row=2, column=0, sticky=W+E+N+S)

bin1 = Canvas(window, borderwidth=2, bg="white", bd=3, relief="groove", width=200, height=200)
bin1.grid(row=1, column=1, sticky=W+E+N+S)

bin2 = Canvas(window, borderwidth=2, bg="white", bd=3, relief="groove", width=200, height=200)
bin2.grid(row=2, column=1, sticky=W+E+N+S)









'''
res1 = Canvas(window, borderwidth=2, bg="white", bd=3, relief="groove", width=200, height=200)
res1.grid(row=1, column=2, sticky=W+E+N+S)

res2 = Canvas(window, borderwidth=2, bg="white", bd=3, relief="groove", width=200, height=200)
res2.grid(row=2, column=2, sticky=W+E+N+S)


bin1 = Label(window, borderwidth=2, bg="white", fg="black", bd=3, relief="groove")
bin1.grid(row=1, column=1, sticky=W+E+N+S)

bin2 = Label(window, borderwidth=2, bg="white", fg="black", bd=3, relief="groove")
bin2.grid(row=2, column=1, sticky=W+E+N+S)


'''

txarray1 = ""


def openFile(): #Read image file
    openFileFormats = (("all files", "*.*"), ("png files", "*.png"), ("gif files", "*.gif"), ("jpeg files", "*.jpg")) #File formats for easy search
    path = askopenfilename(parent = window, filetypes = openFileFormats) #Basic file pick gui
    fp = open(path, "rb") #Read file as a byte map
    global openedImage
    openedImage = Image.open(fp).convert('1', dither=Image.NONE) #Byte map to images
    Reset()
    global fileName
    fileName = fp.name.split("/")[-1]
    imageProcess()



def imageProcess():
    global pix
    global maxSize
    global rowSize,columnSize
    global openedImage
    global arrayFont

    columnSize,rowSize=openedImage.size #Get images width and height

    print("first size : ", rowSize, columnSize)
    '''

    pia = 1;
    if rowSize>columnSize and rowSize>maxSize:
        pia = (rowSize/maxSize)
    elif columnSize>rowSize and columnSize>maxSize:
        pia = (columnSize/maxSize)

    print(pia)

    rowSize = int(rowSize/pia)
    columnSize = int(columnSize/pia)

    print("new size : ", rowSize, columnSize)

    openedImage = openedImage.resize((rowSize,columnSize), Image.ANTIALIAS)

    '''

    pix = openedImage.load() #Images to pixel map

    global pixelValue
    pixelValue = [[0 for x in range(columnSize)] for y in range(rowSize)]  # Set pixelValue sizes

    for i in range(rowSize):
        for j in range(columnSize):
            if (j == 0) or (i == 0) or (j == rowSize - 1) or (i == columnSize - 1):
                pixelValue[i][j] = 0  # Frames with formal black
            else:
                if(pix[j,i] > 200):
                    pixelValue[i][j] = 1
                else:
                    pixelValue[i][j] = 0

    '''


    
    for i in range(rowSize):
        for j in range(columnSize):
            pix[j,i] = cleanNoise(pix[j,i]) # Clean gray pixels -> Black/White imagemenu.add_cascade(label = "File", menu = fileMenu)
            if (j == 0) or (i == 0) or (j == rowSize-1) or (i == columnSize-1):
                pix[j, i] = (0, 0, 0) #Frames with formal black

    global pixelValue
    pixelValue = [[0 for x in range(columnSize)] for y in range(rowSize)]  # Set pixelValue sizes

    for i in range(1, rowSize - 1):
        for j in range(1, columnSize - 1):
            pixelValue[i][j] = convertToBinary(pix[j, i])  # Give value to pixels -> White:1 and Black:0
            
    '''

    global bin1
    bin1.select_clear()
    bin1.delete("bin1")
    global bin2
    bin2.select_clear()
    bin2.delete("bin2")
    global binStatic
    binStatic.select_clear()
    binStatic.delete("binStatic")
    global txarray1

    txarray1 = ""

    for i in range(rowSize):
        for j in range(columnSize):
            print(pixelValue[i][j], end='')  # Print w/b pixel map
            txarray1 += str(pixelValue[i][j])
            #Label(bin1, borderwidth=1, bg="white", text=str(pixelValue[i][j])).grid(row=j, column=i, padx=1, pady=1)
        print("")
        txarray1 += "\n"

    binStatic.create_text(200, 200, text=txarray1, font=("Times New Roman", arrayFont), tag="binStatic")  # "Times New Roman" , "bold"
    binStatic.update()

    bin1.create_text(200,200,text=txarray1, font=("Times New Roman", arrayFont), tag="bin1") #"Times New Roman" , "bold" , Avenir , purisa
    bin1.update()

    bin2.create_text(200, 200, text=txarray1, font=("Times New Roman", arrayFont), tag="bin2")
    bin2.update()


    '''
    data = np.squeeze(np.asarray(pixelValue))
    photop = ImageTk.PhotoImage(image=Image.fromarray(data))

    global bin1
    bin1.create_image(150,150,image=photop,anchor=tk.NW)
    bin1.image= photop
    bin1.update()
    '''



    print("")
    print("")

    '''
    global labelValue
    labelValue = [[0 for x in range(columnSize)] for y in range(rowSize)]

    for i in range(rowSize):
        for j in range(columnSize):
            labelValue[i][j] = 0

    global layerCount
    for i in range(1, rowSize - 1):
        for j in range(1, columnSize - 1):
            if (pixelValue[i][j] == 1):
                layerCount += 1
                countLay(i, j)
            print(labelValue[i][j], end='')
        print("")
        '''



    render = ImageTk.PhotoImage(openedImage)
    img1.config(image=render)
    img1.image = render
    img1.update()
    print("img size:", "height size=", rowSize, "and width size=", columnSize)


def Reset():
    global rowSize,columnSize
    global pix
    global labelValue
    global pixelValue
    global layerCount
    global levialdiLayerCounter
    global levialdiIter
    global tsfLayerCounter
    global fileName

    fileName = ""
    rowSize = 0
    columnSize = 0
    pix = None
    labelValue = None
    pixelValue = None
    layerCount = 0
    levialdiLayerCounter = 0
    levialdiIter = 0
    tsfLayerCounter = 0

    updateResult("levialdi")
    updateResult("tsf")

    global lvResult
    lvResult.select_clear()
    lvResult.delete("lvDONE")


def countLay(i,j):
    global labelValue
    global layerCount

    labelValue[i][j] = layerCount
    pixelValue[i][j] = 0


    if (pixelValue[i - 1][j - 1] == 1):
        countLay(i-1,j-1)

    if (pixelValue[i - 1][j] == 1):
        countLay(i-1,j)

    if (pixelValue[i - 1][j + 1] == 1):
        countLay(i-1, j+1)

    if (pixelValue[i][j - 1] == 1):
        countLay(i, j-1)

    if (pixelValue[i][j + 1] == 1):
        countLay(i, j+1)

    if (pixelValue[i + 1][j - 1] == 1):
        countLay(i+1, j-1)

    if (pixelValue[i + 1][j] == 1):
        countLay(i+1, j)

    if (pixelValue[i + 1][j + 1] == 1):
        countLay(i+1, j+1)





def convertToBinary(Value):
    #Create w/b pixel map - binary map
    if len(Value) == 4:
        r, g, b, op = Value #opacity
    else:
        r, g, b = Value

    average = (r + g + b) / 3

    if average == 255:
        return 1
    else:
        return 0


def cleanNoise(Value):
    #Clean gray pixel according to RGB average
    global isImgOpened
    if len(Value) == 4: #opacity
        r, g, b, op = Value
    else:
        r, g, b = Value

    average = (r + g + b) / 3

    if average > 200:
        return 255, 255, 255
    else:
        return 0, 0, 0



def saveFile():
    #File save
    global levialdiLayerCounter
    global levialdiIter
    global rowSize,columnSize
    global fileName

    fileSize = str(rowSize) + "x" + str(columnSize)

    saveFileFormats = (("csv files", "*.csv"), ("all files", "*.*"))
    output = asksaveasfile(filetypes = saveFileFormats, title = 'Export File', defaultextension = '.csv')#Default save type *.png

    print(fileName)

    with open(output.name, "w") as csv_file:
        fieldNames = ['File Name', 'Image Size', 'Algorithm Name', 'NCC', 'ITER']
        writer = csv.DictWriter(csv_file, fieldnames=fieldNames)

        writer.writeheader()
        writer.writerow({'File Name': fileName, 'Image Size': fileSize, 'Algorithm Name': 'Levialdi','NCC': levialdiLayerCounter,'ITER': levialdiIter})



def writeResult(param):
    if param=="levialdi":
        global res1
        global lvResult
        global levialdiLayerCounter
        global levialdiIter

        lvResult.select_clear()
        lvResult.delete("lvDONE")

        lvResult.create_text(175, 100, text="DONE", font=("Times New Roman", resultFont), tag="lvDONE")
        lvResult.update()

def updateResult(param):
    if param == "levialdi":
        global res1
        global lvResult
        global levialdiLayerCounter
        global levialdiIter

        lvResult.select_clear()
        lvResult.delete("lvResTag")
        lvResult.delete("lvRespo")

        lvResultText = " NCC : \nITER : "
        resultText = str(levialdiLayerCounter) + "\n" + str(levialdiIter)

        lvResult.create_text(150, 50, text=lvResultText, font=("Times New Roman", resultFont, "bold"), tag="lvResTag")
        lvResult.create_text(200, 50, text=resultText, font=("Times New Roman", resultFont),tag="lvRespo")  # "Times New Roman" , "bold"
        lvResult.update()



def runLevialdi():
    global pixelValue
    global rowSize,columnSize
    global levialdiLayerCounter
    global levialdiIter

    emptyLev = deepcopy(pixelValue)
    levialdiMap = deepcopy(pixelValue)

    '''
    npArr = np.array(pixelValue)
    (nrow, ncol) = npArr.shape
    
    print("numpy : ", nrow, ncol)
    print("arr : ", rowSize, columnSize)
    '''

    tap = True
    while tap:
        tap = False
        #for i in range(s, 0, -1):
            #for j in range(t, columnSize - 1):


        for i in range(rowSize - 2, 0, -1):
            for j in range(1, columnSize - 1):

                emptyLev[i][j] = levialdiMap[i][j]


                up= levialdiMap[i - 1][j]
                right= levialdiMap[i][j + 1]
                upRight= levialdiMap[i - 1][j + 1]
                upLeft= levialdiMap[i - 1][j - 1]

                self= levialdiMap[i][j]

                down= levialdiMap[i + 1][j]
                left= levialdiMap[i][j - 1]
                downLeft= levialdiMap[i + 1][j - 1]
                downRight= levialdiMap[i + 1][j + 1]




                if self == 1:
                    if (left + down + downLeft) == 0:
                        if (up + right + upRight + upLeft + downRight) == 0:
                            emptyLev[i][j] = 0
                            levialdiLayerCounter += 1
                            tap = True
                        else:
                            emptyLev[i][j] = 0
                            tap = True
                else:
                    if (left + down) == 2:
                        emptyLev[i][j] = 1
                        tap = True



        levialdiMap = deepcopy(emptyLev)

        levialdiIter += 1
        updateResult("levialdi")

        global bin1
        bin1.select_clear()
        bin1.delete("bin1")

        txarray1 = ""

        for i in range(rowSize):
            for j in range(columnSize):
                print(levialdiMap[i][j], end='')  # Print w/b pixel map
                txarray1 += str(levialdiMap[i][j])
                # Label(bin1, borderwidth=1, bg="white", text=str(pixelValue[i][j])).grid(row=j, column=i, padx=1, pady=1)
            print("")
            txarray1 += "\n"
        print("")
        print("---------------------------------------")
        print("")
        bin1.create_text(200, 200, text=txarray1, font=("Times New Roman", arrayFont), tag="bin1")  # "Times New Roman" , "bold" , Avenir , purisa
        bin1.update()


        '''
        
        for r in range(rowSize):
            for c in range(columnSize):
                print(levialdiMap[r][c], end="")
            print("")

        
        print(" iter : ", iter)
        print("-------------")
        print("")
        '''

    print("")
    print("total count : ", levialdiLayerCounter)

    writeResult("levialdi")


def binary_image():
    Value = 1
    nrow = 100
    ncol = 100
    x, y = np.indices((nrow, ncol))
    mask_lines = np.zeros(shape=(nrow,ncol))

    x0, y0, r0 = 30, 30, 3
    x1, y1, r1 = 70, 30, 10
    x2, y2, r2 = 10, 10, 10


    for i in range (50, 70):
        mask_lines[i][i] = 1
        mask_lines[i][i + 1] = 1
        mask_lines[i][i + 2] = 1
        mask_lines[i][i + 3] = 1
        mask_lines[i][i + 6] = 1

    mask_circle1 = np.abs((x - x0) ** 2 + (y - y0) ** 2 - r0 ** 2 ) <= 5
    mask_square1 = np.fmax(np.absolute( x - x1), np.absolute( y - y1)) <= r1
    mask_square2 = np.fmax(np.absolute( x - x2), np.absolute( y - y2)) <= r2
    #mask_square3 = np.fmax(np.absolute( x - x3), np.absolute( y - y3)) <= r3
    #mask_square4 =  np.fmax(np.absolute( x - x4), np.absolute( y - y4)) <= r4
    #imge = np.logical_or ( np.logical_or(mask_lines, mask_circle1), mask_square1) * Value
    imge = np.logical_or(mask_circle1, mask_square2) * Value

    return imge


def createImage():
    global pix
    global openedImage

    pix = binary_image()

    openedImage = Image.new('RGB', (100, 100), color='white')

    for r in range(100):
        for c in range(100):
            if pix[r,c] == 0:
                openedImage.putpixel((r, c), (0,0,0))

    openedImage = openedImage.convert('1', dither=Image.NONE)

    Reset()
    global fileName
    fileName = "self made image"
    imageProcess()


#LEVIALDI RESULT BOARD
res1 = Label(window, borderwidth=2, bg="white", fg="black", bd=3, relief="groove")
res1.grid(row=1, column=2, sticky=W+E+N+S)


Label(res1, text="LEVIALDI", borderwidth=1, bg="white", fg="black", bd=3, relief="groove").grid(row=0, padx=160, pady=10)
Label(res1, text="RUN", borderwidth=1, bg="white", fg="black", bd=3, relief="groove").grid(row=1, padx=160, pady=10)
Label(res1, text="NCC : \n ITER : ", borderwidth=1, bg="white", fg="black", bd=3, relief="groove").grid(row=2, padx=160, pady=40)
Label(res1, text="CURRENT ITER", borderwidth=1, bg="white", fg="black", bd=3, relief="groove").grid(row=3, padx=160, pady=100)



lvTag = Canvas(res1, borderwidth=2, bg="white", bd=3, relief="groove", width=160, height=40)
lvButtonTab = Button(res1, text='RUN', borderwidth=1, command=runLevialdi, relief=RAISED)

lvButtonTabImg = ImageTk.PhotoImage(file= "."+os.path.sep+"images"+os.path.sep+"run.png")
lvButtonTab.config(image=lvButtonTabImg)
lvButtonTab.image = lvButtonTabImg

lvResult = Canvas(res1, borderwidth=2, bg="white", bd=3, relief="groove", width=160, height=40)
runIter = Canvas(res1, borderwidth=2, bg="white", bd=3, relief="groove", width=160, height=40)

lvTag.grid(row=0, column=0, sticky=W + E + N + S)
lvButtonTab.grid(row=1, column=0, sticky=W + E + N + S)
lvResult.grid(row=2, column=0, sticky=W + E + N + S)
runIter.grid(row=3, column=0, sticky=W + E + N + S)

lvTag.create_text(200,25, text="LEVIALDI", font=("Times New Roman", titleSize, "bold"), tag="lvTag")  # "Times New Roman" , "bold"
lvTag.update()
#LEVIALDI RESULT BOARD END

#TSF RESULT BOARD
res2 = Label(window, borderwidth=2, bg="white", fg="black", bd=3, relief="groove")
res2.grid(row=2, column=2, sticky=W+E+N+S)
#TSF RESULT BOARD END




















#UP MENU
menu = Menu(window)#Simple file, edit and operation menu
window.config(menu = menu)
fileMenu = tk.Menu(menu)


menu.add_cascade(label = "File", menu = fileMenu)

fileMenu.add_command(label ="Open", command = openFile, accelerator="Ctrl+O")
fileMenu.add_command(label ="Create", command = createImage, accelerator="Ctrl+O")

fileMenu.add_command(label ="Save", command = saveFile, accelerator="Ctrl+S")


fileMenu.add_separator()


fileMenu.add_command(label ="Exit", command = window.destroy, accelerator="Ctrl+Q")
#UP MENU END

#SHORTCUTS
def ctrls(self):
    print(self)
    saveFile()

window.bind("<Control-s>", ctrls)
window.bind("<Control-S>", ctrls)

def ctrlq(self):
    print(self)
    sys.exit()

window.bind("<Control-q>", ctrlq)
window.bind("<Control-Q>", ctrlq)

def ctrlo(self):
    print(self)
    openFile()

window.bind("<Control-o>", ctrlo)
window.bind("<Control-O>", ctrlo)
#SHORTCUTS END


window.mainloop()
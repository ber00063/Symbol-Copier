# @author Ashton Berg
#

from tkinter import * 
import pyperclip as pc

root = Tk()
root.title("symbol copier")
#root.geometry("100x320")

#nameLabel = Label(root, text="baller")
#nameLabel.pack()
##nameLabel.grid(row=0, column=0)


#Dictonary storing the unicode to symbol conversions
#Each entry has the unicode value in hex hardcoded
#The hex value gets converted to an int 
#The chr() function converts the int to its corresponding unicode character and returns it
symbolsDict = {
    #"gt": chr(int("003E", 16)),     
    "gte": chr(int("2265", 16)),    
    #"lt": chr(int("003C", 16)),     
    "lte": chr(int("2264", 16)),    
    "pi": chr(int("03C0", 16)),     
    "delta": chr(int("03B4", 16)),  
    "Delta": chr(int("0394", 16)),  
    "sigma": chr(int("03C3", 16)),  
    "Sigma": chr(int("03A3", 16)),   
    "union": chr(int("222A", 16)),  
    "intersection": chr(int("2229", 16)),   
    "implies": chr(int("21D2", 16)),    
    "or": chr(int("2228", 16)),     
    "not": chr(int("00AC", 16))    
}

#Text box for messages
T = Text(root, height = 1, width = 20)

#Function for button click, copies clicked symbol
def myClick(symbol):
    pc.copy(symbol)
    T.delete("1.0", END)
    T.insert(INSERT, "\"" + symbol + "\" symbol copied")



#Function for symbol search
#Copies searched symbol if found
#Clears clipboard if not found
def searchClick(input):
    T.delete("1.0", END)
    if input in symbolsDict:
        pc.copy(symbolsDict[input])
        T.insert(INSERT, "\"" + symbolsDict[input] + "\" symbol copied")
    else:
        pc.copy("")
        if input.__eq__(""):
            T.insert(INSERT, "no symbol given")
        else:
            T.insert(INSERT, "symbol not found")



#Quick Search Box and Copy Button
e = Entry(root)
searchButton = Button(root, text="search and copy", command=lambda: searchClick(e.get()))

#Greater Than or Equal 
greaterThanEqualButton = Button(root, text=symbolsDict["gte"], command=lambda: myClick(symbolsDict["gte"]))

#Less Than or Equal
lessThanEqualButton = Button(root, text=symbolsDict["lte"], command=lambda: myClick(symbolsDict["lte"]))

#Pi
piButton = Button(root, text=symbolsDict["pi"], command=lambda: myClick(symbolsDict["pi"]))

#Lowercase Delta
lowerDeltaButton = Button(root, text=symbolsDict["delta"], command=lambda: myClick(symbolsDict["delta"]))

#Uppercase Delta
upperDeltaButton = Button(root, text=symbolsDict["Delta"], command=lambda: myClick(symbolsDict["Delta"]))

#Lowercase Sigma
lowerSigmaButton = Button(root, text=symbolsDict["sigma"], command=lambda: myClick(symbolsDict["sigma"]))

#Uppercase Sigma
upperSigmaButton = Button(root, text=symbolsDict["Sigma"], command=lambda: myClick(symbolsDict["Sigma"]))

#Union 
unionButton = Button(root, text=symbolsDict["union"], command=lambda: myClick(symbolsDict["union"]))

#Intersection 
intersectionButton = Button(root, text=symbolsDict["intersection"], command=lambda: myClick(symbolsDict["intersection"]))

#Implies 
impliesButton = Button(root, text=symbolsDict["implies"], command=lambda: myClick(symbolsDict["implies"]))

#Logical Or
orButton = Button(root, text=symbolsDict["or"], command=lambda: myClick(symbolsDict["or"]))

#Not Symbol
notButton = Button(root, text=symbolsDict["not"], command=lambda: myClick(symbolsDict["not"]))

#Exit Program
quitButton = Button(root, text="Exit", command=root.quit)



#Pack all buttons and text box
#I was going to use the .grid() function to align the buttons horizontlly and vertically, but I actually liked
# the vertical layout that .pack() automatically creates. It makes it easy to just keep it on the side of my 
# current tab, and keeps the program really simple.
e.pack()
searchButton.pack()
greaterThanEqualButton.pack()
lessThanEqualButton.pack()
piButton.pack()
lowerDeltaButton.pack()
upperDeltaButton.pack()
lowerSigmaButton.pack()
upperSigmaButton.pack()
unionButton.pack()
intersectionButton.pack()
impliesButton.pack()
orButton.pack()
notButton.pack()
quitButton.pack()
T.pack()


root.mainloop()
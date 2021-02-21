import os
import hashlib
import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("BTC Private Key Finder")
        root.iconbitmap('btc.ico')
        global GLineEdit_557,GLabel_342,GLabel_693,GLabel_25
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_206=tk.Button(root)
        GButton_206["activebackground"] = "#90ee90"
        GButton_206["anchor"] = "center"
        GButton_206["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_206["font"] = ft
        GButton_206["fg"] = "#000000"
        GButton_206["justify"] = "center"
        GButton_206["text"] = "search"
        GButton_206["relief"] = "ridge"
        GButton_206.place(x=460,y=80,width=109,height=51)
        GButton_206["command"] = GButton_206_command

        GLineEdit_557=tk.Entry(root)
        GLineEdit_557["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_557["font"] = ft
        GLineEdit_557["fg"] = "#333333"
        GLineEdit_557["justify"] = "center"
        GLineEdit_557["text"] = "Entry"
        GLineEdit_557.place(x=10,y=80,width=440,height=51)

        GLabel_342=tk.Label(root)
        GLabel_342["activebackground"] = "#999999"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_342["font"] = ft
        GLabel_342["fg"] = "#e62a2a"
        GLabel_342["justify"] = "center"
        GLabel_342["text"] = "Primary key"
        GLabel_342.place(x=0,y=450,width=596,height=46)

        GLabel_693=tk.Label(root)
        GLabel_693["activebackground"] = "#999999"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_693["font"] = ft
        GLabel_693["fg"] = "#1760f1"
        GLabel_693["justify"] = "center"
        GLabel_693["text"] = "Address"
        GLabel_693.place(x=0,y=360,width=595,height=49)

        GLabel_453=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_453["font"] = ft
        GLabel_453["fg"] = "#333333"
        GLabel_453["justify"] = "center"
        GLabel_453["text"] = "Address match"
        GLabel_453.place(x=10,y=350,width=88,height=30)

        GLabel_452=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_452["font"] = ft
        GLabel_452["fg"] = "#333333"
        GLabel_452["justify"] = "center"
        GLabel_452["text"] = "Primary key found"
        GLabel_452.place(x=0,y=430,width=119,height=30)

        GLabel_356=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_356["font"] = ft
        GLabel_356["fg"] = "#333333"
        GLabel_356["justify"] = "center"
        GLabel_356["text"] = "Enter wallet address"
        GLabel_356.place(x=0,y=50,width=132,height=30)

        GLabel_857=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_857["font"] = ft
        GLabel_857["fg"] = "#333333"
        GLabel_857["justify"] = "center"
        GLabel_857["text"] = "Search"
        GLabel_857.place(x=0,y=230,width=70,height=25)

        GLabel_25=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_25["font"] = ft
        GLabel_25["fg"] = "#333333"
        GLabel_25["justify"] = "center"
        GLabel_25["text"] = "Address_Search"
        GLabel_25.place(x=70,y=230,width=525,height=25)
        
        GButton_609=tk.Button(root)
        GButton_609["bg"] = "#f51717"
        ft = tkFont.Font(family='Times',size=18)
        GButton_609["font"] = ft
        GButton_609["fg"] = "#393d49"
        GButton_609["justify"] = "center"
        GButton_609["text"] = "X"
        GButton_609.place(x=540,y=10,width=40,height=40)
        GButton_609["command"] = GButton_609_command

def GButton_609_command():
    global start
    start =False

def GButton_206_command():
    global start
    start =True
    key_to_find=GLineEdit_557.get()
    while start:
        randomBytes = os.urandom(32)
        Address= getPublicKey(randomBytes)
        Privkey = getWif(randomBytes)
        GLabel_25.config(text=Address)
        root.update()
        if key_to_find in Address:
            writeFile(Address, Privkey)
            GLabel_693.config(text=Address)
            GLabel_342.config(text=Privkey)
            root.update()
            print ("----------------")
            print("search: " + key_to_find)
            print("Address: " + Address)
            print("Privkey: " + Privkey)
            print ("----------------")
            break





def sha256(data):
    digest = hashlib.new("sha256")
    digest.update(data)
    return digest.digest()


def ripemd160(x):
    d = hashlib.new("ripemd160")
    d.update(x)
    return d.digest()


def b58(data):
    B58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

    if data[0] == 0:
        return "1" + b58(data[1:])

    x = sum([v * (256 ** i) for i, v in enumerate(data[::-1])])
    ret = ""
    while x > 0:
        ret = B58[x % 58] + ret
        x = x // 58

    return ret


class Point:
    def __init__(self,
        x=0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
        y=0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8,
        p=2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 1):
        self.x = x
        self.y = y
        self.p = p

    def __add__(self, other):
        return self.__radd__(other)

    def __mul__(self, other):
        return self.__rmul__(other)

    def __rmul__(self, other):
        n = self
        q = None

        for i in range(256):
            if other & (1 << i):
                q = q + n
            n = n + n

        return q

    def __radd__(self, other):
        if other is None:
            return self
        x1 = other.x
        y1 = other.y
        x2 = self.x
        y2 = self.y
        p = self.p

        if self == other:
            l = pow(2 * y2 % p, p-2, p) * (3 * x2 * x2) % p
        else:
            l = pow(x1 - x2, p-2, p) * (y1 - y2) % p

        newX = (l ** 2 - x2 - x1) % p
        newY = (l * x2 - l * newX - y2) % p

        return Point(newX, newY)

    def toBytes(self):
        x = self.x.to_bytes(32, "big")
        y = self.y.to_bytes(32, "big")
        return b"\x04" + x + y


def getPublicKey(privkey):
    SPEC256k1 = Point()
    pk = int.from_bytes(privkey, "big")
    hash160 = ripemd160(sha256((SPEC256k1 * pk).toBytes()))
    address = b"\x00" + hash160

    address = b58(address + sha256(sha256(address))[:4])
    return address


def getWif(privkey):
    wif = b"\x80" + privkey
    wif = b58(wif + sha256(sha256(wif))[:4])
    return wif
    
def writeFile(myK, mypk):
    f = open("BTC_gen2_output.txt", "a")
    f.write(str(myK) + "\t" + str(mypk) + "\n")
    f.close()

if __name__ == "__main__":
    global start
    start =False
    root=tk.Tk()
    app = App(root)
    root.mainloop()

from tkinter import *
root = Tk()
grad = StringVar()
grad6 = StringVar()
grad7 = StringVar()
sedamh = StringVar()
sedamm = StringVar()
sedamst = StringVar()
sedamp = StringVar()
sedamg = StringVar()
grad8 = StringVar()
osamh = StringVar()
osamm = StringVar()
osamst = StringVar()
osamp = StringVar()
osamg = StringVar()
dodatni = StringVar()


def calc():
    sum= float(grad.get()) + float(grad6.get()) + float(grad7.get()) + float(sedamh.get()) + float(sedamm.get()) + float(sedamst.get()) + float(sedamp.get()) + float(sedamg.get()) + float(grad8.get()) + float(osamh.get()) + float(osamm.get()) + float(osamst.get()) + float(osamp.get()) + float(osamg.get()) + float(dodatni.get())
    Label(root,text=(sum)).grid(row=3,column=5)

  
Label(root,text="prosjek 5.razreda").grid(row=0,column=0)
Entry(root,textvariable=grad).grid(row=0,column=1)

Label(root,text="prosjek 6.razreda").grid(row=1,column=0)
Entry(root,textvariable=grad6).grid(row=1,column=1)

Label(root,text="prosjek 7.razreda").grid(row=2,column=0)
Entry(root,textvariable=grad7).grid(row=2,column=1)

Label(root,text="prosjek ocjena Hrvatskoga jezika 7.razreda").grid(row=3,column=0)
Entry(root,textvariable=sedamh).grid(row=3,column=1)

Label(root,text="prosjek ocjena Matematike 7.razreda").grid(row=4,column=0)
Entry(root,textvariable=sedamm).grid(row=4,column=1)

Label(root,text="prosjek ocjena Stranog jezika 7.razreda").grid(row=5,column=0)
Entry(root,textvariable=sedamst).grid(row=5,column=1)

Label(root,text="prosjek ocjena Povijesti 7.razreda").grid(row=6,column=0)
Entry(root,textvariable=sedamp).grid(row=6,column=1)

Label(root,text="prosjek ocjena Geografije 7.razreda").grid(row=7,column=0)
Entry(root,textvariable=sedamg).grid(row=7,column=1)

Label(root,text="prosjek 8.razreda").grid(row=8,column=0)
Entry(root,textvariable=grad8).grid(row=8,column=1)

Label(root,text="prosjek ocjena Hrvatskoga jezika 8.razreda").grid(row=9,column=0)
Entry(root,textvariable=osamh).grid(row=9,column=1)

Label(root,text="prosjek ocjena Matematike 8.razreda").grid(row=10,column=0)
Entry(root,textvariable=osamm).grid(row=10,column=1)

Label(root,text="prosjek ocjena Stranog jezika 8.razreda").grid(row=11,column=0)
Entry(root,textvariable=osamst).grid(row=11,column=1)

Label(root,text="prosjek ocjena Povijesti 8.razreda").grid(row=12,column=0)
Entry(root,textvariable=osamp).grid(row=12,column=1)

Label(root,text="prosjek ocjena Geografije 8.razreda").grid(row=13,column=0)
Entry(root,textvariable=osamg).grid(row=13,column=1)

Label(root,text="Dodatni bodovi").grid(row=14,column=0)
Entry(root,textvariable=dodatni).grid(row=14,column=1)

Button(root,text="Izračunaj bodove",command=calc).grid(row=0,column=5)

root.mainloot()

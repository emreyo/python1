import Tkinter
import pickle

class std:
	def __init__(self, nm, sn, sn, cn, cpga):
		self.name = nm
		self.surname = sn
		self.stdNum = sn
		self.classNum = cn
		self.cGpa = cpga

	def writeStudent(self):
		print "Student name : ", self.name
		print "Student surname: ", self.surname
		print "Student number: ", self.stdNum
		print "Student class number: ", self.classNum
		print "Student CGPA: ", self.cGpa
		
class simpleapp_tk(Tkinter.Tk):
	
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.k = 0
		self.sList = []
		
		self.initialize()

	def initialize(self):
		self.grid()
		if self.k == 0 :
			self.stdNameVar = ""
			self.stdSNameVar = ""
			self.stdNumVar = ""
			self.stdCNumVar = ""
			self.stdCGPAVar = ""
		else:
			self.stdNameVar = self.sList[self.k-1].name
			self.stdSNameVar = self.sList[self.k-1].surname
			self.stdNumVar = self.sList[self.k-1].stdNum
			self.stdCNumVar = self.sList[self.k-1].classNum
			self.stdCGPAVar = self.sList[self.k-1].cGpa
			

		previousButton = Tkinter.Button(self,text=u"< Previous", command=self.Previous)
		previousButton.grid(column=0, row=0, sticky='EW')

		nextButton = Tkinter.Button(self,text=u"Next   >", command=self.Next)
		nextButton.grid(column=1, row=0, sticky='EW')

		self.stdNameL = Tkinter.StringVar()
		label = Tkinter.Label(self, textvariable=self.stdNameL, anchor="w", fg="white",bg="gray")
		label.grid(column=0, row=1, columnspan=2, sticky='EW')
		self.stdNameL.set(u"Student Name: ")

		self.stdName = Tkinter.StringVar()
		self.entry = Tkinter.Entry(self, textvariable = self.stdName, bg = "gray")
		self.entry.grid(column=2,row=1,sticky='EW')
		self.stdName.set(self.stdNameVar)

		addButton = Tkinter.Button(self,text=u"Add", command=self.Add)
		addButton.grid(column=3, row=1, sticky='EW')

		self.stdSNameL = Tkinter.StringVar()
		label = Tkinter.Label(self, textvariable=self.stdSNameL, anchor="w", fg="white",bg="gray")
		label.grid(column=0, row=2, columnspan=2, sticky='EW')
		self.stdSNameL.set(u"Student surname: ")

		self.stdSName = Tkinter.StringVar()
		self.entry = Tkinter.Entry(self, textvariable = self.stdSName, bg = "gray")
		self.entry.grid(column=2,row=2,sticky='EW')
		self.stdSName.set(self.stdSNameVar)

		modifyButton = Tkinter.Button(self,text=u"Modify", command=self.Modify)
		modifyButton.grid(column=3, row=2, sticky='EW')

		self.stdNumL = Tkinter.StringVar()
		label = Tkinter.Label(self, textvariable=self.stdNumL, anchor="w", fg="white",bg="gray")
		label.grid(column=0, row=3, columnspan=2, sticky='EW')
		self.stdNumL.set(u"Student Number: ")

		self.stdNum = Tkinter.StringVar()
		self.entry = Tkinter.Entry(self, textvariable = self.stdNum, bg = "gray")
		self.entry.grid(column=2,row=3,sticky='EW')
		self.stdNum.set(self.stdNumVar)

		deleteButton = Tkinter.Button(self,text=u"Delete", command=self.Delete, bg = "red")
		deleteButton.grid(column=3, row=3, sticky='EW')

		self.stdCNumL = Tkinter.StringVar()
		label = Tkinter.Label(self, textvariable=self.stdCNumL, anchor="w", fg="white",bg="gray")
		label.grid(column=0, row=4, columnspan=2, sticky='EW')
		self.stdCNumL.set(u"Student Class Number: ")

		self.stdCNum = Tkinter.StringVar()
		self.entry = Tkinter.Entry(self, textvariable = self.stdCNum, bg = "gray")
		self.entry.grid(column=2,row=4,sticky='EW')
		self.stdCNum.set(self.stdCNumVar)

		pickleButton = Tkinter.Button(self,text=u"Pickle", command=self.Pickle)
		pickleButton.grid(column=3, row=4, sticky='EW')

		self.stdCGPAL = Tkinter.StringVar()
		label = Tkinter.Label(self, textvariable=self.stdCGPAL, anchor="w", fg="white",bg="gray")
		label.grid(column=0, row=5, columnspan=2, sticky='EW')
		self.stdCGPAL.set(u"Student CGPA: ")

		self.stdCGPA = Tkinter.StringVar()
		self.entry = Tkinter.Entry(self, textvariable = self.stdCGPA, bg = "gray")
		self.entry.grid(column=2,row=5,sticky='EW')
		self.stdCGPA.set(self.stdCGPAVar)

		unPickleButton = Tkinter.Button(self,text=u"Unpickle", command=self.unPickle)
		unPickleButton.grid(column=3, row=5, sticky='EW')
		
		self.grid_columnconfigure(0,weight=1)
		self.resizable(True,False)
		self.update()
		self.geometry(self.geometry())       
		self.entry.focus_set()
		self.entry.selection_range(0, Tkinter.END)

	def Add(self):
		name = self.stdName.get()
		surname = self.stdSName.get()
		num = self.stdNum.get()
		cnum = self.stdCNum.get()
		cgpa = self.stdCGPA.get()

		newObj = std(name, surname, num, cnum, cgpa)
		self.sList.insert(self.k, newObj)
		self.k = self.k + 1

	def Pickle(self):
		file = open('savedObj', 'w')
		pickle.dump(self.sList, file)
		file.close()
		
	def unPickle(self):
		unPickleFile = open('savedObj', 'r')
		self.sList = pickle.load(unPickleFile)
		unPickleFile.close()
		self.k = self.k + 1
		self.initialize()
		
	def Delete(self):
		if self.k != 0:
			del self.sList[self.k-1]
			if self.k == 1:
				self.k = self.k + 1
			elif self.k == len(self.sList):
				self.k = self.k - 1
			self.initialize()
		else:
			print "No input to delete"

	def Modify(self):
		if self.k != 0:
			name = self.stdName.get()
			surname = self.stdSName.get()
			num = self.stdNum.get()
			cnum = self.stdCNum.get()
			cgpa = self.stdCGPA.get()

			self.sList[self.k-1].__init__(name, surname, num, cnum, cgpa)
		else:
			print "No input to modify"
	def Previous(self):
		if self.k != 1 and self.k > 0: # or self.k-1 != 0 (k = realIndex+1 actually)
			self.k = self.k-1
			self.initialize()

	def Next(self):
		if self.k != len(self.sList):
			self.k = self.k + 1
			self.initialize()

if __name__ == "__main__":
	app = simpleapp_tk(None)
	app.maxsize(500, 500)
	app.title('Student')
	app.mainloop()


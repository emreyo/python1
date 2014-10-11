# emreyo
case = raw_input("Input L for load, S for save: ")
if case == 'L':
	import first
	import pickle
	openFile = raw_input("Enter file name: ")
	unpicklefile = open(openFile, 'r')
	unpickledlist = pickle.load(unpicklefile)
	unpicklefile.close()
	for first.obj in unpickledlist:
		print first.obj.writeStudent()
elif case == 'S':
	import second
	import pickle
	file = open('savedobject', 'w')
	pickle.dump(second.sList, file)
	file.close()
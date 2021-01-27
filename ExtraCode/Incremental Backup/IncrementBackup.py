import zipfile
import os
import os.path as op
import fnmatch
import hashlib
import sys
import shutil

# Class for the nodes
class ListNode:

	def __init__(self, b, i):
		self.data = md5_a_file(b)
		self.path = op.abspath(b)
		self.shortPath = str(i) +"\\" + b
		self.next = None # Set Reference (Following Node)
		self.foldNumb = i # Sets the archive count number
		self.original = True # Writting file or not
		self.origin = "-" # File path based on
		self.dest = "-" # Destination path written to 
		self.delete = False # Last file so must be deleted 
		
	def get_data(self):
		return self.data

	def has_value(self, value): # Compares the value with node value
		return self.data == value

	def printNode(self): # Print data about nodes
		print("Original\tPath\t\tDelete\tCopy\tSource\t\tDestination")
		print(("YES" if self.original else "NO") +"\t\t"+ self.shortPath,end="\t")
		print(("YES" if self.delete else "NO"), end="\t")
		print(self.origin +"\t" +  self.dest)

	def update(self): # Update some values (Makes easier to read)
		self.delete = self.origin != self.dest and self.dest != "-"
		self.original = self.dest == "-" and self.origin == "-"
		
# The linked list
class SingleLinkedList:
	def __init__(self): 
		self.head = None # Making a null first pointer
		self.tail = None

	def add_list_item(self, item): # Adds item to the end of the list
		if not isinstance(item, ListNode):
			item = ListNode(item)
		if self.head is None:
			self.head = item
		else:
			self.tail.next = item
		self.tail = item

	def list_length(self): # Returns size of list
		count = 0
		current_node = self.head
		while current_node is not None:
			count = count + 1
			current_node = current_node.next
		return count

	def printList(self): # Prints Node values
		current_node = self.head        
		while current_node is not None:
			print(current_node.data + " " + current_node.path)
			current_node = current_node.next

	def unordered_search (self, value): # Searches List for Node with data equal to value        
		current_node = self.head # Starting at the head
		node_id = 1 # Position
		while current_node is not None:
			if current_node.has_value(value): # First found index of matching value
				return node_id
			current_node = current_node.next # Move to next node
			node_id = node_id + 1
		return -1

	def remove_list_item_by_id(self, item_id): # Remove node with id for data
		current_id = 1
		current_node = self.head
		previous_node = None
		while current_node is not None:
			if current_id == item_id:
				# if this is the first node (head)
				if previous_node is not None:
					previous_node.next = current_node.next
				else:
					self.head = current_node.next
					# we don't have to look any further
					return
			# needed for the next iteration
			previous_node = current_node
			current_node = current_node.next
			current_id = current_id + 1
		return

# MD5 a file based on chunks
def md5_a_file(filePath, block_size=128 * 16):
	md5 = hashlib.md5()
	f = open(filePath, "rb")
	while True:
		data = f.read(block_size)
		if not data:
			break
		md5.update(data)
	return md5.hexdigest()

""" Returns the any files in the directory and subdirectories
	that match the file pattern of pattern """
def printFiles(folderpath, pattern):
	x = []
	listOfFiles = os.listdir(folderpath)
	for entry in listOfFiles:
		if fnmatch.fnmatch(entry, pattern):
			x.append(entry)
		if op.isdir(entry): # This is if you have zip files further than target folder
			print("I found another folder. Might hold another zip file.")
#			print("I am lazy though so I am going to ignore it")
	return x

""" Sorts files based on the date instead of names
	An example is 2-1-20 is before 2-10-20 """
def sortDates(files): 
	fin = []
	i = 0
	fileName = files[0].rfind(" ")
	# Can turn these into tuplets later on
	while len(files) != 0:
		min = files[0]
		minTime = min[fileName:].split("-")
		for d in files:
			curTime = d[fileName:].split("-")
			if int(curTime[2][:-4]) <= int(minTime[2][:-4]): # TX Year is earlier or same as minimum
				if int(curTime[0]) <= int(minTime[0]): # TX month is earlier or same as minimum
					if int(curTime[1]) < int(minTime[1]): # Tx day is earlier than minimum
						min = d
						minTime = d[fileName:].split("-")
		fin.append(min) # Put minimum into array
		files.remove(min) # Remove minimum
	return fin


""" Gets if a value is found in the list. If it is returns which index """
def linkedFind(lists, value):
	count = 0
	for a in lists:
		if a== None:
			return -1
		c = a.unordered_search(value)
		if c >= 0: # element exist
			return count
		else:
			count+=1
	return -1 # It was not found

def printGrid(grid):
	for u in grid:
		u.printList()
		print("")

def getFiles(fp): # Files Path
	x = []
	y = os.listdir(fp)
#	print(op.abspath(fp))
	while len(y) > 0:
		cur = y[0]
#		print(op.abspath(cur))
		if op.isdir(cur):
			tmp = os.listdir(cur)
			for t in tmp:
				y.append(cur +"\\" +  t) # Added for files in folder (cur)
		elif op.isfile(cur):
			x.append(cur)
		else: # For errors
			x.append(cur)
		y.remove(cur)
#	print(x)
	return x

""" Returns the file name without the date or extension """
def parseName(a): 
	b = a.rfind(" ")
	return a[:b]

def findNames(fl): # Finds the compatable file names
	result = []
	for f in fl:
		tempFile = parseName(f)
		if tempFile not in result:
			result.append(tempFile)
#		if tempFile in result:
#			print(tempFile + " is already valid archive")
#		else:
#			print(tempFile + " is a new archive adding to list")
#			result.append(tempFile)
	return result

""" Compresses the file main file """
def compress():
	workspace = input("Enter the folder reading from: ")
#	workspace = "TestData"
	sets = printFiles(workspace, '*.zip') # Get valid zip files
	resultName = findNames(sets)
	print()
	choice = -1
	if len(resultName) == 1: # Only one option
		tempName = resultName[0]
		print("Archive of " + tempName + " is being assembled")
	else: # Must choose option
		print("How lucky for us. We are given " + str(len(resultName)) + " options")
		print("Select one of the ones below")
		# Could add a way to try and predict what saying
		# EX: taht is corrected to that
		while choice < 0:
			for rn in range(0, len(resultName), 1):
				 print(str(rn) + ". " + resultName[rn])
#			choice = "0"
			choice = input("Enter the number of the file you want: ")
			try:
				choice = int(choice) # Try is for this statement
				if choice >= 0 and choice< len(resultName):
					print("Thanks for entering a valid number")
					
			except:
				print("That is not nice of you. You entered an invalid number")
				print("Checking to see if I can figure it out")
				for rp in resultName:
					if choice == rp:
						print("I think I figured it out despite you not following my directions")
						choice = resultName.index(choice)
						print("I an going with files asscociated with number " + str(choice))
				if type(choice) is not int:
					print("Nope you really screwed up. Try again")
					choice = -1
				else:
					if choice < 0:
						print("At least you entered an integer.... It is not valid so try again")
						choice = -1
				print()
		print("Removing zip filles not being processed from array")
		con = 0
		for fl in sets:
			if parseName(fl) != resultName[choice]:
				sets.remove(fl)
				con+= 1
		print("I have removed " + str(con) + " files from the array")
		print()
		if True: # Cleaning
			del rn
			del fl
			del con
	if True: # Cleaning
		del choice
		del resultName

	sets = sortDates(sets)

	# Since they are zip have to extract them
	# Adjust later for temporary folders
	for i in range(0, len(sets) , 1):
		# Create target Directory if don't exist
		dirName = "Output\\" + str(i)
		if not op.exists(dirName):
			os.makedirs(dirName) # For multiple

		zipfile.ZipFile(workspace + "\\" + sets[i]).extractall(dirName)
#		print("Extraction of " + sets[i] + " complete")
		print(str((i/(len(sets)))*100)+ "  %")
	
	grid = []
	fileContent = [] # For what is going to be written to the file
	os.chdir("Output\\0")
	# Getting all the files set into nodes and stuff
	print("Creating Nodes and adding to an array of LinkedList")
	for i in range(0, len(sets) , 1):
		os.chdir("..\\" + str(i))
		# print("Changing workspace to " + os.getcwd())
		baseFiles = getFiles(".") # What comparing everything to
#		print("Creating Nodes and adding to an array of LinkedList")
		for b in baseFiles: 
			q = ListNode(b,i)
			itemIndex = linkedFind(grid, q.get_data())
			if itemIndex >= 0: # It was found
				grid[itemIndex].add_list_item(q)
			else: # Adds the new item
				qs = SingleLinkedList()
				qs.add_list_item(q)
				grid.append(qs)
	print("I have sucessfully populated the array")
	print()
	os.chdir("..\\")
	if True: # Cleaning Up
		del q
		del b
		del itemIndex
		del dirName

	allFiles=[] # all the list nodes of files ( DO I need?)
# Modify so I can based on last one 
# EX: Original is 0 for 1 and 1 for 2 and 2 for 3 instead of 0 for 1,2,3
	for g in grid:
		current_node = g.head
		current_node.update()
		allFiles.append(current_node)
		originalFile = current_node.shortPath
		while current_node.next is not None:
			current_node= current_node.next
			current_node.origin = originalFile
			current_node.dest = current_node.shortPath
			current_node.update()
			allFiles.append(current_node)
	if True: # Cleaning
		del current_node
		del g

	os.chdir("..\\")
	if not op.exists(workspace + "_comp\\"):
		os.mkdir(workspace + "_comp\\")
	os.chdir(workspace + "_comp\\")
	changesFile = open("stat.txt", "w") # Changes File

	for i in range(0, len(sets) , 1): # Can add something here to make sure it doesn't miss any deleted
		deleteExist = True
		while deleteExist:
			deleteExist = False
			for af in allFiles: # Delete the unwanted files
				if af.delete:
					deleteExist = True
					changesFile.write(af.origin + " " + af.dest + "\n")
					os.remove(af.path)
					allFiles.remove(af)

		af = allFiles[len(allFiles)-1]
		if af.delete: # For the last file
			changesFile.write(af.origin + " " + af.dest + "\n")
			os.remove(af.path)
			allFiles.remove(af)
		changesFile.flush()

		with zipfile.ZipFile(sets[i], 'w') as myzip: # Compressing Files again
			for alf in allFiles:
				if alf.foldNumb == i:
					arcName = alf.shortPath[alf.shortPath.find("\\")+1:]
					myzip.write(alf.path, arcName)
					allFiles.remove(alf)
			changesFile.flush()
			alf = allFiles[len(allFiles)-1]
			if alf.foldNumb == i: # For the last element
				arcName = alf.shortPath[alf.shortPath.find("\\")+1:]
				myzip.write(alf.path, arcName)
				allFiles.remove(alf)
			myzip.write("stat.txt", "stat.abby")

		print(str((i/(len(sets)))*100)+ "  %")
	changesFile.flush()
	changesFile.close()
	delFile.flush()
	delFile.close()
	if False: # Cleaning
		del af
		del alf
		del allFiles
		del arcName
		del baseFiles
		del changesFile
		del fileContent
		del grid
		del i
		del myzip
		del originalFile
		del qs
		del sets
		del tempName
		del workspace
	os.chdir("..")
	print(os.getcwd())
	shutil.rmtree("Output") # Cleans up

	""" THis function is not complete, It was semi-editited from a copy of the compression method """
def decompress():
	# Process to decompress
	"""
		Lots of checking
		Unzip files if there is issue go to the next one
		Because there should be an exception when referencing so have toignore that
		zips also need to be put back in order and 1,2,3,4..... folders
	"""
	workspace = input("Enter the folder reading from: ")
#	workspace = "TestData_comp"
	sets = printFiles(workspace, '*.zip') # Get valid zip files
	resultName = findNames(sets)
	print()
	choice = -1
	if len(resultName) == 1: # Only one option
		tempName = resultName[0]
		print("Archive of " + tempName + " is being assembled")
	else: # Must choose option
		print("How lucky for us. We are given " + str(len(resultName)) + " options")
		print("Select one of the ones below")
		# Could add a way to try and predict what saying
		# EX: taht is corrected to that
		while choice < 0:
			for rn in range(0, len(resultName), 1):
				 print(str(rn) + ". " + resultName[rn])
			choice = "0"
#			choice = input("Enter the number of the file you want: ")
			try:
				choice = int(choice) # Try is for this statement
				if choice >= 0 and choice< len(resultName): 
					print("Thanks for entering a valid number")
					
			except:
				print("That is not nice of you. You entered an invalid number")
				print("Checking to see if I can figure it out")
				for rp in resultName:
					if choice == rp:
						print("I think I figured it out despite you not following my directions")
						choice = resultName.index(choice)
						print("I an going with files asscociated with number " + str(choice))
				if type(choice) is not int:
					print("Nope you really screwed up. Try again")
					choice = -1
				else:
					if choice < 0:
						print("At least you entered an integer.... It is not valid so try again")
						choice = -1
				print()
		print("Removing zip filles not being processed from array")
		con = 0
		for fl in sets:
			if parseName(fl) != resultName[choice]:
				sets.remove(fl)
				con+= 1
		print("I have removed " + str(con) + " files from the array")
		print()
		if True: # Cleaning
			del rn
			del fl
			del con
	if True: # Cleaning
		del choice
		del resultName

	sets = sortDates(sets)

	# Since they are zip have to extract them
	for i in range(0, len(sets) , 1):
		# Create target Directory if don't exist
		dirName = "Output\\" + str(i)
		if not op.exists(dirName):
			os.makedirs(dirName) # For multiple
			print("Directory " , dirName ,  " has been created ")
		else:
			print("Directory " , dirName ,  " already exists")
		print("Extracting files from "+ sets[i] + " into the folder path of " + dirName)
		zipfile.ZipFile(workspace + "\\" + sets[i]).extractall(dirName)
		print("Extraction of " + sets[i] + " complete")

	print("We are now going to have to copy the files ")
	print("After copying over files we are going to recompress????")
	if True:
		return 0


def main():
	print("Welcome to the worderful program that Jacob has created")
	print("So we have very few but at least some options.")
	print("1. Compress")
	print("2. Decompress")
	choices = input("Enter your choice:")
	if choices == "1":
		compress()
	elif choices == "2":
		print("Sorry that this one is almost done. Requires a little bit of code. Check the notes for what is needed")
#		decompress()
	else:
		print("That is not a valid option. That sucks")
		print("Time to quit")
		return 0

	# Could add huffman algorithm but right now that is too much work

# Write the decompress functions

main()

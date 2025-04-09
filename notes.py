# from collections import Counter
# from collections import defaultdict

# ---------------------- USING COUNTER --------------------
# lst = [1, 2, 2, 2, 2, 3, 3, 3, 1, 2, 1, 12, 3, 2, 32, 1, 21, 1, 223, 1]
# c = Counter(lst)
# print(c)
# print(sum(c.values()))
# print(c.clear())
# print(c)
# print(list(c))
# print(set(c))
# print(dict(c))
# print(c.items())
# print(c.most_common(1))
# c_dict = dict(c)
# print(c_dict)
# print(Counter(c_dict))
# print(c.most_common()[:-2-1:-1])
#
# sentence = "What is love?"
#
# words = sentence.split()
#
# print(Counter(words))

# ---------------------- using defaultdict --------------------
# d = defaultdict(object)
# print(d["one"])
# print(d["two"])
#
# for item in d:
#     print(item)

# Can also initialize with default values
# e = defaultdict(lambda: 0)
# print(e['one'])


# ---------------------- using namedtuple --------------------
# from collections import namedtuple
#
# Dog = namedtuple("Dog", ["age", "breed", "name"])
# sam = Dog(age=2, breed="Lab", name="Sammy")
# print(sam)
# print(sam.age)
# print(sam.breed)
# print(sam.name)

# ----------------------- using datetime module ------------------------

# import datetime

# working with time
# t = datetime.time(4, 20, 1)
# print(datetime.time())
# print(t)
# print('hour:', t.hour)
# print('minute:', t.minute)
# print(t.microsecond)
# print(t.tzinfo)
#
# print("Earliest: ", datetime.time.min)
# print("Latest: ", datetime.time.max)
# print("Resolution", datetime.time.resolution)


# working with date
# today = datetime.date.today()
# print(today)
# print("ctime:", today.ctime())
# print("tuple:", today.timetuple())
# print("ordinal", today.toordinal())
# print("Year:", today.year)
# print("Month:", today.month)
# print("Day:", today.day)
#
# print("Earliest: ", datetime.date.min)
# print("Latest: ", datetime.date.max)
# print("Resolution", datetime.date.resolution)
#
# # create new date instance with replace method
# d1 = datetime.date(2015, 3, 11)
# print("d1:", d1)
# #
# d2 = d1.replace(year=1990)
# print("d2:", d2)
# #
# print(d1 - d2)


# --------------------------- Math and Random Modules ----------------------------------
# working with math module
# import math
#
# value = 4.35
# print(math.floor(value))
# print(math.ceil(value))
# print(round(value))
# print(math.pi)
# print(math.e)
# print(math.tau)
# print(math.inf)
# print(math.nan)

# working with the random module
# import random
#
# print(random.randint(0, 100))

# mylist = list(range(0, 20))
# print(mylist)
# print(random.choice(mylist))
# sample with replacement
# print(random.choices(population=mylist, k=5))
# sample without replacement
# print(random.sample(population=mylist, k=5))

# random.shuffle(mylist)
# print(mylist)

# *RANDOM DISTRIBUTIONS
# Uniform Distribution
# print(random.uniform(a=0, b=100))
# Normal/Gaussian Distribution
# print(random.gauss(mu=0, sigma=1))


# ---------------------- Lesson 3: Unzipping and Zipping Files -------------------------
# f = open("new_file.txt", "w+")
# f.write("Here is some text")
# f.close()

# creating file to compress
# f = open("new_file2.txt", "w+")
# f.write("Here is some text")
# f.close()

# Zipping files
# import zipfile

# comp_file = zipfile.ZipFile("comp_file.zip", "w")
# comp_file.write("new_file.txt", compress_type=zipfile.ZIP_DEFLATED)
# comp_file.write("new_file2.txt", compress_type=zipfile.ZIP_DEFLATED)
# comp_file.close()

# Extracting from Zip Files
# zip_obj = zipfile.ZipFile("comp_file.zip", "r")
# zip_obj.extractall("extracted_content")

# Using shutil library
# import shutil

# Creating a zip archive
# directory_to_zip = "C:\\Users\\Admin\\PycharmProjects\\practice-python\\extracted_content"
# shutil.make_archive('example_archive', 'zip', directory_to_zip)

# Extracting a zip archive
# dir_for_extract_result = "C:\\Users\\Admin\\PycharmProjects\\practice-python\\extracted_content"
# shutil.unpack_archive('/example_archive.zip', dir_for_extract_result, 'zip')

# ------------------------- Lesson 4: Advanced Numbers ---------------------------
# Converting to hexadecimal
# print(hex(246))
# print(hex(512))

# Converting to binary
# print(bin(1234))
# print(bin(128))
# print(bin(512))

# Exponentials
# print(pow(3, 4))
# print(pow(3, 4, 5))

# Round numbers
# print(round(49, -1))


# ------------------------- Lesson 5: Advanced Strings ---------------------------
# s = "Hello World"
# print(s.capitalize())
# print(s.upper())
# print(s.lower())
#
# # returns the number of occurrences without overlap
# print(s.count('o'))
# # returns the starting index position of the first occurrence
# print(s.find('o'))
#
# # Formatting
# print(s.center(20, " "))
#
# # the expandtabs() method will expand tab notations \t into spaces.
# print('hello\thi'.expandtabs(20))
#
# # isalnum() will return True if all characters in s are alphanumeric
# print(s.isalnum())
#
# # isalpha() will return True if all characters in s are alphabetic
# print(s.isalpha())
# print(s.islower())
#
# # isspace() will return True if all characters in s are whitespace
# print(s.isspace())
#
# print(s.istitle())
# print(s.isupper())
# print(s.endswith('d'))
#
# print(s.split('r'))
# print(s.partition('r'))


# # ------------------------- Lesson 6: Advanced Sets ---------------------------
# s = set()
# s.add(1)
# s.add(2)
# print(s)

# clear remove all elements from the set
# s.clear()
# print(s)

# returns a copy of the set
# s1 = {1, 2, 3}
# sc = s1.copy()
# s1.add(4)
# print(s1, sc)

# returns the difference of two or more sets.
# print(s1.difference(sc))

# difference_update method returns set1 after removing elements found in set2
# s1 = {1, 2, 3}
# s2 = {1, 4, 5}
# s1.difference_update(s2)
# print(s1)

# the discard method removes an element from a set if it is a member. If the element is not a
# member , do nothing
# s = {1, 2, 3, 4}
# s.discard(3)
# print(s)

# Intersection and intersection_update
# returns the intersection of two or more sets as a new set
# s1 = {1, 2, 3}
# s2 = {1, 2, 4}
# print(s1.intersection(s2))

# intersection_update will update a set with the intersection of itself and another.
# s1 = {1, 2, 3}
# s2 = {1, 2, 4}
# s1.intersection_update(s2)
# print(s1)

# isdisjoint method will return True if two sets have a null intersection
# s1 = {1, 2}
# s2 = {1, 2, 4}
# s3 = {5}
# print(s1.isdisjoint(s2))
# print(s1.isdisjoint(s3))

# issubset method returns True if a set is a subset of another set
# s1 = {1, 2}
# s2 = {1, 2, 4}
# print(s1.issubset(s2))

# issuperset returns True if a set is a superset of another set.
# s1 = {1, 2}
# s2 = {1, 2, 4}
# print(s1.issuperset(s2))
# print(s2.issuperset(s1))

# symmetric difference and symmetric_update
# s1 = {1, 2, 5}
# s2 = {1, 2, 4}
# print(s1.symmetric_difference(s2))
# s1.symmetric_difference_update(s2)
# print(s1)

# the union method returns the union of two sets.
# print(s1.union(s2))

# the update method update a set with the union of itself and others.
# s1.update(s2)
# print(s1)
# print(s2)
# s2.update(s1)
# print(s1)
# print(s2)


# -------------------- Lesson 7: Advanced Dictionaries -------------------------------
# Dictionary Comprehension
# sample_dict = {x: x**2 for x in range(10)}
# print(sample_dict)

# -------------------- Lesson 8: Advanced Lists -------------------------------
# list1 = [1, 2, 3, 4]

# count
# print(list1.count(2))
# append
# list1.append([6, 5])
# print(list1)
# extend
# list1.extend([6, 5])
# print(list1)
# index
# print(list1.index(2))
# insert
# list1.insert(2, "inserted")
# print(list1)
# remove
# list1.remove("inserted")
# print(list1)
# reverse; affects list  permanently
# list1.reverse()
# print(list1)
# sort
# list1.sort()
# print(list1)
# sort with an optional argument reverse
# list1.sort(reverse=True)
# print(list1)


# ------------------------------------ MODULE 9 ---------------------------------------------

# ----------------------------------- Lesson 1. Working with Images -------------------------
# Opening images using the Pillow library
# from PIL import Image
#
# kaisa = Image.open("Kaisa.jpg")
# briar = Image.open("briar.jpg")
# print(type(kaisa))
# print(kaisa.size)
# print(kaisa.format_description)
# print(kaisa.filename)
# x = 0
# y = 0
#
# w = 1215 // 3
# h = 717 // 10

# Crop an image
# kaisa.crop((0, 100, 100, 500)).show()

# print(kaisa.size)
# Show image
# kaisa.show()

# Copying and Pasting Images
# kaisa.paste(im=briar, box=(0, 0))
# kaisa.show()
# kaisa.paste(im=briar, box=(796, 0))
# kaisa.show()

# Resizing
# h, w = kaisa.size
# new_h = int(h / 2)
# new_w = int(h / 2)
# kaisa.resize((new_h, new_w)).show()

# Rotating Images
# kaisa = kaisa.rotate(90, expand=False)
# kaisa.show()

# Transparency
# kaisa.putalpha(200)
# kaisa.show()

# Saving Images
# kaisa.save("kaisa_save.png")


# ------------------------ Lesson 2: Working with PDF Files --------------------------------
# import PyPDF2

# Notice we read it as a binary with 'rb'
# f = open('Get_Started_With_Smallpdf.pdf', 'rb')
# pdf_reader = PyPDF2.PdfReader(f)
# Getting the number of pages of the pdf file
# print(pdf_reader.pages)
# Getting the first page
# page_one = pdf_reader.pages[0]
# We can then extract the text
# page_one_text = page_one.extract_text()
# print(page_one_text, type(page_one_text))

# Copy pages and append pages to the end
# f2 = open("sample-pdf-file.pdf", 'rb')
# pdf_reader = PyPDF2.PdfReader(f2)
# page_one = pdf_reader.pages[0]
#
# pdf_writer = PyPDF2.PdfWriter()
# pdf_writer.add_page(page_one)
# pdf_output = open('Get_Started_With_Smallpdf.pdf', 'wb')
# pdf_writer.write(pdf_output)
# f2.close()
#
# f3 = open("Get_Started_With_Smallpdf.pdf", 'rb')
# pdf_reader = PyPDF2.PdfReader(f3)
# page_two = pdf_reader.pages[0]
# page_two_text = page_two.extract_text()
# print(page_two_text)
# f3.close()

# Let's try to grab all the text from this PDF File
# f4 = open("Get_Started_With_Smallpdf.pdf", "rb")

# List of every page's text.
# The index will correspond to the page number.
# pdf_text = []
#
# pdf_reader = PyPDF2.PdfReader(f4)
# for p in range(len(pdf_reader.pages)):
#     page = pdf_reader.pages[p]
#     pdf_text.append(page.extract_text())
#
# print(pdf_text)
#
# f4.close()

# ---------------------------- MODULE 10: GUI AN INTRODUCTION ----------------------------
# # Framework of GUI
# import tkinter
#
# window = tkinter.Tk()
#
# # to rename the title of the window
# window.title("GUI")
#
# # pack is used to show the object in the window
# label = tkinter.Label(window, text="Welcome to DataCamp's Tutorial on Tkinter!")
# label.pack()
#
# # Button
# button_widget = tkinter.Button(window, text="Click Me!")
# button_widget.pack()
#
#
# window.mainloop()

# # Sample 1: Using pack() method
# import tkinter as tk
#
# window = tk.Tk()
# window.title("GUI")
#
# # You will first create a division with the help of Frame class and align them on Top and Bottom
# top_frame = tk.Frame(window)
# top_frame.pack()
# bottom_frame = tk.Frame(window)
# bottom_frame.pack(side="bottom")
#
# # Once the frames are created then you are all set to add widgets in both the frames.
# btn1 = tk.Button(top_frame, text="Button1", fg="red")
# btn1.pack()
# btn2 = tk.Button(top_frame, text="Button2", fg="green")
# btn2.pack()
# btn3 = tk.Button(bottom_frame, text="Button3", fg="purple")
# btn3.pack(side="left")
# btn4 = tk.Button(bottom_frame, text="Button4", fg="orange")
# btn4.pack(side="left")
#
# window.mainloop()

# # Sample 2: Using grid() method
# from tkinter import *
#
# top = Tk()
# CheckVar1 = IntVar()
# CheckVar2 = IntVar()
#
# Checkbutton(top, text="Machine Learning", variable=CheckVar1,
#             onvalue=1, offvalue=0).grid(row=0, sticky=W)
# Checkbutton(top, text="Deep Learning", variable=CheckVar2,
#             onvalue=0, offvalue=1).grid(row=1, sticky=W)
#
# top.mainloop()

# Lesson 4: Binding or Command Functions

# Sample 1
# import tkinter as tk
# import tkinter.messagebox

# window = tk.Tk()
# window.title("GUI")

# creating a function called DataCamp_Tutorial()
# def datacamp_tutorial():
#     tk.Label(window, text="GUI with Tkinter!").pack()
#
#
# tk.Button(window, text="Click Me!", command=datacamp_tutorial).pack()
# window.mainloop()

# Sample 2

# You will create three different functions for three different events
# def left_click(event):
#     tk.Label(window, text="Left Click!").pack()
#
#
# def middle_click(event):
#     tk.Label(window, text="Middle Click!").pack()
#
#
# def right_click(event):
#     tk.Label(window, text="Right Click!").pack()
#
#
# window.bind("<Button-1>", left_click)
# window.bind("<Button-2>", middle_click)
# window.bind("<Button-3>", right_click)
#
# window.mainloop()

# Lesson 5: Alert Boxes

# Example
# # Let's create an alert box with 'messagebox' function
# tkinter.messagebox.showinfo("Alert Message", "This is just an alert message!")
#
# # Let's also create a question for the user and based upon the response [Yes or
# # No Question] display a message.
# response = tkinter.messagebox.askquestion("Tricky Question", "Do you love Deep Learning?")
#
# # A basic 'if/else' block where if user clicks on 'Yes' then it returns 1 else it returns 0.
# # For each response you will display a message with the help of 'Label' method.
# if response == 1:
#     tk.Label(window, text="Yes, ofcourse I love Deep Learning!").pack()
# else:
#     tk.Label(window, text="No, I don't love Deep Learning").pack()
#
# window.mainloop()

# Lesson 6: Rendering Images
# icon = tk.PhotoImage(file="briar.jpg")
# label = tk.Label(window, image=icon)
# label.pack()
# window.mainloop()

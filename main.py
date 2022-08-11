from tkinter import *
from tkinter import ttk
from pytube import YouTube
import json
from tkinter import filedialog
from tkinter.messagebox import showinfo, showerror

class Main:
	def __init__(self, url: str, quality, directory: str):
		self.url = url
		self.quality = quality
		self.directory = directory

		self.quality = ["144p", "360p", "720p", "1080p", "MP4"]

		self.root = Tk()
		self.root.geometry("500x500")
		self.root.title("uTube Downloader")
		self.root.resizable(False, False)
		self.root.config(bg = "white")

		Main.Gui(self)

		self.root.mainloop()


	def Gui(self):
		# adding photo
		self.logoPhoto = PhotoImage(file="img/unnamed.png")
		self.logoLabel = Label(self.root, image=self.logoPhoto)
		self.logoLabel.place(x=-5, y=-5)

		# adding url entry
		self.urlGet = StringVar()
		self.urlEntry = ttk.Entry(self.root, textvariable=self.url)
		self.urlEntry.place(x=int(self.root.winfo_screenwidth()) / 21, y=int(self.root.winfo_screenheight()) / 5, width=self.root.winfo_screenwidth() / 6)

		# adding treeview of quality
		self.treeview = ttk.Treeview(self.root, columns=("c1"), show="headings")
		self.treeview.place(x=int(self.root.winfo_screenwidth()) / 100, y=int(self.root.winfo_screenheight()) / 4.1, height=125)
		self.treeview.column("# 1", anchor=CENTER)
		self.treeview.heading("# 1", text="Quality")
		self.treeview.insert("", 'end', values=("144p"))
		self.treeview.insert("", 'end', values=("360p"))
		self.treeview.insert("", 'end', values=("720p"))
		self.treeview.insert("", 'end', values=("1080p"))
		self.treeview.insert("", 'end', values=("MP4"))
		self.treeview.bind("<Double-1>", lambda x: Main.Selection(self))

		# adding download button
		self.buttonofDownload = ttk.Button(self.root, text=f"Download!", command=lambda : Main.Download(self))
		self.buttonofDownload.place(x=int(self.root.winfo_screenwidth()) / 8, y=int(self.root.winfo_screenheight()) / 3.35)

		self.fileDir = ttk.Button(self.root, text="Choose Directory", command=lambda : Main.Directory(self))
		self.fileDir.place(x=int(self.root.winfo_screenwidth()) / 32, y=int(self.root.winfo_screenheight()) / 2.7)

		self.footer = Label(self.root, text="Maded by Mehmet SOLAK\nVersion: 1.0.0", bg="white")
		self.footer.place(x=int(self.root.winfo_screenwidth()) / 11, y=int(self.root.winfo_screenheight()) / 2.35)

	def Directory(self):
		self.dir = filedialog.askdirectory()
		if self.dir != "":
			showinfo("Success!", "File directory Selected!")

	def Selection(self):
		self.select = self.treeview.focus()
		self.select = self.treeview.item(self.select, "values")
		self.buttonofDownload.config(text=f"{self.select[0]} Download!")

	def Download(self):
		self.url = self.urlGet.get()
		self.yt = YouTube(self.url)
		if len(self.url) > 1:
			try:
				if self.select[0] == self.quality[0] and self.dir != "":
					pass
			except:
				print("error")
		else:
			showerror("Error!", "Please Choose a Directory!")

if __name__ == "__main__":
	Main(None, None, None)
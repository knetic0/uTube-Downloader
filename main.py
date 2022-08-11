from tkinter import *

class Main:
	def __init__(self, url: str, quality: str, directory: str):
		self.url = url
		self.quality = quality
		self.directory = directory

		self.root = Tk()
		self.root.geometry("500x500")
		self.root.title("uTube Downloader")
		self.resizable(False, False)
		self.root.config(bg = "white")

		Main.Gui(self)

		self.root.mainloop()


	def Gui(self):
		pass


if __name__ == "__main__":
	Main()
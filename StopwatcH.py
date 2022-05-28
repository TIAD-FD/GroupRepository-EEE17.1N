import tkinter as tk
from time import sleep
from threading import Thread



class Stopwatch(tk.Frame):
	def __init__(self, guide):
		tk.Frame.__init__(self, guide)
		self.lap = []
		self.seconds, self.minutes, self.hours = 0, 0, 0
		self.timer = "00:00:00"
		self.running, self.end = False, False
		self.side = tk.Frame(self)
		self.status_label = tk.Label(self.side, text = '')
		self.stopwatch_label = tk.Label(self.side, text=str(self.timer), font = ('Arial', 36, 'bold'), fg = '#000')
		self.button_frame = tk.Frame(self.side)
		self.run_button = tk.Button(self.button_frame, text = "Start", command = self.start)
		self.restart_button = tk.Button(self.button_frame, text = "Reset", command = self.restart)
		self.save_button = tk.Button(self.button_frame, text = "Lap", command = self.save)
		self.exit_button = tk.Button(self.button_frame, text = "Exit", command = self.quit)
		self.saved_list = tk.Canvas(self, width = 150)
		self.list_frame = tk.LabelFrame(self.saved_list, text = "Time laps:")
		self.scrollbar = tk.Scrollbar(self, orient = tk.VERTICAL, command=self.saved_list.yview)

		self.side.pack(side = tk.LEFT, fill = tk.BOTH, expand = 1)
		self.status_label.pack(side = tk.TOP, fill = tk.NONE, expand = 0)
		self.stopwatch_label.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
		self.button_frame.pack(side = tk.BOTTOM, fill = tk.BOTH, expand = 1)
		self.run_button.pack(side = tk.LEFT, fill = tk.BOTH, expand = 1)
		self.restart_button.pack(side = tk.LEFT, fill = tk.BOTH, expand = 1)
		self.save_button.pack(side = tk.LEFT, fill = tk.BOTH, expand = 1)
		self.exit_button.pack(side = tk.LEFT, fill = tk.BOTH, expand = 1)
		self.saved_list.pack(side = tk.RIGHT, fill = tk.BOTH, expand = 0)
		self.scrollbar.pack(side = tk.RIGHT, fill = tk.Y, expand = 0)

		self.saved_list.create_window(0, 0, anchor = 'nw', tags = "saved", window = self.list_frame)
		self.saved_list.update_idletasks()
		self.saved_list.configure(scrollregion = self.saved_list.bbox('all'), yscrollcommand = self.scrollbar.set)
		self.thread = Thread(target = self.update, daemon = True)

	def update(self):
		while True:
			if self.end:
				break
			if self.running:
				if self.seconds < 59:
					self.seconds += 1
				elif self.seconds == 59:
					self.seconds = 0
					self.minutes += 1
					if self.minutes == 60:
						self.minutes = 0
						self.hours += 1
				if self.minutes == 60:
					self.minutes == 0
					self.hours += 1
				self.hours = f'{self.hours}' if self.hours > 9 else f'0{self.hours}'
				self.minutes = f'{self.minutes}' if self.minutes > 9 else f'0{self.minutes}'
				self.seconds = f'{self.seconds}' if self.seconds > 9 else f'0{self.seconds}'			
				self.timer = f"{self.hours}:{self.minutes}:{self.seconds}"
				self.stopwatch_label["text"] = self.timer
				if isinstance(self.seconds, str):
					self.seconds = int(self.seconds)
				if isinstance(self.minutes, str):
					self.minutes = int(self.minutes)
				if isinstance(self.hours, str):
					self.hours = int(self.hours)
				sleep(1)

	def start(self):
		self.running = True
		self.run_button.config(text="Stop", command = self.pause)
		self.status_label.config(text = '')
		self.stopwatch_label.config(fg = '#000')

	def pause(self):
		self.running = False
		self.run_button.config(text="Resume", command = self.start)
		self.status_label.config(text = 'Paused', font = ('Arial', 10), fg = '#f00')
		self.stopwatch_label.config(fg = '#f00')

	def restart(self):
		self.running = False
		self.timer = "00:00:00"
		self.seconds, self.minutes, self.hours = 0, 0, 0
		self.clear()
		self.run_button.config(text="Start", command = self.start)
		self.stopwatch_label["text"] = str(self.timer)
		self.status_label.config(text = '')
		self.stopwatch_label.config(fg = '#000')

	def clear(self):
		self.lap = []
		self.list_frame.destroy()
		self.list_frame = tk.LabelFrame(self.saved_list, text = "Time laps:")
		self.saved_list.delete("saved")
		self.saved_list.create_window(0, 0, anchor='nw', tags = "saved", window = self.list_frame)
		self.saved_list.update_idletasks()
		self.saved_list.configure(scrollregion = self.saved_list.bbox('all'), yscrollcommand = self.scrollbar.set)

	def save(self):
		if self.timer != '00:00:00':
			self.lap.append(self.timer)
			num = len(self.lap)
			savedTime = tk.Label(self.list_frame, text = f"#{num}. {self.lap[-1]}")
			savedTime.grid(row = len(self.lap), column = 0, sticky = "EW")
			self.saved_list.delete("saved")
			self.saved_list.create_window(0, 0, anchor = 'nw', tags = "saved",
											window = self.list_frame)
			self.saved_list.update_idletasks()
			self.saved_list.configure(scrollregion = self.saved_list.bbox('all'),
										yscrollcommand = self.scrollbar.set)

if __name__ == "__main__":
	root = tk.Tk()
	root.minsize(385,100)
	root.geometry("500x200")
	root.title("Stopwatch")


	stopwatch = Stopwatch(root)
	stopwatch.pack(fill=tk.BOTH, expand=1)
	stopwatch.thread.start()

	root.mainloop()
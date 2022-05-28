import tkinter as tk
from threading import Thread

root = tk.Tk()
root.geometry('700x500')
root.title('stopwatch')

saved_canvas = tk.Canvas(height = 640, width = 300)
saved_canvas.place(x = 470, y = 10)
saved_frame = tk.LabelFrame(saved_canvas, text = "Saved Times:")
scrollbar = tk.Scrollbar(orient = tk.VERTICAL, command = saved_canvas.yview, )

saved= []

running = False
hours, minutes, seconds = 0, 0, 0
status_label = tk.Label(text = '')
status_label.place(x = 10, y = 170)
stopwatch_label = "00:00:00"

def start():
	start_btn.config(text="pause", command = pause)
	status_label.config(text = ' ')
	global running
	if not running:
		update()
		running = True

def pause():
	start_btn.config(text="resume", command = start)
	global running
	if running:
		stopwatch_label.after_cancel(update_time)
		running = False
		status_label.config(text = 'Paused', font = ('Arial', 10), fg = '#f00')

def reset():
	status_label.config(text = '')
	start_btn.config(text = "start", command = start)
	global running
	if running:
		stopwatch_label.after_cancel(update_time)
		running = False
		
	global hours, minutes, seconds
	hours, minutes, seconds = 0, 0, 0
	stopwatch_label.config(text = '00:00:00')

def lap():
	saved.append(stopwatch_label)
	num = len(saved)
	savedTime = tk.Label(saved_frame, text = f"#{num}. {saved[-1]}")
	savedTime.grid(row=len(saved), column = 0, sticky ="NW")
	saved_canvas.delete("saved")
	saved_canvas.create_window(0, 0, anchor='nw', tags="saved", window = saved_frame)
	saved_canvas.update_idletasks()
	saved_canvas.configure(scrollregion = saved_canvas.bbox('all'), yscrollcommand = scrollbar.set)
	scrollbar.place(x = 660, y = 10)
	
def update():
	global hours, minutes, seconds
	seconds += 1
	if seconds == 60:
		minutes += 1
		seconds = 0
	if minutes == 60:
		hours += 1
		minutes = 0


	hours_str = f'{hours}' if hours > 9 else f'0{hours}'
	minutes_str = f'{minutes}' if minutes > 9 else f'0{minutes}'
	seconds_str = f'{seconds}' if seconds > 9 else f'0{seconds}'
	
	stopwatch_label.config(text = hours_str + ':' + minutes_str + ':' + seconds_str)
	
	global update_time
	update_time = stopwatch_label.after(1000, update)
	

stopwatch_label = tk.Label(text = '00:00:00', font=('Arial', 30))
stopwatch_label.place(x = 10, y = 40)



start_btn = tk.Button(text = 'start', height = 1, width = 3, font = ('Arial', 10), comman = start)
start_btn.place(x = 10, y = 230)
reset_btn = tk.Button(text = 'reset', height = 1, width = 3, font = ('Arial', 10), command = reset)
reset_btn.place(x = 150, y = 230)
save_btn = tk.Button(text = 'lap', height = 1, width = 3, font = ('Arial', 10), command = lap)
save_btn.place(x = 290, y = 230)


root.mainloop()

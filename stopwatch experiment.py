import tkinter as tk

running = False
hours, minutes, seconds = 0, 0, 0

def start():
	status_label = tk.Label(text = '				')
	status_label.place(x = 70, y = 100)
	global running
	if not running:
		update()
		running = True

def pause():
	global running
	if running:
		stopwatch_label.after_cancel(update_time)
		running = False
		status_label = tk.Label(text = 'Paused', font = ('Arial', 10), fg = '#f00')
	status_label.place(x = 70, y = 100)

def reset():
	status_label = tk.Label(text = '				')
	status_label.place(x = 70, y = 100)
	global running
	if running:
		stopwatch_label.after_cancel(update_time)
		running = False
		
	global hours, minutes, seconds
	hours, minutes, seconds = 0, 0, 0
	stopwatch_label.config(text = '00:00:00')
	
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
	
	
root = tk.Tk()
root.geometry('288x200')
root.title('stopwatch')

stopwatch_label = tk.Label(text = '00:00:00', font=('Arial', 20))
stopwatch_label.place(x = 70, y = 10)

start_btn = tk.Button(text = 'start', height = 5, width = 3, font = ('Arial', 5), comman = start)
start_btn.place(x = 0, y = 160)
pause_btn = tk.Button(text = 'pause', height = 5, width = 3, font = ('Arial', 5), command = pause)
pause_btn.place(x = 105, y = 160)
reset_btn = tk.Button(text = 'reset', height = 5, width = 3, font = ('Arial', 5), command = reset)
reset_btn.place(x = 210, y = 160)
quit_btn = tk.Button(text = 'quit', height = 5, width = 3, font = ('Arial', 5), command = quit)
quit_btn.place(x = 315, y = 160)

root.mainloop()
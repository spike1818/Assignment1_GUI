import tkinter as tk
m = tk.Tk()
button1 = tk.Button(m, text = 'exit', width = 50, height=20, command = m.destroy)
button1.pack()
m.mainloop()
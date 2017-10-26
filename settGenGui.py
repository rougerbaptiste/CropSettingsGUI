import tkinter as tk


root = tk.Tk()
root.wm_title("Configuration tool for CropMetaPop")
root.geometry("500x200")

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

GenBg = "#123456"
SelBg = "#456789"
ColBg = "#789123"
MigBg = "#147258"
SelColBg = "#258369"
SelMigBg = "#369147"

GenFrame = tk.Frame(root, background=GenBg, bd=1, relief="sunken")
SelFrame = tk.Frame(root, background=SelBg, bd=1, relief="sunken")
ColFrame = tk.Frame(root, background=ColBg, bd=1, relief="sunken")
MigFrame = tk.Frame(root, background=MigBg, bd=1, relief="sunken")
SelColFrame = tk.Frame(root, background=SelColBg, bd=1, relief="sunken")
SelMigFrame = tk.Frame(root, background=SelMigBg, bd=1, relief="sunken")

GenFrame.grid(row=0, column=0, sticky="nswe")
SelFrame.grid(row=0, column=1, sticky="nswe")
ColFrame.grid(row=0, column=2, sticky="nswe")
MigFrame.grid(row=1, column=0, sticky="nswe")
SelColFrame.grid(row=1, column=1, sticky="nswe")
SelMigFrame.grid(row=1, column=2, sticky="nswe")



root.mainloop()

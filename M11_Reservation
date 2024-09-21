# Start
import tkinter as tk

class MountainCabinGUI:
    def __init__(self, master):
        self.master = master
        master.title("Mountain Cabin Resort")

        self.cabin_types = {
            "Studio": 600,
            "One-bedroom": 800,
            "Two-bedroom": 1000
        }

        self.lake_view_cost = 300

        self.create_widgets()

    def create_widgets(self):
        self.cabin_label = tk.Label(self.master, text="Select Cabin Type:")
        self.cabin_label.pack()

        self.cabin_var = tk.StringVar(self.master)
        self.cabin_var.set("Studio")  
        self.cabin_menu = tk.OptionMenu(self.master, self.cabin_var, *self.cabin_types.keys())
        self.cabin_menu.pack()

        self.lake_view_var = tk.IntVar(self.master)
        self.lake_view_checkbox = tk.Checkbutton(self.master, text="Lake View (+$300)", variable=self.lake_view_var)
        self.lake_view_checkbox.pack()

        self.reserve_button = tk.Button(self.master, text="Reserve Cabin", command=self.calculate_total_cost)
        self.reserve_button.pack()

        self.total_cost_label = tk.Label(self.master, text="")
        self.total_cost_label.pack()

    def calculate_total_cost(self):
        cabin_type = self.cabin_var.get()
        cabin_cost = self.cabin_types[cabin_type]
        if self.lake_view_var.get() == 1:
            cabin_cost += self.lake_view_cost

        self.total_cost_label.config(text=f"Total Cost: ${cabin_cost} per week")

def main():
    root = tk.Tk()
    app = MountainCabinGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
# end


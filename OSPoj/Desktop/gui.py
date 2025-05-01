import tkinter as tk
from tkinter import messagebox
from page_replacement import PageReplacementSimulator
from visualization import plot_results
from opt import optimal
def run_simulation():
    """Runs the page replacement simulation and displays results."""
    try:
        reference_str = entry_ref.get().strip()
        if not reference_str:
            raise ValueError("Reference string cannot be empty.")
        reference_string = list(map(int, reference_str.split()))
        
        frames = int(entry_frames.get())
        if frames <= 0:
            raise ValueError("Number of frames must be at least 1.")

        simulator = PageReplacementSimulator(frames, reference_string)
        fifo_faults = simulator.fifo()
        lru_faults = simulator.lru()

        result_label.config(text=f"FIFO: {fifo_faults} faults\nLRU: {lru_faults} faults")
        plot_results({'FIFO': fifo_faults, 'LRU': lru_faults})

    except ValueError as e:
        messagebox.showerror("Error", str(e))
root = tk.Tk()
root.title("Page Replacement Simulator")
tk.Label(root, text="Enter Reference String (space-separated):").pack(pady=5)
entry_ref = tk.Entry(root, width=40)
entry_ref.pack(pady=5)

tk.Label(root, text="Enter Number of Frames:").pack(pady=5)
entry_frames = tk.Entry(root, width=40)
entry_frames.pack(pady=5)

btn_run = tk.Button(root, text="Run Simulation", command=run_simulation)
btn_run.pack(pady=10)

result_label = tk.Label(root, text="", font=('Arial', 10))
result_label.pack(pady=10)

root.mainloop()
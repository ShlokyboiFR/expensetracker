from tkinter import Tk
from expense_tracker_gui import ExpenseTrackerGUI
from expense_tracker_analysis import ExpenseTrackerAnalysis

if __name__ == "__main__":
    root = Tk()
    tracker_gui = ExpenseTrackerGUI(root)
    analysis = ExpenseTrackerAnalysis()
    tracker_gui.set_analysis(analysis)
    root.mainloop()

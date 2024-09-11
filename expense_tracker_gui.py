from tkinter import Tk, Label, Entry, Button, Listbox, END
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from expense_tracker_analysis import ExpenseTrackerAnalysis

class ExpenseTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        self.categories = []
        self.expenses = []

        self.category_label = Label(root, text="Category:")
        self.category_label.pack()
        self.category_entry = Entry(root)
        self.category_entry.pack()

        self.amount_label = Label(root, text="Amount:")
        self.amount_label.pack()
        self.amount_entry = Entry(root)
        self.amount_entry.pack()

        self.add_button = Button(root, text="Add Expense", command=self.add_expense)
        self.add_button.pack()

        self.expenses_listbox = Listbox(root)
        self.expenses_listbox.pack()

        self.plot_category_button = Button(root, text="Plot Category Spending", command=self.plot_category_spending)
        self.plot_category_button.pack()

        self.forecast_spending_button = Button(root, text="Forecast Spending", command=self.forecast_spending)
        self.forecast_spending_button.pack()

        self.perform_clustering_button = Button(root, text="Perform Clustering", command=self.perform_clustering)
        self.perform_clustering_button.pack()

        self.detect_anomalies_button = Button(root, text="Detect Anomalies", command=self.detect_anomalies)
        self.detect_anomalies_button.pack()

        self.analysis = ExpenseTrackerAnalysis()

    def add_expense(self):
        category = self.category_entry.get()
        amount = float(self.amount_entry.get())

        self.categories.append(category)
        self.expenses.append((category, amount))

        self.expenses_listbox.insert(END, f"{category}: ${amount}")

        self.category_entry.delete(0, END)
        self.amount_entry.delete(0, END)

    def plot_category_spending(self):
        if self.analysis:
            self.analysis.initialize(self.categories, self.expenses)
            self.analysis.plot_category_spending()

    def forecast_spending(self):
        if self.analysis:
            self.analysis.initialize(self.categories, self.expenses)
            self.analysis.forecast_spending()

    def perform_clustering(self):
        if self.analysis:
            self.analysis.initialize(self.categories, self.expenses)
            self.analysis.perform_clustering()

    def detect_anomalies(self):
        if self.analysis:
            self.analysis.initialize(self.categories, self.expenses)
            self.analysis.detect_anomalies()


root = Tk()
app = ExpenseTrackerGUI(root)
root.mainloop()
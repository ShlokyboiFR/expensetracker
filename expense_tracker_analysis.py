import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import IsolationForest

class ExpenseTrackerAnalysis:
    def __init__(self):
        self.categories = []
        self.expenses = []

    def initialize(self, categories, expenses):
        self.categories = categories
        self.expenses = expenses

    def plot_category_spending(self):
        category_spending = {}
        for category in self.categories:
            category_spending[category] = sum(amount for cat, amount in self.expenses if cat == category)

        categories = list(category_spending.keys())
        spending = list(category_spending.values())

        plt.bar(categories, spending)
        plt.xlabel("Categories")
        plt.ylabel("Spending")
        plt.title("Category Spending")
        plt.show()

    def analyze_spending(self):
        total_spending = sum(amount for _, amount in self.expenses)
        average_spending = np.mean([amount for _, amount in self.expenses])
        max_spending = max([amount for _, amount in self.expenses])
        min_spending = min([amount for _, amount in self.expenses])

        print("Total Spending:", total_spending)
        print("Average Spending:", average_spending)
        print("Max Spending:", max_spending)
        print("Min Spending:", min_spending)

    def forecast_spending(self):
        # Prepare data for forecasting
        x = np.arange(len(self.expenses))
        y = np.array([amount for _, amount in self.expenses])

        # Fit a random forest regression model
        model = RandomForestRegressor()
        model.fit(x.reshape(-1, 1), y)

        # Forecast future spending
        future_x = np.arange(len(self.expenses), len(self.expenses) + 10)  # Forecast for the next 10 periods
        future_y = model.predict(future_x.reshape(-1, 1))

        # Plot the forecast
        plt.plot(x, y, label="Actual Spending")
        plt.plot(future_x, future_y, label="Forecasted Spending")
        plt.xlabel("Period")
        plt.ylabel("Spending")
        plt.title("Spending Forecast")
        plt.legend()
        plt.show()

    def perform_clustering(self):
        # Prepare data for clustering
        X = np.array([(amount,) for _, amount in self.expenses])

        # Perform K-means clustering
        kmeans = KMeans(n_clusters=3)
        kmeans.fit(X)
        labels = kmeans.labels_

        # Plot the clustering results
        plt.scatter(X[:, 0], np.zeros_like(X[:, 0]), c=labels)
        plt.xlabel("Spending")
        plt.title("Spending Clustering")
        plt.show()

    def detect_anomalies(self):
        # Prepare data for anomaly detection
        X = np.array([(amount,) for _, amount in self.expenses])

        # Perform anomaly detection using Isolation Forest
        clf = IsolationForest(contamination=0.05)
        clf.fit(X)
        anomalies = clf.predict(X)

        # Identify anomalous expenses
        anomalous_expenses = [expense for expense, anomaly in zip(self.expenses, anomalies) if anomaly == -1]

        # Print and visualize the anomalous expenses
        print("Anomalous Expenses:")
        for category, amount in anomalous_expenses:
            print(f"{category}: ${amount}")
        print()

        # Plot the anomalies
        plt.scatter(X[:, 0], np.zeros_like(X[:, 0]), c=anomalies)
        plt.xlabel("Spending")
        plt.title("Anomaly Detection")
        plt.show()

    def count_investments(self):
        investment_categories = ['stocks', 'bonds', 'real estate']  # Adjust to your investment categories

        investment_count = 0
        for category in self.categories:
            if category in investment_categories:
                investment_count += 1

        print("Investment Count:", investment_count)

    def analyze_investments(self):
        investment_categories = ['stocks', 'bonds', 'real estate']  # Adjust to your investment categories

        investment_expenses = [(category, amount) for category, amount in self.expenses if category in investment_categories]
        investment_amounts = [amount for _, amount in investment_expenses]

        total_investment = sum(investment_amounts)
        average_investment = np.mean(investment_amounts)
        max_investment = max(investment_amounts)
        min_investment = min(investment_amounts)

        print("Total Investment:", total_investment)
        print("Average Investment:", average_investment)
        print("Max Investment:", max_investment)
        print("MinInvestment:", min_investment)
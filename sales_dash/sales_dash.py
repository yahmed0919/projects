# By Yaseen A.
import matplotlib.pyplot as plt

# Sample data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
revenue = [5000, 7000, 5500, 9000, 6000, 7500]
units_sold = [100, 120, 80, 150, 110, 100]
avg_order_value = [50, 58, 68.75, 60, 54.55, 75]

# Line chart for revenue
plt.plot(months, revenue, marker='o', label='Revenue')

# Bar chart for units sold
plt.bar(months, units_sold, label='Units Sold')

# Plot average order value
plt.plot(months, avg_order_value, marker='s', label='Avg. Order Value')

# Set labels and title
plt.xlabel('Months')
plt.ylabel('Amount ($)')
plt.title('Sales Analysis')

# Display legend
plt.legend()

# Show the plot
plt.show()

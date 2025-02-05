import matplotlib.pyplot as plt

regions = ["Berlin", "Munich", "Nurnberg", "Hamburg", "Frankfurt"]
sales_revenue = [500, 620, 350, 765, 900]

plt.bar(regions, sales_revenue, color='brown')

plt.xlabel("Regions")
plt.ylabel("Sales Revenue ($1000s)")
plt.title("Sales Revenue Across Different Regions(Germany)")

plt.show()

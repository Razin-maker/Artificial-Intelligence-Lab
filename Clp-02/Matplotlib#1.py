import matplotlib.pyplot as plt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
temperatures = [22, 24, 21, 25, 27, 26, 23]

plt.plot(days, temperatures, marker='o', linestyle='-', color='r', label="Temperature (°C)")

plt.xlabel("Days of the Week")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Variations Over a Week")

plt.legend()

plt.show()

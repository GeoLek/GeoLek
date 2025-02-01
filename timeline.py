import matplotlib.pyplot as plt
import datetime
import calendar
import os

# Get the current date, month, and day
current_date = datetime.datetime.now()
current_month = current_date.strftime("%b")
current_month_index = current_date.month - 1  # Convert to zero-based index
current_day = current_date.day

# Define months and calculate progress
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
days_in_months = [calendar.monthrange(current_date.year, i + 1)[1] for i in range(12)]

# Define a dark theme
plt.style.use("dark_background")

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 3), facecolor="#222222")
ax.set_facecolor("#222222")

# Plot each month as a bar in a compact histogram
for i, month in enumerate(months):
    days = days_in_months[i]
    for day in range(days):
        # Experience: Past months fully filled with gold
        if i < current_month_index:
            fill_color = "#FFD700"
        # Current month: Partial gold fill up to today's date
        elif i == current_month_index and day < current_day:
            fill_color = "#FFD700"
        # Future months: Gray
        else:
            fill_color = "#555555"

        ax.bar(i, 1 / days, bottom=day / days, color=fill_color, edgecolor="none", width=0.4)

# Add month labels below each bar with day
for i, month in enumerate(months):
    label = f"{month} ({current_day}/{month})" if i == current_month_index else month
    ax.text(i, -0.08, label, ha="center", va="top", fontsize=10, color="#FFFFFF", fontweight="medium")

# Add "You are here" annotation above the bars on the left side
ax.annotate("You are here ★",
            xy=(current_month_index, 1.05),
            xytext=(current_month_index, 1.2),
            fontsize=12,
            ha="center",
            color="#FFD700",
            weight="bold",
            arrowprops=dict(facecolor='#FFD700', arrowstyle='->'))

# Display "Happy New Month 😊" on the first day of the month **at the bottom right**
if current_day == 1:
    ax.text(11.5, -0.35, "Happy New Month 😊", fontsize=11, color="#FFD700", ha="right", fontweight="bold")

# Add legend below the histogram
ax.text(2, -0.25, "■ Experience", fontsize=10, color="#FFD700", va="center", ha="center", fontweight="bold")
ax.text(6, -0.25, "■ Opportunity", fontsize=10, color="#AAAAAA", va="center", ha="center", fontweight="bold")

# Adjust plot settings
ax.set_xlim(-0.5, 11.5)
ax.set_ylim(0, 1.2)
ax.set_xticks([])
ax.set_yticks([])
ax.axis("off")

# Delete existing timeline.png (if it exists)
if os.path.exists("timeline.png"):
    os.remove("timeline.png")

# Save and show plot
plt.tight_layout()
plt.savefig("timeline.png", dpi=100, bbox_inches="tight")
plt.show()

import matplotlib.pyplot as plt
import datetime
import calendar

# Get the current date, month, and day
current_date = datetime.datetime.now()
current_month = current_date.strftime("%b")
current_day = current_date.day

# Define months and calculate progress
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
days_in_months = [calendar.monthrange(current_date.year, i + 1)[1] for i in range(12)]
progress = []

for i, month in enumerate(months):
    if month == current_month:
        progress.append(round(current_day / days_in_months[i], 2))  # Strict calculation with two decimal places
    else:
        progress.append(0)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 3))

# Plot each month as a bar in a compact histogram
for i, month in enumerate(months):
    # Draw the base bar
    days = days_in_months[i]
    for day in range(days):
        fill_color = "#4A90E2" if month == current_month and day < current_day else "#E5EAF5"
        ax.bar(i, 1 / days, bottom=day / days, color=fill_color, edgecolor="black", width=0.4)

# Add month labels below each bar with day
for i, month in enumerate(months):
    label = f"{month} ({current_day}/{month})" if month == current_month else month
    ax.text(i, -0.08, label, ha="center", va="top", fontsize=9, color="#2C3E50", fontweight="medium")

# Add "YOU ARE HERE" annotation above the bars with Georgia font
current_index = months.index(current_month)
ax.annotate("YOU ARE HERE",
            xy=(current_index, 1.05),
            xytext=(current_index, 1.2),
            fontsize=10,
            ha="center",
            color="#34495E",
            weight="bold",
            fontname='Georgia',
            arrowprops=dict(facecolor='#34495E', arrowstyle='->'))

# Add legend below the histogram
ax.text(2, -0.25, "■ Experience", fontsize=9, color="#4A90E2", va="center", ha="center", fontweight="bold")
ax.text(6, -0.25, "■ Opportunity", fontsize=9, color="#90A4AE", va="center", ha="center", fontweight="bold")

# Add a tiny star in the bottom-right corner of the image
fig.text(0.98, 0.02, "★", fontsize=12, color="#FFD700", ha="right", va="bottom")

# Adjust plot settings
ax.set_xlim(-0.5, 11.5)
ax.set_ylim(0, 1.2)
ax.set_xticks([])
ax.set_yticks([])
ax.axis("off")

# Show plot
plt.tight_layout()
plt.savefig("timeline.png", dpi=100, bbox_inches="tight")
plt.show()

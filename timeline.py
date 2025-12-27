import matplotlib.pyplot as plt
import datetime
import calendar
import os

# ============================
# TIME: STRICTLY UTC
# ============================
current_date = datetime.datetime.utcnow()

current_month = current_date.strftime("%b")
current_month_index = current_date.month - 1  # zero-based
current_day = current_date.day
current_day_of_year = current_date.timetuple().tm_yday

total_days_in_year = 366 if calendar.isleap(current_date.year) else 365

# ============================
# MONTH STRUCTURE
# ============================
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

days_in_months = [
    calendar.monthrange(current_date.year, i + 1)[1]
    for i in range(12)
]

# ============================
# DARK THEME
# ============================
plt.style.use("dark_background")

fig, ax = plt.subplots(figsize=(8, 3), facecolor="#222222")
ax.set_facecolor("#222222")

# ============================
# BARS (EXPERIENCE / OPPORTUNITY)
# ============================
for i, month in enumerate(months):
    days = days_in_months[i]
    for day in range(days):
        if i < current_month_index:
            fill_color = "#FFD700"  # past months
        elif i == current_month_index and day < current_day:
            fill_color = "#FFD700"  # current month progress
        else:
            fill_color = "#555555"  # future

        ax.bar(
            i,
            1 / days,
            bottom=day / days,
            color=fill_color,
            edgecolor="none",
            width=0.4
        )

# ============================
# MONTH LABELS
# ============================
for i, month in enumerate(months):
    label = f"{month} ({current_day}/{month})" if i == current_month_index else month
    ax.text(
        i,
        -0.08,
        label,
        ha="center",
        va="top",
        fontsize=10,
        color="#FFFFFF",
        fontweight="medium"
    )

# ============================
# YOU ARE HERE
# ============================
ax.annotate(
    "You are here ★",
    xy=(current_month_index, 1.05),
    xytext=(current_month_index, 1.2),
    fontsize=12,
    ha="center",
    color="#FFD700",
    weight="bold",
    arrowprops=dict(facecolor="#FFD700", arrowstyle="->")
)

# ============================
# HAPPY NEW MONTH / YEAR
# ============================
if current_day == 1:
    ax.text(
        11.5,
        -0.35,
        "Happy New Month 😊",
        fontsize=11,
        color="#FFD700",
        ha="right",
        fontweight="bold"
    )

# Happy New Year ONLY on Jan 1
if current_date.month == 1 and current_day == 1:
    ax.text(
        11.5,
        -0.46,
        "Happy New Year 🎆",
        fontsize=11,
        color="#FFD700",
        ha="right",
        fontweight="bold"
    )

# ============================
# PAGE COUNTER (YEAR PROGRESS)
# ============================
ax.text(
    6.5,
    -0.30,
    f"Page {current_day_of_year}/{total_days_in_year}",
    fontsize=11,
    color="#00BFFF",  # electric blue
    ha="center",
    fontweight="bold"
)

# ============================
# LEGEND
# ============================
ax.text(1, -0.25, "■ Experience", fontsize=10, color="#FFD700",
        va="center", ha="center", fontweight="bold")

ax.text(3, -0.25, "■ Opportunity", fontsize=10, color="#AAAAAA",
        va="center", ha="center", fontweight="bold")

# ============================
# FINAL TOUCHES
# ============================
ax.set_xlim(-0.5, 11.5)
ax.set_ylim(0, 1.25)
ax.set_xticks([])
ax.set_yticks([])
ax.axis("off")

if os.path.exists("timeline.png"):
    os.remove("timeline.png")

plt.tight_layout()
plt.savefig("timeline.png", dpi=100, bbox_inches="tight")
plt.show()
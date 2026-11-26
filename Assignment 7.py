#Assignment 7

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#let user enter file name/address
filename = input("Enter file name (.csv/.xls/.xlsx): ").strip()
#enter file address - D:/KHUSHI/MIT WPU/Python 1st yr/Data_Visualization/sample_data_assignment_07.csv

# Load the CSV dataset
df = pd.read_csv(filename)

# Display the dataset
print("Dataset:")
print(df)

# 1. Line Plot
plt.figure(figsize=(7, 4))
plt.plot(df["Student"], df["Python"], marker="o")

plt.title("Python Marks of Students")
plt.xlabel("Student")
plt.ylabel("Python Marks")
plt.grid(True)
plt.show()

# 2. Bar Plot
plt.figure(figsize=(7, 4))
plt.bar(df["Student"], df["Maths"])

plt.title("Maths Marks of Students")
plt.xlabel("Student")
plt.ylabel("Maths Marks")
plt.show()

# 3. Scatter Plot
plt.figure(figsize=(7, 4))
plt.scatter(df["Maths"], df["Python"], s=70)

plt.title("Maths vs Python Marks")
plt.xlabel("Maths Marks")
plt.ylabel("Python Marks")
plt.grid(True)
plt.show()

# 4. Calculate Correlation Matrix
correlation = df[["Maths", "Python", "Attendance"]].corr()

print("Correlation Matrix:")
print(correlation)

# 5. Heatmap
plt.figure(figsize=(6, 5))
sns.heatmap(correlation, annot=True, cmap="Blues",
            vmin=-1, vmax=1)

plt.title("Correlation Heatmap")
plt.show()

# Challenge/Extension Task : Modify the program to perform the following additional tasks given below
# 6. Histogram of Python Marks
plt.figure(figsize=(7, 4))

plt.hist(df["Python"], bins=5,
         edgecolor="black", label="Python Marks")

plt.title("Histogram of Python Marks")
plt.xlabel("Python Marks")
plt.ylabel("Number of Students")
plt.legend()
plt.show()

# 7. Box Plot for Maths and Python Marks
plt.figure(figsize=(7, 4))

plt.boxplot([df["Maths"], df["Python"]])
plt.xticks([1, 2], ["Maths", "Python"])

plt.title("Box Plot of Maths and Python Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# 8. Pie Chart of Students from Each City
city_count = df["City"].value_counts()

plt.figure(figsize=(6, 5))

plt.pie(city_count,
        labels=city_count.index,
        autopct="%1.1f%%",
        startangle=90)

plt.title("Students from Each City")
plt.legend(title="City")
plt.show()

# 9. Calculate Average Marks and Attendance
average_maths = df["Maths"].mean()
average_python = df["Python"].mean()
average_attendance = df["Attendance"].mean()

print("\nAverage Maths Marks:", round(average_maths, 2))
print("Average Python Marks:", round(average_python, 2))
print("Average Attendance:", round(average_attendance, 2))

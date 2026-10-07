import tkinter as tk
from tkinter import ttk, messagebox

from employee import load_data, add_employee, search_employee, delete_employee
from performance import add_scores, get_summary
from analysis import employee_chart, department_chart

data = load_data()


def add_record():
    global data

    try:
        record = {
            "ID": id_entry.get(),
            "Name": name_entry.get(),
            "Department": dept_entry.get(),
            "Period": period_entry.get(),
            "Productivity": float(prod_entry.get()),
            "Quality": float(quality_entry.get()),
            "Teamwork": float(team_entry.get()),
            "Attendance": float(att_entry.get())
        }

        if record["ID"] == "" or record["Name"] == "":
            messagebox.showerror("Error", "Enter ID and Name")
            return

        scores = [
            record["Productivity"],
            record["Quality"],
            record["Teamwork"],
            record["Attendance"]
        ]

        if any(score < 0 or score > 100 for score in scores):
            messagebox.showerror("Error", "Scores must be 0 to 100")
            return

        data = add_employee(data, record)

        messagebox.showinfo("Success", "Record added")

        show_data()

    except ValueError:
        messagebox.showerror("Error", "Enter valid data")


def search():
    word = search_entry.get()
    result = search_employee(data, word)
    show_data(result)


def delete():
    global data

    employee_id = id_entry.get()
    period = period_entry.get()

    if employee_id == "" or period == "":
        messagebox.showerror("Error", "Enter ID and Period")
        return

    data = delete_employee(data, employee_id, period)

    show_data()


def summary():
    average, highest, lowest = get_summary(data)

    messagebox.showinfo(
        "Summary",
        "Average: " + str(round(average, 2)) +
        "\nHighest: " + str(round(highest, 2)) +
        "\nLowest: " + str(round(lowest, 2))
    )


def show_data(result=None):

    for item in table.get_children():
        table.delete(item)

    if result is None:
        result = data

    result = add_scores(result)

    for _, row in result.iterrows():

        table.insert(
            "",
            "end",
            values=(
                row["ID"],
                row["Name"],
                row["Department"],
                row["Period"],
                row["Productivity"],
                row["Quality"],
                row["Teamwork"],
                row["Attendance"],
                round(row["Overall Score"], 2)
            )
        )


root = tk.Tk()
root.title("Employee Performance System")
root.geometry("1100x650")

tk.Label( root,text="Employee Performance Tracking System",font=("Arial", 20)).pack(pady=10)

form = tk.Frame(root)
form.pack()

tk.Label(form, text="ID").grid(row=0, column=0)
id_entry = tk.Entry(form)
id_entry.grid(row=0, column=1)

tk.Label(form, text="Name").grid(row=0, column=2)
name_entry = tk.Entry(form)
name_entry.grid(row=0, column=3)

tk.Label(form, text="Department").grid(row=1, column=0)
dept_entry = tk.Entry(form)
dept_entry.grid(row=1, column=1)

tk.Label(form, text="Period").grid(row=1, column=2)
period_entry = tk.Entry(form)
period_entry.grid(row=1, column=3)

tk.Label(form, text="Productivity").grid(row=2, column=0)
prod_entry = tk.Entry(form)
prod_entry.grid(row=2, column=1)

tk.Label(form, text="Quality").grid(row=2, column=2)
quality_entry = tk.Entry(form)
quality_entry.grid(row=2, column=3)

tk.Label(form, text="Teamwork").grid(row=3, column=0)
team_entry = tk.Entry(form)
team_entry.grid(row=3, column=1)

tk.Label(form, text="Attendance").grid(row=3, column=2)
att_entry = tk.Entry(form)
att_entry.grid(row=3, column=3)

tk.Button(
    root,
    text="Add Record",
    command=add_record
).pack(pady=5)

tk.Button(
    root,
    text="Delete Record",
    command=delete
).pack(pady=5)

tk.Button(
    root,
    text="Summary",
    command=summary
).pack(pady=5)

search_frame = tk.Frame(root)
search_frame.pack(pady=5)

tk.Label(
    search_frame,
    text="Search"
).pack(side=tk.LEFT)

search_entry = tk.Entry(search_frame)
search_entry.pack(side=tk.LEFT)

tk.Button(
    search_frame,
    text="Search",
    command=search
).pack(side=tk.LEFT)

tk.Button(
    search_frame,
    text="Show All",
    command=show_data
).pack(side=tk.LEFT)

columns = (
    "ID",
    "Name",
    "Department",
    "Period",
    "Productivity",
    "Quality",
    "Teamwork",
    "Attendance",
    "Overall"
)

table = ttk.Treeview(
    root,
    columns=columns,
    show="headings"
)

for column in columns:
    table.heading(column, text=column)
    table.column(column, width=105)

table.pack(
    fill=tk.BOTH,
    expand=True,
    padx=10,
    pady=10
)

tk.Button(
    root,
    text="Employee Chart",
    command=lambda: employee_chart(data)
).pack(side=tk.LEFT, padx=20)

tk.Button(
    root,
    text="Department Chart",
    command=lambda: department_chart(data)
).pack(side=tk.LEFT, padx=20)

show_data()

root.mainloop()
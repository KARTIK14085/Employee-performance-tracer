import pandas as pd
import os

FILE = "performance.csv"


def load_data():
    if os.path.exists(FILE):
        return pd.read_csv(FILE)

    return pd.DataFrame(columns=[
        "ID",
        "Name",
        "Department",
        "Period",
        "Productivity",
        "Quality",
        "Teamwork",
        "Attendance"
    ])


def save_data(data):
    data.to_csv(FILE, index=False)


def add_employee(data, record):
    new_record = pd.DataFrame([record])

    data = pd.concat(
        [data, new_record],
        ignore_index=True
    )

    save_data(data)

    return data


def search_employee(data, word):
    result = data[
        data["ID"].astype(str).str.contains(word, case=False)
        |
        data["Name"].astype(str).str.contains(word, case=False)
    ]

    return result


def delete_employee(data, employee_id, period):
    data = data[
        ~(
            (data["ID"].astype(str) == employee_id)
            &
            (data["Period"].astype(str) == period)
        )
    ]

    save_data(data)

    return data
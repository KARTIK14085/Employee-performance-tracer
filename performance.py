import numpy as np
def calculate_score(row):
    scores = np.array([
        row["Productivity"],
        row["Quality"],
        row["Teamwork"],
        row["Attendance"]
    ])

    return np.mean(scores)

def add_scores(data):

    if data.empty:
        return data

    data = data.copy()

    data["Overall Score"] = data.apply(calculate_score,axis=1 )
    return data

def get_summary(data):

    data = add_scores(data)

    average = data["Overall Score"].mean()
    highest = data["Overall Score"].max()
    lowest = data["Overall Score"].min()

    return average, highest, lowest


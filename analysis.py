import matplotlib.pyplot as plt
from performance import add_scores

def employee_chart(data):

    data = add_scores(data)

    if data.empty:
        return

    result = data.groupby("Name")["Overall Score"].mean()

    result.plot(kind="bar")

    plt.title("Employee Performance")
    plt.xlabel("Employee")
    plt.ylabel("Score")
    plt.ylim(0, 100)

    plt.show()

def department_chart(data):

    data = add_scores(data)

    if data.empty:
        return

    result = data.groupby("Department")["Overall Score"].mean()

    result.plot(kind="bar")

    plt.title("Department Performance")
    plt.xlabel("Department")
    plt.ylabel("Score")
    plt.ylim(0, 100)

    plt.show()

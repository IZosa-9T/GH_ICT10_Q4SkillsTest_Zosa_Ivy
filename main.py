# numerical python and MATLAB plotting library
from pyscript import display, document
import numpy as np
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)
import matplotlib.pyplot as plt
plt.figure()
plt.close()

months = ["Jan", "Feb", "Mar", "Apr", "May", "jun", 
          "jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

absences_data = [0] * 12

def showgraph(e):
    document.getElementById('output1').innerHTML = ''

    month_val = document.getElementById('monthabsence').value
    absences_val = int(document.getElementById('totalabsences').value)

    # link dropdown values to index
    month_map = {
        "jan": 0, "feb": 1, "mar": 2, "apr": 3, "may": 4, "aug": 7, "sep": 8, "oct": 9, "nov": 10, "dec": 11
    }

    index = month_map[month_val]

    # update only one month
    absences_data[index] = absences_val

    # clear previous plot
    plt.clf()

    plt.plot(months, absences_data, marker='o')

    plt.title("Student Monthly Attendance")
    plt.xlabel("Months")
    plt.ylabel("Absences")

    display(plt, target="output1")
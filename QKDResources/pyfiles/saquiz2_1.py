from IPython.display import Math, display
from ipywidgets import HBox, Label, Layout, Output, VBox, widgets

from QKDResources.pyfiles.helpermethods import (
    empty,
    getComplex,
    qcorrect,
    qformaterror,
    qincorrect,
    qunknownerror,
)

# Layouts
numInputLayout = Layout(width="55px")
strInputLayout1 = Layout(width="90px")
strInputLayout2 = Layout(width="130px")
center = Layout(align_items="center")
hidden = Layout(visibility="hidden")

q_valid1 = widgets.Valid(value=False, readout="Incorrect", layout=hidden)
q_valid2 = widgets.Valid(value=False, readout="Incorrect", layout=hidden)
q_valid3 = widgets.Valid(value=False, readout="Incorrect", layout=hidden)
q_label1 = widgets.HTML(value="")
q_label2 = widgets.HTML(value="")
q_label3 = widgets.HTML(value="")
q_str1 = widgets.Text(placeholder="a + bi", disabled=False, layout=strInputLayout1)
q_str2 = widgets.Text(placeholder="a + bi", disabled=False, layout=strInputLayout1)
q_str3 = widgets.Text(placeholder="a + bi", disabled=False, layout=strInputLayout1)

Q1_output = Output()
Q2_output = Output()
Q3_output = Output()

with Q1_output:
    display(Math(r"\text{Given that } c_1=3i+4, c_2=5+11i\text{ and } c_3=4i")),
    display(Math(r"1.\ \text{Compute: } c_1 \times c_2"))

with Q2_output:
    display(Math(r"2.\ \text{Calculate: }\frac{c_1}{c_3}"))

with Q3_output:
    display(Math(r"3.\ \text{Calculate: }\frac{c_2}{c_1}"))

Qbtn_2_1 = widgets.Button(
    description="Check Answers",
    disabled=False,
    button_style="success",  # 'success', 'info', 'warning', 'danger' or ''
    tooltip="Check Answers",
    icon="check",
)

# Boxes
SAQuiz2_1 = VBox(
    [
        Label("Q01.03 Self Assessment Quiz"),
        Label("May be used for in-class hands-on practice."),
        Label("Solve the following using cartesian representation:"),
        Q1_output,
        HBox([q_str1, q_valid1, q_label1]),
        Q2_output,
        HBox([q_str2, q_valid2, q_label2]),
        Q3_output,
        HBox([q_str3, q_valid3, q_label3]),
        VBox([HBox([Qbtn_2_1])], layout=Layout(align_items="center")),
    ],
)


# Logic
def QCheckAnswers2_1(btn):
    count = 0
    try:
        if getComplex(q_str1.value) == (-13 + 59j):
            qcorrect(q_valid1, q_label1)
            count += 1
        else:
            qincorrect(q_valid1, q_label1)
    except ValueError as error:
        qformaterror(q_valid1, q_label1)
    except:
        qunknownerror(q_valid1, q_label1)

    try:
        if getComplex(q_str2.value) == (0.75 - 1j):
            qcorrect(q_valid2, q_label2)
            count += 1
        else:
            qincorrect(q_valid2, q_label2)
    except ValueError as error:
        qformaterror(q_valid2, q_label2)
    except:
        qunknownerror(q_valid2, q_label2)

    try:
        if getComplex(q_str3.value) == (2.12 + 1.16j):
            qcorrect(q_valid3, q_label3)
            count += 1
        else:
            qincorrect(q_valid3, q_label3)
    except ValueError as error:
        qformaterror(q_valid3, q_label3)
    except:
        qunknownerror(q_valid3, q_label3)

    if q_str1.value == "":
        empty(q_valid1, q_label1)
    if q_str2.value == "":
        empty(q_valid2, q_label2)
    if q_str3.value == "":
        empty(q_valid3, q_label3)

    if count == 3:
        Qbtn_2_1.button_style = "info"
        Qbtn_2_1.description = "Way to Go!"
        Qbtn_2_1.icon = "check"
    if count == 2:
        Qbtn_2_1.button_style = "warning"
        Qbtn_2_1.icon = "times"
        Qbtn_2_1.description = "Close!"
    if count < 1:
        Qbtn_2_1.button_style = "danger"
        Qbtn_2_1.icon = "times"
        Qbtn_2_1.description = "Try Again"


# Events
Qbtn_2_1.on_click(QCheckAnswers2_1)

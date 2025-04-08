import cmath
import random

from IPython.display import Math, display
from ipywidgets import Box, Button, HBox, Label, Layout, Output, VBox, interact, widgets

from QKDResources.pyfiles.helpermethods import (
    buttonsuccess,
    checkComplex,
    makeButton,
    newfillblank,
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
    ],
    layout=Layout(display="flex_flow", height="100%"),
)


# Logic
def QCheckAnswers2_1(btn):
    count = 0
    for q in qlist2_1:
        count += checkComplex(q[1].value, complex(q[0]), q[3], q[4])
    buttonsuccess(Qbtn2_1, count, 3, 2)


def createQuiz2_1():
    display(SAQuiz2_1)
    display(widgets.HTMLMath(value='<font size="+1">'))
    qlist2_1.append(
        newfillblank("1. Compute: $c_1$ &#10005; $c_2$", 0, -13 + 59j, strInputLayout2)
    )
    qlist2_1.append(
        newfillblank(
            "2. Calculate: <sup>${c_1}$</sup>&frasl;<sub>${c_3}$</sub> ",
            0,
            0.75 - 1j,
            strInputLayout2,
        )
    )
    qlist2_1.append(
        newfillblank(
            "3. Resolve: <sup>${c_2}$</sup>&frasl;<sub>${c_1}$</sub> ",
            0,
            2.12 + 1.16j,
            strInputLayout2,
        )
    )
    for q in qlist2_1:
        display(q[2])
        display(HBox([q[1], q[3], q[4]]))
    display(VBox([Qbtn2_1], layout=center))


# Events
Qbtn2_1 = makeButton()
qlist2_1 = []
Qbtn2_1.on_click(QCheckAnswers2_1)

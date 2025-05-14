import cmath
import random

from QKDResources.pyfiles.helpermethods import (
    buttonsuccess,
    checkComplex,
    makeButton,
    makeQuestion,
    newfillblank,
    prepareQuestion,
    qonclick,
)
from ipywidgets import Box, Button, HBox, Label, Layout, VBox, interact, widgets


def q1onClick(btn):
    qonclick(btn, q1)


def q2onClick(btn):
    qonclick(btn, q2)


# Layouts
numInputLayout = Layout(width="55px")
strInputLayout1 = Layout(width="90px")
strInputLayout2 = Layout(width="130px")
center = Layout(align_items="center")
q1 = prepareQuestion(
    r"a.\ \langle V_1,c\cdot V_2\rangle = \overline{c}\langle V_1,V_2\rangle",
    ["hint 1", "hint 2", "hint 3", "hint 4", "hint 5"],
    r"LHS = \langle V_1,c\cdot V_2\rangle = V_1^\dagger c\cdot V_2 = c\cdot V_1^\dagger\cdot V_2 = (\overline{c}\cdot V_1)^\dagger\cdot V_2 = \langle \overline{c}V_1, V_2\rangle = \overline{c}\langle V_1, V_2\rangle = RHS",
)
q2 = prepareQuestion(
    r"b.\ \langle V_1,V_2\rangle = \overline{\langle V_2,V_1\rangle}",
    ["hint 1"],
    r"LHS = \langle V_1,V_2\rangle = V_1^\dagger\cdot V_2=(V_2^\dagger\cdot V_1)^\dagger=(\langle V_2,V_1\rangle)^\dagger=\overline{\langle V_2,V_1\rangle} = RHS",
)
SAQuiz6_1 = VBox(
    [
        widgets.HTML(value='<b><font size="+2">Q02.07 Self Assessment Quiz'),
        widgets.HTML(
            value='<b><font size="-1"<b>May be used for in-class hands-on practice.</b>'
        ),
    ],
    layout=Layout(display="flex_flow", height="100%"),
)


def QCheckAnswers6_1(btn):
    count = 0
    for q in qlist6_1:
        count += checkComplex(q[1].value, complex(q[0]), q[3], q[4])
    buttonsuccess(Qbtn6_1, count, 3, 2)


def createQuiz6_1():
    display(SAQuiz6_1)
    display(
        widgets.HTMLMath(
            value='<font size="+1">1. Compute the inner product of the following.'
        )
    )

    qlist6_1.append(
        newfillblank(
            r"a.\ V_1=\begin{bmatrix}3\\4\\-10i\end{bmatrix} \text{ and } V_2=\begin{bmatrix}3-2i\\0\\1+i\end{bmatrix}",
            -1 + 4j,
            strInputLayout2,
        )
    )
    qlist6_1.append(
        newfillblank(
            r"b.\ V_1=\begin{bmatrix}-3\\-4\\10i\end{bmatrix}\text{ and }V_2=\begin{bmatrix}-3+2i\\0\\-1-i\end{bmatrix}",
            19 - 16j,
            strInputLayout2,
        )
    )
    qlist6_1.append(
        newfillblank(
            r"c.\ A = \begin{bmatrix}-2i& 0& 5+4i\\ 1& -1&-i-1\\ 0& 4-5i& 1\end{bmatrix}\text{ and }B = \begin{bmatrix}4-2i& 1& -5\\ i& -i+2&1\\ 1& 0& 3+4i\end{bmatrix}",
            -21 - 5j,
            strInputLayout2,
        )
    )
    for q in qlist6_1:
        display(q[2])
        display(HBox([Label(layout=Layout(width="40px")), q[1], q[3], q[4]]))
    display(VBox([Qbtn6_1], layout=center))
    makeQuestion(q1, q1onClick)
    makeQuestion(q2, q2onClick)


Qbtn6_1 = makeButton()
Qbtn6_1.on_click(QCheckAnswers6_1)

qlist6_1 = []

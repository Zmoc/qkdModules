import cmath
import random

from QKDResources.pyfiles.helpermethods import (
    buttonsuccess,
    checkComplex,
    checkMatrix,
    makeButton,
    newfillblank,
    newMatrixAdd,
)
from ipywidgets import Box, Button, HBox, Label, Layout, VBox, interact, widgets, Output
from IPython.display import display, Math

# Layouts
numInputLayout = Layout(width="55px")
strInputLayout1 = Layout(width="90px")
strInputLayout2 = Layout(width="170px")
center = Layout(align_items="center")
hidden = Layout(visibility="hidden")

matrixlayout = Layout(display="flex", align_items="stretch", width="100%")

intro_output = Output()
with intro_output:
    display(
        Math(
            r"\text{Let } c_1=2+7i, c_2=1-5i, \text{ and } X= \begin{bmatrix}5i\\5-1i\\7+10i\end{bmatrix} \text{ and } Y= \begin{bmatrix}-2i\\3+5i\\12\end{bmatrix}"
        )
    )

# Boxes
SAQuiz4_1 = VBox(
    [
        widgets.HTML(value='<b><font size="+2">Q02.01 Self Assessment Quiz'),
        widgets.HTML(
            value='<b><font size="-1"<b>May be used for in-class hands-on practice.</b>'
        ),
        intro_output,
    ],
    layout=Layout(display="flex_flow", height="100%"),
)


# Logic
def QCheckAnswers4_1(btn):
    count = 0
    for q in qlist4_1_1:
        count += checkMatrix(q[1], q[0], q[4], q[5])
    buttonsuccess(Qbtn4_1, count, 3, 2)


def createQuiz4_1():
    display(SAQuiz4_1)
    display(widgets.HTML(value='<font size="+2">1. Compute the following.'))
    qlist4_1_1.append(
        newMatrixAdd(
            r"X+Y",
            [3j, 8 + 4j, 19 + 10j],
            strInputLayout2,
            3,
            r"\begin{bmatrix}a\\b\\c\end{bmatrix}",
        )
    )
    qlist4_1_1.append(
        newMatrixAdd(
            r"c_1X+c_2Y",
            [-45 + 8j, 45 + 23j, -44 + 9j],
            strInputLayout2,
            3,
            r"\begin{bmatrix}a\\b\\c\end{bmatrix}",
        )
    )
    qlist4_1_1.append(
        newMatrixAdd(
            r"X-Y",
            [7j, 2 - 6j, -5 + 10j],
            strInputLayout2,
            3,
            r"\begin{bmatrix}a\\b\\c\end{bmatrix}",
        )
    )

    for q in qlist4_1_1:
        display(
            HBox(
                [
                    VBox([Label(), q[2]]),
                    q[3],
                    VBox(
                        [
                            HBox(
                                [q[5], Label()], layout=Layout(justify_content="center")
                            ),
                            HBox([q[1][0], q[1][1], q[1][2], q[4]]),
                        ]
                    ),
                ],
                layout=matrixlayout,
            )
        )

    display(VBox([Qbtn4_1], layout=center))


# Events
Qbtn4_1 = makeButton()
qlist4_1 = []
qlist4_1_1 = []
Qbtn4_1.on_click(QCheckAnswers4_1)

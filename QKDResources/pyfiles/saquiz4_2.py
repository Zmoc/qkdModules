from QKDResources.pyfiles.helpermethods import makeQuestion, prepareQuestion, qonclick
from ipywidgets import Box, Button, HBox, Label, Layout, VBox, interact, widgets, Output
from IPython.display import display, Math


def q1onClick(btn):
    qonclick(btn, q1)


def q2onClick(btn):
    qonclick(btn, q2)


def q3onClick(btn):
    qonclick(btn, q3)


q1 = prepareQuestion(
    r"1.\ (A+B)^T = A^T+B^T",
    ["hint 1", "hint 2", "hint 3", "hint 4", "hint 5"],
    r"(A+B)^T = A^T+B^T = \begin{bmatrix}i& 3+11i\\2+5i&6-10i\end{bmatrix}",
)
q2 = prepareQuestion(
    r"2.\ \overline{A+B}=\overline{A}+\overline{B}",
    ["hint 1"],
    r"\overline{A+B}=\overline{A}+\overline{B} = \begin{bmatrix}-i&2-5i\\3-11i&6+10i\end{bmatrix}",
)
q3 = prepareQuestion(
    r"3.\ (A+B)^\dagger = A^\dagger+B^\dagger",
    ["hint 1", "hint 2", "hint 3"],
    r"LHS = (A+B)^\dagger = (\overline{A+B})^T  =  (\overline{A}+\overline{B})^T  =  \overline{A}^T+\overline{B}^T = A^\dagger+B^\dagger = RHS",
)

intro_output = Output()
with intro_output:
    display(
        Math(
            r"\text{Given } A = \begin{bmatrix}1+i&2\\-3&1-i\end{bmatrix} \text{ and } B = \begin{bmatrix}-1&5i\\6+11i&5-9i\end{bmatrix}, \text{verify the following properties numerically:}"
        )
    )

SAQuiz4_2 = VBox(
    [
        widgets.HTML(value='<b><font size="+2">Q02.02 Self Assessment Quiz'),
        widgets.HTML(
            value='<b><font size="-1"<b>Maybe used for in-class hands-on practice.</b>'
        ),
        intro_output,
    ],
    layout=Layout(display="flex_flow", height="100%"),
)


def createQuiz4_2():
    display(SAQuiz4_2)
    makeQuestion(q1, q1onClick)
    makeQuestion(q2, q2onClick)
    makeQuestion(q3, q3onClick)

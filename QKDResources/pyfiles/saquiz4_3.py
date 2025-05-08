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
    r"1.\ (A\cdot B)\cdot C = A\cdot(B\cdot C)",
    ["hint 1", "hint 2", "hint 3", "hint 4", "hint 5"],
    r"(A\cdot B)\cdot C = A\cdot(B\cdot C) = \begin{bmatrix}46-100i& 15+3i\\196-10i& -3+21i\end{bmatrix}",
)
q2 = prepareQuestion(
    r"2.\ A\cdot(B+C) = (A\cdot B)+(A\cdot C)",
    ["hint 1"],
    r"A\cdot(B+C) = (A\cdot B)+(A\cdot C) = \begin{bmatrix}26-8i&16\\2-26i&1+21i\end{bmatrix}",
)
q3 = prepareQuestion(
    r"3.\ c\cdot(A\cdot B) = (c\cdot A)\cdot B = A\cdot(c\cdot B)",
    ["hint 1", "hint 2", "hint 3"],
    r"c\cdot(A\cdot B) = (c\cdot A)\cdot B = A\cdot(c\cdot B) = \begin{bmatrix}-10-80i& 90-60i\\110-80i& 90+120i\end{bmatrix}",
)

intro_output = Output()
with intro_output:
    display(
        Math(
            r"\text{Let } A= \begin{bmatrix}2& 1-3i\\-1-3i& 4\end{bmatrix}, B=\begin{bmatrix}i&-i\\ 4+1i& 5i\end{bmatrix}, C=\begin{bmatrix}10-1i&0\\-1&1\end{bmatrix} \text{ and } c=5-5i."
        )
    )

SAQuiz4_2 = VBox(
    [
        widgets.HTML(value='<b><font size="+2">Q02.03 Self Assessment Quiz'),
        intro_output,
    ],
    layout=Layout(display="flex_flow", height="100%"),
)


def createQuiz4_3():
    display(SAQuiz4_2)
    display(
        widgets.HTMLMath(
            value='<font size="+1">Verify the following properties numerically:'
        )
    )
    makeQuestion(q1, q1onClick)
    makeQuestion(q2, q2onClick)
    makeQuestion(q3, q3onClick)

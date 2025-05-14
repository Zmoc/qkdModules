from QKDResources.pyfiles.helpermethods import makeQuestion, prepareQuestion, qonclick
from ipywidgets import Box, Button, HBox, Label, Layout, VBox, interact, widgets


def q1onClick(btn):
    qonclick(btn, q1)


def q2onClick(btn):
    qonclick(btn, q2)


def q3onClick(btn):
    qonclick(btn, q3)


def q4onClick(btn):
    qonclick(btn, q4)


q1 = prepareQuestion(
    r"1.\ \text{If a two state system has }\frac{3}{4}\text{ probability of being in state 0 then we can represent this with a probabibility vector:}",
    ["hint 1", "hint 2", "hint 3", "hint 4", "hint 5"],
    r"\begin{bmatrix}\frac{3}{4}\\\\\frac{1}{4}\end{bmatrix}",
)
q2 = prepareQuestion(
    r'2.\ \text{If I "look" at a two state system and find it in state 1, then my knowledge of the state of the system is given by:}',
    ["hint 1"],
    r"\begin{bmatrix}0\\1\end{bmatrix}",
)
q3 = prepareQuestion(
    r"3.\ \text{Consider a system that can be in states 1, 2 and 3. At time }t \text{ the system may be in state 1 with probability } \frac{1}{4},\text{ state 2 with } \frac{1}{2}\text{ and state 3 with }\frac{1}{4}\text{. The system probability vector can be written as:}",
    ["hint 1", "hint 2", "hint 3", "hint 4", "hint 5"],
    r"\begin{bmatrix}\frac{1}{4}\\\\ \frac{1}{2}\\\\ \frac{1}{4}\end{bmatrix}",
)
q4 = prepareQuestion(
    r'4.\ \text{If we "look" at a three state system and find it in state 2, then the probability vector representing our knowledge is given by:}',
    ["hint 1"],
    r"\begin{bmatrix}0\\1\\0\end{bmatrix}",
)
SAQuiz9_1 = VBox(
    [
        widgets.HTML(value='<b><font size="+2">Q03.01 Self Assessment Quiz'),
    ],
    layout=Layout(display="flex_flow", height="100%"),
)


def createQuiz9_1():
    display(SAQuiz9_1)
    makeQuestion(q1, q1onClick)
    makeQuestion(q2, q2onClick)
    makeQuestion(q3, q3onClick)
    makeQuestion(q4, q4onClick)

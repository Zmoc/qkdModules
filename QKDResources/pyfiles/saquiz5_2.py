from QKDResources.pyfiles.helpermethods import makeQuestion, prepareQuestion, qonclick
from ipywidgets import Box, Button, HBox, Label, Layout, VBox, interact, widgets, Output
from IPython.display import display, Math


def q1onClick(btn):
    qonclick(btn, q1)


def q2onClick(btn):
    qonclick(btn, q2)


q1 = prepareQuestion(
    r"a.\ B_1 = \left\{\begin{bmatrix}1\\0\end{bmatrix}, \begin{bmatrix}0\\1\end{bmatrix}\right\}",
    ["hint 1", "hint 2", "hint 3", "hint 4", "hint 5"],
    r"\begin{bmatrix}1&0\\0&1\end{bmatrix}\begin{bmatrix}c_1\\c_2\end{bmatrix} = \begin{bmatrix}x\\y\end{bmatrix} \text{Because we can find the coefficients } c_1 \text{ and } c_2 \text{ for every possible value of } x \text{ and } y \text{; } B_1 \text{ forms a basis for }\mathbb{C}^2",
)
q2 = prepareQuestion(
    r"b.\ B_2 = \left\{\begin{bmatrix}1\\1\end{bmatrix}, \begin{bmatrix}1\\-1\end{bmatrix}\right\}",
    ["hint 1"],
    r"\left|\begin{matrix}1&1\\1&-1\end{matrix}\right| = -2 \text{ Therefore, the set of vectors is linearly independent, and because the vectors form is invertible, }B_2\text{ is a basis set for }\mathbb{C}^2",
)

intro_output = Output()
with intro_output:
    display(Math(r"\text{Verify that the following are basis for }\mathbb{C}^2"))

SAQuiz5_2 = VBox(
    [
        widgets.HTML(value='<b><font size="+2">Q02.05 Self Assessment Quiz'),
        widgets.HTML(
            value='<b><font size="-1"<b>May be used for in-class hands-on practice.</b>'
        ),
        intro_output,
    ],
    layout=Layout(display="flex_flow", height="100%"),
)


def createQuiz5_2():
    display(SAQuiz5_2)
    makeQuestion(q1, q1onClick)
    makeQuestion(q2, q2onClick)

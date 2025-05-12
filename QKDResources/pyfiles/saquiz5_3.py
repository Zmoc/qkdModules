from QKDResources.pyfiles.helpermethods import makeQuestion, prepareQuestion, qonclick
from ipywidgets import Box, Button, HBox, Label, Layout, VBox, interact, widgets


def q1onClick(btn):
    qonclick(btn, q1)


def q2onClick(btn):
    qonclick(btn, q2)


def q3onClick(btn):
    qonclick(btn, q3)


q1 = prepareQuestion(
    r"a.\ \begin{bmatrix} \frac{\sqrt{2}}{2} \\\\ \frac{\sqrt{2}}{2} \end{bmatrix}",
    ["hint 1", "hint 2", "hint 3", "hint 4", "hint 5"],
    r"\frac{1}{\sqrt{2}} \begin{bmatrix}1&1\\1&-1\end{bmatrix} \cdot \begin{bmatrix}\frac{\sqrt{2}}{2}\\\\\frac{\sqrt{2}}{2}\end{bmatrix} = \begin{bmatrix}1\\0\end{bmatrix}",
)
q2 = prepareQuestion(
    r"b.\ \begin{bmatrix}\frac{i}{\sqrt{3}}\\\\\frac{\sqrt{2}}{\sqrt{3}}\end{bmatrix}",
    ["hint 1"],
    r"\frac{1}{\sqrt{2}}\begin{bmatrix}1&1\\1&-1\end{bmatrix} \cdot \begin{bmatrix}\frac{i}{\sqrt{3}}\\\\\frac{\sqrt{2}}{\sqrt{3}} \end{bmatrix} = \begin{bmatrix} \frac{i}{\sqrt{6}} + \frac{1}{\sqrt{3}} \\\\ \frac{i}{\sqrt{6}}-\frac{1}{\sqrt{3}} \end{bmatrix}",
)
q3 = prepareQuestion(
    r"2.\ \text{Prove that Hadamard matrix is its own inverse.}",
    ["hint 1"],
    r"\frac{1}{\sqrt{2}} \begin{bmatrix}1&1\\1&-1\end{bmatrix} \cdot \frac{1}{\sqrt{2}} \begin{bmatrix}1&1\\1&-1\end{bmatrix} = \begin{bmatrix}1&0\\0&1\end{bmatrix}",
)
SAQuiz5_3 = VBox(
    [
        widgets.HTML(value='<b><font size="+2">Q02.06 Self Assessment Quiz'),
        widgets.HTML(
            value='<b><font size="-1"<b>May be used for in-class hands-on practice.</b>'
        ),
    ],
    layout=Layout(display="flex_flow", height="100%"),
)


def createQuiz5_3():
    display(SAQuiz5_3)
    display(
        widgets.HTMLMath(
            value='<font size="+1">1. Represent the following vectors with respect to Hadamard basis,'
        )
    )
    makeQuestion(q1, q1onClick)
    makeQuestion(q2, q2onClick)
    makeQuestion(q3, q3onClick)

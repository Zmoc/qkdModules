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
    r"a.\ \begin{bmatrix}2&-4\\-1&-1\end{bmatrix}",
    ["hint 1", "hint 2", "hint 3", "hint 4", "hint 5"],
    r"\text{Eigenvalues: }\lambda=-2\text{ and }\lambda=3 \text{ Eigenvectors: } \begin{bmatrix}1\\1\end{bmatrix}\text{ and } \begin{bmatrix}-4\\1\end{bmatrix}",
)
q2 = prepareQuestion(
    r"b. \begin{bmatrix}3&-2\\4&-1\end{bmatrix}",
    ["hint 1"],
    r"\text{Eigenvalues: } \lambda=1+2i\text{ and }\lambda=1-2i \text{ Eigenvectors: } \begin{bmatrix}\frac{1}{2}+i\frac{1}{2}\\1\end{bmatrix}\text{ and } \begin{bmatrix}\frac{1}{2}-i\frac{1}{2}\\1\end{bmatrix}",
)
q3 = prepareQuestion(
    r"a.\ A = \begin{bmatrix}2&-i\\i&1\end{bmatrix}",
    ["hint 1", "hint 2", "hint 3", "hint 4", "hint 5"],
    r"A^\dagger = \begin{bmatrix}2&-i\\i&1\end{bmatrix}= A",
)
q4 = prepareQuestion(
    r"b.\ B = \begin{bmatrix}1&1+i&2i\\1-i&5&-3\\-2i&-3&0\end{bmatrix}",
    ["hint 1"],
    r"B^\dagger = \begin{bmatrix}1&1+i&2i\\1-i&5&-3\\-2i&-3&0\end{bmatrix}= B",
)
SAQuiz7_1 = VBox(
    [
        widgets.HTML(value='<b><font size="+2">Q02.09 Self Assessment Quiz'),
    ],
    layout=Layout(display="flex_flow", height="100%"),
)


def createQuiz7_1():
    display(SAQuiz7_1)
    display(
        widgets.HTMLMath(
            value='<font size="+1">1. Compute the eigenvectors and eigenvalues associated with the following matrices.'
        )
    )
    makeQuestion(q1, q1onClick)
    makeQuestion(q2, q2onClick)

    display(
        widgets.HTMLMath(
            value='<font size="+1">2. Verify that the following matrices are Hermitian.'
        )
    )
    makeQuestion(q3, q3onClick)
    makeQuestion(q4, q4onClick)

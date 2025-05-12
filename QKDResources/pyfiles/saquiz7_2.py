from QKDResources.pyfiles.helpermethods import makeQuestion, prepareQuestion, qonclick
from ipywidgets import Box, Button, HBox, Label, Layout, VBox, interact, widgets


def q1onClick(btn):
    qonclick(btn, q1)


def q2onClick(btn):
    qonclick(btn, q2)


q1 = prepareQuestion(
    r"a.\ \frac{1}{2}\begin{bmatrix}1+i& 1+i\\1-i&-1+i\end{bmatrix}",
    ["hint 1", "hint 2", "hint 3", "hint 4", "hint 5"],
    r"A^\dagger\cdot A = \frac{1}{2}\begin{bmatrix}1-i&1+i\\1-i&-1-i\end{bmatrix} \cdot \frac{1}{2}\begin{bmatrix}1+i& 1+i\\1-i&-1+i\end{bmatrix} = \begin{bmatrix}1&0\\0&1\end{bmatrix}",
)
q2 = prepareQuestion(
    r"b.\ \begin{bmatrix}cos\theta&-sin\theta&0\\sin\theta&cos\theta&0\\0&0&1\end{bmatrix}",
    ["hint 1"],
    r"B^\dagger\cdot B = \begin{bmatrix}cos{\theta}& sin{\theta}& 0\\-sin{\theta}& cos{\theta}& 0\\0&0&1\end{bmatrix} \cdot \begin{bmatrix}cos{\theta}&-sin{\theta}&0\\sin{\theta}&cos{\theta}&0\\0&0&1\end{bmatrix} = \begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix}",
)

SAQuiz7_2 = VBox(
    [
        widgets.HTML(value='<b><font size="+2">Q02.10 Self Assessment Quiz'),
    ],
    layout=Layout(display="flex_flow", height="100%"),
)


def createQuiz7_2():
    display(SAQuiz7_2)
    display(
        widgets.HTMLMath(
            value='<font size="+1">1. Verify that the following matrices are unitary,'
        )
    )
    makeQuestion(q1, q1onClick)
    makeQuestion(q2, q2onClick)

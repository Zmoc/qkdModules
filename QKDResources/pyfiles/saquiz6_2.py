from QKDResources.pyfiles.helpermethods import makeQuestion, prepareQuestion, qonclick
from ipywidgets import Box, Button, HBox, Label, Layout, VBox, interact, widgets, Output
from IPython.display import display, Math


def q1onClick(btn):
    qonclick(btn, q1)


def q2onClick(btn):
    qonclick(btn, q2)


q1 = prepareQuestion(
    r"1.\ \rvert V_1+V_2\rvert\leq\rvert V_1\rvert+\rvert V_2\rvert",
    ["hint 1", "hint 2", "hint 3", "hint 4", "hint 5"],
    r"|V_1+V_2| = \sqrt{\langle V,V\rangle} = \sqrt{190} \leq |V_1|+|V_2| = 125+65 = 190",
)
q2 = prepareQuestion(
    r"2.\ \rvert c\cdot V_1\rvert=\rvert c\rvert\times\rvert V_1\rvert \text{ Let } c=5-5i",
    ["hint 1"],
    r"\text{LHS: }|c\cdot V_1|=\left|(5-5i)\cdot\begin{bmatrix}3\\4\\-10i\end{bmatrix}\right|=\sqrt{6250} \quad \text{RHS: }|c|\times|V_1|=\sqrt{50}\cdot\sqrt{125}=\sqrt{6250}",
)

intro_output = Output()
with intro_output:
    display(
        Math(
            r"\text{Given }V_1=\begin{bmatrix}3\\4\\-10i\end{bmatrix} \text{ and } V_2=\begin{bmatrix}8i\\0\\1\end{bmatrix}\text{, verify the following numerically:}"
        )
    )

SAQuiz6_2 = VBox(
    [
        widgets.HTML(value='<b><font size="+2">Q02.08 Self Assessment Quiz'),
        widgets.HTML(
            value='<b><font size="-1"<b>May be used for in-class hands-on practice.</b>'
        ),
        intro_output,
    ],
    layout=Layout(display="flex_flow", height="100%"),
)


def createQuiz6_2():
    display(SAQuiz6_2)

    makeQuestion(q1, q1onClick)
    makeQuestion(q2, q2onClick)

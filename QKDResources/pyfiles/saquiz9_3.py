from QKDResources.pyfiles.helpermethods import makeQuestion, prepareQuestion, qonclick
from ipywidgets import Box, Button, HBox, Label, Layout, VBox, interact, widgets


def q1onClick(btn):
    qonclick(btn, q1)


def q2onClick(btn):
    qonclick(btn, q2)


q1 = prepareQuestion(
    r"1.\ \text{The brightest:}",
    ["hint 1", "hint 2", "hint 3", "hint 4", "hint 5"],
    r"cos^2 (\theta_1-90^{\circ}) \quad cos^2(0^{\circ} - \theta_1) = \frac{1}{4}\text{ After solving you find } \theta = 45^{\circ}",
)

q2 = prepareQuestion(
    r"2.\ \text{About }\frac{1}{3}\text{ bright:}",
    ["hint 1"],
    r"\text{It turns out that no value of } \theta \text{ will result in } \frac{1}{3}\text{. Therefore, it is not achievable.}",
)


SAQuiz9_3 = VBox(
    [
        widgets.HTML(value='<b><font size="+2">Q03.03 Self Assessment Quiz'),
        widgets.HTML(
            value='<font size="+0">What angle should the middle filter be polarized at so that the screen is:'
        ),
    ],
    layout=Layout(display="flex_flow", height="100%"),
)


def createQuiz9_3():
    display(SAQuiz9_3)
    makeQuestion(q1, q1onClick)
    makeQuestion(q2, q2onClick)

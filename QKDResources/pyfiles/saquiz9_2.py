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
    r"1.\ \text{When quantum system states are represented using vectors, what are the elements of such a vector: complex numbers, real numbers or integers?}",
    ["hint 1", "hint 2", "hint 3", "hint 4", "hint 5"],
    r"\text{Complex numbers: The elements can also be real numbers and integers but the set of complex numbers includes them. Therefore the most general case answer is complex numbers.}",
)
q2 = prepareQuestion(
    r"2. \text{What type of matrices are valid operators for a quantum system?}",
    ["hint 1"],
    r"\text{Unitary Matrices}",
)
q3 = prepareQuestion(
    r"3. \text{Are quantum systems reversible? Why?}",
    ["hint 1", "hint 2", "hint 3", "hint 4", "hint 5"],
    r'\text{Yes, quantum systems are reversible because the evolution of a quantum system can be modelled using unitary matrices which can be "inverted".}',
)
SAQuiz9_2 = VBox(
    [
        widgets.HTML(value='<b><font size="+2">Q03.02 Self Assessment Quiz'),
    ],
    layout=Layout(display="flex_flow", height="100%"),
)


def createQuiz9_2():
    display(SAQuiz9_2)
    makeQuestion(q1, q1onClick)
    makeQuestion(q2, q2onClick)
    makeQuestion(q3, q3onClick)

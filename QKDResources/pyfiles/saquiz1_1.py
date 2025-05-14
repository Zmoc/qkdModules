import matplotlib.pyplot as plt
from IPython.display import Math, display
from ipywidgets import Button, Dropdown, HBox, Label, Layout, Output, Valid, VBox

plt.close("all")

# Layout Configurations
hidden = Layout(visibility="hidden")
visible = Layout(visibility="visible")

# Validity Indicators
QValid1_1 = Valid(value=False, readout="Incorrect", layout=hidden)
QValid1_2 = Valid(value=False, readout="Incorrect", layout=hidden)

# Question Text
Q1_output = Output()
Q2_output = Output()
with Q1_output:
    display(Math(r"1.\ \text{Solve for } x \text{ where } x^2 + 25 = 0."))
with Q2_output:
    display(Math(r"2.\ \text{Simplify } i^{225}. \text{ (Hint: find a pattern)}"))

# Answer Selection Dictionary
selected_answer = {"value": None}

# LaTeX Answer Buttons
answer_choices = [
    (r"a.\ x = 5i", "a"),
    (r"b.\ x = -5i", "b"),  # Correct Answer
    (r"c.\ x = i", "c"),
    (r"d.\ x = 5", "d"),
]


def select_answer(ans, btn):
    """Updates the selected answer and highlights the chosen button."""
    selected_answer["value"] = ans
    for b in answer_buttons:
        b.button_style = "primary" if b == btn else ""  # Highlight selected


answer_buttons = [
    Button(
        description="",
        layout=Layout(width="25px", height="25px", padding="0px", border_radius="50%"),
        button_style="",
    )
    for _ in answer_choices
]

answer_outputs = [Output() for _ in answer_choices]

for btn, (text, value), out in zip(answer_buttons, answer_choices, answer_outputs):
    with out:
        display(Math(text))
    btn.on_click(lambda b, v=value, btn=btn: select_answer(v, btn))

QButtons1_1 = HBox(
    [
        HBox([btn, out], layout=Layout(align_items="center", margin="2px"))
        for btn, out in zip(answer_buttons, answer_outputs)
    ]
)

# Dropdown Answer Choices for Q2
QDropdown1_2 = Dropdown(
    options={"1": 1, "-1": 2, "i": 3, "-i": 4},
    value=1,
    description="----->",
)

# Check Answers Button
Qbtn_1 = Button(
    description="Check Answers",
    disabled=False,
    button_style="success",
    tooltip="Check Answers",
    icon="check",
)


# Answer Checking Logic
def QCheckAnswers_1(btn):
    count = 0

    # Check first answer
    if selected_answer["value"] == "b":
        QValid1_1.value = True
        QValid1_1.readout = "Correct"
        count += 1
    else:
        QValid1_1.value = False
        QValid1_1.readout = "Incorrect"

    # Check second answer
    if QDropdown1_2.value == 3:
        QValid1_2.value = True
        QValid1_2.readout = "Correct"
        count += 1
    else:
        QValid1_2.value = False
        QValid1_2.readout = "Incorrect"

    # Update Button Styles
    styles = {
        2: ("info", "Way to Go!"),
        1: ("warning", "Close!"),
        0: ("danger", "Try Again"),
    }
    Qbtn_1.button_style, Qbtn_1.description = styles[count]
    Qbtn_1.icon = "check" if count == 2 else "times"

    QValid1_1.layout = visible
    QValid1_2.layout = visible


Qbtn_1.on_click(QCheckAnswers_1)

# Final Layout
SAQuiz1_1 = VBox(
    [
        Label("Q01.01 Self Assessment Quiz"),
        Label("May be used for in-class hands-on practice."),
        Q1_output,
        HBox([QButtons1_1, QValid1_1]),
        Q2_output,
        HBox([QDropdown1_2, QValid1_2]),
        VBox([Qbtn_1], layout=Layout(align_items="center")),
    ]
)

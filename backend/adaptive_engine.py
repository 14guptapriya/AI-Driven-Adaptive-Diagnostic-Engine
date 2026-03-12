def update_ability(current_ability, correct):

    step=0.08

    if correct:
        current_ability += step
    else:
        current_ability -= step

    current_ability = max(0.1, min(1.0, current_ability))

    return current_ability


def select_question(ability, questions):

    closest = min(
        questions,
        key=lambda q: abs(q["difficulty"] - ability)
    )

    return closest
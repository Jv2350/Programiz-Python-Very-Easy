# Write a function to check whether a student passed or failed his/her examination.
# Instructions
# Assume the pass marks to be 50.
# Return Passed if the student scored more than 50. Otherwise, return I Failed if they failed.


def pass_fail(score):
    return "Passed" if score >= 50 else "Failed"

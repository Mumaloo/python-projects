def gradingStudents(grades):
    final = []
    for grade in grades:
        r = grade
        if grade < 38:
            r = grade
        elif grade % 5 >= 3:
            r = int(round(grade, -1))
            if r < grade:
                r = r + 5
        final.append(r)
    return final


print gradingStudents([73, 67, 38, 33])
#print gradingStudents([67])
def grade_for(marks):
    if marks >= 90:
        print( "A")
    elif marks>= 75 and marks<=89:
        return "B"
    elif marks>= 60 and marks<=74:
        return "C"
    elif marks>= 40 and marks<=59:
        return "D"
    else:
        return "F"

for m in [95, 82, 72, 55, 30]:
    print(m, "->", grade_for(m))
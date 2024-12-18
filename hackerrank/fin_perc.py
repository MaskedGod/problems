student_marks = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [25, 26.5, 28],
}
query_name = "Malika"
sum_of_marks = sum(student_marks[query_name])
length_of_marks = len(student_marks[query_name])
avg = float(sum_of_marks) / float(length_of_marks)
print(f"{avg:.2f}")

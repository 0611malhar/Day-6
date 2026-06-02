'''
A school has a list of students' test scores. The school wants to select only those students who scored 50 or more marks for the next round.
Using Python's filter() function, create a new list containing only the scores of the selected students.
Input:
scores = [35, 78, 49, 90, 52, 41, 67, 28, 85]
Expected Output:
[78, 90, 52, 67, 85]
'''

scores = [35, 78, 49, 90, 52, 41, 67, 28, 85]
s = list(filter(lambda x: x >= 50, scores))
print(s)

'''
A teacher has a list of students' marks. The school has decided to award 5 bonus marks to every student.
Using Python's map() function, create a new list containing the updated marks after adding the bonus marks.
Input:
scores = [35, 78, 49, 90, 52]
Expected Output:
[40, 83, 54, 95, 57]
'''

scores = [35, 78, 49, 90, 52]
updated_scores = list(map(lambda score: score + 5, scores))
print(updated_scores)

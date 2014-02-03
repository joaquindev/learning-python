lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler];

"""
for names in students:
    print names["name"]
    print names["homework"]
    print names["quizzes"]
    print names["tests"] 
"""

def average(lst):
    result = sum(lst);
    return float(result)/len(lst); 

print average([0,2]);
   
def get_average(student):
    return average(student["homework"])*0.1 + average(student["quizzes"])*0.3 + average(student["tests"])*0.6;

def get_letter_grade(score):
    if score >= 90: 
        return "A"
    elif score < 90 and score >= 80: 
        return "B"
    elif score < 80 and score >= 70: 
        return "C"
    elif score < 70 and score >= 60: 
        return "D"
    else:
        return "F"


def get_class_average(class_list):
    total = 0;
    for student in class_list:
        total += get_average(student)
    return float(total)/len(class_list)




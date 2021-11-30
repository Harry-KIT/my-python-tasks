# For loops

student_names = ['Ali', 'Valijon', 'Gulinora', 'Salim', 'Halim']
long_names = []
for student_name in student_names:
    if len(student_name) > 5:
        long_names.append(student_name)

print(long_names)

##################################################################
pairs = []
for student_name1 in student_names:
    for student_name2 in student_names:
        if student_name1 != student_name2:
            pairs.append(
                (student_name1, student_name2)
            )


print(pairs)

##################################################################
# Tuples

student_grades = [('Ali', 'Spanish', 'A'),
                  ('Vali', 'French', 'B+'),
                  ('Gulinora', 'Italian', 'C+'),
                  ('Halim', 'English', 'A+')]

for student_ismi, subject, grade in student_grades:
    if grade.startswith('A'):
        print('Congratulation ', student_ismi, 'on getting an', grade, 'in', subject)


for student_grade in student_grades:
    if student_grade[2].startswith('A'):
        print('Congratulation ', student_grade[0], 'on getting an', student_grade[2], 'in', student_grade[1])

##################################################################

# Dictionary

record = {
    'name': 'Ali',
    'grade': 'A',
    'subject': 'Italian'
}

print(record['name'], 'got a grade of ', record['grade'], 'in', record['subject'])

name, subject, grade = ('Ali', 'Italian', 'A')
print(name, 'got a grade of ', grade, 'in', subject)

##################################################################

# List of Dictionary

student_grades = [('Ali', 'Spanish', 'A'),
                  ('Vali', 'French', 'B+'),
                  ('Gulinora', 'Italian', 'C+'),
                  ('Halim', 'English', 'A+')]

student_grade_record = []

for ism, fan, baho in student_grades:
    records = {
        'name': ism,
        'subject': fan,
        'grade': baho
    }
    student_grade_record.append(records)

print(student_grade_record)
print(student_grade_record[1]['grade'])


for rec in student_grade_record:
    if rec['grade'].startswith('A'):
         print('Congratulation ', rec['name'], 'on getting an', rec['grade'], 'in', rec['subject'])

##################################################################

# Dictionary of Dictionary

student_grades = [('Ali', 'Spanish', 'A'),
                  ('Vali', 'French', 'B+'),
                  ('Gulinora', 'Italian', 'C+'),
                  ('Halim', 'English', 'A+')]

foreign_language_grades = {}

for student_ismi, subject, grade in student_grades:
    record1 = {
        'subject': subject,
        'grade': grade
    }
    foreign_language_grades[student_ismi] = record1

print(foreign_language_grades)
print(foreign_language_grades['Vali'])
print(foreign_language_grades['Vali']['grade'])

##################################################################

# Another Dictionary of Dictionary

student_grades = [('Ali', 'Spanish', 'A'),
                  ('Vali', 'French', 'B+'),
                  ('Gulinora', 'Italian', 'C+'),
                  ('Halim', 'English', 'A+')]

record_cards = {}

for student_ismi, subject, grade in student_grades:
    if student_ismi not in record_cards:
        record_cards[student_ismi]={}
    record_cards[student_ismi][subject] = grade

print(record_cards)
record_cards['Ali']['Math'] = 'D'
print(record_cards)

##################################################################

# Dictionary with tuples

student_grades = [('Ali', 'Spanish', 'A'),
                  ('Vali', 'French', 'B+'),
                  ('Gulinora', 'Italian', 'C+'),
                  ('Halim', 'English', 'A+')]

course_grades = {}

for student_ismi, subject, grade in student_grades:
    course_grades[student_ismi, subject] = grade

print(course_grades)
course_grades['Ali', 'Math'] = 'C+'
print(course_grades)




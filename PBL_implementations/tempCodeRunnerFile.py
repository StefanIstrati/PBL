import json
from classes import Teacher, Course, Group, Offices

def load_data_from_json(file_path):
    teachers = []
    courses = []
    groups = []
    offices = []

    with open(file_path, 'r') as file:
        data = json.load(file)
        for entry in data:
            if entry['type'] == 'Teacher':
                teacher_data = entry['data']
                courses_data = [(course[0], course[1]) for course in teacher_data['courses']]
                teachers.append(Teacher(teacher_data['name'], courses_data, teacher_data['language']))
            elif entry['type'] == 'Course':
                course_data = entry['data']
                courses.append(Course(course_data['name'], course_data['course_type']))
            elif entry['type'] == 'Group':
                group_data = entry['data']
                group_courses = []
                for course in group_data['courses']:
                    if len(course) == 3:
                        group_courses.append((course[0], course[1], course[2]))
                    else:
                        print("Invalid data for group:", group_data['name'])
                groups.append(Group(group_data['name'], group_courses, group_data['language']))
            elif entry['type'] == 'Office':
                office_data = entry['data']
                offices.append(Offices(office_data['name'], office_data['office_type']))

    return teachers, courses, groups, offices

def create_list_of_tuples(teachers, courses, groups, offices):
    classes_taught = {teacher.name: 0 for teacher in teachers}

    result = []
    for group in groups:
        for group_course in group.courses:
            course = next((c for c in courses if c.name == group_course[0] and c.course_type == group_course[1]), None)
            if course:
                eligible_teachers = [teacher for teacher in teachers if (course.name, course.course_type) in teacher.courses]
                if eligible_teachers:
                    eligible_teachers.sort(key=lambda teacher: classes_taught[teacher.name])
                    teacher = eligible_teachers[0]
                    classes_taught[teacher.name] += group_course[2]
                    office = next((o for o in offices if o.office_type == course.course_type), None)
                    if (teacher.language == group.language):
                        result.append((group.name, course.name, course.course_type, teacher.name, office.name, group_course[2], group.language))
    return result


# Example usage:
if __name__ == "__main__":
    json_file = "file_1.json"
    teachers, courses, groups, offices = load_data_from_json(json_file)
    tuples_list = create_list_of_tuples(teachers, courses, groups, offices)

    for tuples in tuples_list:
        print(tuples)
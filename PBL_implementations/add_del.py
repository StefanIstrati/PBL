import json
from classes import Teacher, Course, Group, Offices
from typing import  Any

def data_exists_in_json(file_path: str, data: Any) -> bool:
    try:
        with open(file_path, 'r') as file:
            existing_data = json.load(file)
            for entry in existing_data:
                if entry['type'] == 'Teacher' and entry['data']['name'] == data.name:
                    return True
                elif entry['type'] == 'Course' and entry['data']['name'] == data.name and entry['data']['course_type'] == data.course_type:
                    return True
                elif entry['type'] == 'Group' and entry['data']['name'] == data.name:
                    return True
                elif entry['type'] == 'Office' and entry['data']['name'] == data.name:
                    return True
    except FileNotFoundError:
        pass
    except Exception as e:
        print("Error checking data in JSON:", e)
    return False

def add_data_to_json(file_path: str, data_type: str, data: Any):
    try:
        if not data_exists_in_json(file_path, data):
            with open(file_path, 'r+') as file:
                try:
                    existing_data = json.load(file)
                except json.decoder.JSONDecodeError:
                    existing_data = []

                data_dict = {"type": data_type, "data": data.__dict__}
                existing_data.append(data_dict)
                file.seek(0)
                json.dump(existing_data, file, indent=4)
    except FileNotFoundError:
        with open(file_path, 'w') as file:
            data_dict = {"type": data_type, "data": data.__dict__}
            json.dump([data_dict], file, indent=4)
    except Exception as e:
        print("Error adding data to JSON:", e)

def remove_data_from_json(file_path, name):
    try:
        with open(file_path, 'r+') as file:
            data = json.load(file)
            updated_data = [entry for entry in data if entry['data']['name'] != name]
            file.seek(0)
            json.dump(updated_data, file, indent=4)
            file.truncate()
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Error removing data from JSON:", e)

# Example Usage:
if __name__ == "__main__":
    json_file = "file_1.json"

    courses1 = [("Numerical Analysis", "Seminar"),("Numerical Analysis","Course")]
    teacher1 = Teacher("Mr. Smith", courses1,"Romanian") 
    courses2 = [("Computer Science", "Course"),("Computer Science","Laboratory")]
    teacher2 = Teacher("Mr. Brown", courses2,"Romanian")
    courses3 = [("Physics", "Course")]
    teacher3 = Teacher("Mr. Tronciu", courses3,"Romanian")
    courses4 = [("Physics", "Course"),("Physics", "Seminar"),("Physics", "Laboratory")]
    teacher4 = Teacher("Mr. Jonhson", courses4,"Romanian")

    course1 = Course("Computer Science", "Laboratory")
    course2 = Course("Numerical Analysis", "Seminar")
    course6 = Course("Numerical Analysis", "Course")
    course3 = Course("Physics", "Laboratory")
    course4 = Course("Physics", "Seminar")
    course5 = Course("Physics", "Course")


    group_1_courses = [("Computer Science","Laboratory", 2), ("Numerical Analysis","Course", 1), ("Physics","Seminar", 2), ("Physics","Course", 2), ("Physics","Laboratory", 1)]
    group_2_courses = [("Computer Science","Laboratory", 2), ("Numerical Analysis","Seminar",2), ("Physics","Course", 2), ("Physics","Seminar", 1), ("Physics","Laboratory", 1)]
    group1 = Group("Group A", group_1_courses,"Romanian")
    group2 = Group("Group B", group_2_courses,"Romanian") 

    office1 = Offices("Office A", "Course")
    office2 = Offices("Office B", "Seminar")
    office3 = Offices("Office C", "Laboratory")

    add_data_to_json(json_file, "Teacher", teacher1)
    add_data_to_json(json_file, "Teacher", teacher2)
    add_data_to_json(json_file, "Teacher", teacher3)
    add_data_to_json(json_file, "Teacher", teacher4)

    add_data_to_json(json_file, "Course", course1)
    add_data_to_json(json_file, "Course", course2)
    add_data_to_json(json_file, "Course", course3)
    add_data_to_json(json_file, "Course", course4)
    add_data_to_json(json_file, "Course", course5)
    add_data_to_json(json_file, "Course", course6)

    add_data_to_json(json_file, "Group", group1)
    add_data_to_json(json_file, "Group", group2) 

    add_data_to_json(json_file, "Office", office1)
    add_data_to_json(json_file, "Office", office2)
    add_data_to_json(json_file, "Office", office3)

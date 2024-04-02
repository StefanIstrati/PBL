import json
import networkx as nx
import matplotlib.pyplot as plt
from classes import Teacher, Course, Group, Offices

def load_data_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    teachers, courses, groups, offices = [], [], [], []
    for entry in data:
        if entry['type'] == 'Teacher':
            teacher_data = entry['data']
            teachers.append(Teacher(teacher_data['name'], [(course[0], course[1]) for course in teacher_data['courses']], teacher_data['language']))
        elif entry['type'] == 'Course':
            course_data = entry['data']
            courses.append(Course(course_data['name'], course_data['course_type']))
        elif entry['type'] == 'Group':
            group_data = entry['data']
            groups.append(Group(group_data['name'], [(course[0], course[1], course[2]) for course in group_data['courses'] if len(course) == 3], group_data['language']))
        elif entry['type'] == 'Office':
            office_data = entry['data']
            offices.append(Offices(office_data['name'], office_data['office_type']))
    return teachers, courses, groups, offices

def create_list_of_tuples(teachers, courses, groups, offices):
    classes_taught = {teacher.name: 0 for teacher in teachers}
    result = []
    
    # Organize offices by type
    offices_by_type = {}
    for office in offices:
        if office.office_type not in offices_by_type:
            offices_by_type[office.office_type] = [office]
        else:
            offices_by_type[office.office_type].append(office)
    
    # Round-robin counters for each office type
    office_counters = {office_type: 0 for office_type in offices_by_type}

    for group in groups:
        for group_course in group.courses:
            course = next((c for c in courses if c.name == group_course[0] and c.course_type == group_course[1]), None)
            if course:
                eligible_teachers = [teacher for teacher in teachers if (course.name, course.course_type) in teacher.courses]
                if eligible_teachers:
                    eligible_teachers.sort(key=lambda teacher: classes_taught[teacher.name])
                    teacher = eligible_teachers[0]
                    classes_taught[teacher.name] += int(group_course[2])
                    if course.course_type in offices_by_type:
                        office_list = offices_by_type[course.course_type]
                        office_index = office_counters[course.course_type] % len(office_list)
                        office = office_list[office_index]
                        office_counters[course.course_type] += 1
                    else:
                        office = None 
                    if office and teacher.language == group.language:
                        result.append((group.name, course.name, course.course_type, teacher.name, office.name, group_course[2], group.language))
    return result


def are_conflicting(class1, class2):
    return class1[3] == class2[3] or class1[4] == class2[4] or class1[0] == class2[0]

def greedy_coloring(G):
    colors = {node: -1 for node in G.nodes()}
    available = [False] * G.number_of_nodes()
    nodes = list(G.nodes())
    colors[nodes[0]] = 0
    for node in nodes[1:]:
        available = [True] * len(colors)
        for neighbor in G.neighbors(node):
            if colors[neighbor] != -1:
                available[colors[neighbor]] = False
        clr = 0
        while clr < len(available):
            if available[clr]:
                break
            clr += 1
        colors[node] = clr
    return colors
def create_graph_and_apply_coloring(json_file):
    teachers, courses, groups, offices = load_data_from_json(json_file)
    tuples_list = create_list_of_tuples(teachers, courses, groups, offices)
    G = nx.Graph()
    for class1 in tuples_list:
        for class2 in tuples_list:
            if class1 != class2 and are_conflicting(class1, class2):
                G.add_edge(class1, class2)
    colors = greedy_coloring(G)
    return G, colors

if __name__ == "__main__":
    json_file = "file_1.json"
    teachers, courses, groups, offices = load_data_from_json(json_file)
    tuples_list = create_list_of_tuples(teachers, courses, groups, offices)
    graph = {class_session: [] for class_session in tuples_list}
    G = nx.Graph()
    for class1 in tuples_list:
        for class2 in tuples_list:
            if class1 != class2 and are_conflicting(class1, class2):
                G.add_edge(class1, class2)
    colors = greedy_coloring(G)
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, seed=42)
    color_map = [colors[node] for node in G.nodes()]
    nx.draw(G, pos, with_labels=True, labels={node: f"{node[1][:3]}.. ({node[0]})" for node in G.nodes()}, node_size=3000, node_color=color_map, font_size=10, edge_color="gray", cmap=plt.cm.Paired)
    plt.title("Graphical Representation of Class Sessions and Conflicts with Coloring")
    plt.show()

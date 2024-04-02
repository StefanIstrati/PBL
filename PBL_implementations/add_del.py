import json
from classes import Teacher, Course, Group, Offices
from typing import  Any

def data_exists_in_json(file_path: str, data: Any) -> bool:
    try:
        with open(file_path, 'r') as file:
            existing_data = json.load(file)
            for entry in existing_data:
                if entry['type'] == 'Course' and entry['data']['name'] == data.name and entry['data']['course_type'] == data.course_type:
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

    add_data_to_json(json_file, "Teacher", Teacher("A. Buga",[("MT","Lab")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("A. Cazac",[("SDA","Lab"),("SDA","Seminar")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("A. Costas",[("MS","Curs"),("MS","Seminar")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("A. Cozari",[("RO","Lab")],"Russian"))
    add_data_to_json(json_file, "Teacher", Teacher("A. Gaidarii",[("MD","Lab")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("A. Gonta",[("CSA","Curs"),("CSA","Seminar")],"French"))
    add_data_to_json(json_file, "Teacher", Teacher("A. Lupusor",[("CSA","Curs"),("CSA","Seminar")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("A. Nastas",[("GC","Lab"),("GC","Curs")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("A. Popovici",[("SA","Lab")],"English"))
    add_data_to_json(json_file, "Teacher", Teacher("A. Puscasu",[("LE","Seminar")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("V. Orlov",[("PP","Lab")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("A. Rotari",[("GC","Lab")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("A. Rotari",[("SDA","Lab"),("SDA","Seminar")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("A. Sisianu",[("LE","Seminar")],"Russian"))
    add_data_to_json(json_file, "Teacher", Teacher("A. Ursu",[("GC","Lab")],"French"))
    add_data_to_json(json_file, "Teacher", Teacher("A. Vinari",[("MD","Lab"),("MD","Seminar")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("A. Zgureanu",[("Cript","Curs")],"Russian"))
    add_data_to_json(json_file, "Teacher", Teacher("C. Crudu",[("LE","Seminar")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("C. Fistic",[("MN","Seminar")],"English"))
    add_data_to_json(json_file, "Teacher", Teacher("C. Tintiuc",[("LE","Seminar")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("D. Barcari",[("SDA","Lab"),("SDA","Seminar")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("D. Cozma",[("AM2","Curs"),("AM2","Seminar")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("D. Istrati",[("LF","Seminar")],"French"))
    add_data_to_json(json_file, "Teacher", Teacher("D. Prijilevschi",[("CSA","Seminar")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("D. Zgardan",[("BB","Curs")],"Romanian "))
    add_data_to_json(json_file, "Teacher", Teacher("E. Bucicovschi",[("TW","Lab")],"Russian"))
    add_data_to_json(json_file, "Teacher", Teacher("E. Bucicovschi",[("GC","Lab")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("E. Ciobanu",[("MD","Lab"),("MD","Seminar")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("E. Cojuhari",[("MS","Curs"),("MS","Seminar")],"English"))
    add_data_to_json(json_file, "Teacher", Teacher("E. Cojuhari",[("AM2","Curs"),("AM2","Seminar")],"English"))
    add_data_to_json(json_file, "Teacher", Teacher("E. Gogoi",[("LE","Curs"),("LE","Seminar")],"English"))
    add_data_to_json(json_file, "Teacher", Teacher("E. Gogoi",[("CSA","Curs"),("CSA","Seminar")],"English"))
    add_data_to_json(json_file, "Teacher", Teacher("E. Hodinitu",[("RO","Seminar")],"Russian"))
    add_data_to_json(json_file, "Teacher", Teacher("E. Nemerenco",[("Cript","Lab")],"Russian"))
    add_data_to_json(json_file, "Teacher", Teacher("E. Tocarschi",[("CSA","Curs"),("CSA","Seminar")],"Russian"))
    add_data_to_json(json_file, "Teacher", Teacher("G. Ceban",[("MD","Curs")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("G. Cebotari",[("MD","Curs"),("MD","Seminar")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("G. Flocea",[("CSA","Curs"),("CSA","Seminar")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("G. Marusic",[("MD","Curs")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("I. Balmus",[("MT","Lab")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("I. Bodnariuc",[("GC","Lab"),("GC","Curs")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("I. Danilov",[("SDA","Curs")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("I. Lisnic",[("MD","Lab"),("MD","Seminar"),("MD","Curs")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("I. Sanduleac",[("SA","Lab"),("SA","Seminar")],"Russian"))
    add_data_to_json(json_file, "Teacher", Teacher("I. Sanduleac",[("MT","Lab"),("MT","Curs")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("L. Brinzan",[("SDA","Lab"),("SDA","Seminar")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("L. Dohotaru",[("AM2","Curs")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("L. Mihail-Velescu",[("LE","Seminar")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("L. Rotaru",[("GC","Curs")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("V. Rusu",[("MS","Seminar")],"Russian"))
    add_data_to_json(json_file, "Teacher", Teacher("L. Stanciu",[("AM2","Seminar")],"Russian"))
    add_data_to_json(json_file, "Teacher", Teacher("L. Tugarev",[("CSA","Curs"),("CSA","Seminar")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("A. Rotari",[("MS","Seminar")],"Russian"))
    add_data_to_json(json_file, "Teacher", Teacher("M. Gaidau",[("Proiect","Seminar")],"English"))
    add_data_to_json(json_file, "Teacher", Teacher("M. Golovaci",[("RO","Seminar")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("M. Gutu",[("SDA","Lab"),("SDA","Seminar")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("M. Kulev",[("SDA","Curs")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("M. Mantaluta",[("SDA","Lab"),("SDA","Seminar")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("M. Osovschi",[("GC","Lab")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("M. Rotaru",[("Proiect","Seminar")],"English"))
    add_data_to_json(json_file, "Teacher", Teacher("M. Rotaru",[("MD","Lab"),("MD","Seminar")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("N. Burlacu",[("SDA","Lab"),("SDA","Seminar"),("SDA","Curs")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("N. Carbune",[("CSA","Curs"),("CSA","Seminar")],"Russian"))
    add_data_to_json(json_file, "Teacher", Teacher("N. Falico",[("SDA","Curs"),("SDA","Seminar")],"Russian"))
    add_data_to_json(json_file, "Teacher", Teacher("N. Lupoi",[("AM2","Seminar")],"Russian"))
    add_data_to_json(json_file, "Teacher", Teacher("N. Palamarciuc",[("MD","Lab"),("MD","Seminar")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("N. Vladei",[("BB","Lab")],"Romanian "))
    add_data_to_json(json_file, "Teacher", Teacher("O. Razdoronaia",[("SDA","Lab"),("SDA","Seminar")],"Russian"))
    add_data_to_json(json_file, "Teacher", Teacher("O. Vacaras",[("AM2","Curs"),("AM2","Seminar")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("O. Vacaras",[("MS","Seminar")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("P. Chircu",[("MS","Lab"),("MS","Curs")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("P. Molosnic",[("MS","Curs"),("MS","Seminar")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("R. Braniste",[("PP","Lab"),("PP","Curs")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("R. Gorobet",[("MT","Lab")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("S. Andronic",[("MT","Curs")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("St. Stratulat",[("SDA","Lab"),("SDA","Seminar"),("SDA","Curs")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("T. Strukova",[("MT","Lab")],"Russian"))
    add_data_to_json(json_file, "Teacher", Teacher("T. Tiholaz",[("MD","Lab"),("MD","Seminar")],"Russian"))
    add_data_to_json(json_file, "Teacher", Teacher("V. Astafi",[("MD","Lab"),("MD","Seminar"),("MD","Curs")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("V. Bobicev",[("TW","Curs")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("V. Bostan",[("MN","Curs")],"English"))
    add_data_to_json(json_file, "Teacher", Teacher("V. Carbune",[("GC","Lab"),("GC","Curs")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("V. Melnic",[("MD","Lab"),("MD","Seminar"),("MD","Curs")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("V. Melnic",[("AM2","Curs"),("AM2","Seminar")],"French"))
    add_data_to_json(json_file, "Teacher", Teacher("V. Melnic",[("Proiect","Seminar")],"English"))
    add_data_to_json(json_file, "Teacher", Teacher("V. Mititelu",[("SDA","Lab"),("SDA","Seminar")],"Russian"))
    add_data_to_json(json_file, "Teacher", Teacher("V. Orlov",[("AM2","Curs"),("AM2","Seminar")],"Russian "))
    add_data_to_json(json_file, "Teacher", Teacher("V. Orlov",[("MS","Curs"),("MS","Seminar")],"Russian"))
    add_data_to_json(json_file, "Teacher", Teacher("V. Pricop",[("AM2","Curs"),("AM2","Seminar")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("V. Pricop",[("MS","Curs")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("V. Rusu",[("SDA","Lab"),("SDA","Seminar"),("SDA","Curs")],"French"))
    add_data_to_json(json_file, "Teacher", Teacher("V. Rusu",[("MT","Lab"),("MT","Curs")],"Russian"))
    add_data_to_json(json_file, "Teacher", Teacher("V. Seiciuc",[("AM2","Curs"),("AM2","Seminar")],"Russian"))
    add_data_to_json(json_file, "Teacher", Teacher("V. Struna",[("PP","Lab")],"Russian"))
    add_data_to_json(json_file, "Teacher", Teacher("V. Struna",[("GC","Lab")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("V. Subbotchin",[("GC","Lab")],"Russian"))
    add_data_to_json(json_file, "Teacher", Teacher("V. Toncu",[("SDA","Lab"),("SDA","Seminar"),("SDA","Curs")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("V. Tronciu",[("SA","Curs")],"English"))
    add_data_to_json(json_file, "Teacher", Teacher("V. Tutunaru",[("SDA","Lab"),("SDA","Seminar")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("A. Popovici",[("SA","Lab")],"Russian"))
    add_data_to_json(json_file, "Teacher", Teacher("A. Rotari",[("SDA","Lab"),("SDA","Seminar")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("A. Sisianu",[("LE","Seminar")],"Romanian"))
    add_data_to_json(json_file, "Teacher", Teacher("C. Fistic",[("MN","Seminar")],"Russian"))
    add_data_to_json(json_file, "Teacher", Teacher("D. Prijilevschi",[("CSA","Seminar")],"Russian"))
    add_data_to_json(json_file, "Teacher", Teacher("D. Zgardan",[("BB","Curs")],"Russian"))
    add_data_to_json(json_file, "Teacher", Teacher("G. Flocea",[("CSA","Curs"),("CSA","Seminar")],"Russian"))
    add_data_to_json(json_file, "Teacher", Teacher("L. Dohotaru",[("AM2","Curs")],"Russian"))
    add_data_to_json(json_file, "Teacher", Teacher("V. Rusu",[("MS","Seminar")],"Romania"))
    add_data_to_json(json_file, "Teacher", Teacher("N. Burlacu",[("SDA","Lab"),("SDA","Seminar"),("SDA","Curs")],"English"))
    add_data_to_json(json_file, "Teacher", Teacher("P. Molosnic",[("MS","Curs"),("MS","Seminar")],"Russian"))
    add_data_to_json(json_file, "Teacher", Teacher("R. Gorobet",[("MT","Lab")],"French"))
    add_data_to_json(json_file, "Teacher", Teacher("V. Astafi",[("MD","Lab"),("MD","Seminar"),("MD","Curs")],"Russian"))


    add_data_to_json(json_file,"Group",Group("CR-231",[("SDA","Seminar",0.5),("MS","Seminar",0.5),("AM2","Curs",1),("CSA","Curs",1),("MT","Lab",1),("MSDA","Lab",1),("MD","Curs",1),("MS","Curs",1),("SDA","Curs",1),("MT","Curs",1),("AM2","Seminar",1),("GC","Lab",1),("MD","Lab",1),("GC","Curs",1),("Fizica","Ed.",0.5),("CSA","Seminar",0.5),("MD","Seminar",0.5),("LE","Seminar",1)],"Romanian"))	
    add_data_to_json(json_file,"Group",Group("CR-232",[("MS","Seminar",0.5),("AM2","Curs",1),("CSA","Curs",1),("MD","Curs",1),("MS","Curs",1),("SDA","Lab",1),("SDA","Curs",1),("MT","Curs",1),("LE","Seminar",1),("AM2","Semina",1),("GC","Lab",1),("GC","Curs",1),("CSA","Seminar",0.5),("Fizica","Ed.",0.5),("MD","Seminar",0.5),("MT","Lab",1),("MD","Lab",1),("SDA","Seminar",0.5)],"Romanian"))	
    add_data_to_json(json_file,"Group",Group("RM-231",[("AM2","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("SDA","Seminar",0.5),("CSA","Seminar",0.5),("GC","Lab",1),("MD","Curs",1),("MS","Curs",1),("SDA","Curs",1),("MT","Curs",1),("SDA","Lab",1),("MS","Seminar",0.5),("LE","Seminar",1),("GC","Curs",1),("MT","Lab",1),("MD","Lab",1),("MD","Seminar",0.5),("Fizica","Ed.",0.5)],"Romanian"))	
    add_data_to_json(json_file,"Group",Group("MN-231/EA-231",[("AM2","Curs",1),("CSA","Curs",1),("CSA","Seminar",0.5),("MS","Seminar",0.5),("MD","Curs",1),("MS","Curs",1),("AM2","Seminar",1),("SDA","Curs",1),("MT","Curs",1),("SDA","Lab",1),("GC","Curs",1),("MD","Lab",1),("MT","Lab",1),("MD","Seminar",0.5),("GC","Lab",1),("LE","Seminar",1),("SDA0.5","Seminar",""),("Fizica","Ed.",0.5)],"Romanian"))	
    add_data_to_json(json_file,"Group",Group("IBM-231",[("SDA","Seminar",1),("MS","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("MT","Lab",1),("MS","Curs",1),("SDA","Curs",1),("MT","Curs",1),("AM2","Seminar",1),("BB","Lab",1),("BB","Curs",1),("Fizica","Ed.",1),("CSA","Seminar",1),("MD","Seminar",1),("LE","Seminar",1),("GC","Lab",1),("GC","Curs",1),],"Romanian"))	
    add_data_to_json(json_file,"Group",Group("FI-231",[("AM2","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("SDA","Seminar",0.5),("CSA","Seminar",0.5),("GC","Lab",1),("MD","Curs",1),("MS","Curs",1),("SDA","Curs",1),("MT","Curs",1),("SDA","Lab",1),("MS","Seminar",1),("Straina","Seminar",1),("GC","Curs",1),("MT","Lab",1),("MD","Lab",1),("MD","Seminar",1),("Fizica","Ed.",0.5)],"French"))	
    add_data_to_json(json_file,"Group",Group("TI-231",[("AM2","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("SDA","Seminar",0.5),("CSA","Seminar",0.5),("GC","Lab",1),("MD","Curs",1),("MS","Curs",1),("SDA","Curs",1),("MT","Curs",1),("SDA","Lab",1),("MS","Seminar",1),("LE","Seminar",1),("GC","Curs",1),("MT","Lab",1),("MD","Lab",1),("MD","Seminar",1),("Fizica","Ed.",0.5)],"Romanian"))	
    add_data_to_json(json_file,"Group",Group("TI-232",[("AM2","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("SDA","Seminar",0.5),("CSA","Seminar",0.5),("GC","Lab",1),("MD","Curs",1),("MS","Curs",1),("SDA","Curs",1),("MT","Curs",1),("SDA","Lab",1),("MS","Seminar",1),("LE","Seminar",1),("GC","Curs",1),("MT","Lab",1),("MD","Lab",1),("MD","Seminar",1),("Fizica","Ed.",0.5)],"Romanian"))	
    add_data_to_json(json_file,"Group",Group("TI-233",[("AM2","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("SDA","Seminar",0.5),("CSA","Seminar",0.5),("GC","Lab",1),("MD","Curs",1),("MS","Curs",1),("SDA","Curs",1),("MT","Curs",1),("SDA","Lab",1),("MS","Seminar",1),("LE","Seminar",1),("GC","Curs",1),("MT","Lab",1),("MD","Lab",1),("MD","Seminar",1),("Fizica","Ed.",0.5)],"Romanian"))	
    add_data_to_json(json_file,"Group",Group("TI-234",[("AM2","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("SDA","Seminar",0.5),("CSA","Seminar",0.5),("GC","Lab",1),("MD","Curs",1),("MS","Curs",1),("SDA","Curs",1),("MT","Curs",1),("SDA","Lab",1),("MS","Seminar",1),("LE","Seminar",1),("GC","Curs",1),("MT","Lab",1),("MD","Lab",1),("MD","Seminar",1),("Fizica","Ed.",0.5)],"Romanian"))	
    add_data_to_json(json_file,"Group",Group("TI-235",[("AM2","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("SDA","Seminar",0.5),("CSA","Seminar",0.5),("GC","Lab",1),("MD","Curs",1),("MS","Curs",1),("SDA","Curs",1),("MT","Curs",1),("SDA","Lab",1),("MS","Seminar",1),("LE","Seminar",1),("GC","Curs",1),("MT","Lab",1),("MD","Lab",1),("MD","Seminar",1),("Fizica","Ed.",0.5)],"Romanian"))	
    add_data_to_json(json_file,"Group",Group("TI-236",[("AM2","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("SDA","Seminar",0.5),("CSA","Seminar",0.5),("GC","Lab",1),("MD","Curs",1),("MS","Curs",1),("SDA","Curs",1),("MT","Curs",1),("SDA","Lab",1),("MS","Seminar",1),("LE","Seminar",1),("GC","Curs",1),("MT","Lab",1),("MD","Lab",1),("MD","Seminar",1),("Fizica","Ed.",0.5)],"Romanian"))	
    add_data_to_json(json_file,"Group",Group("TI-237",[("AM2","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("SDA","Seminar",0.5),("CSA","Seminar",0.5),("GC","Lab",1),("MD","Curs",1),("MS","Curs",1),("SDA","Curs",1),("MT","Curs",1),("SDA","Lab",1),("MS","Seminar",1),("LE","Seminar",1),("GC","Curs",1),("MT","Lab",1),("MD","Lab",1),("MD","Seminar",1),("Fizica","Ed.",0.5)],"Romanian"))	
    add_data_to_json(json_file,"Group",Group("SI-231",[("AM2","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("SDA","Seminar",0.5),("CSA","Seminar",0.5),("Cript.","Curs",1),("MD","Curs",1),("MS","Curs",1),("SDA","Curs",1),("MT","Curs",1),("SDA","Lab",1),("MS","Seminar",1),("LE","Seminar",1),("Cript.","Lab",1),("MT","Lab",1),("MD","Lab",1),("MD","Seminar",1),("Fizica","Ed.",0.5)],"Romanian"))	
    add_data_to_json(json_file,"Group",Group("SI-232",[("AM2","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("SDA","Seminar",0.5),("CSA","Seminar",0.5),("Cript.","Curs",1),("MD","Curs",1),("MS","Curs",1),("SDA","Curs",1),("MT","Curs",1),("SDA","Lab",1),("MS","Seminar",1),("LE","Seminar",1),("Cript.","Lab",1),("MT","Lab",1),("MD","Lab",1),("MD","Seminar",1),("Fizica","Ed.",0.5)],"Romanian"))	
    add_data_to_json(json_file,"Group",Group("AI-231",[("AM2","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("SDA","Seminar",0.5),("CSA","Seminar",0.5),("GC","Lab",1),("MD","Curs",1),("MS","Curs",1),("SDA","Curs",1),("MT","Curs",1),("SDA","Lab",1),("MS","Seminar",1),("LE","Seminar",1),("GC","Curs",1),("MT","Lab",1),("MD","Lab",1),("MD","Seminar",1),("Fizica","Ed.",0.5)],"Romanian"))	
    add_data_to_json(json_file,"Group",Group("AI-232",[("AM2","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("SDA","Seminar",0.5),("CSA","Seminar",0.5),("GC","Lab",1),("MD","Curs",1),("MS","Curs",1),("SDA","Curs",1),("MT","Curs",1),("SDA","Lab",1),("MS","Seminar",1),("LE","Seminar",1),("GC","Curs",1),("MT","Lab",1),("MD","Lab",1),("MD","Seminar",1),("Fizica","Ed.",0.5)],"Russian"))	#ru start 
    add_data_to_json(json_file,"Group",Group("CR-233",[("AM2","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("SDA","Seminar",0.5),("CSA","Seminar",0.5),("GC","Lab",1),("MD","Curs",1),("MS","Curs",1),("SDA","Curs",1),("MT","Curs",1),("SDA","Lab",1),("MS","Seminar",1),("LE","Seminar",1),("GC","Curs",1),("MT","Lab",1),("MD","Lab",1),("MD","Seminar",1),("Fizica","Ed.",0.5)],"Russian"))	
    add_data_to_json(json_file,"Group",Group("MN/EA-232",[("AM2","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("SDA","Seminar",0.5),("CSA","Seminar",0.5),("GC","Lab",1),("MD","Curs",1),("MS","Curs",1),("SDA","Curs",1),("MT","Curs",1),("SDA","Lab",1),("MS","Seminar",1),("LE","Seminar",1),("GC","Curs",1),("MT","Lab",1),("MD","Lab",1),("MD","Seminar",1),("Fizica","Ed.",0.5)],"Russian"))	
    add_data_to_json(json_file,"Group",Group("IBM-232",[("SDA","Seminar",1),("MS","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("MT","Lab",1),("MS","Curs",1),("SDA","Curs",1),("MT","Curs",1),("AM2","Seminar",1),("BB","Lab",1),("BB","Curs",1),("Fizica","Ed.",1),("CSA","Seminar",1),("MD","Seminar",1),("LE","Seminar",1),("GC","Lab",1),("GC","Curs",1),("Romana","Seminar",1)],"Russian"))	
    add_data_to_json(json_file,"Group",Group("SI-233",[("AM2","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("SDA","Seminar",0.5),("CSA","Seminar",0.5),("Cript.","Curs",1),("MD","Curs",1),("MS","Curs",1),("SDA","Curs",1),("MT","Curs",1),("SDA","Lab",1),("MS","Seminar",1),("LE","Seminar",1),("Cript.","Lab",1),("MT","Lab",1),("MD","Lab",1),("MD","Seminar",1),("Fizica","Ed.",0.5)],"Russian"))	
    add_data_to_json(json_file,"Group",Group("SI-234",[("AM2","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("SDA","Seminar",0.5),("CSA","Seminar",0.5),("Cript.","Curs",1),("MD","Curs",1),("MS","Curs",1),("SDA","Curs",1),("MT","Curs",1),("SDA","Lab",1),("MS","Seminar",1),("LE","Seminar",1),("Cript.","Lab",1),("MT","Lab",1),("MD","Lab",1),("MD","Seminar",1),("Fizica","Ed.",0.5)],"Russian"))	
    add_data_to_json(json_file,"Group",Group("TI-238",[("AM2","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("SDA","Seminar",0.5),("CSA","Seminar",0.5),("GC","Lab",1),("MD","Curs",1),("MS","Curs",1),("SDA","Curs",1),("MT","Curs",1),("SDA","Lab",1),("MS","Seminar",1),("LE","Seminar",1),("GC","Curs",1),("MT","Lab",1),("MD","Lab",1),("MD","Seminar",1),("Fizica","Ed.",0.5)],"Russian"))	
    add_data_to_json(json_file,"Group",Group("TI-239",[("AM2","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("SDA","Seminar",0.5),("CSA","Seminar",0.5),("GC","Lab",1),("MD","Curs",1),("MS","Curs",1),("SDA","Curs",1),("MT","Curs",1),("SDA","Lab",1),("MS","Seminar",1),("LE","Seminar",1),("GC","Curs",1),("MT","Lab",1),("MD","Lab",1),("MD","Seminar",1),("Fizica","Ed.",0.5)],"Russian"))	
    add_data_to_json(json_file,"Group",Group("TI-2310",[("AM2","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("SDA","Seminar",0.5),("CSA","Seminar",0.5),("GC","Lab",1),("MD","Curs",1),("MS","Curs",1),("SDA","Curs",1),("MT","Curs",1),("SDA","Lab",1),("MS","Seminar",1),("LE","Seminar",1),("GC","Curs",1),("MT","Lab",1),("MD","Lab",1),("MD","Seminar",1),("Fizica","Ed.",0.5)],"Russian")) #ru end 	
    add_data_to_json(json_file,"Group",Group("IA-231",[("AM2","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("SDA","Seminar",0.5),("CSA","Seminar",0.5),("GC","Lab",1),("MD","Curs",1),("PP","Curs",1),("SDA","Curs",1),("TW","Curs",1),("SDA","Lab",1),("PP","Lab",1),("LE","Seminar",1),("GC","Curs",1),("TW","Lab",1),("MD","Lab",1),("MD","Seminar",1),("Fizica","Ed.",0.5)],"Romanian"))	
    add_data_to_json(json_file,"Group",Group("IA-232",[("AM2","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("SDA","Seminar",0.5),("CSA","Seminar",0.5),("GC","Lab",1),("MD","Curs",1),("PP","Curs",1),("SDA","Curs",1),("TW","Curs",1),("SDA","Lab",1),("PP","Lab",1),("LE","Seminar",1),("GC","Curs",1),("TW","Lab",1),("MD","Lab",1),("MD","Seminar",1),("Fizica","Ed.",0.5)],"Romanian"))	
    add_data_to_json(json_file,"Group",Group("IA-233",[("AM2","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("SDA","Seminar",0.5),("CSA","Seminar",0.5),("GC","Lab",1),("MD","Curs",1),("PP","Curs",1),("SDA","Curs",1),("TW","Curs",1),("SDA","Lab",1),("PP","Lab",1),("LE","Seminar",1),("GC","Curs",1),("TW","Lab",1),("MD","Lab",1),("MD","Seminar",1),("Fizica","Ed.",0.5)],"Romanian"))	
    add_data_to_json(json_file,"Group",Group("SD-231",[("AM2","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("SDA","Seminar",0.5),("CSA","Seminar",0.5),("GC","Lab",1),("MD","Curs",1),("PP","Curs",1),("SDA","Curs",1),("TW","Curs",1),("SDA","Lab",1),("PP","Lab",1),("LE","Seminar",1),("GC","Curs",1),("TW","Lab",1),("MD","Lab",1),("MD","Seminar",1),("Fizica","Ed.",0.5)],"Romanian"))	
    add_data_to_json(json_file,"Group",Group("IA-234",[("AM2","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("SDA","Seminar",0.5),("CSA","Seminar",0.5),("GC","Lab",1),("MD","Curs",1),("PP","Curs",1),("SDA","Curs",1),("TW","Curs",1),("SDA","Lab",1),("PP","Lab",1),("LE","Seminar",1),("GC","Curs",1),("TW","Lab",1),("MD","Lab",1),("MD","Seminar",1),("Fizica","Ed.",0.5)],"Russian"))#start ru
    add_data_to_json(json_file,"Group",Group("IA-235",[("AM2","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("SDA","Seminar",0.5),("CSA","Seminar",0.5),("GC","Lab",1),("MD","Curs",1),("PP","Curs",1),("SDA","Curs",1),("TW","Curs",1),("SDA","Lab",1),("PP","Lab",1),("LE","Seminar",1),("GC","Curs",1),("TW","Lab",1),("MD","Lab",1),("MD","Seminar",1),("Fizica","Ed.",0.5)],"Russian"))	
    add_data_to_json(json_file,"Group",Group("SD-232",[("AM2","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("SDA","Seminar",0.5),("CSA","Seminar",0.5),("GC","Lab",1),("MD","Curs",1),("PP","Curs",1),("SDA","Curs",1),("TW","Curs",1),("SDA","Lab",1),("PP","Lab",1),("LE","Seminar",1),("GC","Curs",1),("TW","Lab",1),("MD","Lab",1),("MD","Seminar",1),("Fizica","Ed.",0.5)],"Russian"))#end ru
    add_data_to_json(json_file,"Group",Group("FAF-231",[("AM2","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("SDA","Seminar",0.5),("CSA","Seminar",0.5),("Fizica","Lab",1),("MS","Curs",1),("MN","Curs",1),("SDA","Curs",1),("SA","Curs",1),("SDA","Lab",1),("LE","Seminar",1),("Proiect","Seminar",1),("MN","Seminar",1),("Fizica","Ed.",0.5),("MS","Seminar",0.5),("Fizica","Seminar",1),],"English"))#strart en
    add_data_to_json(json_file,"Group",Group("FAF-232",[("AM2","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("SDA","Seminar",0.5),("CSA","Seminar",0.5),("Fizica","Lab",1),("MS","Curs",1),("MN","Curs",1),("SDA","Curs",1),("SA","Curs",1),("SDA","Lab",1),("LE","Seminar",1),("Proiect","Seminar",1),("MN","Seminar",1),("Fizica","Ed.",0.5),("MS","Seminar",0.5),("Fizica","Seminar",1),],"English"))	
    add_data_to_json(json_file,"Group",Group("FAF-233",[("AM2","Seminar",1),("AM2","Curs",1),("CSA","Curs",1),("SDA","Seminar",0.5),("CSA","Seminar",0.5),("Fizica","Lab",1),("MS","Curs",1),("MN","Curs",1),("SDA","Curs",1),("SA","Curs",1),("SDA","Lab",1),("LE","Seminar",1),("Proiect","Seminar",1),("MN","Seminar",1),("Fizica","Ed.",0.5),("MS","Seminar",0.5),("Fizica","Seminar",1),],"English"))#end en



    add_data_to_json(json_file,"Course",Course("SDA","Seminar"))	
    add_data_to_json(json_file,"Course",Course("MS","Seminar"))	
    add_data_to_json(json_file,"Course",Course("AM2","Curs"))	
    add_data_to_json(json_file,"Course",Course("CSA","Curs"))	
    add_data_to_json(json_file,"Course",Course("MT","Lab."))	
    add_data_to_json(json_file,"Course",Course("MSDA","Lab."))	
    add_data_to_json(json_file,"Course",Course("MD","Curs"))	
    add_data_to_json(json_file,"Course",Course("MS","Curs"))	
    add_data_to_json(json_file,"Course",Course("SDA","Lab"))	
    add_data_to_json(json_file,"Course",Course("SDA","Curs"))	
    add_data_to_json(json_file,"Course",Course("MT","Curs"))	
    add_data_to_json(json_file,"Course",Course("AM2","Seminar"))	
    add_data_to_json(json_file,"Course",Course("LE","Seminar"))	
    add_data_to_json(json_file,"Course",Course("GC","Lab"))	
    add_data_to_json(json_file,"Course",Course("MD","Lab"))	
    add_data_to_json(json_file,"Course",Course("CSA","Seminar"))	
    add_data_to_json(json_file,"Course",Course("MD","Seminar"))	
    add_data_to_json(json_file,"Course",Course("BB","Curs"))	
    add_data_to_json(json_file,"Course",Course("BB","Lab"))	
    add_data_to_json(json_file,"Course",Course("GC","Curs"))
    add_data_to_json(json_file,"Course",Course("FR","Seminar"))	
    add_data_to_json(json_file,"Course",Course("MS","Lab."))
    add_data_to_json(json_file,"Course",Course("Crip","Curs"))	
    add_data_to_json(json_file,"Course",Course("Crip","Lab."))	
    add_data_to_json(json_file,"Course",Course("RO","Seminar"))	
    add_data_to_json(json_file,"Course",Course("PP","Lab."))	
    add_data_to_json(json_file,"Course",Course("PP","Curs"))	
    add_data_to_json(json_file,"Course",Course("TW","Lab"))	
    add_data_to_json(json_file,"Course",Course("TW","Curs"))	
    add_data_to_json(json_file,"Course",Course("Proiect","Seminar"))	
    add_data_to_json(json_file,"Course",Course("St. Apl","Seminar"))	
    add_data_to_json(json_file,"Course",Course("St. Apl","Lab."))	
    add_data_to_json(json_file,"Course",Course("MN","Seminar"))	
    add_data_to_json(json_file,"Course",Course("St. Apl","Curs"))	
    add_data_to_json(json_file,"Course",Course("MN","Curs "))


    add_data_to_json(json_file,"Office",Offices("6-2","Curs"))				
    add_data_to_json(json_file,"Office",Offices("104","Curs"))	
    add_data_to_json(json_file,"Office",Offices("3-3","Curs"))									
    add_data_to_json(json_file,"Office",Offices("404","Curs"))						
    add_data_to_json(json_file,"Office",Offices("203","Curs"))	
    add_data_to_json(json_file,"Office",Offices("622","Curs"))	
    add_data_to_json(json_file,"Office",Offices("5-412","Curs"))	
    add_data_to_json(json_file,"Office",Offices("609","Curs"))										
    add_data_to_json(json_file,"Office",Offices("401","Curs"))															
    add_data_to_json(json_file,"Office",Offices("405","Curs"))					
    add_data_to_json(json_file,"Office",Offices("618","Seminar"))	
    add_data_to_json(json_file,"Office",Offices("611","Seminar"))			
    add_data_to_json(json_file,"Office",Offices("623","Seminar"))						
    add_data_to_json(json_file,"Office",Offices("624","Seminar"))	
    add_data_to_json(json_file,"Office",Offices("606","Seminar"))	
    add_data_to_json(json_file,"Office",Offices("607","Seminar"))		
    add_data_to_json(json_file,"Office",Offices("613","Seminar"))		
    add_data_to_json(json_file,"Office",Offices("404","Seminar"))	
    add_data_to_json(json_file,"Office",Offices("407","Seminar"))	
    add_data_to_json(json_file,"Office",Offices("707","Seminar"))	
    add_data_to_json(json_file,"Office",Offices("718","Seminar"))			
    add_data_to_json(json_file,"Office",Offices("203","Seminar"))	
    add_data_to_json(json_file,"Office",Offices("622","Seminar"))	
    add_data_to_json(json_file,"Office",Offices("5-412","Seminar"))	
    add_data_to_json(json_file,"Office",Offices("609","Seminar"))	
    add_data_to_json(json_file,"Office",Offices("312","Seminar"))			
    add_data_to_json(json_file,"Office",Offices("601","Seminar"))	
    add_data_to_json(json_file,"Office",Offices("201","Seminar"))		
    add_data_to_json(json_file,"Office",Offices("202","Seminar"))		
    add_data_to_json(json_file,"Office",Offices("512","Seminar"))	
    add_data_to_json(json_file,"Office",Offices("401","Seminar"))	
    add_data_to_json(json_file,"Office",Offices("501","Seminar"))	
    add_data_to_json(json_file,"Office",Offices("519","Seminar"))	
    add_data_to_json(json_file,"Office",Offices("630","Seminar"))			
    add_data_to_json(json_file,"Office",Offices("524","Seminar"))					
    add_data_to_json(json_file,"Office",Offices("722","Seminar"))			
    add_data_to_json(json_file,"Office",Offices("224","Seminar"))		
    add_data_to_json(json_file,"Office",Offices("115","Seminar"))			
    add_data_to_json(json_file,"Office",Offices("118","Seminar"))	
    add_data_to_json(json_file,"Office",Offices("113","Seminar"))
    add_data_to_json(json_file,"Office",Offices("110","Lab"))		
    add_data_to_json(json_file,"Office",Offices("215","Lab"))			
    add_data_to_json(json_file,"Office",Offices("D-01","Lab"))	
    add_data_to_json(json_file,"Office",Offices("D-03","Lab"))				
    add_data_to_json(json_file,"Office",Offices("D-02","Lab"))		
    add_data_to_json(json_file,"Office",Offices("212","Lab"))		
    add_data_to_json(json_file,"Office",Offices("407","Lab"))			
    add_data_to_json(json_file,"Office",Offices("217","Lab"))	
    add_data_to_json(json_file,"Office",Offices("5-114","Lab"))		
    add_data_to_json(json_file,"Office",Offices("622","Lab"))				
    add_data_to_json(json_file,"Office",Offices("D-04","Lab"))	
    add_data_to_json(json_file,"Office",Offices("6-414A","Lab"))			
    add_data_to_json(json_file,"Office",Offices("112","Lab"))		
    add_data_to_json(json_file,"Office",Offices("114","Lab"))			
    add_data_to_json(json_file,"Office",Offices("501","Lab"))			
    add_data_to_json(json_file,"Office",Offices("503","Lab"))	
    add_data_to_json(json_file,"Office",Offices("608","Lab"))		
    add_data_to_json(json_file,"Office",Offices("513A","Lab"))	
    add_data_to_json(json_file,"Office",Offices("513 B","Lab"))	
    add_data_to_json(json_file,"Office",Offices("516","Lab"))	
    add_data_to_json(json_file,"Office",Offices("518","Lab"))		
    add_data_to_json(json_file,"Office",Offices("619","Lab"))	
    add_data_to_json(json_file,"Office",Offices("214","Lab"))				
    add_data_to_json(json_file,"Office",Offices("301","Lab"))	
    add_data_to_json(json_file,"Office",Offices("303","Lab"))	
    add_data_to_json(json_file,"Office",Offices("118","Lab"))

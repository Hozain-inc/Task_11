import csv
from pathlib import Path
workspace = Path("workspace_file")
workspace.mkdir(exist_ok= True)
csv_file = workspace / "contacts.csv"

#header = name age, phone, track

#def save_participant(path, participant_dic):
    # file =Path(csv_file)
    # with open(path, "a", newline="", encoding="utf-8") as f:
    #  writer = csv.DictWriter (f,fieldnames=["name", "age", "phone","track"])
    #  writer.writerows(participant_dic)  # Write all rows at once
    # participant_dic


fieldnames= ["Name", "Age", "Phone", "Track"]
def save_participant(file_path, participant_dict):
    file = Path(file_path)
    with open(file, "a", encoding="utf-8",) as f:
        writer = csv.DictWriter(f,fieldnames = fieldnames)
        
        if not file.exists() or file.stat().st_size == 0:
            writer.writeheader()
        
        writer.writerow(participant_dict)
def load_participants(path):
    print("\nReading CSV file:")

    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row_number, row in (reader):
            if row_number == 0:  
                print(f"Headers: {' | '.join(row)}")
            #print("-" * 40)
        else:  
            name, age, phone, track = row
            print(f"{name} ({age} years old) - {phone}: {track}")





import csv
from pathlib import Path
import file_ops
# from file_ops import save_paticipant, Load_participant

workspace = Path("workspace_file")
csv_file = workspace / "contacts.csv"

participant_dic = {}

while True:
    name = input("Enter your name: ")
    while name =="":
        name = input("Name cannot be empty,Enter your name: ")
    
    age = input("Enter your age : ")
    while age.isalpha():
        age = input("Invalid! Enter your age in digit: ")
    
    phone = input("Enter your phone number: ")
    while phone.isalpha() and len(phone) != 11:
       phone = input("Invalid!,Enter your correct phone number: ")
        
    track=input("Enter your track: ")
    while track =="":
       track=input("Track cannot be empty,Enter your track: ")
       
    participant_dic["Name"] = name
    participant_dic["Age"] = age
    participant_dic["Phone"]= phone
    participant_dic["Track"] = track


    file_ops.save_participant(csv_file,  participant_dic)
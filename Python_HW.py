
from datetime import datetime,timedelta


def find_monday(y,w):   
    day = datetime(y,1,1)    
    day_monday = (7-day.weekday())%7   
    frst_monday = day + timedelta(days = day_monday + 7 * (w-1))   
    res = frst_monday.strftime("%a %d %B %H:%M:%S")  
    print(res)
    
#find_monday(2015,50)


def difference_date(date1,date2):    
    d1 = datetime.strptime(date1, "%d %m %Y %H:%M:%S")    
    d2 = datetime.strptime(date2, "%d %m %Y %H:%M:%S")   
    if d1 >= d2: res = d1 - d2    
    else: res = d2 - d1    
    print(res)

#difference_date("5 12 2023 13:13:00", "1 9 2023 13:13:00")


def merge_files():
    file_contents = []

    while True:
        filename = input("Enter name file and 'quit' for end: ")

        if filename == 'quit':
            break

        with open(filename, 'r') as r_file:
            content = r_file.read()
            file_contents.append(content)
            print(f"File '{filename}' add.")

    merged_content = '\n'.join(file_contents)

    output_filename = "result.txt"
    with open(output_filename, 'w') as output_file:
        output_file.write(merged_content)

#merge_files()


def censured(): 
    with open("text.txt","r") as r_file:        
        lines = r_file.read()       
        lines = lines.split()   
        
        with open("censured.txt", "r") as r_cen:          
            words = r_cen.read()
            words = words.split()     
            
            for i in range(len(lines)):                
                if lines[i] in words:                    
                    lines[i] = "*****"            
            
            with open("text.txt","w") as w_text:                
                for i in lines:                   
                    w_text.write(i + " ")
    print("Ready")

#censured()


import os

def create_folder():
    w_m = 'watch_me'
    os.makedirs(w_m, exist_ok=True)

    for folder in ['video', 'sub']:
        files = os.listdir(folder)

        for f in files:
            s_file = os.path.join(folder, f)
            d_file = os.path.join(w_m, f)
            with open(s_file, 'rb') as s_file, open(d_file, 'wb') as d_file:
                d_file.write(s_file.read())
            print(f'Copy files in {w_m}')

#create_folder()


def rename_files():
    files = os.listdir()

    for file_name in files:
        parts = file_name.split('_')

        if len(parts) == 2:
            first_name, last_name = parts

            new_file_name = f'{last_name}_{first_name}.jpg'

            old_file_path = os.path.join(os.getcwd(), file_name)
            new_file_path = os.path.join(os.getcwd(), new_file_name)

            os.rename(old_file_path, new_file_path)
            print(f'File {file_name} renames {new_file_name}')

#rename_files()
#Работает но ломает программу потому что в названии есть _
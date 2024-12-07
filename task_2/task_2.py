from pathlib import Path

absolute_path = Path('task_2/db.txt').absolute()

def get_cats_info(path):
    cats = []
    if path.exists():
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                id, name, age = line.split(',')
                cats.append({
                    "id": id,
                    "name": name,
                    "age": int(age),
                })
        return cats 
    else:
        return  f"Not valid path {path}"       
                


print(get_cats_info(absolute_path))
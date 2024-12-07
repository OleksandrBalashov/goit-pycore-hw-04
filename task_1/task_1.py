from pathlib import Path

absolute_path = Path('task_1/db.txt').absolute()

def total_salary(path): 
     total = 0
     average = 0
     if path.exists():          
          with open(path, 'r', encoding='utf-8') as file:
               lines = file.readlines()

               for line in lines:
                    _, salary = line.split(',')
                    total += int(salary)

               if lines:
                    average = total//len(lines)
                   
     else:
          print(f'No valid {path}')
          return None

     return total, average
    
          
          
result = total_salary(absolute_path)

if result:
     total, average = result
     print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
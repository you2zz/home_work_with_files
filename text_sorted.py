# Задача № 3

import os

with open('sorted/1.txt', encoding='utf-8') as file1, open('sorted/2.txt', encoding='utf-8') as file2, open('sorted/3.txt', encoding='utf-8') as file3, open('new_file.txt', 'w', encoding='utf-8') as output_file:
    
    al_line_txt1, al_line_txt2, al_line_txt3 = [os.path.basename('sorted/1.txt') + '\n'], [os.path.basename('sorted/2.txt') + '\n'], [os.path.basename('sorted/3.txt') + '\n']

    for line in file1:
        al_line_txt1.append(line)
    al_line_txt1.insert(1, str(len(al_line_txt1) - 1) + '\n')

    for line in file2:
        al_line_txt2.append(line)
    al_line_txt2.insert(1, str(len(al_line_txt2) - 1) + '\n')

    for line in file3:
        al_line_txt3.append(line)
    al_line_txt3.insert(1, str(len(al_line_txt3) - 1) + '\n')
    
    all_file = sorted([al_line_txt1, al_line_txt2, al_line_txt3], key=len)    
        
    for x in all_file:
        for line in x:
            output_file.write(line)
        output_file.write('\n')
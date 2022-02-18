stud_1 = input(f'Введите фамилию студента № 1:')
group_1 = input(f'Введите группу студента № 1:')
stud_2 = input(f'Введите фамилию студента № 2:')
group_2 = input(f'Введите группу студента № 2:')
stud_3 = input(f'Введите фамилию студента № 3:')
group_3 = input(f'Введите группу студента № 3:')

print(' '*10, 'Фамилия', ' '*10, 'Группа') # lenght 36
print(stud_1, ' '*(34-len(group_1)-len(stud_1)), group_1)
print(stud_2, ' '*(34-len(group_2)-len(stud_2)), group_2)
print(stud_3, ' '*(34-len(group_3)-len(stud_3)), group_3)

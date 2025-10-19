def office_access(tpl, employee_id):
    if employee_id not in tpl:
        return ()
    
    indices = [i for i, x in enumerate(tpl) if x == employee_id]
    
    if len(indices) == 1:
        return tpl[indices[0]:]
    else:
        return tpl[indices[0]:indices[1] + 1]

print(office_access((1, 2, 3), 8))
print(office_access((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(office_access((1, 2, 8, 5, 1, 2, 9), 8))

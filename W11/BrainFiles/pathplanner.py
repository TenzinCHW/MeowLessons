__author__ = 'HanWei'



def pathplanner(instructions):
    timestovisit = {A:[0,0],B:[0,0],C:[0,0],D:[0,0]}
    path = ['Straight','Straight','X']
    for i in instructions:
        if i[0] == 'A':
            timestovisit[i[0]] += int(math.ceil(int(i[1:]/6.0)))
            timestovisit[i] += int(i[1:])%6
        elif i[0] == 'B':
            B[0] += int(math.ceil(int(i[1:]/6.0)))
            B[1] += int(i[1:])%6
        elif i[0] == 'C':
            C[0] += int(math.ceil(int(i[1:]/6.0)))
            C[1] += int(i[1:])%6
        elif i[0] == 'D':
            D[0] += int(math.ceil(int(i[1:]/6.0)))
            D[1] += int(i[1:])%6
        else:
            print '%s is not a valid destination.' % i[0]
    if A[1] == 0:
        path.append('')

    return path
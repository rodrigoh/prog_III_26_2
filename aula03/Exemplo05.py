la = [1,2,3,4]

if 2 in la:
    print('O número 2 existe em la')

lb = [1,2,3,4]

lc = la

print('la é lc: ',la is lc)
print('la é lb: ',la is lb)
print('la está em lb', la in lb)
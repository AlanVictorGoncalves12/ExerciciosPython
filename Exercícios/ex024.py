#Programa que eu criei
"""cid = str(input('Em que cidade você nasceu? ')).strip()
if 'santo' in cid.lower() == True:
    if cid.find('santo') == 0:
        print('santo' in cid.lower())
if cid.find('santo') == 0:
    print('santo' in cid.lower())
else:
    print(False)"""

#O apresentado no video
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
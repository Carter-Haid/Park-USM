import re

name = 'example.txt'


with open(name, 'r') as file:
    text = file.readlines()

index_prohibited = 0
index_available = 0
day = []
time = []
for each in range(len(text)):
    pattern = re.compile(r'prohibited:')
    pattern2 = re.compile(r'following\slots:')
    pattern3 = re.compile(r'\,\s[A-Z][a-z]{2,10}\s[0-9]{1,2}(nd|rd|th)?')
    pattern4 = re.compile(r'[0-9]{2}(:[0-9]{0,2})?\s(am|pm)')
    matches = re.search(pattern, text[each])
    matches2 = re.search(pattern2, text[each])
    matches3 = re.search(pattern3, text[each])
    matches4 = re.search(pattern4, text[each])
    if matches:
        index_prohibited = each+1
    elif matches2:
        index_available = each + 1
    if matches3:
        x = pattern3.finditer(text[each])
        for match in x:
            day.append(match.group(0).split(',')[1])
    if matches4:
        x = pattern4.finditer(text[each])
        for match in x:
            time.append(match.group(0))


print('\n\nProhibited Lots:-')
for x in range(index_prohibited, index_available-1):
    try:
        print(text[x].split()[0])
    except:
        pass

print('\n\nAvailable Lots:-')

for x in range(index_available, len(text)):
    try:
        print(text[x].split()[0])
    except:
        pass

if len(day) == 2 and len(time) == 2:
    print(f"\n\nStarting : {day[0]} {time[0]}")
    print(f"Ending   : {day[1]} {time[1]}")
else:
    print("\n\nDays and time couldn't be extracted properly, contact developer with sample file.")
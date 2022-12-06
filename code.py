import xml.etree.ElementTree as ET
tree = ET.parse('C:\\Users\\dines\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\SLPY1GSG\\Orders[1]\\orders.xml')

root = tree.getroot()

i = 0
for elem in root:
    if i>10:
        break
    for subelem in elem:
        if i>10:
            break
        i+=1
        print(subelem.txt)

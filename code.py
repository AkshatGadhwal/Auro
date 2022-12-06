import xml.etree.ElementTree as ET
tree = ET.parse('C:\\Users\\dines\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\SLPY1GSG\\Orders[1]\\orders.xml')

root = tree.getroot()

i = 0

books = []
buy = {}
sell = {}
orders = {}

def matching(order_id):
    a = 10
    

for elem in root.iter():
    if elem.tag == 'AddOrder':
        book = elem.attrib['book']
        order_id = elem.attrib['orderId']
        operation = elem.attrib['operation']
        if book not in books:
            books.append(book)
        if operation == 'BUY':
            if book not in buy:
                buy[book] = []
            buy[book].append(order_id)
        else:
            if book not in sell:
                sell[book] = []
            sell[book].append(order_id)
        orders[order_id] = {'operation':elem.attrib['operation'],'price':elem.attrib['price'],'volume':elem.attrib['volume']}
    elif elem.tag == 'DeleteOrder':
        book = elem.attrib['book']
        order_id = elem.attrib['orderId']
        if order_id in orders:
            book = orders[order_id]['book']
            operation = orders[order_id]['operation']
            orders.delete(order_id)
            if operation == 'BUY':
                buy[book].delete(order_id)
            else:
                sell[book].delete(order_id)
                
                
for book in books:
    print("processing... "+book)
    l = max(len(sell[book]),len(buy[book]))
    for i in range(l):
        a = ''
        b = ''
        if i<len(buy[book]):
            a = orders[buy[book][i]]['volume'] + ' @'+ orders[buy[book][i]]['price']
        else:
            a = "          "
        if i<len(sell[book]):
            b = orders[sell[book][i]]['volume'] + ' @'+ orders[sell[book][i]]['price']
        print(a+' -- '+b)
    print()


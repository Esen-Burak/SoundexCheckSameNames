class Node:
    def __init__(self, value):
        self.value = value
        self.children = {}

def insert(root, code, name):
    current = root
    for char in code:
        if char not in current.children:
            current.children[char] = Node(None)
        current = current.children[char]
    current.value = name

def print_tree(node, indent=0):
    if node.value is not None:
        print(" " * indent + node.value)
    for char, child in node.children.items():
        print_tree(child, indent + 4)
def find_value(root, code):
    current = root
    for char in code:
        if char in current.children:
            current = current.children[char]
        else:
            return None
    return current.value if current.value is not None else "Kod bulunamadı"
# Ana ağacı oluştur
root = Node('*')

# Verilen isim ve kodları kullanarak ağaca ekle
data = [
    ('Johnson', 'J525'), ('Jonson', 'J525'),
    ('Adams', 'A352'), ('Addams', 'A352'),
    ('Davis', 'D120'), ('Davies', 'D120'),
    ('Simons', 'S520'), ('Simmons', 'S520'),
    ('Richards', 'R263'), ('Richardson', 'R263'),
    ('Taylor', 'T460'), ('Tailor', 'T460'),
    ('Carter', 'C636'), ('Chater', 'C360'),
    ('Stevenson', 'S315'), ('Stephenson', 'S315'),
    ('Taylor', 'T460'), ('Naylor', 'N460'),
    ('Smith', 'S530'), ('Smythe', 'S530'),
    ('McDonald', 'M235'), ('MacDonald', 'M235'),
    ('Harris', 'H620'), ('Harrys', 'H620'),
    ('Sim', 'S500'), ('Sym', 'S500'),
    ('Williams', 'W452'), ('Wilson', 'W425'),
    ('Baker', 'B260'), ('Barker', 'B626'),
    ('Wells', 'W420'), ('Wills', 'W420'),
    ('Fraser', 'F626'), ('Frazer', 'F626'),
    ('Jones', 'J520'), ('Johns', 'J520'),
    ('Wilks', 'W420'), ('Wilkinson', 'W425'),
    ('Hunt', 'H530'), ('Hunter', 'H536'),
    ('Sanders', 'S536'), ('Saunders', 'S536'),
    ('Parsons', 'P625'), ('Pearson', 'P625'),
    ('Robson', 'R125'), ('Robertson', 'R163'),
    ('Harker', 'H626'), ('Parker', 'P626')
]

for name, code in data:
    insert(root, code, name)
result = find_value(root, 'J525')
print("Değer:", result)
# Ağacı yazdır
print_tree(root)
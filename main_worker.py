import soundex
from flask import Flask, jsonify, request
from tree import Node, insert, find_values
import json
import os

app = Flask(__name__)

def createTree():
    # Ana ağacı oluştur
    tree = Node()
        
    with open('names.json', 'r') as file:
        data = json.load(file)
    womenNames = [item['name'] for item in data if item.get('sex') != 'E']
    
    soundex_codes = []
    for name in womenNames:
        soundex_code = soundex.soundex(name)
        soundex_codes.append(soundex_code)
    
    # Elde edilen kodları verilen isim ve kodlar listesine eşleştirerek bir tuple listesi oluştur
    name_code_tuples = [(womenNames[i], soundex_codes[i]) for i in range(len(womenNames))]
    
    # mainss fonksiyonunun dönüş değerini ağaca ekle
    for name, code in name_code_tuples:
        insert(tree, code, name)
        
    return tree

# mainss fonksiyonunu bir kere çağır
tree = createTree()
#example -> http://localhost:10001/find_same_names?name=sophia
@app.route('/find_same_names', methods=['GET'])
def find_values_route():
    name = request.args.get('name')
    if name:
        code = soundex.soundex(name)
        result = find_values(tree, code)
        return jsonify({"values": result})
    else:
        return jsonify({"error": "Kod parametresi eksik"}), 400

if __name__ == '__main__':
    # Program ayağa kalkarken app.run() çağrılır
    app.run(host=os.environ.get('HOST',"localhost"),port=int(os.environ.get('PORT',10002)),debug=True)

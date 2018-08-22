from difflib import SequenceMatcher, get_close_matches

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
nome="D1OGO.IMT"
res="D10G01 IMT"

words = ["D1OGO.IMT"]
print(get_close_matches("D10G01 IMT", words))

print(similar(nome,res))

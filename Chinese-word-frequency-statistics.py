import json
import re

with open('/content/Shopee_training_ckipseg_v3_OK.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

pattern = r'[ \n]'
output = {}


for entry in data:
    tags = entry['description_wseg']
    tags2 = entry['description_wpos']
    items = [item.strip() for item in re.split(pattern, tags) if item.strip()]
    items2 = [item2.strip() for item2 in re.split(pattern, tags2) if item2.strip()]
    combined_dict = zip(items, items2)
    #print( combined_dict)
    for word, pos in combined_dict:
        if word not in output:
            output[word] = {}

        if pos in output[word]:
            output[word][pos] += 1
        else:
            output[word][pos] = 1


with open('/content/output_11257065.json', 'w', encoding='utf-8') as outfile:
    json.dump(output, outfile, ensure_ascii=False, indent=2)

print("Output file 'output.json' has been created.")

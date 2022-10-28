import os
import json
alldic={}
for i in os.listdir("./formats/"):
    if i[-4:]=="json":
        print(i)
        with open("./formats/"+i) as f:
            dic=json.load(f)
            alldic[i[:-5]]=dic
with open('./formatbook.json', 'w') as f:
    json.dump(alldic,f,indent=4)
import pandas as pd 
import json 

with open("C:/Users/user/Documents/Archivo JSON JUAN ARANGO.json", 'r', encoding='utf-8') as f:
    data=json.load(f)
    
df = pd.read_xml("C:/Users/user/Documents/Archivo XML JUAN ARANGO.xml")
# df= pd.json_normalize(data,record_path="Empleados")
print (df)


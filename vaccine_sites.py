import json
from os import scandir
import urllib.request
from pprint import pprint

class VaccineSites:
    def __init__(self):
        self.all_data = []

    def url(self):
        self.json_url = f"https://services.arcgis.com/njFNhDsUCentVYJW/arcgis/rest/services/MD_Vaccination_Locations/FeatureServer/4/query?where=1%3D1&outFields=*&outSR=4326&f=json"
        self.res = urllib.request.urlopen(self.json_url).read().decode('utf-8')
        self.vac_json = json.loads(self.res)
        
    def parseJson(self):
        data = self.vac_json["features"]
        
        for item in data:
            self.all_data.append(item.get("attributes"))
        
        return self.all_data
    
class Selector:
    def __init__(self):
        self.selected_data =  []
        
    def filter(self, all_data):
        self.all_data = all_data
        self.input = input("County: ").title()
        for item in all_data:
            if item["County"] == f"{self.input}":
                self.selected_data.append(item)
                
        counter = 0
        if len(self.selected_data) == 0: 
            for dic in self.all_data:
                for key, values in dic.items():
                    self.selected_data.append(f'Result {counter}: {key} --> {values}')
                counter += 1
        
        return self.selected_data

class TxtFileGen:
    def __init__(self):
        self.file = open("vaccine_sites_query_results.txt","w")
        
    def writer(self, selected_data):
        self.file.write(json.dumps(selected_data, indent=4))

def main():
    vs = VaccineSites()
    vs.url()
    all_data = vs.parseJson()
    
    s = Selector()
    selected_data = s.filter(all_data)
    
    tfg = TxtFileGen()
    tfg.writer(selected_data)

if __name__ == "__main__":
    main()
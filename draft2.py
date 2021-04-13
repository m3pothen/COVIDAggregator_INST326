import json
import urllib.request

originalUrl = "https://services.arcgis.com/njFNhDsUCentVYJW/arcgis/rest/services/MD_Vaccination_Locations/FeatureServer/4/query?where=1%3D1&outFields=*&outSR=4326&f=json"

class UserInfo:  
    """A class for Maryland residents to get information on 
        vaccine distribution
    """ 
    def __init__(self, name, county):
        #initialize parameters 
        #use input statements to get info from user 
        
    def urls():
        """Gives the user the url to the website of the site"""
        
        countyInput = input("Type in the County name in MD:")
        countyUrl = f"https://services.arcgis.com/njFNhDsUCentVYJW/arcgis/rest/services/MD_Vaccination_Locations/FeatureServer/4/query?where=County%20%3D%20'{countyInput}'&outFields=*&returnGeometry=false&outSR=4326&f=json"
        data = urllib.request.urlopen(countyUrl).read().decode('utf-8')
        vacSites = json.loads(data)
        print(vacSites)
        
    def get_site(county): 
       """Gets the addresses of vaccine sites in MD
       
       Args:
        county (string): MD county user lives in
        
       """ 
        # finds list of vaccine sites based on user county 
    
    def vaccine_type(site_name):
        """Tells user if vaccine site gives out Pzfier, Moderna, or J&J vaccine
        
        Args:
            site_name (string): the name of the vaccine site

        """
        #input a vaccine site and output the type of vaccines available 
    
    def available_times(site_name): 
        """Gives the user the availabe appt times of the site
        
        Args:
            site_name (string): the name of the vaccine site

        """
        #input vaccine site name and output available appointment times 

    def summary():
        """Gives a summary of vaccine distribution for user
        
        Side effects:
            Prints out a summary of information on vaccine sites
            and users eligibility to get the vaccine 
        """
        #prints out summary for user 
        #invokes the Eligibility calculator class 

class EligibilityCalculator(UserInfo): 
    """A subclass of UserInfo to determine user eligibility for vaccine"""
    def get_health_info():
        """Gets info on age, occupation, and medical conditions of user"""
        #ask series of input questions and store in boolean vars 
    
    def determine_phase(): 
        """Determines what vaccine distribution phase user falls under"""
        #based on boolean vars^^ determine phase user is in 
        #use series of if-statements 
    
    def vaccine_appt_time(county):
        """Tells user where they are eligble to get the vaccine 
        
        Returns: 
            list of strings: counties where user can be vaccinated 
            string: phase user's county is in 
        """
        #returns list of counties the user is eligble in 
        #if user is not eligible in their county, 
        # the phase the user's county is in will be returned 

def main():
    VaccineSites.url()

if __name__ == "__main__": 
    my_user = User_Info("name", "Laurel")
    main()
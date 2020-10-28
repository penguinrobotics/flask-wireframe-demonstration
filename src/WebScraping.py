import requests
from bs4 import BeautifulSoup
import TeamStore as teams
import Configuration as config

ROOT = "http://10.0.0.217/" #TODO this needs to be a config
TOURNY = ROOT + "division1/rankings"
SKILLS = ROOT + "skills/rankings"

# Offsets to make lists easier ----------------------------------------
def __number_offset(index):
    return index+1

def __name_offset(index):
    return index+2

def __rank_index(index):
    return index

def __wlt_offset(index):
    return index+3

def __wp_offset(index):
    return index+4

def __ap_offset(index):
    print("This feature doesn't exist anymore")
    return index+5

def __sp_offset(index):
    return index+5

def __score_offset(index):
    return index+3

def __prog_score_offset(index):
    return index+4

def __drive_score_offset(index):
    return index+6

def __prog_attempt_offset(index):
    return index+5

def __drive_attempt_offset(index):
    return index+7
#End offsets ----

#Converts the HTML elements into raw strings for processing
def __preprocess_elms(elms):
    converted = []
    for raw in elms:
        converted.append(raw.get_text())
    return converted

def get_tourny_ranks():
    page = requests.get(TOURNY)
    soup = BeautifulSoup(page.content, 'html.parser')
    tableElms = soup.find_all('td')
    
    #print(tableElms)
    #print(preprocess_elms(tableElms))
    
    elms = __preprocess_elms(tableElms)
    for index in range(0, len(tableElms), 6):
        teams.add_rank(elms[__number_offset(index)], elms[index]) #Guarentess the team exists now
        team = teams.teams[elms[__number_offset(index)]] #Get a ref
        
        team.set_name(elms[__name_offset(index)])
        team.set_wlt(elms[__wlt_offset(index)])
        team.set_wp(elms[__wp_offset(index)])
        #team.set_ap(elms[__ap_offset(index)])
        team.set_sp(elms[__sp_offset(index)])

def get_skills_ranks():
    page = requests.get(SKILLS)
    soup = BeautifulSoup(page.content, 'html.parser')
    tableElms = soup.find_all('td')
    
    elms = __preprocess_elms(tableElms)
    
    for index in range(0, len(tableElms), 8):
        teams.add_skills_rank(elms[__number_offset(index)], elms[index]) #Guarentees existance
        team = teams.teams[elms[__number_offset(index)]] #Gets a ref

        team.set_skills_score(elms[__score_offset(index)])
        team.set_prog_score(elms[__prog_score_offset(index)])
        team.set_drive_score(elms[__drive_score_offset(index)])
        team.set_prog_attempts(elms[__prog_attempt_offset(index)])
        team.set_drive_attempts(elms[__drive_attempt_offset(index)])

def update_scores():
    global root
    root = config.get_tm_address()
    print("Scraping VexTM")
    get_tourny_ranks()
    print("Tournament ranks retrieved")
    get_skills_ranks()
    print("Skills Ranks retrieved")

#Main Executing Stuff ---------------------------------------------------------------------------------------------------------------
#    load_judged_scores()
#    get_tourny_rank()
#    get_skills_ranks()
#    save_combined_scores()
#    print("Program Ending")
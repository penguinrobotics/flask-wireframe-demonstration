import WebScraping
import json
import Configuration as config
from pathlib import Path

#Vex Team Database Management ------------------------------------------------------------------------------------------------------
class CompetingTeam:

    def init_from_serial(self, number, serial):
        self.team_number = serial['number'] #Actually String ###X
        self.name = serial['name'] #String
        
        self.rank = serial['rank'] #Integer
        self.wlt = serial['wlt'] #String
        self.wp = serial['wp'] #Integer
        self.ap = serial['ap'] #Integer
        self.sp = serial['sp'] #Integer
        
        #From Skills Page
        self.skills_rank = serial['skrank'] #Number
        self.skills_score = serial['skscore'] #Number
        self.prog_score = serial['progscore'] #Number
        self.prog_attempts = serial['progruns'] #Number
        self.driving_score = serial['drivescore'] #Number
        self.driving_attempts = serial['driveruns'] #Number

        self.judge_score = serial['judged']

    def __init__(self, number, serial=None):
        if serial is None:
            #From Rankings Page
            self.team_number = number #Actually String ###X
            self.name = "" #String
        
            self.rank = 0 #Integer
            self.wlt = "x-x-x" #String
            self.wp = 0 #Integer
            self.ap = 0 #Integer
            self.sp = 0 #Integer
        
            #From Skills Page
            self.skills_rank = 0 #Number
            self.skills_score = 0 #Number
            self.prog_score = 0 #Number
            self.prog_attempts = 0 #Number
            self.driving_score = 0 #Number
            self.driving_attempts = 0 #Number
        
            #Judges Information
            self.judge_score = 0 #Number
        else:
            self.init_from_serial(number, serial)
        
    def get_number(self):
        return self.team_number
    
    def set_name(self, name):
        self.name = name
    
    def set_rank(self, rank):
        self.rank = rank
    
    def set_wlt(self, nwlt):
        self.wlt = nwlt
    
    def set_wp(self, wp):
        self.wp = wp
    
    def set_ap(self, ap):
        self.ap = ap
    
    def set_sp(self, sp):
        self.sp = sp
    
    def set_skills_rank(self, skillsrank):
        self.skills_rank = skillsrank
    
    def set_skills_score(self, skillscore):
        self.skills_score = skillscore
    
    def set_prog_score(self, progscore):
        self.prog_score = progscore
    
    def set_drive_score(self, drivescore):
        self.driving_score = drivescore
    
    def set_prog_attempts(self, progattempts):
        self.prog_attempts = progattempts
    
    def set_drive_attempts(self, driveattempts):
        self.driving_attempts = driveattempts
    
    def set_judge_score(self, judgescore):
        self.judge_score = judgescore
        
    def get_judged_score(self):
        return self.judge_score
    
    def get_has_judged_score(self):
        return self.judge_score != 0

    def serialize(self):
        return {"number": self.team_number,
        "name": self.name,
        "rank": self.rank,
        "wlt": self.wlt,
        "wp": self.wp,
        "ap": self.ap,
        "sp": self.sp,
        "skrank": self.skills_rank,
        "skscore": self.skills_score,
        "progscore": self.prog_score,
        "progruns": self.prog_attempts,
        "drivescore": self.driving_score,
        "driveruns": self.driving_attempts,
        "judged": self.judge_score}

#module componenets
teams = {}

def add_team(team):
    if not team.get_number() in teams:
        teams[team.get_number()] = team

def add_judged_score(number, score):
    if not number in teams:
        teams[number] = CompetingTeam(number)
    teams[number].set_judge_score(score)

def add_rank(number, rank):
    if not number in teams:
        teams[number] = CompetingTeam(number)
        teams[number].set_judge_score(0)
    teams[number].set_rank(rank)

def add_skills_rank(number, srank):
    if not number in teams:
        teams[number] = CompetingTeam(number)
    teams[number].set_skills_rank(srank)

def update_online():
    print("Team Store connecting to VexTM")
    WebScraping.update_scores()
    print("Team Store returned from VexTM")

def get_unjudged_teams():
    #print("Accessing unjudged teams for display")
    unjudged_teams = []
    for key in teams:
        #print("Checking team", key, " and finding ", type(teams[key]))
        if not teams[key].get_has_judged_score():
            unjudged_teams.append(teams[key].get_number())
    print("Returning unjudged teams = ", unjudged_teams)
    return unjudged_teams

def contains_team(question):
    return question in teams

def load_from_file():
    global teams
    try:
        with open('storage/' + config.TOURNAMENT_NAME + '/teams.json') as f:
            stored_teams = json.load(f)
            print("Loading Teams From File")
            for key in stored_teams:
                teams[key] = CompetingTeam(key, stored_teams)
    except Exception as e:
        print(e)
        print("Failed to load teams from file")

def save_to_file():
    global teams
    save_dict = {}
    for key in teams:
        save_dict[key] = teams[key].serialize()
    try:
        with open('storage/' + config.TOURNAMENT_NAME + '/teams.json', 'w') as json_file:
            json.dump(save_dict, json_file)
            print("Teams Saved Successfuly")
    except Exception as e:
        Path("storage/" + config.TOURNAMENT_NAME).mkdir(parents=True, exist_ok=True)
        print(e)
        print("Error Saving Teams, directory created for next cycle")

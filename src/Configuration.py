import json

__TM_KEY = "tmip"
__TNM_KEY = "tny"

TM_IP = "10.0.0.217"
TOURNAMENT_NAME = "hello-world"

def get_tm_address():
    return "http://" + TM_IP + "/"

def update_tm_ip(newip):
    global TM_IP
    TM_IP = newip
    save_config_file()

def update_tourny_name(newname):
    global TOURNAMENT_NAME
    TOURNAMENT_NAME = newname
    save_config_file()

def load_config_from_file():
    global TM_IP
    global TOURNAMENT_NAME
    global __TM_KEY
    global __TNM_KEY
    print("Loading Config From File")
    try:
        with open('storage/config.json') as f:
            data = json.load(f)
            TM_IP = data[__TNM_KEY]
            TOURNAMENT_NAME = data[__TNM_KEY]
            print("Loaded data", TM_IP, ", ", TOURNAMENT_NAME)
    except:
        print("Failed to load config file. Saving to create one")
        save_config_file()

def save_config_file():
    print("Saving Config File")
    global TM_IP
    global __TM_KEY
    global TOURNAMENT_NAME
    global __TNM_KEY
    config = {__TM_KEY: TM_IP,
    __TNM_KEY: TOURNAMENT_NAME
    }
    try:
        with open('storage/config.json', 'w') as json_file:
            json.dump(config, json_file)
        print("Write Successful")
    except:
        print("Failed writing config file")

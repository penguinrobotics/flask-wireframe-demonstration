accounts = {
    "kaiden": "kdn",
    "daruvin": "dvn",
    "tim": "tm"
}

def account_valid(username, password):
    return username in accounts and accounts[username] == password

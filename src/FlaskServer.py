import flask
from flask import Flask
from flask import request
import TeamStore as team_store
import Accounts as accounts
import Configuration as config

app = Flask(__name__)

@app.route('/')
def root():
    if request.args.get('submit') is None:
        return flask.render_template('login.html')
    else:
        username = request.args.get('username')
        password = request.args.get('password')
        if username == "display":
            return flask.redirect("/display")
        elif username == "admin" and password == "pyrsadmin": #TODO Configure admin password
            return flask.redirect('/admin?username=' + username + '&' + 'password=' + password + '&auth=true')
        elif username == "admin" and password != "pyrsadmin":
            return flask.render_template('login-invalid.html')
        else:
            if accounts.account_valid(username, password):
                return flask.redirect('/submission?username=' + username + "&password=" + password)
            else:
                return flask.render_template('login-invalid.html')

@app.route('/admin')
def admin():
    return flask.render_template('admin/admin.html', ip=config.TM_IP, tourny=config.TOURNAMENT_NAME)

@app.route('/admin/ip')
def set_ip():
    if request.args.get('submit') is None:
        return flask.render_template('admin/admin-ip.html', ipin=config.TM_IP)
    else:
        ip = request.args.get('ip')
        #config.TM_IP = ip
        config.update_tm_ip(ip)
        return flask.redirect('/admin')

@app.route('/admin/name')
def set_name():
    if request.args.get('submit') is None:
        return flask.render_template('admin/admin-name.html', tourny=config.TOURNAMENT_NAME)
    else:
        name = request.args.get('name')
        #config.TOURNAMENT_NAME = name
        config.update_tourny_name(name)
        return flask.redirect('/admin')

@app.route('/summary')
def summary_sheet():
    return flask.render_template('team-summary.html', teams=list(team_store.teams.values()))

@app.route('/display')
def display():
    return flask.render_template("judged-display.html", unjudged=team_store.get_unjudged_teams())

@app.route('/submission')
def submission():
    judge = request.args.get('username')
    if request.args.get('submit') is None:
        return flask.render_template('team-submission.html', name=judge)
    else:
        #judge = request.args.get('username')
        team = request.args.get('team')
        score = request.args.get('score')
        if team_store.contains_team(team) and score.isnumeric():
            team_store.add_judged_score(team, score)
            return flask.render_template('team-submission.html', name=judge, message="Team " + team + " Scored")
        else:
            return flask.render_template('team-submission.html', name=judge, message="That last response was invalid")

active = True

# Needs to be at the bottom
def start():
    global active
    print("Starting flask component of Penguin Server")
    active = True
    app.run()
    print("Flask Exited")
    active = False

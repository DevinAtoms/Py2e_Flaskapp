import os
from flask import Flask, redirect, url_for, request, render_template
import requests
from spells import init_actor, spell_parse, spell_print

app = Flask(__name__)

global refresh_token

global access_token


def del_name(itemdict):
    dictname = [key for key in itemdict]
    for key in dictname:
        if key == 'ArmorClass':
            del itemdict[key]['compset']
        else:
            del itemdict[key]['name']
    return itemdict


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/spell_card/')
def spell_card():
    spells = {'Acid Splash': {'spCastingText': ['twoaction']}, 'Mage Armor': {'spCastingText': ['twoaction']},
              'Magic Missile': {'spCastingText': ['threeaction']}, 'Heal': {'spCastingText': ['oneaction',
                                                                                              'threeaction']}}
    return render_template('card.html', spells=spells)


@app.route('/token/')
def token_req():
    return render_template('token.html')


@app.route('/token/', methods=['POST'])
def token_req_post():
    acc_req = {'refreshToken': os.environ['refresh_token'], 'toolName': 'Py2e'}
    acc_resp = requests.post('https://api.herolab.online/v1/access/acquire-access-token', json=acc_req)
    access_token = acc_resp.json()['accessToken']
    player = request.form['token']
    ch_req = {'accessToken': access_token, 'elementToken': player}
    ch_resp = requests.post('https://api.herolab.online/v1/character/get', json=ch_req)
    spells = init_actor(ch_resp.json()['export'])
    for s in spells:
        spell_print(spells[s])
    return render_template('token.html', spells=spells)


if __name__ == '__main__':
    app.run(debug=True)

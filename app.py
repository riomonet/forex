import os
import requests
from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from currency_symbols import CurrencySymbols

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretsarecool'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# app.config['TESTING'] = True
# app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

debug = DebugToolbarExtension(app)

@app.route('/main')
def main ():
    return render_template('/main.html', currency_list = currency_list)

@app.route('/next')
def next ():
    frm = get_value('from')
    to =  get_value('to')
    amount = get_value('amount')
    output = mk_output(frm, to, amount)
    
    return render_template('/main.html', currency_list = currency_list, output = output ,frm=frm,to=to,amount=amount)

def mk_output(frm, to, amount):
    frm_sym = get_symbol(frm)    
    to_sym = get_symbol(to)
    rate =  get_rate(frm, to)
    total = float(rate) * float(amount)
    amount = float(amount)

    if to == 'BTC':
        t = f'{total:.8f}'
    else:
        t = f'{total:.2f}'

    if frm == 'BTC':
        f = f'{amount:.8f}'
    else:
        f = f'{amount:.2f}'
    return f'{frm_sym} {f} {frm} =  {to_sym} {t} {to}'

    
def get_symbol(code):
    return CurrencySymbols.get_symbol(code)

def get_value(name):
    return request.args.get(name)

def get_rate(frm, to):
    return call_api( f'https://api.exchangerate.host/convert?from={frm}&to={to}').get('result')



def call_api(url):
    "get data from api call"
    return requests.get(url).json()


currency_list = call_api( 'https://api.exchangerate.host/symbols').get('symbols').items()








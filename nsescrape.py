import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request


app = Flask(__name__)
@app.route('/all', methods = ['GET', 'POST'])
def home():
    #nifty50
    r = requests.get('https://www.nseindia.com/market-data/live-equity-market', headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"})
    soup = BeautifulSoup(r.content,'html.parser')
    s = soup.find('div', class_='index_val')
    content = str(s.find_all('span')[0])
    data = {'nifty50':content.split('s="val ltp">')[1].split('<i')[0].strip()}
    #sensex
    r = requests.get('https://economictimes.indiatimes.com/indices/sensex_30_companies', headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"})
    soup = BeautifulSoup(r.content,'html.parser')
    s = soup.find('div', id='headStuff')
    content = str(s.find_all('div')[0])
    data["sensex"] = content.split('ltp">')[1].split('</di')[0].strip()
    #gold
    r = requests.get('https://www.goodreturns.in/gold-rates/', headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"})
    soup = BeautifulSoup(r.content,'html.parser')
    s = soup.find('strong', id='el')
    content = str(s) #tr(s.find_all('i')[0])
    data["gold"] = content.split('</i>')[1].split('</s')[0].strip()
    #silver
    r = requests.get('https://www.goodreturns.in/silver-rates/', headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"})
    soup = BeautifulSoup(r.content,'html.parser')
    s = soup.find('strong', id='el')
    content = str(s) #tr(s.find_all('i')[0])
    data["silver"] = content.split('</i>')[1].split('</s')[0].strip()
    #ust to inr
    r = requests.get('https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=INR', headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"})
    soup = BeautifulSoup(r.content,'html.parser')
    s = soup.find('p', class_='result__BigRate-sc-1bsijpp-1')
    content = str(s) #tr(s.find_all('i')[0])
    data["usd2inr"] = content.split('Aod">')[1].split('<span')[0].strip()
    #json response
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug = True)

import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route('/nifty50', methods = ['GET', 'POST'])
def home():
    r = requests.get('https://www.nseindia.com/market-data/live-equity-market', headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"})
    soup = BeautifulSoup(r.content,'html.parser')
    s = soup.find('div', class_='index_val')
    content = str(s.find_all('span')[0])
    data = content.split('s="val ltp">')[1].split('<i')[0].strip()
    return jsonify({'data':data})

if __name__ == '__main__':
    app.run(debug = True)
import random
import string
from flask import Flask, render_template, request, redirect, url_for
from mongoengine import connect
from model import Link
from datetime import datetime, timedelta
import json


app = Flask(__name__)

connect(host="mongodb+srv://admin:admin@cluster0.6o1gi.mongodb.net/shorter?retryWrites=true&w=majority")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shortened_link():
    url = request.json['url']
    if url and url is not None:
        expired_date = request.json['expiredDate']
        hash_url = ''.join(random.choices(string.ascii_letters, k=4))
        expired_date = datetime.now() + timedelta(days=int(expired_date))
        while Link.objects(hash=hash_url):
            hash_url = ''.join(random.choices(string.ascii_letters, k=4))
        Link(expired_date=expired_date, url=url, hash=hash_url).save()
        return json.dumps({"success": True, "hash": hash_url, "url": request.base_url.replace("shorten", hash_url) }), 200, {"ContentType": "application/json"}
    else:
        return json.dumps({"success": False}), 400, {"ContentType": "application/json"}

@app.route('/<hash_url>')
def hash_redirect(hash_url):
    link = Link.objects(hash=hash_url).first()
    if datetime.now() > link.expired_date:
        return redirect(url_for('index'))
    return redirect(link.url)


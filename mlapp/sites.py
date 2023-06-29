from flask import Blueprint, render_template, request, flash, redirect, url_for
from .dbase import urldatabase
from . import db
import pickle
from .scraper import scraper
import pandas as pd

sites = Blueprint('sites', __name__)

load_model = pickle.load(open('trained_model.pkl', 'rb'))
load_vect = pickle.load(open('vectorizer.pkl', 'rb'))

@sites.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        geturl = request.form.get('url')
        input_data = scraper(geturl)
        df = pd.DataFrame({'Text_cleaning' : [input_data]})
        df = df['Text_cleaning']
        load_data = load_vect.transform(df)
        prediction = load_model.predict(load_data)
        prediction = prediction[0]
        if bool(db.session.query(urldatabase).filter_by(url=geturl).first()) == False:
            saveurldata = urldatabase(url = geturl, category = prediction)
            db.session.add(saveurldata)
            db.session.commit()
        urls = db.session.query(urldatabase).all()
        return render_template('home.html',prediction=prediction, urls = urls)
    else:
        return render_template('home.html')

import os
import requests
import operator
import re
import nltk
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from stop_words import stops
from collections import Counter
from bs4 import BeautifulSoup
from flask_bootstrap import Bootstrap
from coolmonk import resume_data
from newsapi import NewsApiClient
from datetime import datetime, timedelta
import pytz

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['data']=resume_data
db = SQLAlchemy(app)
bootstrap = Bootstrap()
bootstrap.init_app(app)

from models import Result

@app.route("/words", methods=['GET', 'POST'])
def wordcount():
   errors = []
   results = {} 
   if request.method == "POST":
      try:
         url = request.form['url']
         r = requests.get(url)
      except:
         errors.append(
           "Unable to get URL. Please make sure it's valid and try again."
         )
         return render_template('wordcount.html', errors=errors)
      if r:
         # text processing
         raw = BeautifulSoup(r.text, 'html.parser').get_text()
         nltk.data.path.append('./nltk_data/')  # set the path
         tokens = nltk.word_tokenize(raw)
         text = nltk.Text(tokens)
         # remove punctuation, count raw words
         nonPunct = re.compile('.*[A-Za-z].*')
         raw_words = [w for w in text if nonPunct.match(w)]
         raw_word_count = Counter(raw_words)
         # stop words
         no_stop_words = [w for w in raw_words if w.lower() not in stops]
         no_stop_words_count = Counter(no_stop_words)
         # save the results
         results = sorted(
             no_stop_words_count.items(),
             key=operator.itemgetter(1),
             reverse=True
         )
         try:
             result = Result(
             url=url,
             result_all=raw_word_count,
                result_no_stop_words=no_stop_words_count
             )
             db.session.add(result)
             db.session.commit()
         except:
             errors.append("Unable to add item to database.") 
   return render_template('wordcount.html', errors=errors, results=results)     

@app.route('/me')
@app.route('/')
def index():
   return render_template('index.html')

@app.route('/work')
def about():
   return render_template('about.html')

@app.route('/news')
def news():
   news_api = NewsApiClient(api_key=app.config['NEWS_API_KEY'])
     
   pst = pytz.timezone('America/Los_Angeles')
   curr_utc_time = datetime.utcnow()
   from_utc_time = pytz.UTC.localize(curr_utc_time - timedelta(days=1))
   from_pst_time = from_utc_time.astimezone(pst)
   to_utc_time = pytz.UTC.localize(curr_utc_time)
   to_pst_time = to_utc_time.astimezone(pst)

   sources='wired,the-globe-and-mail,techcrunch,the-verge,reuters,hacker-news,cnn,bbc-news,ars-technica'
   all_articles = news_api.get_everything(sources=sources,
                                      from_param=str(to_pst_time.date()),
                                      to=str(to_pst_time.date()),
                                      language='en',
                                      sort_by='popularity',
                                      page=5) 

   #all_articles = news_api.get_top_headlines(country='us',
   #                                   language='en',
   #                                   page=2)

   return render_template('news_feed.html', all_articles=all_articles)
    

if __name__ == "__main__":
   app.run(host='0.0.0.0')

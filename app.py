from flask import Flask, render_template, redirect,jsonify
import selenium
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)

mongo = PyMongo(app)

@app.route('/')
def home():
    mars_data=mongo.db.mars_data.find_one()
    
    return render_template("index.html", mars_data = mars_data)

@app.route('/scrape')
def scrape():
    mars_data= mongo.db.mars_data
    mars_details = scrape_mars.scrape_mars()

    mongo.db.mars_data.insert_one(mars_details)
    print('data is inserted into mongo')
    print('success')
    return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
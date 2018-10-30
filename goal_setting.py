from flask import Flask, render_template, request, redirect, url_for
import os
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


def get_category_names():
    categories = []
    for category in mongo.db.collection_names():
        if not category.startswith("system."):
            categories.append(category)
    return categories 

@app.route("/")
def home_page():
    return render_template("home.html")
    
@app.route('/categories')
def get_categories():
    categories = get_category_names()
    return render_template("categories.html", categories=categories)

@app.route('/categories/add', methods=["POST"])
def add_category():
    category_name = request.form["category_name"]
    mongo.db.create_collection(category_name)
    return redirect(url_for("get_categories"))
    
    

if __name__ == "__main__":
        app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)






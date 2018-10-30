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
    
 
 
@app.route("/goals")
def get_goals():
    categories = get_category_names()
    return render_template("goals.html", categories=categories, category='Goals List')
    
@app.route("/goals/<category>")
def get_goals_by_category(category):
    goals = mongo.db[category].find()
    categories = get_category_names()
    return render_template("goals.html", goals=goals, categories=categories, category=category)

    
@app.route("/add_goal", methods=["GET", "POST"])
def add_goal():
    if request.method=="POST":
        form_values = request.form.to_dict()
        form_values["is_done"] = "is_done" in form_values
        category = form_values["category_name"]
        mongo.db[category].insert_one(form_values)
        return redirect("/goals")
    else:
        categories = get_category_names()
        return render_template("add_goal.html", categories=categories)
        
        

if __name__ == "__main__":
        app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)






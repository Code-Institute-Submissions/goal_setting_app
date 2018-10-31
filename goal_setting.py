from flask import Flask, render_template, request, redirect, url_for
import os
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from base64 import b64encode
import base64

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
    
@app.route("/overview")
def overview_page():
    return render_template("overview.html")
    
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


@app.route("/goals/<category>/<goal_id>")
def goal_details(category, goal_id):
        the_goal =  mongo.db[category].find_one({"_id": ObjectId(goal_id)})
        return render_template('goal_detail.html', goal=the_goal)


@app.route("/goals/<category>/<goal_id>/add_step", methods=["GET", "POST"])
def add_step(category, goal_id):
        the_goal =  mongo.db[category].find_one({"_id": ObjectId(goal_id)})
        if request.method=="POST":
        
            step = {
                "name": request.form["step"],
                "is_done": False
            }
            
            current_steps = the_goal.get("steps", [])
            current_steps.append(step)
            the_goal["steps"] = current_steps
            
            mongo.db[category].update({"_id":ObjectId(goal_id)},the_goal)
        
            return redirect(url_for("goal_details", category=category, goal_id=goal_id))
        else:
            categories = get_category_names()
            return render_template("add_step.html", goal=the_goal)





    
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






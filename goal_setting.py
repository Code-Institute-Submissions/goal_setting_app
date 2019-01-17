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


# ---------------------------------home page----------------------------------

@app.route("/")
def overview_page():
    categories = mongo.db["Categories"].find()
    
    unfinished = []
    finished = []
    for category in categories:
        category_name = category["category_name"]
        unfinished += mongo.db[category_name].find({"is_done":False})
        finished += mongo.db[category_name].find({"is_done":True})
    return render_template("overview.html", unfinished=unfinished, finished=finished)
    
    
  # ---------------------------------progress page----------------------------------
  
@app.route("/progress")
def progress_page():
    categories = mongo.db["Categories"].find()
    
    unfinished = []
    finished = []
    for category in categories:
        category_name = category["category_name"]
        unfinished += mongo.db[category_name].find({"is_done":False})
        finished += mongo.db[category_name].find({"is_done":True})
    return render_template("progress.html", unfinished=unfinished, finished=finished)
    
    
    
# ---------------------------------categories page----------------------------------

@app.route('/categories')
def get_categories():
    return render_template("categories.html")
    
# ---------------------------------add category----------------------------------

@app.route('/categories/add', methods=["POST"])
def add_category():
    image = request.files['image']  
    image_string = base64.b64encode(image.read()).decode("utf-8")
    form_values = request.form.to_dict()
        
    form_values["image"] = "data:image/png;base64," + image_string

    category_name = request.form["category_name"]
    mongo.db.create_collection(category_name)
    mongo.db["Categories"].insert_one(form_values)
    return redirect(url_for("get_goals"))
   
# ---------------------------------goalspage----------------------------------

@app.route("/goals")
def get_goals():
    categories = mongo.db["Categories"].find()
    return render_template("goals.html", categories=categories, category='Goals')
    
@app.route("/goals/<category>")
def get_goals_by_category(category):
    goals = mongo.db[category].find()
    categories = mongo.db["Categories"].find()
    return render_template("goals.html", goals=goals, categories=categories, category=category)


# ---------------------------------goal detail page----------------------------------

@app.route("/goals/<category>/<goal_id>")
def goal_details(category, goal_id):
        the_goal =  mongo.db[category].find_one({"_id": ObjectId(goal_id)})
        return render_template('goal_detail.html', goal=the_goal)


# ---------------------------------add new step form----------------------------------

@app.route("/goals/<category>/<goal_id>/add_step", methods=["GET", "POST"])
def add_step(category, goal_id):
        the_goal =  mongo.db[category].find_one({"_id": ObjectId(goal_id)})
        if request.method=="POST":
        
            step = {
                "_id": ObjectId(),
                "name": request.form["step"],
                "is_done": False
            }
            if 'steps' in the_goal:
                current_steps = the_goal['steps']
            else:
                
                the_goal['steps'] = []
                current_steps = the_goal['steps']
                
            
            
            current_steps.append(step)
            
            
            done=0
            for step in current_steps:
                if step["is_done"]:
                    done+=1
            
            the_goal["status"]= "So far, you have completed {0} out of {1} steps".format(done, len(the_goal["steps"])) 
            the_goal["is_done"] = False
            
            the_goal["steps"] = current_steps
            
            
            mongo.db[category].update({"_id":ObjectId(goal_id)},the_goal)
        
            return redirect(url_for("goal_details", category=category, goal_id=goal_id))
        else:
            return render_template("add_step.html", goal=the_goal)
            

# ---------------------------------mark step as done or not done form----------------------------------

@app.route("/goals/<category>/<goal_id>/<step_id>/done", methods=["POST"])
def mark_done(category, goal_id, step_id):
    the_goal = mongo.db[category].find_one({"_id": ObjectId(goal_id)})
    
    done=0
    for step in the_goal["steps"]:
        if step["_id"]==ObjectId(step_id):
            step["is_done"] = True
        if step["is_done"]:
            done+=1
    
    num_steps = len(the_goal["steps"])
    
    the_goal["status"]= "So far, you have completed {0} out of {1} steps".format(done, num_steps)
    the_goal["is_done"] = done==num_steps
    mongo.db[category].update({"_id":ObjectId(goal_id)},the_goal)
    
    return redirect(url_for("goal_details", category=category, goal_id=goal_id))
    
@app.route("/goals/<category>/<goal_id>/<step_id>/not_done", methods=["POST"])
def mark_not_done(category, goal_id, step_id):
    the_goal = mongo.db[category].find_one({"_id": ObjectId(goal_id)})
    
    done=0
    for step in the_goal["steps"]:
        if step["_id"]==ObjectId(step_id):
            step["is_done"] = False
        if step["is_done"]:
            done+=1
        
    the_goal["status"]= "So far, you have completed {0} out of {1} steps".format(done, len(the_goal["steps"]))
    the_goal["is_done"] = False
    mongo.db[category].update({"_id":ObjectId(goal_id)},the_goal)
    
    return redirect(url_for("goal_details", category=category, goal_id=goal_id))
    
    
# --------------------------------add new goal----------------------------------
    
@app.route("/add_goal", methods=["GET", "POST"])
def add_goal():
    if request.method=="POST":

        form_values = request.form.to_dict()
        form_values["is_done"] = "is_done" in form_values
        category = form_values["category_name"]
        mongo.db[category].insert_one(form_values)
        return redirect("/goals")
    else:
        categories = mongo.db.Categories.find()
        return render_template("add_goal.html", categories=categories)


if __name__ == "__main__":
        app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)






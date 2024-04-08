from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)



app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myfirstdb.db"


db= SQLAlchemy(app)

class ContactUS(db.Model):
   id = db.Column(db.Integer, primary_key=True,autoincrement=True)
   Title = db.Column(db.String(141))
   Message = db.Column(db.Text)


with app.app_context():
   db.create_all()





@app.route("/aboutus")
def homepage():
  return render_template("aboutus.html")

@app.route("/")
def indexpage():
  return render_template("home.html")

@app.route("/groupsales")
def contactUs():
  return render_template("groupsales.html")

@app.route("/services")
def servicess():
   return render_template("services.html")

@app.route("/about")
def about():
   return render_template("about.html")

@app.route("/attractions")
def attractions():
   return render_template("attractions.html")

@app.route("/dining")
def dining():
   return render_template("dining.html")

@app.route("/meeting")
def meeting():
   return render_template("meeting.html")

@app.route("/photogallery")
def photogallery():
   return render_template("photogallery.html")

@app.route("/shoping")
def shoping():
   return render_template("shoping.html")

@app.route("/exterior")
def exterior():
   return render_template("exterior.html")

@app.route("/hotelfaclities")
def hotelfaclities():
   return render_template("hotelfaclities.html")

@app.route("/space")
def space():
   return render_template("space.html")

@app.route("/rooomssuits")
def roomssuits():
   return render_template("rooomssuits.html")



@app.route("/savethisdata", methods= ["post"])
def savethisdata():
   if request.method=="POST":
    NAME=request.form.get("title")
    ADDRESS=request.form.get("desc")
       
    data = ContactUS(Title = NAME,Message = ADDRESS)
    db.session.add(data)
    db.session.commit()
    return redirect("/services")
   
# @app.route("/deletethisdata/<x>",method =["[post]"])
# def deletethisdata(x):
#    return "your data saved------------------."




if __name__=="__main__":
    app.run(port=1000,debug=True)
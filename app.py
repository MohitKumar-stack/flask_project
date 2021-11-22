from flask import Flask,render_template,redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError
import flask
import flask_sqlalchemy
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False



db = SQLAlchemy(app)
class Todo(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   Email = db.Column(db.String(100))
   Password = db.Column(db.String(100))  

   def __repr__(self) -> str:
       return f"{self.Email} -{self.Password}"
  


@app.route("/",methods = ['POST','GET'])
def hello_world():
    # if flask.request.method == 'OST':
    username = flask.request.values.get('name') 
    password = flask.request.values.get('pass')
    todo =Todo(Email=username,Password =password )
    db.session.add(todo)
    db.session.commit()
    alldata =todo.query.all()
    return render_template("index.html" ,alldata= alldata)
        
@app.route("/delete/<int:number>")
def delete(number):
    delete_no =Todo.query.filter_by(id=number).first()
    db.session.delete(delete_no)
    db.session.commit()
    return redirect("/")

@app.route("/update/<int:number>") 
def update(number):
    pass


if __name__ =="__main__":
    app.run(debug=True)   
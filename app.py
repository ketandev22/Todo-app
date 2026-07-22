from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///task.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Todo(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(200),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

def __repr__(self)->str:
    return f"{self.sno}-{self.title}"


@app.route('/',methods=['GET','POST'])         #main endpoint
def hello_World():
    if request.method=='POST':
        title=request.form['title']
        desc=request.form['desc']
        toto=Todo(title=title,desc=desc)
        db.session.add(toto)
        db.session.commit()

    
    allTodo=Todo.query.all()
    return render_template("index.html",allTodo=allTodo)

@app.route('/info')
def information():
    return "Welcome to info page"


if __name__=="__main__":
    app.run(debug=True,port=8000)

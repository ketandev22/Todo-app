from flask import Flask,render_template,request,redirect
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
        return redirect("/")

    
    allTodo=Todo.query.all()
    return render_template("index.html",allTodo=allTodo)

@app.route('/delete/<int:sno>')                  #2nd Endpoint (delete)
def delete(sno):
    toto=Todo.query.filter_by(sno=sno).first()
    db.session.delete(toto)
    db.session.commit()
    return redirect("/")

@app.route('/update/<int:sno>',methods=['GET','POST'])         #3rd Endpoint (update)
def update(sno):
    toto=Todo.query.filter_by(sno=sno).first()
    if request.method=='POST':
        toto.title=request.form['title']
        toto.desc=request.form['desc']
        
        db.session.commit()
        return redirect("/")
    return render_template('update.html',toto=toto)


if __name__=="__main__":
    app.run(debug=True,port=8000)


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def xyz():
    return render_template("registration.html")
@app.route("/basicdetails",methods=['GET','POST'])
def abc():
    if(request.method=='POST'):
        name=request.form['n1']
        email=request.form['e1']
        phone=request.form['p1']
        course=request.form['c1']
        print(name,email,phone,course)
        return render_template("registration.html")
if __name__=="__main__":
    app.run()








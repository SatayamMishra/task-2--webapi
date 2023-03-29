from flask import Flask, render_template, request

import sqlite3 as sql

app =  Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def new_assistants():
    return render_template('assistants.html')

@app.route('/addrec',methods=['POST','GET'])
def addrec():
    if request.method == 'POST':
        try:
            id = request.form['id']
            native_english_speaker = request.form['native_english_speaker']
            course_instructor = request.form['course_instructor']
            course = request.form['course']
            semester = request.form['semester']
            class_size = request.form['class_size']
            performance_score = request.form['performance_score']
            
            with sql.connect("TA.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO TA (id, native_english_speaker, course_instructor, course, semester, class_size, performance_score) VALUES(?, ?, ?, ?, ?, ?, ?)",(id, native_english_speaker, course_instructor, course, semester, class_size, performance_score))
                con.commit()
                msg = "Record Successfully added"

        
        except:
            con.rollback()
            msg = "error in insert operation"
            

        finally:
            return render_template("result.html",msg=msg)
            con.close()
            
@app.route('/list')
def list():
    con = sql.connect('TA.db')
    con.row_factory = sql.Row
    cur = con.cursor()
    
    cur.execute("select * from TA")
    rows = cur.fetchall()
    
    return render_template("list.html",rows=rows)
     
            
if __name__ == '__main__':
    app.run(app.run('0.0.0.0', port=8586)) 
from flask import Flask, render_template, url_for, request, redirect
import pymysql.cursors

app = Flask(__name__)
#
# Coneccion a la base de datos
#
config = {'user':'root',
        'password':'helloworld',
        'host':'127.0.0.1',
        'database':'testapp',
        'cursorclass':pymysql.cursors.DictCursor}

@app.route('/', methods=['POST','GET'])
def index(): 
    if request.method == 'POST':
        if request.json and 'content' in request.json:
            task_content = request.json.get('content',"")
        else: 
            task_content = request.form['content'] 
        #
        try: 
            connection = pymysql.connect(**config)
            with connection.cursor() as cursor:
            # Crear una nueva tarea
                sql = "INSERT INTO tasks (content) VALUES (%s)"
                cursor.execute(sql, task_content)
                connection.commit()
                if request.json:
                    return "Recorded!"
                else: 
                    return redirect('/')  
        except: 
            return 'There was an issue adding your task' 
    else:
        try:
            connection = pymysql.connect(**config)
            with connection.cursor() as cursor:
                # Leer un registro de la base de datos
                sql = "SELECT * FROM tasks"
                cursor.execute(sql)
                tasks = cursor.fetchall()
            return render_template('index.html', tasks=tasks)
        except:
            return 'There was an showing tasks' 

@app.route('/delete/<int:id>', methods=['GET','DELETE'])
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete) 
        db.session.commit()
        if request.method == 'DELETE':
            return "Deleted!!"
        elif request.method == 'GET':
            return redirect('/')
        else:
            render_template('index.html', tasks=tasks)
    except:
        return "There was a problem deleting that task"

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id) 
    if request.method == 'POST':
        if request.json and 'content' in request.json:
            task.content = request.json.get('content', "")
        else:
            task.content = request.form['content'] 
        try: 
            db.session.commit()
            if request.json:
                return "Updated!"
            else:
                return redirect('/') 
        except: 
            return 'There was an issue updating your task' 
    else: 
        return render_template('update.html', task=task)


if __name__ == "__main__": 
    app.run(host='0.0.0.0',debug=True)

from flask import Flask, render_template, url_for, request, redirect
import pymysql.cursors

app = Flask(__name__)
#
# Coneccion a la base de datos
#
def getMysqlConnection():
    return pymysql.connect(host='db_mysql', user='root', port=3306, password='helloworld', database='testapp', cursorclass=pymysql.cursors.DictCursor)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        if request.json and 'content' in request.json:
            task_content = request.json.get('content',"")
        else:
            task_content = request.form['content']
        #
        try:
            connection = getMysqlConnection()
            with connection.cursor() as cursor:
            # Crear una nueva tarea
                sql = "INSERT INTO tasks (content) VALUES (%s)"
                cursor.execute(sql, task_content)
                connection.commit()
                connection.close()
                if request.json:
                    return "Recorded!"
                else:
                    return redirect('/')
        except:
            return 'There was an issue adding your task'
    else:
        try:
            connection = getMysqlConnection()
            with connection.cursor() as cursor:
                # Leer un registro de la base de datos
                sql = "SELECT * FROM tasks"
                cursor.execute(sql)
                tasks = cursor.fetchall()
                connection.close()
                return render_template('index.html', tasks=tasks)
        except Exception as e:
            print(e)
            return 'There was a problem showing the tasks '

@app.route('/delete/<int:id>', methods=['GET','DELETE'])
def delete(id):
    try:
        connection = getMysqlConnection()
        with connection.cursor() as cursor:
        # Borrar una tarea
            sql = "DELETE FROM tasks WHERE id = (%s)"
            cursor.execute(sql, id)
            connection.commit()
            connection.close()
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
    if request.method == 'POST':
        if request.json and 'content' in request.json:
            task_content = request.json.get('content', "")
        else:
            task_content = request.form['content']
        try:
            task_to_update = (task_content, id)
            connection = getMysqlConnection()
            with connection.cursor() as cursor:
            #Actualizar una tarea
                sql = "UPDATE tasks SET content = (%s) WHERE id = (%s)"
                cursor.execute(sql, task_to_update)
                connection.commit()
                connection.close()
            if request.json:
                return "Updated!"
            else:
                return redirect('/')
        except:
            return 'There was an issue updating your task'
    else:
        try:
            connection = getMysqlConnection()
            with connection.cursor() as cursor:
                sql = "SELECT * FROM tasks WHERE id = (%s)"
                cursor.execute(sql, task_id)
                task=cursor.fetchone()
                connection.close()
                return render_template('update.html', task=task)
        except:
            return 'There was an issue getting your task'


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000,debug=True)

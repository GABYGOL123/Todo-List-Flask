from flask import Flask, render_template, request

app = Flask(__name__)

todos = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        todo = request.form.get('todo')
        todos.append({'task': todo, 'completed': False})

    return render_template('index.html', todos=todos)


@app.route('/complete_all', methods=['POST'])
def complete_all():
    for todo in todos:
        todo['completed'] = True

    return render_template('index.html', todos=todos)


if __name__ == '__main__':
    app.run()

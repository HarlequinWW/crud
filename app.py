from flask import Flask, render_template, request, redirect, flash
from models import Todo, db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://harlequin:0000@192.168.56.101:22/crudv'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "StrengGeheim"

db.init_app(app)


@app.route('/')
def home():
    all_data = Todo.query.all()
    return render_template('index.html', notes=all_data)


@app.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        data = Todo(title, content)
        db.session.add(data)
        db.session.commit()

        flash("Done!")

        return redirect('/')


@app.route('/update/<id>/', methods=['POST'])
def update(id):
    #data = Todo.query.get(request.form.get('id'))
    data = Todo.query.get(id)
    data.title = request.form['title']
    data.content = request.form['content']

    db.session.commit()

    flash("Done!")

    return redirect('/')


@app.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    data = Todo.query.get(id)
    db.session.delete(data)
    db.session.commit()

    flash("Done!")

    return redirect('/')


with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)

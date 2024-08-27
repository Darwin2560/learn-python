from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    message = 'Hello, World!👋'
    return render_template('index.html', msm=message)

class Blog:
    def __init__(self, title, description):
        self.title = title
        self.description = description

@app.route('/blogs')
def blog():
    b1 = Blog(
        '¿Que es Python?',
        'Descripción de Blog 1'
    )

    b2 = Blog(
        '¿Que es Flask?',
        'Descripción de Blog 2'
    )

    blogs = [b1, b2]

    return render_template('blog.html', blogs=blogs)

@app.route('/greet/<name>')
def greet(name):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True) 

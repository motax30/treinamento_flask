from flask import (
    Flask, render_template, request,
)
from article_data import Articles
    
app = Flask(__name__)

Articles = Articles()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)

@app.route('/article/<int:id>/')
def display_article(id):       
    Article = list(
        filter(lambda article: article['id'] == id, Articles))[0]
    return render_template('article_detail.html', article=Article)

if __name__ == '__main__':
    app.run(debug=True)
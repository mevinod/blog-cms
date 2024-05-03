from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define your database models
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Post(id={self.id}, title='{self.title}', content='{self.content}')"

# Create the database tables within application context
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    # Fetch all posts from the database
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    # Fetch the post with the specified ID from the database
    post = Post.query.get_or_404(post_id)
    return render_template('post_detail.html', post=post)

@app.route('/enter_key', methods=['GET', 'POST'])
def enter_key():
    if request.method == 'POST':
        # Retrieve the key entered by the user
        entered_key = request.form.get('key')
        
        # Check if the entered key matches the expected key
        if entered_key == Config.SECRET_KEY:
            # Key is correct, store it in the session
            session['key_entered'] = entered_key
            return redirect(url_for('create_post'))
        else:
            # Key is incorrect, display an error message
            flash('Invalid key. Please enter the correct key.', 'error')
            return redirect(url_for('enter_key'))
    
    return render_template('enter_key.html')

@app.route('/create', methods=['GET', 'POST'])
def create_post():
    # Check if the user has entered the correct key
    entered_key = session.get('key_entered')
    if not entered_key or entered_key != Config.SECRET_KEY:
        flash('Please enter the key first.', 'error')
        return redirect(url_for('enter_key'))

    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        # Check if title and content are provided
        if not title or not content:
            flash('Title and content are required.', 'error')
            return redirect(url_for('create_post'))
        # Create a new post object
        new_post = Post(title=title, content=content)
        
        # Add the new post to the database
        db.session.add(new_post)
        db.session.commit()
        
        flash('Post created successfully!', 'success')
        return redirect(url_for('home'))
    
    return render_template('create_post.html')

if __name__ == '__main__':
    app.run(debug=True)

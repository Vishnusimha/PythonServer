from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

# SQLAlchemy Model for Posts
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    is_approved = db.Column(db.Boolean, default=False)
    likes = db.Column(db.Integer, default=0)

# SQLAlchemy Model for Comments
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    post = db.relationship('Post', backref=db.backref('comments', lazy=True))

# Route for Posting Anonymously
@app.route('/post', methods=['POST'])
def create_post():
    with app.app_context():
        content = request.json.get('content')
        if not content:
            return jsonify({'error': 'Content is required'}), 400
        
        post = Post(content=content)
        db.session.add(post)
        db.session.commit()
        
        return jsonify({'message': 'Post submitted successfully!'})

# Route for Adding Comments to a Post
@app.route('/post/<int:post_id>/comment', methods=['POST'])
def add_comment(post_id):
    with app.app_context():
        post = Post.query.get_or_404(post_id)
        content = request.json.get('content')
        if not content:
            return jsonify({'error': 'Content is required'}), 400
        
        comment = Comment(content=content, post=post)
        db.session.add(comment)
        db.session.commit()
        
        return jsonify({'message': 'Comment added successfully!'})

# Route for Fetching Comments for a Post
@app.route('/post/<int:post_id>/comments', methods=['GET'])
def get_comments(post_id):
    with app.app_context():
        post = Post.query.get_or_404(post_id)
        comments = [{'id': comment.id, 'content': comment.content} for comment in post.comments]
        return jsonify({'comments': comments})

# Route for Liking a Post
@app.route('/post/<int:post_id>/like', methods=['POST'])
def like_post(post_id):
    with app.app_context():
        post = Post.query.get_or_404(post_id)
        post.likes += 1
        db.session.commit()
        return jsonify({'message': 'Post liked successfully!'})

# Route for Disliking a Post
@app.route('/post/<int:post_id>/dislike', methods=['POST'])
def dislike_post(post_id):
    with app.app_context():
        post = Post.query.get_or_404(post_id)
        if post.likes > 0:
            post.likes -= 1
            db.session.commit()
            return jsonify({'message': 'Post disliked successfully!'})
        else:
            return jsonify({'error': 'Post has no likes to dislike!'})
        
# Route for Getting Number of Likes for a Post
@app.route('/post/<int:post_id>/likes', methods=['GET'])
def get_post_likes(post_id):
    with app.app_context():
        post = Post.query.get_or_404(post_id)
        return jsonify({'likes': post.likes})
    
# Route for Deleting All Posts
@app.route('/posts', methods=['DELETE'])
def delete_all_posts():
    with app.app_context():
        Post.query.delete()
        db.session.commit()
        return jsonify({'message': 'All posts deleted successfully!'})

# Route for Deleting All Comments
@app.route('/comments', methods=['DELETE'])
def delete_all_comments():
    with app.app_context():
        Comment.query.delete()
        db.session.commit()
        return jsonify({'message': 'All comments deleted successfully!'})
    
# Route for Deleting Comments for a Specific Post
@app.route('/post/<int:post_id>/comments', methods=['DELETE'])
def delete_comments_for_post(post_id):
    with app.app_context():
        post = Post.query.get_or_404(post_id)
        Comment.query.filter_by(post_id=post_id).delete()
        db.session.commit()
        return jsonify({'message': f'All comments for post {post_id} deleted successfully!'})

# Route for Getting All Posts with Associated Comments
@app.route('/posts', methods=['GET'])
def get_all_posts_with_comments():
    with app.app_context():
        posts = Post.query.all()
        formatted_posts = []
        
        for post in posts:
            post_data = {
                'id': post.id,
                'content': post.content,
                'likes': post.likes,
                'comments': [{'id': comment.id, 'content': comment.content} for comment in post.comments]
            }
            formatted_posts.append(post_data)
        
        return jsonify({'posts': formatted_posts})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

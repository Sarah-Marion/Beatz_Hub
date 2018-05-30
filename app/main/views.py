from flask import render_template, request, redirect, url_for, flash, abort
from . import main
from flask_admin.contrib.sqla import ModelView
from flask_login import login_required, current_user
from . forms import PostForm, CommentForm, SubscribersForm
from ..import db, basic_auth
import markdown2
from ..models import User, Post, Role, Comment, Subscribers
from datetime import datetime



@main.route('/')
def index():
    title = 'Home | Beats Hub'

    return render_template('index.html', title=title)



@main.route('/profile/<username>')
@login_required

def profile(username):
    
    user = User.query.filter_by(username = username).first_or_404()
    title = "Profile"       
    return render_template('profile.html' , user=user,title=title)

@main.route('/post', methods=['GET', 'POST'])
def post():
    all = Post.query.all()
    all.reverse()
    print(all)

    Comments = CommentForm()
    if Comments.validate_on_submit():
        comment = Comment(comment = Comments.comment.data, commenter = Comments.commenter.data)
        db.session.add(comment)
        db.session.commit()
        print(comment)
        return redirect(url_for('main.post'))

    allcomments = Comment.query.all()
    title = "Post Article"
    Blog = PostForm()
  
    if Blog.validate_on_submit():
        post = Post( title = Blog.title.data ,post = Blog.Entry.data, user_id = current_user.id, timeposted = datetime.utcnow() )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.post'))
 
    return render_template('post.html', Post = Blog, title = title, posts = all, comment = Comments, allcomments = allcomments)



@main.route('/post/<id>', methods=['POST','GET'])
def fullpost(id):
    
    title= f'Posts' 
    post = Post.query.filter_by(id=id).first()
    Comments = CommentForm()
    if Comments.validate_on_submit():
        comment = Comment(comment = Comments.comment.data, post_id=id, commenter = Comments.commenter.data)
        db.session.add(comment)
        db.session.commit()
        print(comment)
        return redirect(url_for('main.fullpost', id=post.id))
    allcomments = Comment.query.all()
    postcomments = Comment.query.filter_by(post_id=id).all()
     

    return render_template('fullpost.html', title = title, post = post, comment = Comments, allcomments = allcomments, postcomments = postcomments)

            

@main.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?, (id,)')
    db.commit()
    return redirect(url_for('main.index'))
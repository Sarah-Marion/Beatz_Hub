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
    title = 'Home | Beatz Hub'

    return render_template('index.html', title=title)

@main.route('/home/', methods = ['GET', 'POST'])
@login_required
def home():
    all_posts = Post.get_all_posts()
    all_posts.reverse()

    title = 'Home | Beatz Hub'    
    return render_template('home.html', title = title, posts = all_posts)

@main.route('/create/', methods = ['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    letter = 0
    
    if form.validate_on_submit():
        title_data = form.title.data
        post_data = form.Entry.data
        video_data = form.youtube.data
        if video_data:
            # video_data = video_data.split('')
            while letter < len(video_data):
                if video_data[letter] == '=':
                    new_word = video_data[letter+1:letter+12]
                    letter += 1
                    continue
                else:
                    letter +=1
                    continue
            
            new_post = Post(title=title_data, post = post_data, user_id = current_user.id, group = current_user.group, image_url=new_word, timeposted = datetime.now())
        else:
            new_post = Post(title=title_data, post = post_data, user_id = current_user.id, group = current_user.group, timeposted = datetime.now())
            
        new_post.save_post()

        return redirect(url_for('main.home'))
    
    return render_template('create_posts.html', title='Create Post', post_form = form)

# @main.route('/post/', methods=['GET', 'POST'])
# def post():
#     all = Post.query.all()
#     all.reverse()
#     print(all)

#     Comments = CommentForm()
#     if Comments.validate_on_submit():
#         comment = Comment(comment = Comments.comment.data, commenter = Comments.commenter.data)
#         db.session.add(comment)
#         db.session.commit()
#         print(comment)
#         return redirect(url_for('main.post'))

#     allcomments = Comment.query.all()
#     title = "Post Article"
#     Blog = PostForm()
  
#     if Blog.validate_on_submit():
#         post = Post( title = Blog.title.data ,post = Blog.Entry.data, user_id = current_user.id, timeposted = datetime.utcnow() )
#         db.session.add(post)
#         db.session.commit()
#         return redirect(url_for('main.post'))
 
#     return render_template('post.html', Post = Blog, title = title, posts = all, comment = Comments, allcomments = allcomments)


@main.route('/post/<int:id>', methods=['POST','GET'])
def fullpost(id):
    
    title= f'Posts' 
    post = Post.get_post(id)
    Comments = CommentForm()

    if Comments.validate_on_submit():
        comment = Comment(comment = Comments.comment.data, commenter = Comments.commenter.data, post_id=id)
        db.session.add(comment)
        db.session.commit()

        return redirect(url_for('main.fullpost', id=post.id))

    postcomments = Comment.get_post_comments(id)
     

    return render_template('fullpost.html', title = title, post = post, comment = Comments, postcomments = postcomments)

@main.route('/<group>/')
def category(group):
    posts = Post.get_post_category(group)
    posts.reverse()

    return render_template('posts.html', title=f'{group}', posts = posts)

@main.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?, (id,)')
    db.commit()
    return redirect(url_for('main.index'))

@main.route('/profile/<username>')
def profile(username):
    
    user = User.query.filter_by(username = username).first_or_404()
    title = f"{username} Profile"
    return render_template('profile/profile.html' , user=user,title=title)

@main.route('/profile/<uname>/update', methods=['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    
    update_form = UpdateProfile()

    if update_form.validate_on_submit():
        user.bio = update_form.bio.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname = user.username,id_user=user.id))
    title = 'Update Bio'
    return render_template('profile/update.html', form=update_form, title = title)

@main.route('/profile/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        # user_photo = PhotoProfile(pic_path = path,user = user)
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname,id_user=current_user.id))
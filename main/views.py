from flask import Blueprint, render_template, request
from posts_dao import PostsDAO
from constanse import PATH_POSTS, PATH_COMMENTS

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

posts_dao_main = PostsDAO(PATH_POSTS, PATH_COMMENTS)


@main_blueprint.route('/')
def main_page():
    posts = posts_dao_main.get_all()
    return render_template('index.html', posts=posts)


@main_blueprint.route('/posts/<int:post_pk>')
def get_post_by_id(post_pk):
    post = posts_dao_main.get_by_pk(post_pk)
    comments = posts_dao_main.get_comments_by_post_id(post_pk)
    return render_template('post.html', post=post, comments=comments)


@main_blueprint.route('/search')
def search_page():
    key_search = request.args.get("s")
    posts = posts_dao_main.search_for_content(key_search)
    return render_template('search.html', posts=posts, key_search=key_search)


@main_blueprint.route('/users/<user_name>')
def get_post_by_user(user_name):
    posts = posts_dao_main.get_by_user(user_name)
    return render_template('user-feed.html', user_name=user_name, posts=posts)


@main_blueprint.route('/tag/<tag_name>')
def get_post_by_tag(tag_name):
    posts = posts_dao_main.get_by_tag(tag_name)
    return render_template('tag.html', tag_name=tag_name, posts=posts)

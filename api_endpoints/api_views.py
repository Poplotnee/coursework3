from flask import Blueprint, jsonify
from posts_dao import PostsDAO
import logging

posts_dao_api = PostsDAO()

api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/api/posts')
def get_api_posts():
    logging.info('Request  for a list of posts')
    result = posts_dao_api.get_all()
    return jsonify(result)


@api_blueprint.route('/api/posts/<int:post_pk>')
def get_api_post(post_pk):
    logging.info(f'Request for post id: {post_pk}')
    result = posts_dao_api.get_by_pk(post_pk)
    return jsonify(result)

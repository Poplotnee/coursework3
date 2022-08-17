from DAO.posts_dao import PostsDAO

import pytest

from constanse import PATH_POSTS_TEST, PATH_COMMENTS_TEST


@pytest.fixture()
def posts_dao():
    posts_dao_instance = PostsDAO(PATH_POSTS_TEST, PATH_COMMENTS_TEST)
    return posts_dao_instance


post_keys_should_be = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}
comments_keys_should_be = {"post_id", "commenter_name", "comment", "pk"}


class TestPostDao:

    def test_get_all(self, posts_dao):
        """ Проверяем, верный ли список кандидатов возвращается """
        posts = posts_dao.get_all()
        assert type(posts) == list, "возвращается не список"
        assert len(posts) > 0, "возвращается пустой список"
        assert set(posts[0].keys()) == post_keys_should_be, "неверный список ключей"

    def test_get_by_user(self, posts_dao):
        posts = posts_dao.get_by_user('leo')
        assert type(posts) == list, "возвращается не список"
        assert (posts[0]['poster_name'] == 'leo'), "возвращается неправильный пользователь"
        assert set(posts[0].keys()) == post_keys_should_be, "неверный список ключей"

    def test_search_for_content(self, posts_dao):
        posts = posts_dao.search_for_content('Мне казалось')
        assert type(posts) == list, "возвращается не список"
        assert (posts[0]['poster_name'] == 'leo'), "возвращается неправильный пользователь"
        assert set(posts[0].keys()) == post_keys_should_be, "неверный список ключей"

    def test_get_by_pk(self, posts_dao):
        post = posts_dao.get_by_pk(1)
        assert type(post) == dict, "возвращается не словарь"
        assert post['poster_name'] == 'leo', "возвращается неправильный кандидат"
        assert set(post.keys()) == post_keys_should_be, "неверный список ключей"

    def test_get_comments_by_post_id(self, posts_dao):
        comments = posts_dao.get_comments_by_post_id(1)
        assert type(comments) == list, "возвращается не список"
        assert comments[0]["commenter_name"] == "hanna", "возвращается неправильный пользователь"
        assert set(comments[0].keys()) == comments_keys_should_be, "неверный список ключей"

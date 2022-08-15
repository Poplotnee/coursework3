from posts_dao import PostsDAO

import pytest


@pytest.fixture()
def posts_dao():
    posts_dao_instance = PostsDAO()
    print(posts_dao_instance)
    return posts_dao_instance


keys_should_be = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}


class TestPostDao:

    def test_get_all(self, posts_dao):
        """ Проверяем, верный ли список кандидатов возвращается """
        posts = posts_dao.get_all()
        assert type(posts) == list, "возвращается не список"
        assert len(posts) > 0, "возвращается пустой список"
        assert set(posts[0].keys()) == keys_should_be, "неверный список ключей"

    def test_get_by_user(self, posts_dao):
        posts = posts_dao.get_by_user('leo')
        assert type(posts) == list, "возвращается не список"
        assert (posts[0]['poster_name'] == 'leo'), "возвращается неправильный кандидат"
        assert set(posts[0].keys()) == keys_should_be, "неверный список ключей"

    def test_search_for_content(self, posts_dao):
        posts = posts_dao.search_for_content('Мне казалось')
        assert type(posts) == list, "возвращается не список"
        assert (posts[0]['poster_name'] == 'leo'), "возвращается неправильный кандидат"
        assert set(posts[0].keys()) == keys_should_be, "неверный список ключей"

    def test_get_by_pk(self, posts_dao):
        """ Проверяем, верный ли кандидат возвращается при запросе по пк """
        posts = posts_dao.test_get_by_pk(1)
        assert type(posts) == list, "возвращается не список"
        assert (posts[0]['poster_name'] == 'leo'), "возвращается неправильный кандидат"
        assert set(posts[0].keys()) == keys_should_be, "неверный список ключей"

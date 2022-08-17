import pytest
from app import app

keys_should_be = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}

def test_all():
    response = app.test_client().get('/api/posts')
    print(type(response.json))

def test_app_all_posts():
    '''Тестируем API всех постов'''
    response = app.test_client().get('/api/posts')
    assert isinstance(response.json.get, list), 'Возвращает не список'
    assert response.json[0].keys() == keys_should_be, 'Неверный список ключей'


def test_app_one_post():
    '''Тестируем API одного поста'''
    response = app.test_client().get('/api/posts/1')
    assert isinstance(response.json.get, dict), 'Возвращает не словарь'
    assert response.json.keys() == keys_should_be, 'Неверный список ключей'


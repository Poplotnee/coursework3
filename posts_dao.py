from flask import json


class PostsDAO:

    def get_all(self) -> list:
        '''Возвращает все посты'''
        with open(r'C:\Users\Евгений\PycharmProjects\coursework2_source\data\data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data

    def get_by_user(self, user_name: str) -> list:
        '''Получает имя пользователя, возвращает все посты пользователя'''
        user_post_list = []
        is_there_such_a_user = False
        for post in self.get_all():
            if post['poster_name'].lower() == user_name.lower():
                user_post_list.append(post)
                is_there_such_a_user = True
        if is_there_such_a_user == False:
            raise ValueError('Нет такого пользователя')
        return user_post_list

    def search_for_content(self, query: str) -> list:
        '''Получает набор символов, возвращает все посты содержащие этот набор'''
        query_post_list = []
        for post in self.get_all():
            if query.lower() in post['content'].lower():
                query_post_list.append(post)
        return query_post_list

    def get_by_pk(self, pk: int) -> dict:
        '''Получает номер в виде целого числа, возвращает пост под этим номером'''
        for post in self.get_all():
            if pk == post['pk']:
                return post

    def get_comments_by_post_id(self, post_id: int) -> list:
        '''Получает номер в виде целого числа, возвращает коментарии под этим номером'''
        with open('data/comments.json', 'r', encoding='utf-8') as file:
            comments_list = json.load(file)
            list_comments_by_post_id = []
            is_there_such_a_post = False
            for comment in comments_list:
                if post_id == comment['post_id']:
                    list_comments_by_post_id.append(comment)
                    is_there_such_a_post = True
            if is_there_such_a_post == False:
                raise ValueError('Нет такого поста')
            return list_comments_by_post_id

    def get_by_tag(self, tag: str) -> list:
        '''Получает тэг, возвращает лист постов с таким же тэгом'''
        for post in self.get_all():
            tag_post_list = []
            if tag in post['content']:
                tag_post_list.append(post)
            return tag_post_list

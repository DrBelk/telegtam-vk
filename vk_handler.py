import vk_api
import random
import string

from error_codes import *

class vk_handler:
    success_login = False
    def login(self, email, password):
        vk_session = vk_api.VkApi(email, password)
        try:
            vk_session.auth(token_only=True)
        except vk_api.AuthError as error_msg:
            print(error_msg)
            return VK_LOGIN_ERROR
        vk = vk_session.get_api()
        success_login = True
        return VK_OK

def test():
    my_user_id = 120276081
    
    won = False
    while (not won):
        get_response = vk.wall.getComments(post_id = 345936, 
                                           owner_id = -26558787, 
                                           sort = 'desc',
                                           count = 1)

        if get_response['items']:
            print ('Последний комментарий от пользователя №',
                   get_response['items'][0]['from_id'],
                   'от', get_response['items'][0]['date'],
                   'гласит:', get_response['items'][0]['text'])

        if get_response['items'][0]['from_id'] != my_user_id:
            create_response = vk.wall.createComment(post_id = 345936, 
                                                    owner_id = -26558787, 
                                                    message = message())

            if create_response['comment_id']:
                print('Comment created, id is', create_response['comment_id'])

            get_response = vk.wall.getComments(post_id = 345936, 
                                               owner_id = -26558787, 
                                               sort = 'desc',
                                               count = 1)

            if get_response['items']:
                print ('Последний комментарий от пользователя №', 
                       get_response['items'][0]['from_id'],
                       'от', get_response['items'][0]['date'],
                       'гласит:', get_response['items'][0]['text'])

            print ('Сплю 45 минут') 
            time.sleep(45 * 60)
        else:
            print ('Сплю 16 минут')
            time.sleep(16 * 60)
            get_response = vk.wall.getComments(post_id = 345936, 
                                               owner_id = -26558787, 
                                               sort = 'desc',
                                               count = 1)
            if get_response['items']:
                print ('Последний комментарий от пользователя №', 
                       get_response['items'][0]['from_id'],
                       'от', get_response['items'][0]['date'],
                       'гласит:', get_response['items'][0]['text'])

            if get_response['items'][0]['from_id'] == my_user_id:
                won = True

    print ('Я выиграль!!')
    create_response = vk.wall.createComment(post_id = 345936, 
                                            owner_id = -26558787, 
                                            message = 'уряяя')

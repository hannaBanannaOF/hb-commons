from social_core.backends.oauth import BaseOAuth2
from django.conf import settings

class HannaBanannaOAuth2(BaseOAuth2):
    """Personalized OAuth authentication backend"""
    name = 'hannabananna'
    defaultUrl = settings.HANNABANNA_AUTH_URL
    AUTHORIZATION_URL = '{0}/authorize/'.format(defaultUrl)
    ACCESS_TOKEN_URL = '{0}/o/token/'.format(defaultUrl)
    ACCESS_TOKEN_METHOD = 'POST'
    EXTRA_DATA = [
        ('id', 'id'),
        ('email', 'email'),
        ('nickname', 'nickname'),
        ('first_name', 'first_name'),
        ('last_name', 'last_name'),
        ('photo', 'photo')
    ]
    def get_user_details(self, response):
        return {
            'id': response.get('id'),
            'email': response.get('email'),
            'nickname': response.get('username') or '',
            'first_name': response.get('first_name') or '',
            'last_name': response.get('last_name') or '',
            'photo': response.get('photo') or ''
            }

    def user_data(self, access_token, *args, **kwargs):
        return self.get_json('{0}/user/'.format(self.defaultUrl), headers={'Authorization': 'Bearer %s' % access_token})
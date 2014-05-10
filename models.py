# -*- coding: utf-8 -*-

from hashlib import md5


class Mentee(object):
    """
    Member object for Mentee
    """

    def __init__(self, config, gen):
        # get info
        self.name = config.get('info', 'name')
        self.birth = config.get('info', 'birth')
        self.gen = gen
        if config.has_option('info', 'email'):
            self.email = config.get('info', 'email')
        else:
            self.email = None

        if self.email:  # email could be hashed by md5
            self.hashed_email = md5(self.email).hexdigest()
        else:
            self.hashed_email = config.get('info', 'hashed_email')
        self.sex = config.get('info', 'sex')

        # get social
        socials = ['twitter', 'facebook', 'github']
        for social in socials:
            self.__setattr__(social, config.get('social', social) if config.has_option('social', social) else None)

        # validate object
        self.validate()

    def validate(self):
        if not self.name:
            raise NotValidValueError('Not valid name')

        if not self.birth:
            raise NotValidValueError('Not valid birth')

        if not self.hashed_email:
            raise NotValidValueError('Not valid email or hashed one')

        if not self.sex in ['male', 'female']:
            raise NotValidValueError('Not valid sex')


class NotValidValueError(Exception):
    """
    Exception raised when name was not valid.
    """

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return str(self.msg)
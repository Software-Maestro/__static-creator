# -*- coding: utf-8 -*-

from models import Mentee, NotValidValueError
from ConfigParser import RawConfigParser, ConfigParser
from os import listdir
from os.path import join, isfile, isdir
import codecs

from jinja2 import Template, FileSystemLoader, Environment
env = Environment(loader=FileSystemLoader(searchpath='theme/'))


def get_mentee():
    path = './member/mentee'
    mentee_list = []

    for class_name in listdir(path):
        class_path = join(path, class_name)
        if isdir(class_path):
            for mentee_name in listdir(class_path):
                mentee_path = join(class_path, mentee_name)
                if isfile(mentee_path):
                    config = ConfigParser()
                    config.read(mentee_path)
                    mentee = Mentee(config=config)
                    mentee.gen = class_name
                    mentee_list.append(mentee)

    print '%s mentee collected.' % len(mentee_list)
    return mentee_list


def generate_html_mentee():
    mentee_list = get_mentee()

    template = env.get_template('mentee.html')

    with codecs.open('./output/mentee.html', mode='w', encoding='utf-8') as fp:
        fp.write(template.render(members=mentee_list))

    print './output/mentee.html was generated.'


def get_mentor():
    path = './member/mentor'
    mentor_list = []

    print '%s mentor collected.' % len(mentor_list)
    return mentor_list


def generate_html_mentor():
    mentor_list = get_mentor()


def generate_html_index():
    pass


def generate_html():
    generate_html_index()
    generate_html_mentee()
    generate_html_mentor()


if __name__ == '__main__':
    generate_html()
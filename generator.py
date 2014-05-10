# -*- coding: utf-8 -*-

from models import Mentee
from ConfigParser import ConfigParser
from os import listdir
from os.path import join, isfile, isdir
import codecs

from jinja2 import FileSystemLoader, Environment
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
                    mentee = Mentee(config=config, gen=class_name)
                    mentee_list.append(mentee)

    print '%s mentee collected.' % len(mentee_list)
    return mentee_list


def generate_html_mentee():
    mentee_list = get_mentee()

    template = env.get_template('mentee.html')

    with codecs.open('./output/mentee.html', mode='w', encoding='utf-8') as fp:
        fp.write(template.render(members=mentee_list))

    print './output/mentee.html was generated.'

    return len(mentee_list)


def get_mentor():
    path = './member/mentor'
    mentor_list = []

    print '%s mentor collected.' % len(mentor_list)
    return mentor_list


def generate_html_mentor():
    mentor_list = get_mentor()

    return len(mentor_list)


def generate_html_index(count):

    template = env.get_template('index.html')

    with codecs.open('./output/index.html', mode='w', encoding='utf-8') as fp:
        fp.write(template.render(count=count))

    print './output/index.html was generated.'


def generate_html():
    mentee_count = generate_html_mentee()
    mentor_count = generate_html_mentor()
    generate_html_index(mentor_count + mentee_count)


if __name__ == '__main__':
    generate_html()
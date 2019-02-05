import os
import json
from datetime import datetime
from django.core.management import BaseCommand
from django.contrib.auth.models import User
from blogapi.blog.models import Author, Post


class Command(BaseCommand):

    help = 'Import a set of posts (in json format) to the database'

    def add_arguments(self, parser):
        parser.add_argument('directory', type=str, help='Directory in which the json files reside')
        parser.add_argument('user', type=str, help='The user that should be set as the author of the posts')

    def handle(self, *args, **kwargs):
        directory = kwargs['directory']
        user = kwargs['user']


        if not os.path.isdir(directory):
            return f'{input_dir} is not a directory'

        user = User.objects.get(username='antoine')
        author = Author.objects.get(user=user)

        for filename in os.listdir(directory):
            with open(os.path.join(directory, filename), 'r') as fd:
                post = json.load(fd)
                date = datetime.strptime(post['date'], '%Y-%m-%d %H:%M:%S')
                Post.objects.create(author=author,
                                    title=post['title'],
                                    content=post['content'],
                                    state='D',
                                    published_date=date)

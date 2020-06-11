#!/usr/bin/env python3
# -*-coding: utf8-*-

import orm
import asyncio
from models import User

loop = asyncio.get_event_loop()


async def test():
    await orm.create_pool(loop=loop, user='root', password='123456', db='awesome')

    u = User(name='Bart', email='John@google.com', passwd='1234567890', image='about:blank')

    await u.save()
    # lst = await User.findAll()
    # print(lst[0].get('id'))
# loop.run_until_complete(test())


class Chain:
    def __init__(self, path=''):
        print('__init__:', path)
        self._path = path

    def __getattr__(self, path):
        print('__getattr__:', path)
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


Chain().status.user.timeline.list

#/usr/bin/env python3

# -*- coding:utf-8 -*-

import requests

wiki_url = 'https://wiki.cheatengine.org/index.php?title=Lua'

res = requests.request('GET', wiki_url)

print(res.content)
"""
The MIT License (MIT)

Copyright (c) 2021-present boobfuck

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
import itertools

import aiohttp

from .errors import *
from .models import *

async def text_or_json(response):
    if response.headers['content-type'] == 'text/html':
        return await response.text(encoding='utf-8')
    else:
        return await response.json()

class Route:
    BASE = 'https://eporner.com/api/v2'

    def __init__(self, method, path):
        self.method = method
        self.path = path
        self.url = self.BASE + path

class HTTP:
    
    def __init__(self):
        self.user_agent = 'eporner.py (https://github.com/boobfuck/eporner.py)'
        headers = {
            'User-Agent': self.user_agent
        }
        self._session = aiohttp.ClientSession(headers=headers)

    def parse_removed(self, data):
        if data == []:
            raise NoResults('No results found')

        return data

    def parse_ids(self, data):
        if data == []:
            raise NoResults('No results found.')

        dthumb = data.get('default_thumb')
        thumbs_list = []
        thumbs = data.get('thumbs')
        for thumb in thumbs:
            thumbs_list.append(
                Thumbnail(
                    size=thumb.get('size'),
                    width=thumb.get('width'),
                    height=thumb.get('height'),
                    src=thumb.get('src')
                )
            )

        return Video(
            id=data.get('id'),
            title=data.get('title'),
            tags=data.get('keywords').split(', '),
            views=data.get('views'),
            rate=data.get('rate'),
            url=data.get('url'),
            added=data.get('added'),
            length_sec=data.get('length_sec'),
            length=data.get('length_min'),
            embed_url=data.get('embed'),
            default_thumb=Thumbnail(
                size=dthumb.get('size'),
                width=dthumb.get('width'),
                height=dthumb.get('height'),
                src=dthumb.get('src')
            ),
            thumbs=thumbs_list
        )

    def parse_videos(self, data):
        videos_list = []
        thumbs_list = []
        datas = data.get('videos')
        dthumbs = [data['default_thumb'] for data in datas]
        thumbs = [data['thumbs'] for data in datas]
        
        for thumb in itertools.chain.from_iterable(thumbs):
            thumbs_list.append(
                Thumbnail(
                    size=thumb.get('size'),
                    width=thumb.get('width'),
                    height=thumb.get('height'),
                    src=thumb.get('src')
                )
            )

        for data, dthumb in zip(datas, dthumbs):
            videos_list.append(
                Video(
                    id=data.get('id'),
                    title=data.get('title'),
                    tags=data.get('keywords').strip(', '),
                    views=data.get('views'),
                    rate=data.get('rate'),
                    url=data.get('url'),
                    added=data.get('added'),
                    length_sec=data.get('length_sec'),
                    length=data.get('length_min'),
                    embed_url=data.get('embed'),
                    default_thumb=Thumbnail(
                        size=dthumb.get('size'),
                        width=dthumb.get('width'),
                        height=dthumb.get('height'),
                        src=dthumb.get('src')
                        ),
                    thumbs=thumbs_list
                )
            )
        return videos_list

    def parse_result(self, data):
        if data.get('count') == 0:
            raise NoResults('No resuls found.')

        return Result(
            count=data.get('count'),
            current_page=data.get('page'),
            total_count=data.get('total_count'),
            total_pages=data.get('total_pages'),
            videos=self.parse_videos(data)
        )

    async def request(self, route, **kwargs):
        method = route.method
        url = route.url

        async with self._session.request(method, url, **kwargs) as response:
            data = await text_or_json(response)

            if response.status == 200:
                return data
            else:
                raise HTTPException(response, data)

    def search_videos(self, **kwargs):
        return self.request(Route('GET', '/video/search/'), **kwargs)

    def search_id(self, **kwargs):
        return self.request(Route('GET', '/video/id/'), **kwargs)

    def search_removed(self, **kwargs):
        return self.request(Route('GET', '/video/removed/'), **kwargs)

    async def close(self):
        await self._session.close()


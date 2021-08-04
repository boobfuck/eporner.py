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

from __future__ import annotations

import asyncio

from .http import *
from .enums import *

class Client:
    def __init__(self) -> None:
        self.http = HTTP()

    async def get_videos(
        self,
        query: str,
        *,
        per_page: int = 30,
        page: int = 1,
        thumbsize: Thumbsize = Thumbsize.medium,
        order: Order = Order.latest,
        gay_content: GayContent = GayContent.none,
        low_quality: LowQuality = LowQuality.include
    ) -> Result:
        """
        Gets the videos.

        ### Parameters
        query (str) - The search query. Special value "all" can be passed to query for all videos.
        per_page (int) - Limits the number of results per page. Valid range is 1 - 1000. Default: 30.
        page (int) - The results page number. Valid range is 1 - 1000000, but no more than ``total_pages`` received in response. Default: 1.
        thumbsize (Thumbsize) - The thumbail size. Default: ``Thumbsize.medium``.
        order (Order) - How results should be sorted. Default: ``Order.latest```.
        gay_content (GayContent) - Whether to include gay content or not. Default ``GayContent.none``.
        low_quality (LowQuality) - Whether to include low quality content or not. Default: ``LowQuality.include``.
        """

        params = {
            'query': query,
            'per_page': per_page,
            'page': page,
            'thumbsize': thumbsize.value,
            'order': order.value,
            'gay': gay_content.value,
            'lq': low_quality.value
        }

        data = await self.http.search_videos(params=params)
        return self.http.parse_result(data)

    async def get_id(self, id: str) -> Video:
        """
        Gets a video by it's unique ID.

        ### Parameters
        id (str) - The unique video ID.
        """

        params = {
            'id': id
        }
        data = await self.http.search_id(params=params)
        return self.http.parse_ids(data)

    # This current does not work.
    # I have contacted the API team for info.
    # Will update once I get a response, for
    # now, this method will stay.
    async def get_removed(self) -> list[str]:
        """
        Returns results for all removed IDs.
        """

        params = {
            'format': 'txt'
        }
        data = await self.http.search_removed(params=params)
        return self.http.parse_removed(data)

    def close(self) -> None:
        """Closes the internal client session."""
        asyncio.create_task(self.http.close())

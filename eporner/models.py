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

import datetime
from dataclasses import dataclass

@dataclass
class Result:
    """
    The result of the query.
    ### Attributes
    count (int) - The number of videos returned on current result page.
    current_page (int) - The urrent result page number.
    total_count (int) -The total number of all videos found matching your criteria.
    total_pages (int) - The total number of pages with all results matching your criteria assuming current ``per_page`` value.
    videos (list) - A list of ``Video`` objects.
    """
    count: int
    current_page: int
    total_count: int
    total_pages: int
    videos: list

@dataclass
class Thumbnail:
    """
    The thumbnail information.

    ### Atrributes
    size (str) - The thumbnail size: big, medium, small.
    width (int) - The width of the thumbnail.
    height (int) - The height of the thumbnail.
    src (str) - The url of the thumbnail.
    """
    # TODO: Rename src to url?
    size: str
    width: int
    height: int
    src: str

@dataclass
class Video:
    """
    id (in) - Unique ID of the video.
    title (str) - The video title.
    tags (list) - The tags assigned to the video.
    views (int) - The Estimated number of video views.
    rate (float) - The video rate. Valid range is ``0.00`` to ``5.00``.
    url (str) - The URL of the video on Eporner.
    added (str) - The date of the video added on Eporner.
    length_sec (int) - The video length in seconds.
    length (str) - The video length in ``mm:ss`` format or ``hh:mm:ss`` format if video longer than 60 minutes.
    embed_url (str) - The embed url of the video.
    default_thumb (Thumbnail) - The video's default thumbnail information.
    thumbs (list) - A list of ``Thumbnail`` objects.
    """
    id: str
    title: str
    tags: list
    views: int
    rate: float
    url: str
    added: str
    length_sec: int
    length: str
    embed_url: str
    default_thumb: Thumbnail
    thumbs: list

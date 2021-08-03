# API Reference

## Client

### Client
*class* `eporner.Client`   
The client for getting results from the API.

### Methods
*async def* `get_videos(query, *, per_page=30, page=1, thumbsize=Thumbsize.medium, order=Order.latest, gay_content=GayContent.none, low_quality=LowQuality.include)`  
Gets videos from Eporner.com.

Parameters  
**query** (str) - The search query. Special value `"all"` can be passed to query for all videos.  
**per_page** (int) - Limits the number of results per page. Valid range is 1 - 1000. Default: 30.  
**page** (int) - The results page number. Valid range is 1 - 1000000, but no more than ``total_pages`` received in response. Default: 1.  
**thumbsize** ([Thumbsize](#class-thumbsize)) - The thumbail size. Default: ``Thumbsize.medium``.  
**order** ([Order](#class-order)) - How results should be sorted. Default: ``Order.latest``.  
**gay_content** ([GayContent](#class-gaycontent)) - Whether to include gay content or not. Default ``GayContent.none``.  
**low_quality** ([LowQuality,](#class-lowquality)) - Whether to include low quality content or not. Default: ``LowQuality.include``.

Returns  
[Result](#class-result)

-----

*async def* `get_id(id)`  
Gets a video using its unique ID.

Parameters  
**id** (str) - The unique ID of the video.

Returns  
[Video](#class-video)

-----

*async def* `get_removed()`  
Gets a list of video IDs that were removed from Eporner.

| Note                                                |
| --------------------------------------------------- |
| This method does not work currently due to the API. |


Returns  
list[str]

-----

*def* `close()`  
Closes the client session.


## Enums

### *class* `Thumbsize`
The thumbnail sizes of the video.

`small`  
The small thumbnail size (190x152).  
`medium`  
The medium thumbnail size (427x240).  
`big`  
The big thumbnail size (640x360).

### *class* `Order`
How results should be sorted.

`latest`  
Newest videos first.  
`shortest`  
Shortest videos first.  
`longest`  
Longest videos first.  
`top_rated`  
Top rated videos first.  
`top_weekly`  
Top weekly videos first.  
`top_monthly`  
Top montly videos first.  
`most_popular`  
Most popular all-time videos first.

### *class* `GayContent`
Wheather results should include gay content.

`none`  
Gay contents not included.  
`include`  
Include gay contents.  
`only`  
Include only gay contents.

### *class* `LowQuality`  
Wheather results should include low quality content.

`none`  
Low quality contents not included.  
`include`  
Include low quality contents.  
`only`  
Include only low quality contents.


## Models

### *class* `Result`
The result containing information about the query.

Attributes  
**count** (int) - The number of videos returned on current result page.  
**current_page** (int) - The urrent result page number.  
**total_count** (int) - The total number of all videos found matching your criteria.  
**total_pages** (int) - The total number of pages with all results matching your criteria assuming current ``per_page`` value.  
**videos** (list) - A list of [Video](#class-video) objects.

### *class* `Video`
The video class containing information about the video.

Attributes  
**id** (int) - The unique ID of the video.  
**title** (str) - The video title.  
**tags** (list) - The tags assigned to the video.  
**views** (int) - The Estimated number of video views.  
**rate** (float) - The video rate. Valid range is ``0.00`` to ``5.00``.  
**url** (str) - The URL of the video on Eporner.  
**added** (str) - The date of the video added on Eporner.  
**length_sec** (int) - The video length in seconds.  
**length** (str) - The video length in ``mm:ss`` format or ``hh:mm:ss`` format if video longer than 60 minutes.  
**embed_url** (str) - The embed url of the video.  
**default_thumb** ([Thumbnail](#class-thumbnail)) - The video's default thumbnail information.  
**thumbs** (list) - A list of ``Thumbnail`` objects.

### *class* `Thumbnail`  
Information about the thumbnail of the video.

Attributes  
**size** (str) - The thumbnail size, i.e: big, medium, small.  
**width** (int) - The width of the thumbnail.  
**height** (int) - The height of the thumbnail.  
**src** (str) - The URL of the thumbnail.

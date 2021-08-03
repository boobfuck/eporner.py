# Installation
Install eporner.py via `pip`:

```shell
$ pip install eporner.py
```

# Quickstart
Here's a simple example.

```python
import asyncio
import eporner

async def main():
    client = eporner.Client()
    result = await client.get_videos('busty milf')

    vid = result.videos[0] # first video
    print(vid.title)
    print(vid.url)
    print(vid.default_thumb.src)

    client.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
Check the [API Reference](manuals.md) for more information.

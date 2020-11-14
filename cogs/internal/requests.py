import aiohttp


async def get_data(url):
    async with aiohttp.request('get', url) as resp:
        data = await resp.json()
    return data

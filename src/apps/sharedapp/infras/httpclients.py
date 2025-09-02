import aiohttp
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_fixed


class HttpClient:
    def __init__(self, *args, **kwargs):
        super(HttpClient, self).__init__(*args, **kwargs)
        self.attempt=0

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_fixed(2),
        retry=retry_if_exception_type(aiohttp.ClientError),
    )
    async def fetch_data(self, session: aiohttp.ClientSession, url: str):
        async with session.get(url) as response:
            self.attempt += 1
            print(f"Attempt url {url}: {self.attempt} times")
            response.raise_for_status()  # Raise an exception for bad status codes
            return await response.json()

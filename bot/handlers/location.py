import asyncio
from geopy.geocoders import Nominatim
from geopy.adapters import AioHTTPAdapter

async def get_location_name(latitude, longitude):
    async with Nominatim(
        user_agent="my_app",
        adapter_factory=AioHTTPAdapter
    ) as geolocator:
        location = await geolocator.reverse((latitude, longitude))
        return location.address

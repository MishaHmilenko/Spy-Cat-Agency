import aiohttp


class CatBreedValidator:

    API_URL = "https://api.thecatapi.com/v1/breeds"

    @staticmethod
    async def validate_breed(breed_name: str) -> bool:
        async with aiohttp.ClientSession() as session:
            async with session.get(CatBreedValidator.API_URL) as response:
                breeds = await response.json()

                for breed in breeds:
                    if breed['name'].lower() == breed_name.lower():
                        return True
                return False

import httpx
from core.config import settings

class GHLService:

    @staticmethod
    async def get_account_info():
        headers = {
            "Authorization":f"Bearer {settings.GHL_AUTH}",
            "Content-Type": "application/json",
            "Version":"2021-07-28"
        }
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{settings.GHL_URL}/users/?locationId={settings.ID_LOCATION}",
                headers=headers
            )

        response.raise_for_status()
        return response.json()
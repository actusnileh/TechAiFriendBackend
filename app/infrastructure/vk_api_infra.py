import datetime
from typing import (
    Any,
    Dict,
    List,
)

import httpx

from app.core.configs import settings


class VkApiInfra:
    def __init__(self, version: str = "5.199"):
        self.access_token = settings.VK_API_TOKEN
        self.version = version
        self.base_url = "https://api.vk.com/method/"

    async def _request(self, method: str, params: Dict[str, Any]) -> Dict[str, Any]:
        params["access_token"] = self.access_token
        params["v"] = self.version
        async with httpx.AsyncClient() as client:
            response = await client.get(self.base_url + method, params=params)
            response.raise_for_status()
            return response.json()

    async def get_user_info(self, user_id: str) -> Dict[str, Any]:
        params = {"user_ids": user_id, "fields": "bdate"}
        response = await self._request("users.get", params)
        user_data = response.get("response", [{}])[0]
        return {
            "id": user_data.get("id"),
            "bdate": user_data.get("bdate", None),
        }

    async def get_user_posts(
        self,
        user_id: str,
        count: int = 100,
    ) -> List[Dict[str, Any]]:
        params = {"owner_id": user_id, "count": count}
        response = await self._request("wall.get", params)
        posts = response.get("response", {}).get("items", [])

        return [
            {
                "vkPostID": post.get("id"),
                "date": datetime.datetime.fromtimestamp(post["date"]).strftime(
                    "%Y-%m-%d %H:%M:%S",
                ),
                "text": post.get("text", ""),
                "author": (
                    post.get("owner_id", "Неизвестно")
                    if "copy_history" not in post
                    else post["copy_history"][0].get("owner_id", "Неизвестно")
                ),
                "source": "Репост от" if "copy_history" in post else "Пользователь",
                "likesCount": post.get("likes", {}).get("count", 0),
            }
            for post in posts
        ]

    async def get_user_photos(
        self,
        user_id: int,
        count: int = 15,
    ) -> List[Dict[str, Any]]:
        params = {
            "owner_id": user_id,
            "count": count,
            "album_id": "profile",
            "extended": True,
        }
        response = await self._request("photos.getAll", params)
        photos = response.get("response", {}).get("items", [])

        return [
            {
                "photoID": photo["id"],
                "date": datetime.datetime.fromtimestamp(photo["date"]).strftime(
                    "%Y-%m-%d %H:%M:%S",
                ),
                "likesCount": photo.get("likes", {}).get("count", 0),
                "url": photo["sizes"][-1]["url"] if photo.get("sizes") else None,
            }
            for photo in photos
        ]

    async def get_user_groups(
        self,
        user_id: str,
        count: int = 200,
    ) -> List[Dict[str, Any]]:
        params = {
            "user_id": user_id,
            "count": count,
            "extended": 1,
            "fields": "name,description",
        }
        response = await self._request("groups.get", params)
        groups = response.get("response", {}).get("items", [])

        return [
            {
                "id": group.get("id"),
                "name": group.get("name"),
                "description": group.get("description", None),
            }
            for group in groups
        ]

    async def get_user_interests(self, user_id: str) -> str:
        params = {"user_id": user_id, "fields": "interests"}
        response = await self._request("users.get", params)
        return response.get("response", [{}])[0].get("interests", "")

    async def get_user_friends(self, user_id: str) -> List[Dict[str, Any]]:
        params = {"user_id": user_id, "fields": "city,education,career"}
        response = await self._request("friends.get", params)
        friends = response.get("response", {}).get("items", [])

        return [
            {
                "id": friend.get("id"),
                "city": friend.get("city", {}).get("title"),
                "university_name": friend.get("university_name"),
                "company": (
                    friend.get("career", [{}])[0].get("company")
                    if friend.get("career")
                    else None
                ),
            }
            for friend in friends
        ]

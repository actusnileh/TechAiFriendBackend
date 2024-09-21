from app.infrastructure.vk_api_infra import VkApiInfra
from app.repository.friends_repository import FriendsRepository
from app.repository.groups_repository import GroupsRepository
from app.repository.photo_repository import PhotosRepository
from app.repository.posts_repository import PostsRepository
from app.repository.user_repository import UserRepository
from app.utils.api_utils import (
    calculate_age,
    calculate_avg_likes,
    extract_year,
)


class UserService:
    def __init__(self):
        self.infra = VkApiInfra()

    async def add_user(self, url: str):
        user_info = await self.infra.get_user_info(url)
        user_posts = await self.infra.get_user_posts(user_info["id"])
        user_photos = await self.infra.get_user_photos(user_info["id"])
        user_groups = await self.infra.get_user_groups(user_info["id"])
        user_interests = await self.infra.get_user_interests(user_info["id"])
        user_friends = await self.infra.get_user_friends(user_info["id"])

        await UserRepository.add(
            vk_id=user_info["id"],
            age=calculate_age(user_info.get("bdate")),
            date_of_birth=user_info.get("bdate", ""),
            year_of_birth=extract_year(user_info.get("bdate")),
            average_likes_photos=calculate_avg_likes(user_photos),
            average_likes_posts=calculate_avg_likes(user_posts),
            interest=user_interests,
            friends_count=len(user_friends),
            posts_count=str(len(user_posts)),
            photo_count=str(len(user_photos)),
        )

        for post in user_posts:
            await PostsRepository.add(
                user_id=user_info["id"],
                post_vk_id=post["vkPostID"],
                post_date=post["date"],
                post_text=post["text"],
                post_author=post["author"],
                post_friend_or_not_friend=post["source"] == "Репост от",
            )

        for photo in user_photos:
            await PhotosRepository.add(
                user_id=user_info["id"],
                photo_id=photo["photoID"],
                photo_url=photo["url"],
                photo_count_likes=photo["likesCount"],
                photo_description=None,
            )

        for group in user_groups:
            await GroupsRepository.add(
                user_id=user_info["id"],
                group_id=group["id"],
                group_name=group["name"],
                group_description=group["description"],
            )

        for friend in user_friends:
            await FriendsRepository.add(
                user_id=user_info["id"],
                friend_id=friend["id"],
                friend_city=friend["city"],
                friend_education=friend.get("university_name"),
                friend_job=friend.get("company"),
            )

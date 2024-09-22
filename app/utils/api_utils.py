import datetime
import re


def calculate_avg_likes(items: list[dict]) -> float:
    total_likes = sum(item["likesCount"] for item in items)

    return total_likes / len(items) if items else 0


def calculate_age(bdate: str) -> int:
    if not bdate or bdate.count(".") != 2:
        return 0

    birth_year = int(bdate.split(".")[-1])
    current_year = datetime.datetime.now().year

    return current_year - birth_year


def extract_year(bdate: str) -> int:
    if not bdate or bdate.count(".") != 2:
        return 0
    return int(bdate.split(".")[-1])


def extract_user_id(url: str) -> str:
    match = re.search(r"vk\.com/(.+)$", url)
    if match:
        return match.group(1)
    raise ValueError("Invalid URL format")

from redis_om import HashModel
from .db import redis_db


class Task(HashModel):
    original_url: str
    shortened_url: str
    url_str: str
    takma_ad: str
    created_by: str
    created_at_gmt: str
    click_count: int
    expire_date: int

    class Meta:
        database: redis_db


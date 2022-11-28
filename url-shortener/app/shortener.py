import random
import string
import time
from .data_schema import Task

def url_shorter(url,expire=-99,takma_ad=''):
    N=random.randint(6,10)
    random_str = ''.join(random.choices(string.ascii_letters, k=N))
    gmt_time=time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())

    data = Task(
        original_url=url,
        shortened_url="http://localhost:8000/"+random_str,
        url_str=random_str,
        takma_ad="",
        created_by="deneme",
        created_at_gmt=gmt_time,
        click_count=0,
        expire_date=expire,
        )
    
    return data
 
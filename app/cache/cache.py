import redis
from typing import Optional
from config.config import config




class RedisCache:

    _instance:Optional[redis] = None

    def __init__(self, host:str, port:str, username:str=None, password:str=None, db:str = 0, **kwargs):
        try:
            self.redis = redis.Redis(host, port, db, username, password, kwargs)
            self.redis.ping()
        except redis.AuthenticationError as e:
            raise e
        except redis.ConnectionError as e:
            raise e
        except Exception as e:
            raise e
        

    def __new__(cls,*args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls
    
    def get_redis_client(self) -> redis.Redis:
        return self.redis


def get_redis_client():
    redis_client:RedisCache = RedisCache(config.redis_host, config.redis_port)
    return redis_client

    

    




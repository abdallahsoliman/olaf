from django.contrib.sessions.backends.base import CreateError, SessionBase
from sessions.redis_backend import RedisBackend

class SessionStore(SessionBase):
    """
    Redis sessions backend
    """

    def __init__(self, session_key=None):
        super(SessionStore, self).__init__(session_key)
        self.redis = RedisBackend()


    def _get_or_create_session_key(self):
        if self._session_key is None:
            self._session_key = self._get_new_session_key()

        return self._session_key


    def load(self):
        session_data = self.redis.get(self.session_key)
        if session_data is not None:
            return self.decode(session_data)
        else:
            self.create()
            return {}


    def exists(self, session_key):
        return self.redis.exists(session_key)


    def create(self):
        while True:
            self._session_key = self._get_new_session_key()

            try:
                self.save(must_create=True)
            except CreateError:
                continue

            self.modified = True
            self._session_cache = {}
            return


    def save(self, must_create=False):
        session_key = self._get_or_create_session_key()
        expire_in = self.get_expiry_age()
        session_data = self.encode(self._get_session(no_load=must_create))
        self.redis.save(session_key, expire_in, session_data, must_create)


    def delete(self, session_key=None):
        if session_key is None:
            if self.session_key is None:
                return
            else:
                session_key = self.session_key

        self.redis.delete(session_key)

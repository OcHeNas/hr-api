from fastapi_users import FastAPIUsers
from fastapi_users.authentication import CookieTransport, AuthenticationBackend
from fastapi_users.authentication import JWTStrategy
from fastapi import Depends

from src.auth.manager import get_user_manager
from src.auth.models import User
from src.config import SECRET_AUTH

cookie_transport = CookieTransport(cookie_max_age=3600)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET_AUTH, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()

def check_user_role(required_roles: list):
    def check_role(user: User = Depends(fastapi_users.current_user())):
        if user.role_name not in required_roles:
            raise HTTPException(status_code=403, detail="User does not have enough privileges")
        return user
    return check_role
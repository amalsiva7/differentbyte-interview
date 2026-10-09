from schemas import UserData


async def validate_user(user: UserData):
    if user.email is None:
        raise
    if user.name is None:
        raise
    return user

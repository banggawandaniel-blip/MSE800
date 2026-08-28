from services import UserService


def create_admin():
    """Create the default administrator account."""

    user_service = UserService()

    success, message = user_service.register_user(
        "admin",
        "admin123",
        "admin"
    )

    print(message)

    user_service.close()


if __name__ == "__main__":
    create_admin()
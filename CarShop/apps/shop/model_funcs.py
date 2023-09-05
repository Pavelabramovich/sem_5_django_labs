# This file is needed because Django can only serialize functions declared somewhere as a link
# to a module and a function name. Therefore, this file should be modified with extreme caution.

from apps.core.image_tools import get_random_color


def get_category_logo_filename(instance):
    return f"logo_{instance.uuid}"


def get_category_image_filename(instance):
    return f"image_{instance.uuid}"


def get_profile_avatar_filename(instance):
    return f"avatar_{instance.user.id}"


def get_profile_avatar_color(instance):
    return get_random_color(instance.user.id)


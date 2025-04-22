def user_listing_path(instance, filename):
    """
    Function to define the upload path for user profile photos.
    The uploaded file will be stored in MEDIA_ROOT/user_<id>/<filename>.
    :param instance: The instance of the Profile model.
    :param filename: The name of the uploaded file.(the name of the image eg : user_3/img1.jpeg)
    """
    return f'user_{instance.seller.user.id}/listings/{filename}'
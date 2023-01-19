class Sticker:
    def __init__(self, file_id, width, height, thumb=None, emoji=None, file_size=None, custom_emoji_id=None, mask_position=None, premium_animation=None, set_name=None, is_video=None, is_animated=None, type=None, file_unique_id=None):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.thumb = thumb
        self.emoji = emoji
        self.file_size = file_size
        self.custom_emoji_id = custom_emoji_id
        self.mask_position = mask_position
        self.premium_animation = premium_animation
        self.set_name = set_name
        self.is_video = is_video
        self.is_animated = is_animated
        self.type = type
        self.file_unique_id = file_unique_id

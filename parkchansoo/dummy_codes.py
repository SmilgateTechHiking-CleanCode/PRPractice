"""
아래 코드는 실제로는 존재하지 않는 코드입니다.
프로젝트의 다른 파일에서 import 되어야하나 현재는 리팩토링을 위한 부분만 가져왔습니다.
"""

def get_if_special_theme(theme_id: str) -> str:
    pass

RESERVED_PRESET_MAP_PREFIXES = {
    "random_pick": "random_pick",
}

PRESET_MAP = {
    "key1": "포토북",
    "key2": "포토북2",
    "key3": "포토북3",
}
VIDEO_PRESET_MAP = {
    "key1": "비디오북",
}

class CRUD:
    def list_random_choice_theme_api(self, preset_group, gender):
        pass

    def get_theme_by_id(self, theme_id):
        pass


class Schema:
    class MLModel:
        pass

class RandomThemeHandler:
    def check_cached(self, photo, model_id):
        pass

    def encode(self, preset_id, get_random_photo_id):
        pass


crud  = CRUD()
schemas = Schema()
random_theme_handler = RandomThemeHandler()

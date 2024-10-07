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

"""
위 코드는 실제로는 존재하지 않는 코드입니다.
다른 파일에서 import 되어야하나 현재는 리팩토링을 위한 부분만 가져왔습니다.
"""


import abc
import random
import typing
import logging

from fastapi import HTTPException


logger = logging.getLogger(__name__)




class ReservedThemeHandler:
    reserved_theme_keyword = None

    @classmethod
    def get_reserved_theme_handler(cls, handler_str) -> type[typing.Self]:
        for sub_cls in cls.__subclasses__():
            if handler_str == sub_cls.reserved_theme_keyword:
                return sub_cls
        raise HTTPException(
            status_code=400, detail=f"handler_str {handler_str} not found. maybe got invalid prefix from theme_id"
        )

    @property
    @abc.abstractmethod
    def cache_hit(self) -> list[str]:
        pass

    @property
    @abc.abstractmethod
    def cache_miss(self) -> list[str]:
        pass


class RandomPickThemeHandler(ReservedThemeHandler):
    reserved_theme_keyword = "random_pick"

    def __init__(self, theme_id, model_id, gender: str = None):
        """
        :param theme_id: `random_pick{1}_{preset_group}` 과 같은 형태
        """
        self._cached = []
        self._not_cached = []
        self.theme_id = theme_id
        self.model_id = model_id
        self.gender = gender
        theme_id = theme_id.replace("random_pick", "")
        count, self.preset_group = theme_id.split("_")
        try:
            self.count = int(count)
        except ValueError:
            raise HTTPException(
                status_code=400, detail=f"random_pick count must be integer. but got {count} from {theme_id}"
            )
        chosen_theme_photos = self.pick()
        for photo in chosen_theme_photos:
            result = random_theme_handler.check_cached(photo, self.model_id)
            if result:
                self._cached.append(result)
            else:
                self._not_cached.append(photo)

    @property
    def cache_hit(self) -> list[str]:
        return self._cached

    @property
    def cache_miss(self) -> list[str]:
        return self._not_cached

    def pick(self) -> list[str]:
        chosen_themes = crud.list_random_choice_theme_api(self.preset_group, self.gender)
        if self.count > len(chosen_themes):
            raise HTTPException(
                status_code=400,
                detail=f"random_pick count must be less than {len(chosen_themes)}. but got {self.count} from {self.theme_id}",
            )
        counted_themes = random.sample(chosen_themes, k=self.count)
        return [random_theme_handler.encode(theme.preset_id, theme.get_random_photo_id()) for theme in counted_themes]


def map_theme_id_preset(theme_id, model_infos: dict[str, schemas.MLModel]) -> tuple[list[str], list[str]]:
    if get_if_special_theme(theme_id):
        prefix = get_if_special_theme(theme_id)
        handler = ReservedThemeHandler.get_reserved_theme_handler(RESERVED_PRESET_MAP_PREFIXES[prefix])
        if len(model_infos) > 1:
            logger.error(f"model_infos must be only one. but got {model_infos}. 현재 랜덤상자에서는 하나의 모델만 지원합니다.")
        model_id, model_info = list(model_infos.items())[0]
        handler_obj = handler(theme_id, model_id, model_info.gender)
        return handler_obj.cache_miss, handler_obj.cache_hit

    theme_db_obj = crud.get_theme_by_id(theme_id)
    if theme_db_obj:
        return [theme_db_obj.preset_name], []

    theme_name_from_literal = {**PRESET_MAP, **VIDEO_PRESET_MAP}.get(theme_id)
    if theme_name_from_literal:
        return [theme_name_from_literal], []
    return [], []

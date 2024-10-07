
import abc
import random
import typing
import logging
from dataclasses import dataclass

from fastapi import HTTPException
# Note. 현재는 중요하지 않아서 dummy 용으로 구현해둔 코드를 * 로 가져옴
from dummy_codes import * 


logger = logging.getLogger(__name__)


class ThemeHandlerNotFound(Exception):
    pass



class ThemeInfomationError(Exception):
    pass



@dataclass
class ThemeSelection:
    cache_miss: list[str]
    cache_hit: list[str]


class ThemeHandlerFactory:
    @classmethod
    def build(cls, theme_id, additional_info: typing.Dict) -> ReservedThemeHandler:
        if get_if_special_theme(theme_id):
            prefix = get_if_special_theme(theme_id)
            handler = ReservedThemeHandler.get_reserved_theme_handler(RESERVED_PRESET_MAP_PREFIXES[prefix])
            return handler(theme_id)
        theme_db_obj = crud.get_theme_by_id(theme_id)
        if theme_db_obj:
            return DBThemeHandler(theme_id)
        if theme_id in PRESET_MAP:
            return ThemeHandler(theme_id)
        raise ThemeHandlerNotFound("theme_id 에 해당하는 handler 가 없습니다.")




class ReservedThemeHandler:
    def __init__(self, theme_id, additional_info: typing.Dict) -> 'ReservedThemeHandler':
        self.theme_id = theme_id
        self.additional_info = additional_info
        return ThemeHandlerFactory.build(theme_id, additional_info)

    @property
    @abc.abstractmethod
    def get_theme_selection(self) -> ThemeSelection:
        pass


class DBThemeHandler(ReservedThemeHandler):
    def __init__(self, theme_id, *args, **kwargs) -> None:
        self.theme_id = theme_id

    @property
    def get_theme_selection(self) -> ThemeSelection:
        theme_db_obj = crud.get_theme_by_id(self.theme_id)
        return ThemeSelection([theme_db_obj.preset_name], [])
    

class LiteralThemeHandler(ReservedThemeHandler):
    """
    [Deprecated]
    theme_id 가 preset_map 에 있는 경우
    """

    def get_theme_selection(self) -> ThemeSelection:
        theme_name_from_literal = {**PRESET_MAP, **VIDEO_PRESET_MAP}.get(self.theme_id)
        if theme_name_from_literal:
            return ThemeSelection([theme_name_from_literal], [])


class RandomPickThemeHandler(ReservedThemeHandler):
    count: int

    def get_theme_selection(self) -> ThemeSelection:
        """
        :param theme_id: `random_pick{1}_{preset_group}` 과 같은 형태
        """
        theme_selection = ThemeSelection([], [])
        model_id = self.additional_info["model_id"]
        gender = self.additional_info["gender"]
        theme_id = self.theme_id.replace("random_pick", "")
        count, self.preset_group = theme_id.split("_")
        try:
            count = int(count)
        except ValueError:
            raise ThemeInfomationError(f"random_pick count must be integer. but got {count} from {theme_id}")
        chosen_themes = crud.list_random_choice_theme_api(self.preset_group, gender=gender)
        if count > len(chosen_themes):
            raise HTTPException(
                status_code=400,
                detail=f"random_pick count must be less than {len(chosen_themes)}. but got {cnt} from {self.theme_id}",
            )

        chosen_theme_photos = self.pick(count, chosen_themes)
        for photo in chosen_theme_photos:
            result = random_theme_handler.check_cached(photo, model_id)
            if result:
                theme_selection.cached.append(result)
            else:
                theme_selection.not_cached.append(photo)
        return theme_selection


    def pick(self, cnt, chosen_themes) -> list[str]:
        counted_themes = random.sample(chosen_themes, k=cnt)
        return [random_theme_handler.encode(theme.preset_id, theme.get_random_photo_id()) for theme in counted_themes]


def map_theme_id_preset(theme_id, model_infos: dict[str, schemas.MLModel]) -> ThemeSelection:
    return ReservedThemeHandler(theme_id, model_infos).get_theme_selection()
import abc
import enum


class NotValidComponentError(Exception):
    pass


class CakeComponent(enum.Enum):
    @classmethod
    @abc.abstractmethod
    def from_prompt(self, prompt):
        pass

    @classmethod
    def handle_prompt(cls, prompt=None, default=None):
        if prompt is None:
            return default
        try:
            return cls.from_prompt(prompt)
        except KeyError:
            raise NotValidComponentError(f"{prompt}은 유효한 값이 아닙니다.")            


class Bread(CakeComponent):
    sponge = "스폰지 케이스 베이스"
    chocolate = "초콜릿 케이스 베이스"
    normal = "일반 케이스 베이스"

    @classmethod
    def from_prompt(cls, prompt):
        return {
            "스폰지": cls.sponge,
            "초콜릿": cls.chocolate,
            "일반": cls.normal
        }[prompt]

class Cream(CakeComponent):
    vanilla = "바닐라 크림"
    chocolate = "초콜릿 크림"
    normal = "일반 크림"

    @classmethod
    def from_prompt(cls, prompt):
        return {
            "바닐라": cls.vanilla,
            "초콜릿": cls.chocolate,
            "일반": cls.normal
        }[prompt]


class Decoration(CakeComponent):
    chocolate = "초콜릿 장식"
    fruit = "과일 장식"
    normal = "일반 장식"

    @classmethod
    def from_prompt(cls, prompt):
        return {
            "초콜릿": cls.chocolate,
            "과일": cls.fruit,
            "일반": cls.normal
        }[prompt]


class Cake:
    base = Bread.sponge
    cream = Cream.vanilla
    decoration = Decoration.chocolate
    
    def make_cake(self, base_type=None, cream_type=None, decoration_type=None):
        try:
            self.base = Bread.handle_prompt(base_type, self.base)
            self.cream = Cream.handle_prompt(cream_type, self.cream)
            self.decoration = Decoration.handle_prompt(decoration_type, self.decoration)
        except NotValidComponentError as e:
            print("케이크를 만들 수 없습니다:", e)
        return self.get_description()

    def get_description(self):
        return "\n".join([
            self.base.value,
            self.cream.value,
            self.decoration.value,
            "케이크가 완성되었습니다!"
        ])
    


if __name__ == "__main__":
    cake = Cake()
    print(cake.make_cake())

    print("\n다른 종류의 케이크 만들기:")

    another_cake = Cake()
    print(another_cake.make_cake("초콜릿", "초콜릿", "과일"))

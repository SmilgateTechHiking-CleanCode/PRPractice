from abc import ABC, abstractmethod


class CakeBase(ABC):
    def __init__(self):
        self.base_type = ""

    @abstractmethod
    def prepare(self):
        pass


class SpongeCakeBase(CakeBase):
    def prepare(self):
        self.base_type = "스폰지 케이크 베이스"
        return f"{self.base_type} 준비"


class ChocolateCakeBase(CakeBase):
    def prepare(self):
        self.base_type = "초콜릿 케이크 베이스"
        return f"{self.base_type} 준비"


class CreamLayer(ABC):
    def __init__(self):
        self.cream_type = ""

    @abstractmethod
    def add(self):
        pass


class VanillaCream(CreamLayer):
    def add(self):
        self.cream_type = "바닐라 크림"
        return f"{self.cream_type} 추가"


class ChocolateCream(CreamLayer):
    def add(self):
        self.cream_type = "초콜릿 크림"
        return f"{self.cream_type} 추가"


class Decoration(ABC):
    def __init__(self):
        self.decoration_type = ""

    @abstractmethod
    def decorate(self):
        pass


class ChocolateDecoration(Decoration):
    def decorate(self):
        self.decoration_type = "초콜릿 장식"
        return f"{self.decoration_type} 추가"


class FruitDecoration(Decoration):
    def decorate(self):
        self.decoration_type = "과일 장식"
        return f"{self.decoration_type} 추가"


class CakeFactory:
    def __init__(self, base: CakeBase, cream: CreamLayer, decoration: Decoration):
        self.base = base
        self.cream = cream
        self.decoration = decoration
        self.cake_description = []

    def create_cake(self):
        self.cake_description.append(self.base.prepare())
        self.cake_description.append(self.cream.add())
        self.cake_description.append(self.decoration.decorate())
        self.cake_description.append("케이크가 완성되었습니다!")
        return "\n".join(self.cake_description)


# 클라이언트 코드
base = SpongeCakeBase()
cream = VanillaCream()
decoration = ChocolateDecoration()

cake_factory = CakeFactory(base, cream, decoration)
print(cake_factory.create_cake())

print("\n다른 종류의 케이크 만들기:")

# 다른 종류의 케이크를 만들고 싶다면
chocolate_base = ChocolateCakeBase()
chocolate_cream = ChocolateCream()
fruit_decoration = FruitDecoration()

another_cake_factory = CakeFactory(
    chocolate_base, chocolate_cream, fruit_decoration)
print(another_cake_factory.create_cake())

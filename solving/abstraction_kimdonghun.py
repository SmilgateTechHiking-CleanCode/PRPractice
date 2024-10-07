from abc import ABC, abstractmethod
class Base(ABC): 
    @abstractmethod
    def prepare(self):
        pass

class SpongeBase(Base):
    def prepare(self):
        return "스폰지 케이크 베이스"

class ChocolateBase(Base):
    def prepare(self):
        return "초콜릿 케이크 베이스"

class BasicBase(Base):
    def prepare(self):
        return "일반 케이크 베이스"


class Cream(ABC):
    @abstractmethod
    def add(self):
        pass
    
class VanilaCream(Cream):
    def add(self):
        return "바닐라 크림"
class ChocolateCream(Cream):
    def add(self):
        return "초콜릿 크림"
class BasicCream(Cream):
    def add(self):
        return "일반 크림"
    
class Decorate(ABC):
    @abstractmethod
    def decorate(self):
        pass
class ChocolateDecorate(Decorate):
    def decorate(self):
        return "초콜릿 장식"
    
class FruitDecorate(Decorate):
    def decorate(self):
        return "과일 장식"
class BasicDecorate(Decorate):
    def decorate(self):
        return "일반 장식"
    

class SelectBase:
    def get_base(self, base_type="스폰지"):
        if base_type == "스폰지":
            return SpongeBase()
        elif base_type == "초콜릿":
            return ChocolateBase()
        else:
            return BasicBase()

class SelectCream:
    def get_cream(self, cream_type="바닐라"):
        if cream_type == '바닐라':
            return VanilaCream()
        elif cream_type == '초콜릿':
            return ChocolateCream()
        else:
            return BasicCream()

class SelectDecoration:
    def get_decoration(self, decorate_type="초콜릿"):
        if decorate_type == "초콜릿":
            return ChocolateDecorate()
        elif decorate_type == "과일":
            return FruitDecorate()
        else:
            return BasicDecorate()
class Cake:
    def __init__(self):
        self.base = ""
        self.cream = ""
        self.decoration = ""
        self.cake_description = []

    def prepare_base(self, base_type="스폰지"):
        base = SelectBase.get_base(base_type)
        self.base = base.prepare()
        self.cake_description.append(f"{self.base} 준비")

    def add_cream(self, cream_type="바닐라"):
        cream = SelectCream.get_cream(cream_type)
        self.cream = cream.add()
        self.cake_description.append(f"{self.cream} 추가")

    def decorate(self, decoration_type="초콜릿"):
        decoration = SelectDecoration.get_decoration(decoration_type)
        self.decoration = decoration.decorate()
        self.cake_description.append(f"{self.decoration} 추가")

    def make_cake(self, base_type="스폰지", cream_type="바닐라", decoration_type="초콜릿"):
        self.prepare_base(base_type)
        self.add_cream(cream_type)
        self.decorate(decoration_type)
        self.cake_description.append("케이크가 완성되었습니다!")
        return "\n".join(self.cake_description)


        
# 클라이언트 코드
cake = Cake()
print(cake.make_cake())

print("\n다른 종류의 케이크 만들기:")

another_cake = Cake()
print(another_cake.make_cake("초콜릿", "초콜릿", "과일"))

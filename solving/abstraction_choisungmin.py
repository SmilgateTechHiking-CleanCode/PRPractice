# 직접 접근을 못하게 한다? -> getter?

class Cake:
    def __init__(self):
        self.cake_description = []


    def make_cake(self, base_type="스폰지", cream_type="바닐라", decoration_type="초콜릿"):
        base = Base(base_type)
        cream = Cream(cream_type)
        decoration = Decoration(decoration_type)

        self.cake_description.append(f"{base}")
        self.cake_description.append(f"{cream}")
        self.cake_description.append(f"{decoration}")
        self.cake_description.append("케이크가 완성되었습니다!")
        return "\n".join(self.cake_description)


class Base:
    def __init__(self, base_type="스폰지"):
        self.base = self.get_base_type(base_type)
    
    def get_base_type(self, base_type):
        base_types = {
            "스폰지": "스폰지 케이크 베이스",
            "초콜릿": "초콜릿 케이크 베이스"
        }
        return base_types.get(base_type, "일반 케이크 베이스")
    
    def __str__(self):
        return self.base
    
class Cream:
    def __init__(self, cream_type="바닐라"):
        self.cream = self.get_cream(cream_type)

    def get_cream(self, cream_type):
        cream_types={
            "바닐라": "바닐라 크림",
            "초콜릿": "초콜릿 크림"
        }
        return cream_types.get(cream_type, "일반 크림")

    def __str__(self):
        return self.cream

class Decoration:
    def __init__(self, decoration_type="초콜릿"):
        self.decorate = self.get_decorate(decoration_type)

    def get_decorate(self, decoration_type):
        decoration_types = {
            "초콜릿": "초콜릿 장식",
            "과일": "과일 장식"
        }
        return decoration_types.get(decoration_type, "일반 장식")
    
    def __str__(self):
        return self.decorate

# 클라이언트 코드
cake = Cake()
print(cake.make_cake())

print("\n다른 종류의 케이크 만들기:")

another_cake = Cake()
print(another_cake.make_cake("초콜릿", "초콜릿", "과일"))

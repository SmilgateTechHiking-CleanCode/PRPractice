class CakeBase:
    def __init__(self, base_type="스폰지"):
        self.base = self.prepare_base(base_type)

    def prepare_base(self, base_type):
        if base_type == "스폰지":
            return "스폰지 케이크 베이스 준비"
        elif base_type == "초콜릿":
            return "초콜릿 케이크 베이스 준비"
        else:
            return "일반 케이크 베이스 준비"

class CakeCream:
    def __init__(self, cream_type="바닐라"):
        self.cream = self.add_cream(cream_type)

    def add_cream(self, cream_type):
        if cream_type == "바닐라":
            return "바닐라 크림 추가"
        elif cream_type == "초콜릿":
            return "초콜릿 크림 추가"
        else:
            return "일반 크림 추가"
            
class CakeDecoration:
    def __init__(self, decoration_type="초콜릿"):
        self.decoration = self.apply_decoration(decoration_type)

    def apply_decoration(self, decoration_type):
        if decoration_type == "초콜릿":
            return "초콜릿 장식 추가"
        elif decoration_type == "과일":
            return "과일 장식 추가"
        else:
            return "일반 장식 추가"

class Cake:
    def __init__(self, base_type="스폰지", cream_type="바닐라", decoration_type="초콜릿"):
        self.base = CakeBase(base_type)
        self.cream = CakeCream(cream_type)
        self.decoration = CakeDecoration(decoration_type)

    def make_cake(self):
        cake_description = []
        cake_description.append(self.base.base)
        cake_description.append(self.cream.cream)
        cake_description.append(self.decoration.decoration)
        cake_description.append("케이크가 완성되었습니다!")
        
        return "\n".join(cake_description)


# 클라이언트 코드
cake = Cake()
print(cake.make_cake())

print("\n다른 종류의 케이크 만들기:")

another_cake = Cake("초콜릿", "초콜릿", "과일")
print(another_cake.make_cake())

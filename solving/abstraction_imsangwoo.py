class Cake:
    def __init__(self):
        self.cake_description = []

    def make_cake(self, base_type="스폰지", cream_type="바닐라", decoration_type="초콜릿"):
        baseCake = Base()
        cream = Cream()
        deco = Decoration()

        self.cake_description.append(baseCake.prepare_base(base_type))
        self.cake_description.append(cream.add_cream(cream_type))
        self.cake_description.append(deco.decorate(decoration_type))
        self.cake_description.append("케이크가 완성되었습니다!")
        return "\n".join(self.cake_description)


class Base(Cake):
    def __init__(self):
        self.base = ""

    def prepare_base(self, base_type="스폰지"):
        if base_type == "스폰지":
            self.base = "스폰지 케이크 베이스"
        elif base_type == "초콜릿":
            self.base = "초콜릿 케이크 베이스"
        else:
            self.base = "일반 케이크 베이스"
        return (f"{self.base} 준비")  

class Cream(Cake):
    def __init__(self):
        self.cream = ""
    def add_cream(self, cream_type="바닐라"):
        if cream_type == "바닐라":
            self.cream = "바닐라 크림"
        elif cream_type == "초콜릿":
            self.cream = "초콜릿 크림"
        else:
            self.cream = "일반 크림"
        return (f"{self.cream} 추가")
 

class Decoration(Cake):
    def __init__(self):
        self.decoration = ""
    def decorate(self, decoration_type="초콜릿"):
        if decoration_type == "초콜릿":
            self.decoration = "초콜릿 장식"
        elif decoration_type == "과일":
            self.decoration = "과일 장식"
        else:
            self.decoration = "일반 장식"
        return (f"{self.decoration} 추가")

# 클라이언트 코드
cake = Cake()
print(cake.make_cake())

print("\n다른 종류의 케이크 만들기:")

another_cake = Cake()
print(another_cake.make_cake("초콜릿", "초콜릿", "과일"))

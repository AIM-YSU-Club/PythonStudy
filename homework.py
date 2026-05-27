# 숙제: Student 클래스 만들기
# Student에 정의된 속성들을 이용해서 각자 메소드를 하나씩 만들고 사용해보세요.
# 본인이 작성한 코드에 주석을 달아주세요. (# 이름/코드설명)

class Student():
    name: str               # 이름
    age: int                # 나이
    bodyWeight: float       # 체중
    bodyHeight: float       # 신장(키)
    bestFriend: "Student"   # 베프 객체에 대한 참조를 저장하는 속성
    favoiteFoods: list[str]  # 좋아하는 음식 리스트

    # 우재성 / 생성자 메소드. 객체를 생성할 호출됩니다.
    def __init__(self, name: str, age: int, bodyWeight: float, bodyHeight: float):
        self.name = name
        self.age = age
        self.bodyWeight = bodyWeight
        self.bodyHeight = bodyHeight

    # 우재성 / 베프를 설정하는 메소드. 자기 자신과 같은 타입의 객체를 받고 저장합니다.
    def setBestFriend(self, bf: "Student"):
        self.bestFriend = bf

    # 여기서부터 각자 메소드를 하나씩 만들어보세요!

    # 홍서준 / 상대방의 키를 빼앗는 메소드
    def stealHeight(self, target: "Student", want: float):
        self.bodyHeight += want
        target.bodyHeight -= want

        print(f"\n{self.name}님이 {target.name}님의 키를 {want}cm만큼 빼앗았습니다.\n")
        print("-"*70)
        print(f"\n{self.name}님의 키 : {self.bodyHeight}")
        print(f"{target.name}님의 키 : {target.bodyHeight}\n")
        print("-"*70)
        print(f"\n{target.name}님은 완전한 '난쟁이 똥자루'가 되었습니다.")
        print("앞으로 의류 구입 비용이 절감 되시겠네요. 아동복 코너 입성을 진심으로 축하드립니다!\n")


# 홍서준 / 사용법 안내
print("공백으로 문자 구별되기 때문에 아래 예시와 같이 작성해주세요. ")
print("예시) 최석팔 170")
print("예시) 김광철 196\n")

# 홍서준 / input으로 입력받은 문자를 split()을 이용해 공백으로 구분 지어 각 변수에 저장
steal_name, steal_height = input("사용자님의 이름과 키를 입력해주세요 : ").split()
target_name, target_height = input("키를 뺏을 대상의 이름과 키를 입력해주세요 : ").split()
want_height = float(input("빼앗고 싶은 키를 입력 하세요 : "))

# 홍서준 / 생성자 메소드를 호출하여 값을 넣고 변수에 저장
# 불 필요한 데이터는 None 처리하고, 키는 연산을 위해 float으로 강제 형변환
stealer = Student(steal_name, None, None, float(steal_height))
target = Student(target_name, None, None, float(target_height))

# 홍서준 / stealer 객체의 stealHeight 메소드를 불러옴
stealer.stealHeight(target, want_height)

# # 우재성 / jaeseong 객체와 denji 객체를 생성합니다.
# # <- 이런식으로 객체를 생성하자마자 값을 넣어주는게 '생성자 메소드' 덕분에 가능합니다.
# jaeseong = Student("우재성", 27, 165)
# denji = Student("덴지", 20, 170)

# # # 우재성 / setBestFriend 메소드를 호출하여 덴지를 베프로 설정합니다.
# jaeseong.setBestFriend(denji)
# # # # 우재성 / jaeseong 객체의 베프의 이름을 출력합니다.
# print(jaeseong.bestFriend.name)

# ** 숙제 TIP **
# 객체란 속성과 메소드를 가진 기능의 주체입니다. 이를 좀더 풀어서 설명하면
# 객체는 어떤 정보를 가질 수 있으며 그 정보를 이용해서 어떤 행동을 할 수 있습니다.
# Student 객체가 할 수 있는 행동이란 무엇이 있을 지 고민하고, 메소드로 만들어보세요.
# 좋아하는 음식 추가하기, 키 크기, 몸무게 줄이기, 베프 갈아타기 등등 여러분이 상상하는대로!
# 메소드를 하나 씩 만들고, 그 메소드를 호출할 객체를 생성해 자유롭게 사용해보세요.
# 숙제 제출: 다음주 화요일까지

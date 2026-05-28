# 숙제: Student 클래스 만들기
# Student에 정의된 속성들을 이용해서 각자 메소드를 하나씩 만들고 사용해보세요.
# 본인이 작성한 코드에 주석을 달아주세요. (# 이름/코드설명)

class Student():
    name: str               # 이름
    age: int                # 나이
    bodyWeight: float       # 체중
    bodyHeight: float       # 신장(키)
    bestFriend: "Student"   # 베프 객체에 대한 참조를 저장하는 속성
    favoiteFoods: list[str] # 좋아하는 음식 리스트

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

# 유성원 / 친한친구를 추가하는 메소드 입니다. 친구 이름을 받아서 그 리스트에 추가합니다.
class FriendList :
    def __init__(self):
        self.friends = []

    def add_friend(self, name):
        self.friends.append(name)

ysw_list = FriendList()

ysw_list.add_friend("신정민")
ysw_list.add_friend("박주성")

print(ysw_list.friends)

    
# 우재성 / jaeseong 객체와 denji 객체를 생성합니다.
# jaeseong = Student("우재성", 27, 165) # <- 이런식으로 객체를 생성하자마자 값을 넣어주는게 '생성자 메소드' 덕분에 가능합니다.
# denji = Student("덴지", 20, 170)

# 우재성 / setBestFriend 메소드를 호출하여 덴지를 베프로 설정합니다.
# jaeseong.setBestFriend(denji)
# 우재성 / jaeseong 객체의 베프의 이름을 출력합니다.
# print(jaeseong.bestFriend.name)

# ** 숙제 TIP **
# 객체란 속성과 메소드를 가진 기능의 주체입니다. 이를 좀더 풀어서 설명하면
# 객체는 어떤 정보를 가질 수 있으며 그 정보를 이용해서 어떤 행동을 할 수 있습니다.
# Student 객체가 할 수 있는 행동이란 무엇이 있을 지 고민하고, 메소드로 만들어보세요.
# 좋아하는 음식 추가하기, 키 크기, 몸무게 줄이기, 베프 갈아타기 등등 여러분이 상상하는대로!
# 메소드를 하나 씩 만들고, 그 메소드를 호출할 객체를 생성해 자유롭게 사용해보세요.
# 숙제 제출: 다음주 화요일까지
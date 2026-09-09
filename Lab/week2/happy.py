#
# 생일 축하 함수
#

def say_happy_birthday(name : str) -> None:
    print("안녕하세요?")
    print(name + "님의 생일 축하합니다.")
    return None

def test_say_happy_birthday() -> None:
    say_happy_birthday("조필구")
    say_happy_birthday("남요한")
    say_happy_birthday("허민")
    say_happy_birthday("황현준")

def test_say_happy_birthday2() -> None:
    names = ["조필구", "남요한", "허민", "황현준"]
    for name in names:
        say_happy_birthday(name)

def test_say_happy_birthday3() -> None:
    say_happy_birthday(3.14159)
    say_happy_birthday(100)
    say_happy_birthday([1,2,3])

test_say_happy_birthday3()

if __name__ == "__main__":
    test_say_happy_birthday2()
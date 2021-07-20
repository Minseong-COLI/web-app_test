

def decorator(func):
    def decorated(input_text):
        print("함수 시작!")
        func(input_text)
        print("함수 끝!")

    return decorated


@decorator
def hello_world(input_text):
    print(input_text)


hello_world('hello')


def decorator(func):
    def decorated(height, width):
        if height > 0 and width > 0 :
            func(height, width)
        else:
            print("입력이 잘못 되었습니다.")
    return decorated


@decorator
def triangle(h, w):
    print(1/2 * h * w)


@decorator
def rectangle(h, w):
    print(h * w)


triangle(5, 4)
rectangle(5, 4)
triangle(-1, 5)
rectangle(-1, -3)
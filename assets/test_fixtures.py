import pytest

@pytest.fixture(autouse= True,scope="class")
def main():
    print("\n Yal",end=" ")
    yield
    print("veer")

@pytest.mark.usefixtures("main")
class Test_fixctures():

    def test1(main):
        print("hi")


    def test2(main):
        print("hello")

    def test3(self):
        print("hi23")

    def test_veer(self):
        print("heloo23")

class Test1_Yals:
    def test_veer2(self):
        print("Hi python")

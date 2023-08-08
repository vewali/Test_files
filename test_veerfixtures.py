import time

from selenium import webdriver

import pytest
@pytest.fixture(autouse= True,scope="module")
def demo():
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach",True)
    lanch = webdriver.Chrome(options=opts)
    lanch.implicitly_wait(100)
    lanch.get("https://chat.qspiders.com/")
   # username= lanch.find_element("xpath",'//input[@type="text"]').send_keys("9916993732")


    yield
    lanch.quit()

#pytestmark = pytest.mark.usefixtures("demo")
def test_login(self,demo):

    lanch_1 = demo
    time.sleep(2)
    lanch_1.find_element("xpath",'//input[@type="text"]').send_keys("9916993732")
    time.sleep(2)
    lanch_1.find_element("xpath",'//input[@type="password"]').send_keys("veer3732")
    time.sleep(2)

    lanch_1.find_element("xpath",'//button[@type="submit"]').click


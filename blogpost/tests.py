from django.test import LiveServerTestCase
from selenium import webdriver
from  blogpost.models import Blogpost
class HomePageTestCase(LiveServerTestCase):

    def setUp(self):
        Blogpost.objects.create(
            title='hello',
            author='admin',
            slug='this_is_a_test',
            body='This is a blog',

        )
        self.selenium=webdriver.Chrome(executable_path="E:/driver/chromedriver.exe")
        self.selenium.maximize_window()
        super(HomePageTestCase,self).setUp()
    def tearDown(self):
        self.selenium.quit()
        super(HomePageTestCase,self).tearDown()
    def test_details(self):
        self.selenium.get(
            '%s%s'%(self.live_server_url,"/")
        )
        self.selenium.find_element_by_link_text("hello").click()
        self.assertIn("hello",self.selenium.title)

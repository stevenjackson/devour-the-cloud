from locust import HttpLocust, TaskSet, task
from bs4 import BeautifulSoup
from faker import Faker
from http.cookies import SimpleCookie

fake = Faker()

class Helpers:
    def parse_csrf(self, string):
        tag = BeautifulSoup(string, "html.parser").find("input", attrs={"name":"csrfmiddlewaretoken"})
        if tag is not None:
            return tag["value"]

    def post_ajax(self, url, params):
        csrf_token = self.client.cookies.get("csrftoken", "")
        response =  self.client.post(url, params, headers={"X-CSRFToken": csrf_token, "X-Requested-With": "XMLHttpRequest"})
        #These ajax responses don't have domains in the cookie so CookieJar is throwing them away
        self.store_cookies(response)
        return response

    def store_cookies(self, response):
        cookies = SimpleCookie(response.headers["Set-Cookie"])
        for key, item in cookies.items():
            self.client.cookies.set(item.key, item.value)

class VisitorBehavior(TaskSet, Helpers):
    @task
    def buy(self):
        pass

class Visitor(HttpLocust):
    task_set = VisitorBehavior
    min_wait = 5000
    max_wait = 10000

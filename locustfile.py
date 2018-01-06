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
        self.client.get("/")
        self.client.get("/products/category/apparel-1/")
        self.client.get("/products/codemash-1/")
        self.post_ajax("/products/codemash-1/add/", {"quantity":1, "variant":1 })
        response = self.client.get("/checkout/")
        csrf_token = self.parse_csrf(response.text)
        response = self.client.post("/checkout/shipping-address/", {
            "csrfmiddlewaretoken":csrf_token,
            "email":fake.email(),
            "phone":"1234567890",
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "company_name": fake.company(),
            "street_address_1": fake.street_address(),
            "street_address_2": "",
            "city": "The Land",
            "country_area": "OH",
            "postal_code": "44111",
            "country": "US",
        })
        csrf_token = self.parse_csrf(response.text)
        response = self.client.post("/checkout/shipping-method/", {
            "csrfmiddlewaretoken":csrf_token,
            "method": "1"
        })
        csrf_token = self.parse_csrf(response.text)
        response = self.client.post("/checkout/summary/", {
            "csrfmiddlewaretoken":csrf_token,
            "address": "shipping_address"
        })
        csrf_token = self.parse_csrf(response.text)
        response = self.client.post(response.url, {
            "csrfmiddlewaretoken":csrf_token,
            "method": "default"
    }, name="/order/[order-id]/payment")

class Visitor(HttpLocust):
    task_set = VisitorBehavior
    min_wait = 5000
    max_wait = 10000

from locust import HttpLocust, TaskSet, task
from http.cookies import SimpleCookie
from bs4 import BeautifulSoup
import json
import time
from faker import Faker

fake = Faker()

HOST = "http://localhost:8000"
MIN_WAIT = 5000
MAX_WAIT = 9000
USER_SPEED = 1 #higher is faster

class Helpers:
    def parse_csrf(self, string):
        tag = BeautifulSoup(string, "html.parser").find("input", attrs={"name":"csrfmiddlewaretoken"})
        if tag is not None:
            return tag["value"]

    def post_ajax(self, url, params, **kwargs):
        csrf_token = self.client.cookies.get("csrftoken", "")
        kwargs.update(headers={"X-CSRFToken": csrf_token, "X-Requested-With": "XMLHttpRequest"})
        response =  self.client.post(url, params, **kwargs)
        #These ajax responses don't have domains in the cookie so CookieJar is throwing them away
        self.store_cookies(response)
        return response

    def store_cookies(self, response):
        if not "Set-Cookie" in response.headers:
            return

        cookies = SimpleCookie(response.headers["Set-Cookie"])
        for key, item in cookies.items():
            self.client.cookies.set(item.key, item.value)

    def parse_product_links(self, string):
        links = BeautifulSoup(string, "html.parser").select(".category-list a")
        return [ link['href'] for link in links ]

    def parse_variants(self, string):
        soup = BeautifulSoup(string, "html.parser")
        variants = soup.select_one("#variant-picker")["data-variant-picker-data"]
        return json.loads(variants)["variants"]

    def generate_email(self):
        return "{}_{:f}@example.com".format(fake.user_name(), time.time())

    def simulate_user_form_fill_time(self, task_time):
        time.sleep(task_time / USER_SPEED)

class SharedTasks(Helpers):
    def register_user(self):
        response = self.client.get("/account/signup/")
        csrf_token = self.parse_csrf(response.text)
        response = self.client.post("/account/signup/", {
            "csrfmiddlewaretoken":csrf_token,
            "email":self.generate_email(),
            "password":fake.password()
        })

    def find_hoodie(self):
        self.client.get("/", name="1 home")
        self.client.get("/products/category/apparel-1/", name="2 /products/category/apparel-1/")
        self.client.get("/products/codemash-1/", name="3 /products/codemash-1/")

    def add_to_cart(self):
        self.post_ajax("/products/codemash-1/add/", {"quantity":1, "variant":1 }, name="4 products/codemash-1/add/")

    def checkout(self):
        response = self.client.get("/checkout/", name="5 /checkout/")
        csrf_token = self.parse_csrf(response.text)
        self.simulate_user_form_fill_time(30)
        response = self.client.post("/checkout/shipping-address/", {
            "csrfmiddlewaretoken":csrf_token,
            "address":"new_address",
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
        }, name="6 /checkout/shipping-address/")
        csrf_token = self.parse_csrf(response.text)
        self.simulate_user_form_fill_time(5)
        response = self.client.post("/checkout/shipping-method/", {
            "csrfmiddlewaretoken":csrf_token,
            "method": "1"
        }, name="7 /checkout/shipping-method/")
        csrf_token = self.parse_csrf(response.text)
        response = self.client.post("/checkout/summary/", {
            "csrfmiddlewaretoken":csrf_token,
            "address": "shipping_address"
        }, name="8 /checkout/summary/")
        csrf_token = self.parse_csrf(response.text)
        response = self.client.post(response.url, {
            "csrfmiddlewaretoken":csrf_token,
            "method": "default"
        }, name="9 /order/[order-id]/payment")

class VisitorBehavior(TaskSet, SharedTasks):
    @task(3)
    def just_visiting(self):
        self.client.get("/")

    @task(47)
    def search(self):
        self.find_hoodie()

    @task(25)
    def bail_on_cart(self):
        self.find_hoodie()
        self.add_to_cart()

    @task(25)
    def buy(self):
        self.find_hoodie()
        self.add_to_cart()
        self.checkout()

class ReturningUserBehavior(TaskSet, SharedTasks):
    def on_start(self):
        self.register_user()

    @task(20)
    def search(self):
        self.find_hoodie()

    @task(5)
    def bail_on_cart(self):
        self.find_hoodie()
        self.add_to_cart()

    @task(75)
    def buy(self):
        self.find_hoodie()
        self.add_to_cart()
        self.checkout()

class Visitor(HttpLocust):
    weight = 80
    task_set = VisitorBehavior
    host = HOST
    min_wait = MIN_WAIT
    max_wait = MAX_WAIT

class ReturningUser(HttpLocust):
    weight = 20
    task_set = ReturningUserBehavior
    host = HOST
    min_wait = MIN_WAIT
    max_wait = MAX_WAIT

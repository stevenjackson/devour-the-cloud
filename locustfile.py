from locust import HttpLocust, TaskSet, task
from bs4 import BeautifulSoup
from faker import Faker

fake = Faker()

class Helpers:
    def parse_csrf(self, string):
        tag = BeautifulSoup(string, "html.parser").find("input", attrs={"name":"csrfmiddlewaretoken"})
        if tag is not None:
            return tag["value"]

class VisitorBehavior(TaskSet, Helpers):
    @task
    def register_user(self):
        pass

class Visitor(HttpLocust):
    task_set = VisitorBehavior
    min_wait = 5000
    max_wait = 10000

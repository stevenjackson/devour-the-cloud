from locust import HttpLocust, TaskSet

class VisitorBehavior(TaskSet):
    def visit(self):
        self.client.get("/")

class Visitor(HttpLocust):
    task_set = VisitorBehavior

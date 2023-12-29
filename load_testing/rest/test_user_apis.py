import time
from locust import HttpUser, task, between
import random

class UserList(HttpUser):
    wait_time = between(min_wait=1, max_wait=3)
    # wait user between 1 and 3 seconds after each task

    @task
    def list_users(self):
        self.client.get("rest/users/")
        time.sleep(1)
    
    @task(weight=3)
    def get_users(self):
        self.client.get(f"rest/users/{random.randint(1, 3)}")
    
    def on_start(self):
        print("Call this on each virtual user start")
        return super().on_start()
    
    def on_end(self):
        print("Call this on each virtual user end")
        return super().on_end()


from locust import HttpUser, task, between

#locust -f fastapi_example/locust.py --class SyncAPIUser -P 25002
class SyncAPIUser(HttpUser):
    wait_time = between(0, 0)

    @task(1)
    def hit_fast_async(self):
        self.client.get("/fast")

    @task(1)
    def hit_slow_sync(self):
        self.client.get("/sync")

class AsyncAPIUser(HttpUser):
    wait_time = between(0, 0)

    @task(1)
    def hit_fast_async(self):
        self.client.get("/fast")

    @task(1)
    def hit_slow_sync(self):
        self.client.get("/async")

class BadAsyncAPIUser(HttpUser):
    wait_time = between(0, 0)

    @task(1)
    def hit_fast_async(self):
        self.client.get("/fast")

    @task(1)
    def hit_slow_sync(self):
        self.client.get("/bad-async")
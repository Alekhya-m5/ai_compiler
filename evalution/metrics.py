import time


class Metrics:

    def __init__(self):

        self.total_runs = 0
        self.successful_runs = 0
        self.failed_runs = 0

        self.total_latency = 0

    def start_timer(self):

        return time.time()

    def stop_timer(self, start):

        latency = time.time() - start

        self.total_latency += latency

        return latency

    def record_success(self):

        self.total_runs += 1

        self.successful_runs += 1

    def record_failure(self):

        self.total_runs += 1

        self.failed_runs += 1

    def report(self):

        avg_latency = 0

        if self.total_runs > 0:

            avg_latency = (
                self.total_latency /
                self.total_runs
            )

        return {
            "total_runs": self.total_runs,
            "successful_runs": self.successful_runs,
            "failed_runs": self.failed_runs,
            "success_rate": (
                self.successful_runs /
                self.total_runs * 100
            ) if self.total_runs else 0,
            "average_latency": avg_latency
        }
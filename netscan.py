from colorama import init, Fore
from requests import get
from random import randint
from threading import Thread

init(autoreset=True)


class Scan:
    def __init__(
        self: None,
        timeout: int,
        threads: int
    ) -> None:
        self.timeout = timeout
        self.threads = threads

        self.ips = {}

    @property
    def ip_addr(self: None) -> str:
        return ".".join(
            [
                str(randint(1, 225)) for _ in range(4)
            ]
        )

    def log(self: None) -> None:
        while True:
            for ip in {**self.ips}:
                print(self.ips[ip]['colour'] + ip)
                del self.ips[ip]

    def scan_internet(self: None) -> None:
        while True:
            ip_addr = self.ip_addr

            try:
                get(
                    "http://" + ip_addr,
                    timeout=self.timeout
                )

            except:
                self.ips[ip_addr] = {
                    "active": False,
                    "colour": Fore.RED
                }

            else:
                self.ips[ip_addr] = {
                    "active": True,
                    "colour": Fore.GREEN
                }

    def start(self: None) -> None:
        threads = []

        logger = Thread(target=self.log)
        logger.start()
        threads.append(logger)

        for _ in range(self.threads):
            thread = Thread(target=self.scan_internet)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

if __name__ == "__main__":
    Scan(
        timeout=15,
        threads=10000000000000000000
    ).start()
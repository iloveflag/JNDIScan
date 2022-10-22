import requests


class Dnslog:
    def __init__(self):
        self.url = "http://www.dnslog.cn"
        self.s = requests.Session()
        self.domain = self.s.get(self.url + "/getdomain.php").text

    def get_domain(self):
        return self.domain

    def get_logs(self):
        r = self.s.get(self.url + "/getrecords.php")
        return r.json()

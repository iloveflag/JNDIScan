class Template:
    def __init__(self, rhost, rport, lhost,lport):
        self.rhost = rhost
        self.rport = rport
        self.lhost = lhost
        self.lport = lport

    def encode_all(string):
        return "".join("%{0:0>2}".format(format(ord(char), "x")) for char in string)






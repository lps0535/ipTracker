class IpMapper(object):
    def ip_to_number(self,ip):
        lst = map(int, ip.split("."))
        number = 16777216*lst[0] + 65536*lst[1] + 256*lst[2] + lst[3]
        return self.search_number(number)

    def search_number(self, number):
        file = open('iplocation.csv')
        for line in file.readlines():
            start = int(line.split(',')[0].strip("\""))
            end = int(line.split(',')[1].strip("\""))
            if number >= start and number <= end:
                return line

ip = raw_input("Ip address: ")
ipObj = IpMapper()
print ipObj.ip_to_number(ip)

class CpStockCode:
    def __init__(self):
        self.stocks = {'유한양행': 'A000100'}

    def GetCount(self):
        return len(self.stocks)

    def NameToCode(self, name):
        return self.stocks[name]


# CpStockCode 클래스를 이용해 instCpStockCode 객체를 생성한 예.
# 즉, instCpStockCode 객체는 CpStockCode 클래스의 인스턴스입니다.
instCpStockCode = CpStockCode()
print(instCpStockCode.GetCount())
print(instCpStockCode.NameToCode('유한양행'))
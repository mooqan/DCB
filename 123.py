class NewYear:
    def __init__(self, name, gift):
        self.name = name
        self.gift = gift

    def neviebivaetsya(self):
        print("Hello " + self.name +
              ", this " + self.gift + " for u ")


p1 = NewYear("Sol Nur", "hudi")
p1.neviebivaetsya()

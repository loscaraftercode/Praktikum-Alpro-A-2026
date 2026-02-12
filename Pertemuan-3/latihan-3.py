#Mouse
class KelasMouse:
    def __init__(self, merek, banyakDPI, sensor, banyaktombol):
        self.merek = merek
        self.banyakDPI = banyakDPI
        self.sensor = sensor
        self.banyaktombol = banyaktombol

    def infoMouse(self):
        print("Merek        :", self.merek)
        print("DPI Maks     :", self.banyakDPI)
        print("Sensor       :", self.sensor)
        print("Jumlah Tombol:", self.banyaktombol)

    def ubahDPI(self, dpiBaru):
        self.banyakDPI = dpiBaru
        print("DPI berhasil diubah menjadi", self.banyakDPI)

    def ubahSensor(self, sensorBaru):
        self.sensor = sensorBaru
        print("Sensor berhasil diubah menjadi", self.sensor)


p1 = KelasMouse("razer", 26000, "PMW3000", 12)

p1.infoMouse()
print("----")
p1.ubahDPI(18000)
p1.ubahSensor("PMW3395")
print("----")
p1.infoMouse()


p2 = KelasMouse("Asus", 19000, "PMW3000", 9)

p2.infoMouse()
print("----")
p2.ubahSensor("PMW3050")
print("----")
p2.infoMouse()

p3 = KelasMouse("razer", 32000, "PMW3000", 16)

p1.infoMouse()
print("----")
p3.ubahDPI(18000)
p3.ubahSensor("PMW3395")
print("----")
p3.infoMouse()


#Keyboard
class KelasKeyboard:
    def __init__(self, merek, ukuran, banyakTombol, jenisSwitch):
        self.merek = merek
        self.ukuran = ukuran 
        self.banyakTombol = banyakTombol
        self.jenisSwitch = jenisSwitch

    def infoKeyboard(self):
        print("Merek        :", self.merek)
        print("ukuran       :", self.ukuran)
        print("banyakTombol :", self.banyakTombol)
        print("JenisSwitch  :", self.jenisSwitch)
    
    def ubahJenisSwitch(self, jenisSwitch):
        self.jenisSwitch = jenisSwitch
        print("Jenis Switch berhasil diubah menjadi :",self.jenisSwitch)

p1 = KelasKeyboard("Techware", 96, 103, "Red Switch")
p1.infoKeyboard()
p1.ubahJenisSwitch("Brown Switch")
p1.infoKeyboard()

#Monitor 
class kelasMonitor:
    def __init__(self, merek, ukuran, jenisLayar, RefreshRate):
        self.merek = merek
        self.ukuran = ukuran
        self.jenisLayar = jenisLayar
        self.RefreshRate = RefreshRate

    def infoMonitor(self):
        print("Merek        :", self.merek)
        print("ukuran       :", self.ukuran)
        print("jenisLayar :", self.jenisLayar)
        print("RefreshRate  :", self.RefreshRate)

    def ubahRefreshRate(self, RefreshRate):
        self.RefreshRate = RefreshRate
        print ("Refresh Rate telah diubah menjadi:", self.RefreshRate)

p1 = kelasMonitor("Acer", 27, "OLED", 340)
p1.infoMonitor()

    
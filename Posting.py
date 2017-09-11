class Jurnal():
    def __init__(self, keterangan, profit, bulan, tahun):
        self.keterangan = keterangan
        self.profit = profit
        self.bulan = bulan
        self.tahun = tahun
class Posting():
    def __init__(self, keterangan,profit,deposit, bulan, tahun):
        self.keterangan = keterangan
        self.profit = profit
        self.deposit = deposit
        self.bulan = bulan
        self.tahun = tahun

def EnterJurnal(JurnalDB):
    jurnal0= Jurnal(" Dana Triwulan",3000000000,8,2017)
    JurnalDB.append(jurnal0)
    jurnal1= Jurnal("Denda KSM",200000,9,2015)
    JurnalDB.append(jurnal1)
    jurnal2= Jurnal("Uang Bangunan",50000000,8,2014)
    JurnalDB.append(jurnal2)
    jurnal3= Jurnal("Uang Bangunan",15000000,4,2013)
    JurnalDB.append(jurnal3)
    jurnal4 = Jurnal("Dana Asrama",2500000,7,2014)
    JurnalDB.append(jurnal4)
    jurnal5 = Jurnal("pendaftaran",350000,10,2015)
    JurnalDB.append(jurnal5)

if __name__== '__main__':
    JurnalDB = []

    EnterJurnal(JurnalDB)

    PostingDB = []
    for i in range(len(JurnalDB)):
        PostingDB.append(Posting(JurnalDB[i].keterangan,JurnalDB[i].profit, 0, JurnalDB[i].bulan, JurnalDB[i].tahun))


print "Bulan - Tahun  |  Profit     -  Deposit |  Keterangan"
for i in range(len(PostingDB)):
    print " |", PostingDB[i].bulan, " - " ,PostingDB[i].tahun, " | " ,PostingDB[i].profit, "   - " ,PostingDB[i].deposit, "       | ",PostingDB[i].keterangan
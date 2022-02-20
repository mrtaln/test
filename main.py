# Verilen excel dosyasında gerekli işlemleri yapmak için Pandas kütüphanesi kullanılmıştır.
import pandas as pd 

# Verilen excel dosyası, içerisinde oluşturulan kolonlarla header hücresi olmadan okunarak "excel" isimli değişkene atanmıştır.
excel = pd.read_excel("TestCaseData.xlsx", usecols = "A:B", header=None) 

# Başlangıç ve bitiş olmak üzere iki adet (rastgele) tarih belirlenmiştir.
start_date = "2021-05-02"
end_date = "2021-06-15"

# Verilen excel dosyasındaki tarihler pandas kütüphanesindeki datetime objesine dönüştürülmüştür.
excel[0] = pd.to_datetime(excel[0])

# Belirlenen tarih aralığında sorgulama yapabilmek için boolen değerlerden mask oluşturulmuştur.
mask = (excel[0] > start_date) & (excel[0] <= end_date)

# Bu boolen değerler kullanılarak loc fonksiyonu ile 
# excel dosyası içerisindeki ilgili tarih aralığındaki 
# liste tekrardan excel değişkenine atanmıştır.
excel = excel.loc[mask]

# Belirlenen tarih aralığındaki değerlerin min ve max değerlerinin indexleri bulunmuş ve ilgili değişkenlere atanmıştır.
minValueIndexObj = excel[1].idxmin()
maxValueIndexObj = excel[1].idxmax()

# Min ve max değerlerin indexleri ile ilgili tarihler değişkenlere atanmıştır.
dateValueMin = excel[0][minValueIndexObj]
dateValueMax = excel[0][maxValueIndexObj]

# İlgili tarih aralığındaki değerlerin tümü, bu değerlerin toplamı ve min/max değerlerin tarihleri konsola yazdırılmıştır. 
print("İlgili tarih araligindaki tum degerler: ", excel)
print("İlgili tarih araligindeki degerlerin toplami: ", excel[1].sum())
print("Minimum degerin tarihi: ", dateValueMin)
print("Maksimum degerin tarihi: ", dateValueMax)
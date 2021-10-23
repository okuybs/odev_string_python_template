YBS401-2021-fall-2
Ödev kapsamında yapmanız gereken:
aşağıdaki fonksiyonların içeriklerini düzeltmenizdir.
hazırlayan @aucan
Öğrenci Ad Soyad=İsmail Uzundağ   
Öğrenci No=2017507025 
Bölüm=YBS
Sınıf=4.Sınıf
'''

def format_string():
    '''
    Fonksiyonun geri dönüş değeri 
    "Adı:Ali,Soyadı:Yılmaz,Yaşı:20"
    olacak şekilde eksik kısımları doldurmanızdır. (1 puan)
    Sadece #------**------ işareti ile belirtilen 
    kısımlar arasını değiştiriniz. 
    text değişkenini string format fonksiyonu ile doldurmanız beklenmektedir.
    '''
    name = "Ali"
    surname = "Yılmaz"
    birth = 2001
    #-------**-----------
    
    age=2021-birth
    text="Adı:{},Soyadı:{},Yaşı:{}".format(name,surname,age)
    
    
    
    #-------**-----------
    return text


def concat_string():
    '''
    Fonksiyonun geri dönüş değeri 
    "29 Ekim Cumhuriyet Bayramımız Kutlu Olsun!"
    olacak şekilde eksik kısımları doldurmanızdır. (1 puan)
    Sadece #------**------ işareti ile belirtilen 
    kısımlar arasını değiştiriniz. 
    text değişkeni içerisini str1 str2 str3 değişkenlerini uygun hale getirip birleştirerek doldurmanız beklenmektedir.
    Küçük BÜYÜK harfe, boşluklara, str+number hatasına ve birleştirme sırasına dikkat ediniz.
    '''
    str1 = "  kutlu olsun!          "
    str2 = "    ekim cumhuriyet bayramımız    "
    str3 = 29
    #-------**-----------
    
    a=str2.strip()
    b=str1.strip()
    c=str(str3)
    text="{} {} {}".format(c.title(),a.title(),b.title())

    #-------**-----------
    return text


def slice_string():
    '''
    Fonksiyonun geri dönüş değeri 
    "deF!N!567%&/_"
    olacak şekilde eksik kısımları doldurmanızdır. (1 puan)
    Sadece #------**------ işareti ile belirtilen 
    kısımlar arasını değiştiriniz. 
    text değişkeni içerisini numbers aplhabets signs değişkenlerini uygun hale getirip birleştirerek doldurmanız beklenmektedir.
    Küçük BÜYÜK harfe ve birleştirme sırasına dikkat ediniz.
    Slicing Strings bölümünde öğrendiğiniz gibi yapmanız gerekmektedir. 
    örneğin "ABC012.," için 
    text = alphabets[0:3] + numbers[0:3] + signs[0:2] 
    '''
    numbers = "0123456789"
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    signs = ".,!'^+$%&/()=?*-_"
    #-------**-----------
    
    a=alphabets.lower()
    text=a[3:5]+alphabets[5:6]+signs[2:3]+alphabets[13:14]+signs[2:3]+numbers[5:8]+signs[7:10]+signs[16:]
    
    
    
    
    #-------**-----------
    return text



def replace_string():
    '''
    Fonksiyonun geri dönüş değeri 
    "Korkut Ata Üniversitesi bölgenin en iyisidir."
    olacak şekilde eksik kısımları doldurmanızdır. (1 puan)
    Sadece #------**------ işareti ile belirtilen 
    kısımlar arasını değiştiriniz. 
    text değişkeni içerisini first_text,searchv,replacev değişkenlerini uygun hale getirip doldurmanız beklenmektedir.
    Küçük BÜYÜK harfe dikkat ediniz.
    Replace Strings bölümünde öğrendiğiniz gibi yapmanız gerekmektedir.  
    '''
    first_text = "Çukurova Üniversitesi bölgenin en iyisidir." #orjinal metin
    searchv = "çukurova" #aranan ifade
    replacev = "korkut ata" #değişecek ifade
    #-------**-----------
    
    
    a=replacev.title()
    text=first_text.replace("Çukurova",a)
    
    
    #-------**-----------
    return text


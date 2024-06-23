from django.db import models


class GenelBilgilerLast2024(models.Model):
    id = models.BigIntegerField(primary_key=True)
    pro_code = models.TextField(blank=True, null=True)
    bolum_adi = models.TextField(blank=True, null=True)
    number_0_12_0_06_katsayı_ile_yerleşen_son_kişinin_başarı_sıras = models.TextField(db_column='0,12 + 0,06 Katsayı ile Yerleşen Son Kişinin Başarı Sıras', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_0_12_0_06_katsayı_ile_yerleşen_son_kişinin_puanı_field = models.TextField(db_column='0,12 + 0,06 Katsayı ile Yerleşen Son Kişinin Puanı*', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    number_0_12_katsayı_ile_yerleşen_son_kişinin_başarı_sırası_field = models.TextField(db_column='0,12 Katsayı ile Yerleşen Son Kişinin Başarı Sırası*', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    number_0_12_katsayı_ile_yerleşen_son_kişinin_puanı_field = models.TextField(db_column='0,12 Katsayı ile Yerleşen Son Kişinin Puanı*', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    obp_si_kırılarak_yerleşen_sayısı = models.TextField(db_column="OBP'si Kırılarak Yerleşen Sayısı", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tavan_basari_sirasi_0_12_field = models.TextField(db_column='Tavan_Basari_Sirasi_(0,12)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    tavan_puan_0_12_field = models.TextField(db_column='Tavan_Puan_(0,12)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    boş_kalan_kontenjan = models.TextField(db_column='Boş Kalan Kontenjan', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    burs_türü = models.TextField(db_column='Burs Türü', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ek_yerleşen = models.TextField(db_column='Ek Yerleşen', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fakülte_yüksekokul = models.TextField(db_column='Fakülte / Yüksekokul', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    genel_kontenjan = models.TextField(db_column='Genel Kontenjan', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    genel_kontenjana_yerleşen = models.TextField(db_column='Genel Kontenjana Yerleşen', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    okul_birincisi_kontenjanı = models.TextField(db_column='Okul Birincisi Kontenjanı', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    okul_birincisi_kontenjanına_yerleşen = models.TextField(db_column='Okul Birincisi Kontenjanına Yerleşen', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    puan_türü = models.TextField(db_column='Puan Türü', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    toplam_kontenjan = models.TextField(db_column='Toplam Kontenjan', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    toplam_yerleşen = models.TextField(db_column='Toplam Yerleşen', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    yerleşenlerin_ortalama_diploma_notu = models.TextField(db_column='Yerleşenlerin Ortalama Diploma Notu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    yerleşenlerin_ortalama_obp_si = models.TextField(db_column="Yerleşenlerin Ortalama OBP'si", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    yerleşip_kayıt_yaptırmayan = models.TextField(db_column='Yerleşip Kayıt Yaptırmayan', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ösym_program_kodu = models.TextField(db_column='ÖSYM Program Kodu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    üniversite = models.TextField(db_column='Üniversite', blank=True, null=True)  # Field name made lowercase.
    üniversite_türü = models.TextField(db_column='Üniversite Türü', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    i_lk_yerleşme_oranı = models.TextField(db_column='İlk Yerleşme Oranı', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    yil = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genel_bilgiler_last_2024'


class HacettepeData(models.Model):
    year = models.IntegerField(blank=True, null=True)
    number = models.CharField(blank=True, null=True)
    gecen_yildan_degisim = models.CharField(blank=True, null=True)
    universite = models.CharField()
    sehir = models.CharField()
    fakulte_veya_bolum = models.CharField()
    puan_turu = models.CharField(blank=True, null=True)
    toplam_kontenjan_ve_gecen_yildan_farki = models.CharField(blank=True, null=True)
    toplam_yerlesen = models.CharField(blank=True, null=True)
    genel_kontenjan_en_dusuk_puan = models.CharField(blank=True, null=True)
    genel_kontenjan_en_yuksek_puan = models.CharField(blank=True, null=True)
    genel_kontenjan_en_dusuk_siralama_ve_bir_onceki_yildan_farki = models.CharField(blank=True, null=True)
    empty_area1 = models.CharField(blank=True, null=True)
    empty_area2 = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hacettepe_data'
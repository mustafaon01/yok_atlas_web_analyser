from django.db import models


class GeneralInformation(models.Model):
    id = models.BigIntegerField(primary_key=True)
    pro_code = models.TextField(blank=True, null=True)
    bolum_adi = models.TextField(blank=True, null=True)
    number_0_12_0_06_katsayı_ile_yerleşen_son_kişinin_başarı_sıras = models.TextField(
        db_column='0,12 + 0,06 Katsayı ile Yerleşen Son Kişinin Başarı Sıras', blank=True, null=True)
    number_0_12_0_06_katsayı_ile_yerleşen_son_kişinin_puanı_field = models.TextField(
        db_column='0,12 + 0,06 Katsayı ile Yerleşen Son Kişinin Puanı*', blank=True, null=True)
    number_0_12_katsayı_ile_yerleşen_son_kişinin_başarı_sırası_field = models.TextField(
        db_column='0,12 Katsayı ile Yerleşen Son Kişinin Başarı Sırası*', blank=True, null=True)
    number_0_12_katsayı_ile_yerleşen_son_kişinin_puanı_field = models.TextField(
        db_column='0,12 Katsayı ile Yerleşen Son Kişinin Puanı*', blank=True, null=True)
    obp_si_kırılarak_yerleşen_sayısı = models.TextField(db_column="OBP'si Kırılarak Yerleşen Sayısı", blank=True,
                                                        null=True)
    tavan_basari_sirasi_0_12_field = models.TextField(db_column='Tavan_Basari_Sirasi_(0,12)', blank=True, null=True)
    tavan_puan_0_12_field = models.TextField(db_column='Tavan_Puan_(0,12)', blank=True, null=True)
    boş_kalan_kontenjan = models.TextField(db_column='Boş Kalan Kontenjan', blank=True, null=True)
    burs_türü = models.TextField(db_column='Burs Türü', blank=True, null=True)
    ek_yerleşen = models.TextField(db_column='Ek Yerleşen', blank=True, null=True)
    fakülte_yüksekokul = models.TextField(db_column='Fakülte / Yüksekokul', blank=True, null=True)
    genel_kontenjan = models.TextField(db_column='Genel Kontenjan', blank=True, null=True)
    genel_kontenjana_yerleşen = models.TextField(db_column='Genel Kontenjana Yerleşen', blank=True, null=True)
    okul_birincisi_kontenjanı = models.TextField(db_column='Okul Birincisi Kontenjanı', blank=True, null=True)
    okul_birincisi_kontenjanına_yerleşen = models.TextField(db_column='Okul Birincisi Kontenjanına Yerleşen',
                                                            blank=True, null=True)
    puan_türü = models.TextField(db_column='Puan Türü', blank=True, null=True)
    toplam_kontenjan = models.TextField(db_column='Toplam Kontenjan', blank=True, null=True)
    toplam_yerleşen = models.TextField(db_column='Toplam Yerleşen', blank=True, null=True)
    yerleşenlerin_ortalama_diploma_notu = models.TextField(db_column='Yerleşenlerin Ortalama Diploma Notu', blank=True,
                                                           null=True)
    yerleşenlerin_ortalama_obp_si = models.TextField(db_column="Yerleşenlerin Ortalama OBP'si", blank=True, null=True)
    yerleşip_kayıt_yaptırmayan = models.TextField(db_column='Yerleşip Kayıt Yaptırmayan', blank=True, null=True)
    ösym_program_kodu = models.TextField(db_column='ÖSYM Program Kodu', blank=True, null=True)
    üniversite = models.TextField(db_column='Üniversite', blank=True, null=True)
    üniversite_türü = models.TextField(db_column='Üniversite Türü', blank=True, null=True)
    i_lk_yerleşme_oranı = models.TextField(db_column='İlk Yerleşme Oranı', blank=True, null=True)
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


class HighSchoolTable(models.Model):
    id = models.BigIntegerField(blank=False, null=False, primary_key=True)
    pro_code = models.BigIntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    university = models.TextField(blank=True, null=True)
    major_name = models.TextField(blank=True, null=True)
    university_type = models.TextField(blank=True, null=True)
    grade_type = models.TextField(blank=True, null=True)
    scholarship_type = models.TextField(blank=True, null=True)
    hihg_school = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    district = models.TextField(blank=True, null=True)
    new_graduate = models.TextField(blank=True, null=True)
    old_graduate = models.TextField(blank=True, null=True)
    total = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'high_school_table'


class VwPreferenceTendencySamePrograms(models.Model):
    id = models.BigIntegerField(blank=False, null=False, primary_key=True)
    üniversite = models.TextField(db_column='Üniversite', blank=True, null=True)
    bolum_adi = models.TextField(blank=True, null=True)
    pro_code = models.BigIntegerField(blank=True, null=True)
    yil = models.BigIntegerField(blank=True, null=True)
    program = models.TextField(db_column='Program', blank=True, null=True)
    tercih_sayısı = models.TextField(db_column='Tercih Sayısı', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vw_preference_tendency_same_programs'


class TercihSihirbazi(models.Model):
    id = models.BigIntegerField(blank=False, null=False, primary_key=True)
    yop_kodu = models.TextField(blank=True, null=True)
    universite = models.TextField(blank=True, null=True)
    fakulte = models.TextField(blank=True, null=True)
    program_adi = models.TextField(blank=True, null=True)
    sehir = models.TextField(blank=True, null=True)
    universite_turu = models.TextField(blank=True, null=True)
    ucret_burs = models.TextField(blank=True, null=True)
    puan_turu = models.TextField(blank=True, null=True)
    ogretim_turu = models.TextField(blank=True, null=True)
    yil = models.TextField(blank=True, null=True)
    doluluk_statu = models.TextField(blank=True, null=True)
    kontenjan = models.TextField(blank=True, null=True)
    taban_puan = models.FloatField(blank=True, null=True)
    tbs = models.TextField(blank=True, null=True)
    yerlesen = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tercih_sihirbazi'

def hesapla_kalori(yas, boy, kilo, cinsiyet, aktivite):
      if cinsiyet == "Erkek":
          bmr = 88.362 + (13.397 * float(kilo)) + (4.799 * float(boy)) - (5.677 * float(yas))
      elif cinsiyet == "Kadın":
          bmr = 447.593 + (9.247 * float(kilo)) + (3.098 * float(boy)) - (4.330 * float(yas))
      else:
          raise ValueError("Cinsiyet belirtilmeli: 'Erkek' veya 'Kadın'")

      if aktivite == "Hiç yok":
          kalori_ihtiyaci = bmr * 1.2
      elif aktivite == "Az":
          kalori_ihtiyaci = bmr * 1.375
      elif aktivite == "Orta seviye":
          kalori_ihtiyaci = bmr * 1.55
      elif aktivite == "Fazla":
          kalori_ihtiyaci = bmr * 1.725
      elif aktivite == "Çok fazla":
          kalori_ihtiyaci = bmr * 1.9
      else:
          raise ValueError("Hareket düzeyi belirtilmeli")

      return int(kalori_ihtiyaci)
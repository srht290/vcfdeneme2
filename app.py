import pandas as pd

# Excel dosyasını oku
excel_file = 'contacts.xlsx'  # Excel dosyasının adı
df = pd.read_excel(excel_file)

# VCF dosyasını oluşturmak için bir fonksiyon tanımlayın
def create_vcf_record(name, phone, email):
    return f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
END:VCARD
"""

# VCF dosyasını oluşturun
vcf_file = 'contacts.vcf'
with open(vcf_file, 'w') as vcf:
    for index, row in df.iterrows():
        name = row['Name']  # Excel'deki isim sütununun adı
        phone = row['Phone']  # Excel'deki telefon sütununun adı
        email = row['Email']  # Excel'deki e-posta sütununun adı
        vcf.write(create_vcf_record(name, phone, email))
        
print(f"VCF dosyası '{vcf_file}' olarak kaydedildi.")

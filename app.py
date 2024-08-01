import pandas as pd

# Excel dosyasının yolu
excel_file = 'contacts.xlsx'

# Excel dosyasını oku
df = pd.read_excel(excel_file)

# VCard kaydını oluşturma fonksiyonu
def create_vcf_record(name, surname, phone, email, photo_url):
    photo_line = f"PHOTO;VALUE=URI:{photo_url}" if pd.notna(photo_url) else ""
    return f"""BEGIN:VCARD
VERSION:3.0
FN:{name} {surname}
TEL;TYPE=CELL:{phone}
EMAIL:{email}
{photo_line}
END:VCARD
"""

# VCF dosyasının adı
vcf_file = 'contacts.vcf'

# VCF dosyasını yazma
with open(vcf_file, 'w') as vcf:
    for index, row in df.iterrows():
        name = row['First Name']
        surname = row['Last Name']
        phone = row['Mobile Phone']
        email = row['E-mail Address']
        photo_url = row.get('Photo URL', '')  # Fotoğraf URL'si
        vcf.write(create_vcf_record(name, surname, phone, email, photo_url))

print(f"VCF dosyası '{vcf_file}' olarak kaydedildi.")

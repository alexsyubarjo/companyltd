import os

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

index_content = read_file('index.html')

# Extract header
header_start = index_content.find('<!-- 2. Header -->')
header_end = index_content.find('  <main>')
header = index_content[header_start:header_end]

# Modify header navigation for subpages (e.g., #solusi -> index.html#solusi)
header = header.replace('href="#solusi"', 'href="index.html#solusi"')
header = header.replace('href="#proses"', 'href="index.html#proses"')
header = header.replace('href="#studi-kasus"', 'href="index.html#studi-kasus"')
header = header.replace('href="#harga"', 'href="index.html#harga"')
header = header.replace('href="#faq"', 'href="index.html#faq"')
header = header.replace('href="#kontak"', 'href="index.html#kontak"')
header = header.replace('href="#audit"', 'href="index.html#audit"')
header = header.replace('href="#"', 'href="index.html"')

# Extract footer
footer_start = index_content.find('<!-- 14. Footer -->')
footer_end = index_content.find('</html>')
footer = index_content[footer_start:footer_end]

# Modify footer navigation for subpages
footer = footer.replace('href="#solusi"', 'href="index.html#solusi"')
footer = footer.replace('href="#proses"', 'href="index.html#proses"')
footer = footer.replace('href="#studi-kasus"', 'href="index.html#studi-kasus"')
footer = footer.replace('href="#harga"', 'href="index.html#harga"')
footer = footer.replace('href="#faq"', 'href="index.html#faq"')
footer = footer.replace('href="#kontak"', 'href="index.html#kontak"')
footer = footer.replace('href="#audit"', 'href="index.html#audit"')
footer = footer.replace('href="#"', 'href="index.html"')


def generate_page(filename, title, description, benefits):
    benefits_html = ""
    for benefit in benefits:
        benefits_html += f'''
          <article class="problem-card">
            <h3>{benefit["title"]}</h3>
            <p>{benefit["desc"]}</p>
          </article>'''

    html = f'''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} — alexsyubarjoltd</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="icon" href="/favicon.ico" sizes="any" />
  <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
  <link rel="icon" type="image/png" sizes="48x48" href="/favicon-48.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  {header}
  <main style="padding-top: 100px;">
    <section class="section section-alt hero">
      <div class="container center">
        <span class="eyebrow">Layanan Kami</span>
        <h1>{title}</h1>
        <p class="hero-sub" style="margin: 0 auto; max-width: 800px;">{description}</p>
        <div style="margin-top: 32px;">
           <a href="index.html#kontak" class="btn btn-primary">Mulai Konsultasi</a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-header center">
          <h2>Kenapa Memilih Layanan Ini?</h2>
        </div>
        <div class="problem-grid">
           {benefits_html}
        </div>
      </div>
    </section>
  </main>
  {footer}
</html>'''
    write_file(filename, html)

pages = [
    {
        "filename": "company-profile.html",
        "title": "Website Company Profile",
        "description": "Bangun kredibilitas bisnis Anda dengan website company profile yang profesional, responsif, dan mencerminkan identitas brand yang kuat.",
        "benefits": [
            {"title": "Desain Profesional", "desc": "Tampilan modern yang meningkatkan kepercayaan klien."},
            {"title": "Responsif & Cepat", "desc": "Website optimal diakses dari smartphone maupun desktop."},
            {"title": "SEO Dasar", "desc": "Struktur website yang ramah terhadap mesin pencari Google."}
        ]
    },
    {
        "filename": "ecommerce.html",
        "title": "Website E-Commerce",
        "description": "Tingkatkan penjualan dengan platform toko online yang memiliki fitur keranjang belanja, payment gateway, dan manajemen produk yang mudah.",
        "benefits": [
            {"title": "Payment Gateway", "desc": "Terima pembayaran secara otomatis melalui transfer bank dan e-wallet."},
            {"title": "Manajemen Produk", "desc": "Kelola stok, harga, dan katalog produk dengan mudah."},
            {"title": "Pengalaman Belanja Mulus", "desc": "Proses checkout yang ringkas untuk mengurangi cart abandonment."}
        ]
    },
    {
        "filename": "landing-page.html",
        "title": "Landing Page Campaign",
        "description": "Halaman khusus yang dirancang dengan teknik copywriting dan desain yang fokus untuk memaksimalkan tingkat konversi dari iklan Anda.",
        "benefits": [
            {"title": "Fokus Konversi", "desc": "Tata letak dan Call-To-Action yang dioptimalkan untuk hasil maksimal."},
            {"title": "A/B Testing Ready", "desc": "Struktur yang mudah diuji untuk menemukan formula pemenang."},
            {"title": "Loading Kilat", "desc": "Memastikan pengunjung dari iklan tidak kabur karena loading lambat."}
        ]
    },
    {
        "filename": "web-app.html",
        "title": "Web App Development",
        "description": "Sistem informasi, dashboard, atau portal custom yang dibangun sesuai dengan alur kerja bisnis Anda untuk meningkatkan efisiensi operasional.",
        "benefits": [
            {"title": "Custom Sesuai Kebutuhan", "desc": "Disesuaikan persis dengan proses bisnis perusahaan Anda."},
            {"title": "Skalabilitas", "desc": "Dibangun menggunakan teknologi modern yang siap tumbuh bersama bisnis."},
            {"title": "Keamanan Data", "desc": "Penerapan standar keamanan untuk melindungi data sensitif internal."}
        ]
    },
    {
        "filename": "pentesting.html",
        "title": "Security Pentesting",
        "description": "Simulasi serangan siber yang komprehensif untuk menemukan dan menutup celah keamanan sebelum dieksploitasi oleh pihak yang tidak bertanggung jawab.",
        "benefits": [
            {"title": "Simulasi Dunia Nyata", "desc": "Menggunakan metode serangan yang biasa dilakukan oleh hacker."},
            {"title": "Identifikasi Risiko", "desc": "Menemukan celah sebelum menjadi masalah besar yang merugikan."},
            {"title": "Laporan Detil", "desc": "Laporan eksekutif dan teknis beserta rekomendasi perbaikan."}
        ]
    },
    {
        "filename": "vulnerability.html",
        "title": "Vulnerability Assessment",
        "description": "Pemindaian menyeluruh terhadap infrastruktur digital Anda untuk mengidentifikasi kerentanan keamanan secara sistematis dan berkala.",
        "benefits": [
            {"title": "Deteksi Dini", "desc": "Pemindaian cepat untuk menemukan kelemahan umum."},
            {"title": "Skoring Risiko", "desc": "Penilaian kerentanan berdasarkan standar CVSS."},
            {"title": "Cost Effective", "desc": "Cara efisien untuk memantau keamanan sistem secara rutin."}
        ]
    },
    {
        "filename": "audit-infrastruktur.html",
        "title": "Audit Infrastruktur Digital",
        "description": "Evaluasi dan peninjauan mendalam terhadap konfigurasi server, jaringan, dan arsitektur cloud untuk memastikan keamanan standar industri.",
        "benefits": [
            {"title": "Tinjauan Arsitektur", "desc": "Memastikan desain sistem tahan terhadap gangguan dan serangan."},
            {"title": "Hardening Server", "desc": "Rekomendasi konfigurasi untuk memperkuat pertahanan server."},
            {"title": "Compliance Check", "desc": "Membantu memastikan sistem mematuhi standar keamanan terkait."}
        ]
    },
    {
        "filename": "maintenance.html",
        "title": "Maintenance & Hardening",
        "description": "Layanan pemeliharaan berkelanjutan, pembaruan keamanan, dan optimasi performa agar website Anda selalu dalam kondisi terbaik.",
        "benefits": [
            {"title": "Pembaruan Berkala", "desc": "Selalu mendapatkan versi software dan patch keamanan terbaru."},
            {"title": "Backup Rutin", "desc": "Cadangan data berkala agar bisnis bisa segera pulih jika terjadi insiden."},
            {"title": "Monitoring 24/7", "desc": "Pemantauan uptime dan deteksi anomali pada sistem Anda."}
        ]
    }
]

for page in pages:
    generate_page(page["filename"], page["title"], page["description"], page["benefits"])
    print(f"Generated {page['filename']}")

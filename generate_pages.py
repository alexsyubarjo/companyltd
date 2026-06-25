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
            {"title": "Desain Profesional Custom", "desc": "Tampilan modern yang unik dan disesuaikan dengan identitas brand Anda."},
            {"title": "Responsif & Cepat", "desc": "Website yang dioptimalkan sepenuhnya agar lancar diakses dari smartphone, tablet, maupun desktop."},
            {"title": "Struktur Ramah SEO", "desc": "Optimasi dasar struktur HTML agar halaman Anda lebih mudah dirayap dan mendapatkan ranking di Google."},
            {"title": "Integrasi Kontak & WhatsApp", "desc": "Mempermudah calon pelanggan untuk langsung menghubungi sales team Anda lewat tombol interaktif."},
            {"title": "Google Analytics & Tracking", "desc": "Lacak jumlah pengunjung, asal lalu lintas, dan perilaku pengunjung untuk strategi pemasaran Anda."}
        ]
    },
    {
        "filename": "ecommerce.html",
        "title": "Website E-Commerce",
        "description": "Tingkatkan penjualan dengan platform toko online yang memiliki fitur katalog produk, keranjang belanja, dan checkout yang mulus.",
        "benefits": [
            {"title": "Integrasi Payment Gateway", "desc": "Terima pembayaran otomatis via Transfer Bank, Virtual Account, Kartu Kredit, dan E-Wallet (Gopay, OVO, dll)."},
            {"title": "Manajemen Produk Intuitif", "desc": "Kelola kategori produk, varian warna/ukuran, harga promo, dan stok barang secara mandiri dengan mudah."},
            {"title": "Pengalaman Belanja Mulus", "desc": "Desain alur checkout yang dipersingkat untuk meminimalkan pembatalan keranjang belanja (cart abandonment)."},
            {"title": "Kalkulator Ongkir Otomatis", "desc": "Terintegrasi dengan API ekspedisi lokal (JNE, J&T, SiCepat) untuk menghitung ongkir real-time."},
            {"title": "Laporan Penjualan Otomatis", "desc": "Dashboard statistik untuk memantau produk terlaris, pendapatan harian, dan tren transaksi."}
        ]
    },
    {
        "filename": "landing-page.html",
        "title": "Landing Page Campaign",
        "description": "Halaman khusus yang dirancang dengan teknik copywriting dan tata letak fokus konversi untuk memaksimalkan ROI iklan Anda.",
        "benefits": [
            {"title": "Copywriting Persuasif", "desc": "Teks penawaran yang dirancang khusus untuk memengaruhi psikologi pembeli dan meningkatkan penjualan."},
            {"title": "Kecepatan Loading Ekstra", "desc": "Dioptimalkan agar terbuka kurang dari 2 detik demi menjaga calon pembeli dari iklan berbayar Anda tidak kabur."},
            {"title": "Form Leads Teroptimasi", "desc": "Form input data yang ringkas untuk mengumpulkan kontak potensial (nama, email, nomor HP) dengan mudah."},
            {"title": "Tracking Pixel & Tag Ready", "desc": "Siap dipasang Google Tag, Facebook Pixel, atau TikTok Pixel untuk melacak konversi iklan dengan akurat."},
            {"title": "A/B Testing Friendly", "desc": "Struktur kode yang bersih dan teratur memudahkan pengujian berbagai variasi headline dan tombol CTA."}
        ]
    },
    {
        "filename": "web-app.html",
        "title": "Web App Development",
        "description": "Sistem informasi, dashboard custom, atau portal klien yang dibangun khusus untuk meningkatkan efisiensi operasional bisnis Anda.",
        "benefits": [
            {"title": "Solusi Kustom & Spesifik", "desc": "Dibangun persis mengikuti alur kerja (workflow) unik dan kebutuhan bisnis internal perusahaan Anda."},
            {"title": "Arsitektur Scalable", "desc": "Menggunakan framework JavaScript modern untuk memastikan performa tetap prima seiring bertambahnya data."},
            {"title": "Keamanan Data End-to-End", "desc": "Dilengkapi dengan autentikasi multi-level dan enkripsi database untuk melindungi data sensitif perusahaan."},
            {"title": "Integrasi API Pihak Ketiga", "desc": "Hubungkan aplikasi Anda dengan layanan luar seperti CRM, sistem inventaris, atau API pihak ketiga lainnya."},
            {"title": "Dashboard Visual Dinamis", "desc": "Sajikan data bisnis dalam bentuk grafik dan tabel interaktif untuk mempermudah pengambilan keputusan."}
        ]
    },
    {
        "filename": "pentesting.html",
        "title": "Security Pentesting",
        "description": "Simulasi serangan siber nyata yang komprehensif untuk mendeteksi celah keamanan sistem sebelum disalahgunakan hacker.",
        "benefits": [
            {"title": "Metode Serangan Riil", "desc": "Menguji pertahanan sistem menggunakan teknik-teknik penetrasi terbaru yang biasa dipakai hacker black-hat."},
            {"title": "Deteksi Celah Kritis", "desc": "Menemukan celah keamanan tersembunyi (seperti SQLi, XSS, SSRF) sebelum dieksploitasi pihak luar."},
            {"title": "Laporan Teknis Mendalam", "desc": "Dokumentasi langkah demi langkah eksploitasi celah beserta instruksi remediasi untuk tim developer Anda."},
            {"title": "Rekomendasi Remediasi", "desc": "Panduan konkret tentang cara menambal setiap kerentanan yang ditemukan agar sistem benar-benar aman."},
            {"title": "Sertifikat Kepatuhan", "desc": "Memberikan bukti dokumentasi audit keamanan yang berguna untuk kepatuhan regulasi atau audit eksternal."}
        ]
    },
    {
        "filename": "vulnerability.html",
        "title": "Vulnerability Assessment",
        "description": "Pemindaian dan evaluasi sistematis terhadap seluruh sistem digital Anda untuk mendeteksi kerentanan keamanan secara berkala.",
        "benefits": [
            {"title": "Scan Kerentanan Otomatis", "desc": "Pemindaian menyeluruh ke seluruh port, server, dan web app untuk mendeteksi celah keamanan umum."},
            {"title": "Skoring Risiko Terstandar", "desc": "Mengklasifikasikan tingkat keparahan risiko berdasarkan skor standar industri global (CVSS)."},
            {"title": "Laporan Inventaris Aset", "desc": "Memetakan seluruh aset digital yang Anda miliki beserta status keamanannya saat ini."},
            {"title": "Efisiensi Biaya (Cost-Effective)", "desc": "Cara yang sangat efisien dan terjangkau untuk melakukan pengecekan kesehatan keamanan sistem secara rutin."},
            {"title": "Rencana Aksi Mitigasi", "desc": "Daftar prioritas kerentanan yang harus segera diperbaiki berdasarkan tingkat bahayanya."}
        ]
    },
    {
        "filename": "audit-infrastruktur.html",
        "title": "Audit Infrastruktur Digital",
        "description": "Evaluasi mendalam terhadap arsitektur server, konfigurasi jaringan, dan setup cloud untuk memastikan efisiensi dan kepatuhan standar industri.",
        "benefits": [
            {"title": "Analisis Arsitektur Cloud/Server", "desc": "Evaluasi ketahanan, keamanan, dan skalabilitas setup cloud (AWS, GCP, Azure) atau VPS Anda."},
            {"title": "Review Kebijakan Akses (IAM)", "desc": "Memastikan prinsip hak akses minimum (least privilege) diterapkan secara ketat di infrastruktur Anda."},
            {"title": "Optimasi Biaya Server", "desc": "Mengidentifikasi pemborosan sumber daya server untuk membantu menghemat pengeluaran bulanan cloud Anda."},
            {"title": "Penyelarasan Kepatuhan (Compliance)", "desc": "Membantu sistem Anda memenuhi standar keamanan industri (seperti ISO 27001 atau PCI-DSS)."},
            {"title": "Rekomendasi Disaster Recovery", "desc": "Menyusun rencana backup dan pemulihan darurat agar bisnis tetap berjalan saat terjadi insiden server down."}
        ]
    },
    {
        "filename": "maintenance.html",
        "title": "Maintenance & Hardening",
        "description": "Layanan pemeliharaan berkelanjutan, pembaruan keamanan, dan optimasi performa agar website Anda selalu dalam kondisi terbaik.",
        "benefits": [
            {"title": "Pembaruan & Patching Rutin", "desc": "Update rutin engine CMS, framework, plugin, dan library untuk menutup celah keamanan baru yang rilis."},
            {"title": "Backup Otomatis & Terenkripsi", "desc": "Cadangkan seluruh database dan file website secara rutin ke server penyimpanan terpisah yang aman."},
            {"title": "Monitoring Uptime 24/7", "desc": "Pemantauan status website Anda tanpa henti dengan notifikasi instan jika terjadi gangguan akses."},
            {"title": "Pengerasan Keamanan (Hardening)", "desc": "Memperkuat server dengan firewall khusus, penutupan port yang tidak terpakai, dan pemblokiran brute-force."},
            {"title": "Pembersihan & Deteksi Malware", "desc": "Pemindaian rutin terhadap file server untuk mendeteksi dan membersihkan file berbahaya (backdoor/malware)."}
        ]
    }
]

for page in pages:
    generate_page(page["filename"], page["title"], page["description"], page["benefits"])
    print(f"Generated {page['filename']}")

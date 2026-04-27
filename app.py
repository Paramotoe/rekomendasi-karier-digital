import streamlit as st

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Sistem Cerdas Karier Digital",
    page_icon="💼",
    layout="centered"
)

# =========================
# SIDEBAR
# =========================
st.sidebar.title("💡 Tentang Sistem")
st.sidebar.write(
    """
    Aplikasi ini adalah **sistem cerdas berbasis aturan (rule-based)** 
    yang membantu memberikan rekomendasi jalur karier digital 
    yang selaras dengan profil dan preferensi pengguna.

    Sistem mempertimbangkan beberapa aspek utama:
    - Minat dan gaya kerja
    - Kemampuan teknis
    - Konsistensi dan ketersediaan waktu
    - Kondisi perangkat & bahasa
    - Tujuan penghasilan
    """
)

st.sidebar.markdown("---")
st.sidebar.write(
    """
    ⚙️ **Catatan Teknis:**
    - Sistem tidak menggunakan machine learning.
    - Semua keputusan dihasilkan dari kumpulan **aturan IF–THEN** 
      yang dapat diaudit dan dijelaskan kembali.
    """
)

# =========================
# HEADER
# =========================
st.title("💼 Sistem Cerdas Rekomendasi Karier Digital")

st.write(
    """
    Dunia kerja saat ini banyak bergeser ke arah **karier digital**: 
    content creator, freelance designer, developer remote, online tutor, social media specialist, dan banyak lagi.

    Di sisi lain, banyak orang sebenarnya punya potensi,
    tetapi merasa **malu, ragu, atau belum percaya diri** untuk mulai.

    Sistem ini dirancang sebagai **alat bantu pengambilan keputusan**:
    bukan untuk memutuskan hidup kamu, tetapi untuk memberikan **gambaran rasional** 
    tentang jalur yang paling mungkin cocok berdasarkan jawabanmu.
    """
)

st.markdown("---")

# =========================
# INPUT DATA
# =========================
st.header("👤 Profil & Preferensi Kamu")

nama = st.text_input("Nama lengkap atau panggilan:")

col1, col2 = st.columns(2)

with col1:
    minat = st.selectbox(
        "Minat utama di dunia digital:",
        [
            "Konten & media (video, sosial media)",
            "Desain visual",
            "Ngoding / teknologi",
            "Ngajar / edukasi",
            "Bisnis / jualan"
        ]
    )

with col2:
    waktu_luang = st.selectbox(
        "Waktu fokus per hari untuk karier digital:",
        [
            "< 1 jam",
            "1–2 jam",
            "2–4 jam",
            "> 4 jam"
        ]
    )

col3, col4 = st.columns(2)

with col3:
    berani_kamera = st.selectbox(
        "Kenyamanan tampil di depan kamera:",
        [
            "Sangat berani",
            "Lumayan berani",
            "Masih malu",
            "Tidak nyaman sama sekali"
        ]
    )

with col4:
    gaya_komunikasi = st.selectbox(
        "Gaya komunikasi yang paling kuat:",
        [
            "Lebih kuat lisan",
            "Lebih kuat tulisan",
            "Seimbang",
            "Kurang percaya diri"
        ]
    )

col5, col6 = st.columns(2)

with col5:
    skill_teknis = st.selectbox(
        "Level kemampuan teknis di bidang minat:",
        [
            "Benar-benar pemula",
            "Pemula tapi sudah belajar",
            "Menengah",
            "Lanjutan"
        ]
    )

with col6:
    target_penghasilan = st.selectbox(
        "Tujuan penghasilan dari karier digital:",
        [
            "Cuma iseng / belajar dulu",
            "Sampingan kecil",
            "Sampingan serius",
            "Penghasilan utama"
        ]
    )

st.subheader("💻 Kondisi Pendukung")

col7, col8 = st.columns(2)

with col7:
    perangkat = st.selectbox(
        "Perangkat & koneksi yang tersedia:",
        [
            "HP saja",
            "HP + laptop standar",
            "HP + laptop cukup kuat",
            "HP + laptop kuat + internet stabil"
        ]
    )

with col8:
    bahasa_inggris = st.selectbox(
        "Kemampuan bahasa Inggris:",
        [
            "Dasar banget",
            "Bisa baca / nonton",
            "Bisa ngobrol / menulis",
            "Lancar"
        ]
    )

col9, col10 = st.columns(2)

with col9:
    konsistensi = st.selectbox(
        "Kebiasaan konsistensi kamu:",
        [
            "Sering lompat-lompat minat",
            "Cukup konsisten",
            "Biasanya konsisten kalau suka",
            "Sangat konsisten"
        ]
    )

with col10:
    preferensi_kerja = st.selectbox(
        "Tipe kerja yang kamu sukai:",
        [
            "Lebih suka kerja sendiri",
            "Lebih suka kerja di balik layar",
            "Suka interaksi & tim",
            "Suka tampil di depan publik"
        ]
    )

st.markdown("---")

# =========================
# FUNGSI BANTU: SKOR KESIAPAN
# =========================
def hitung_skor_kesiapan(skill: str, kons: str, waktu: str) -> int:
    skor = 0

    # Skill teknis
    if skill == "Benar-benar pemula":
        skor += 10
    elif skill == "Pemula tapi sudah belajar":
        skor += 30
    elif skill == "Menengah":
        skor += 60
    elif skill == "Lanjutan":
        skor += 80

    # Konsistensi
    if kons == "Sering lompat-lompat minat":
        skor += 10
    elif kons == "Cukup konsisten":
        skor += 30
    elif kons == "Biasanya konsisten kalau suka":
        skor += 50
    elif kons == "Sangat konsisten":
        skor += 70

    # Waktu luang
    if waktu == "< 1 jam":
        skor += 10
    elif waktu == "1–2 jam":
        skor += 30
    elif waktu == "2–4 jam":
        skor += 50
    elif waktu == "> 4 jam":
        skor += 70

    return min(skor, 100)

def label_kesiapan(skor: int) -> str:
    if skor < 40:
        return "Tahap Eksplorasi"
    elif skor < 70:
        return "Tahap Siap Pemula"
    else:
        return "Tahap Siap Serius"

# =========================
# PROSES KEPUTUSAN (RULE-BASED)
# =========================
st.header("🧾 Hasil Analisis Sistem")

if st.button("Proses Rekomendasi"):
    if not nama:
        st.error("Tolong isi nama dulu agar laporan lebih personal.")
    else:
        karier_utama = ""
        alasan_utama = ""
        langkah_utama = []
        faktor_pendukung = []
        faktor_tantangan = []
        saran_6_12_bulan = ""

        # =========================
        # 1. TAMPILKAN PROFIL RINGKAS
        # =========================
        st.success(f"Ringkasan analisis untuk: **{nama}**")

        st.markdown("### 📌 Profil Singkat Kamu")
        st.write(f"- Minat digital utama: **{minat}**")
        st.write(f"- Waktu fokus harian: **{waktu_luang}**")
        st.write(f"- Level skill teknis: **{skill_teknis}**")
        st.write(f"- Tujuan finansial: **{target_penghasilan}**")
        st.write(f"- Perangkat & koneksi: **{perangkat}**")
        st.write(f"- Konsistensi: **{konsistensi}**")
        st.write(f"- Preferensi kerja: **{preferensi_kerja}**")

        st.markdown("---")

        # =========================
        # 2. TENTUKAN KARIER UTAMA (ATURAN IF–THEN)
        # =========================

        # 1) KONTEN & MEDIA
        if minat == "Konten & media (video, sosial media)":
            if berani_kamera in ["Sangat berani", "Lumayan berani"]:
                karier_utama = "Content Creator / Influencer (YouTube, TikTok, Reels)"
                alasan_utama = (
                    "Kamu tertarik dengan dunia konten dan tidak keberatan tampil di depan kamera. "
                    "Ini adalah kombinasi yang kuat untuk membangun audiens dan personal brand."
                )
                langkah_utama = [
                    "Tentukan niche awal yang dekat dengan keseharianmu (gaming, edukasi singkat, produktivitas, hiburan, dll).",
                    "Pilih 1–2 platform utama dan buat jadwal upload yang realistis (misalnya 3 konten per minggu).",
                    "Evaluasi secara berkala konten mana yang performanya terbaik dan pelajari polanya."
                ]
                saran_6_12_bulan = (
                    "Bangun komunitas kecil di sekitar kontenmu, kemudian mulai eksplorasi monetisasi "
                    "seperti kerja sama brand, affiliate, atau jasa terkait niche."
                )
            else:
                karier_utama = "Content Writer / Copywriter / Scriptwriter"
                alasan_utama = (
                    "Kamu tertarik di dunia konten, tetapi kurang nyaman tampil di depan kamera. "
                    "Sistem mengarahkanmu ke jalur penulisan ide, naskah, dan teks persuasif."
                )
                langkah_utama = [
                    "Pelajari dasar copywriting dan storytelling (struktur, hook, call to action).",
                    "Latih diri menulis caption, thread, atau naskah video pendek secara rutin.",
                    "Bangun portofolio tulisan di blog, Medium, Notion, atau feed media sosial."
                ]
                saran_6_12_bulan = (
                    "Mulai menawarkan jasa penulisan ke UMKM, content creator, atau agensi. "
                    "Kumpulkan testimoni dan perkuat spesialisasi (copy jualan, script edukasi, dll)."
                )

        # 2) DESAIN VISUAL
        elif minat == "Desain visual":
            if perangkat != "HP saja" and skill_teknis in ["Pemula tapi sudah belajar", "Menengah", "Lanjutan"]:
                karier_utama = "Freelance Desain Grafis / Video Editor / Thumbnail Artist"
                alasan_utama = (
                    "Minat visualmu didukung oleh perangkat yang memadai. "
                    "Ini membuat jalur freelance desain dan editing menjadi realistis."
                )
                langkah_utama = [
                    "Pilih 1–2 tools utama (misalnya Canva + CapCut, atau Photoshop + Premiere).",
                    "Buat 10–15 karya contoh (poster, feed, thumbnail, video pendek).",
                    "Susun portofolio rapi di satu tempat (Instagram khusus portfolio, Behance, atau website sederhana)."
                ]
                saran_6_12_bulan = (
                    "Secara bertahap, naikkan kompleksitas proyek dan perluas jaringan klienmu "
                    "melalui komunitas, media sosial, atau platform freelance."
                )
            else:
                karier_utama = "Penguatan Dasar Desain Visual"
                alasan_utama = (
                    "Minat desain sudah jelas, tetapi sistem mendeteksi bahwa skill dan/atau perangkat "
                    "masih perlu diperkuat sebelum menerima proyek profesional."
                )
                langkah_utama = [
                    "Mulai dari tools ringan (Canva, aplikasi mobile) untuk memahami layout dan komposisi.",
                    "Ikuti satu kursus atau playlist tentang dasar desain (warna, tipografi, hirarki visual).",
                    "Latih diri dengan membuat desain untuk diri sendiri, teman, atau proyek fiktif."
                ]
                saran_6_12_bulan = (
                    "Jika fondasi sudah kuat, beralih ke tools yang lebih advance dan bangun portofolio yang siap dilihat klien."
                )

        # 3) NGODING / TEKNOLOGI
        elif minat == "Ngoding / teknologi":
            if skill_teknis in ["Menengah", "Lanjutan"] and perangkat in [
                "HP + laptop cukup kuat",
                "HP + laptop kuat + internet stabil"
            ]:
                karier_utama = "Freelance Web / App Developer (Remote)"
                alasan_utama = (
                    "Kamu memiliki skill teknis yang cukup matang dengan perangkat yang mendukung. "
                    "Ini sangat relevan untuk jalur developer freelance."
                )
                langkah_utama = [
                    "Fokus pada satu stack utama (misal MERN, Laravel, Django, Flutter).",
                    "Bangun minimal 2–3 project portfolio yang benar-benar bisa dijalankan.",
                    "Perbaiki dokumentasi dan tampilan GitHub agar terlihat profesional."
                ]
                saran_6_12_bulan = (
                    "Mulai mencari proyek kecil, berkontribusi ke open source, dan membangun profil profesional "
                    "di LinkedIn atau platform sejenis."
                )
            else:
                karier_utama = "Penguatan Fondasi Pemrograman"
                alasan_utama = (
                    "Minatmu di teknologi kuat, namun sistem menilai fondasi skill dan/atau perangkat "
                    "perlu diperkuat sebelum masuk ke proyek klien."
                )
                langkah_utama = [
                    "Ikuti roadmap belajar pemrograman yang terstruktur (frontend/backend/mobile).",
                    "Latihan ngoding minimal 30–60 menit per hari dengan fokus praktik.",
                    "Bangun beberapa project kecil untuk melatih problem solving."
                ]
                saran_6_12_bulan = (
                    "Setelah fondasi lebih kuat, mulai membangun project yang lebih kompleks dan siapkan portofolio developer."
                )

        # 4) NGAJAR / EDUKASI
        elif minat == "Ngajar / edukasi":
            if gaya_komunikasi != "Kurang percaya diri" and waktu_luang in ["2–4 jam", "> 4 jam"]:
                karier_utama = "Online Tutor / Course Creator"
                alasan_utama = (
                    "Kamu menyukai aktivitas menjelaskan dan punya waktu yang cukup. "
                    "Ini cocok untuk mengajar secara online atau membuat kursus digital."
                )
                langkah_utama = [
                    "Pilih satu topik yang kamu kuasai dan sering orang tanyakan.",
                    "Buat outline materi dan pecah menjadi beberapa sesi singkat.",
                    "Uji coba mengajar dalam lingkaran kecil (teman/keluarga) secara online."
                ]
                saran_6_12_bulan = (
                    "Kembangkan materi menjadi format kelas rutin atau kursus berbayar dan bangun reputasi sebagai pengajar."
                )
            else:
                karier_utama = "Persiapan Menuju Karier Edukasi Online"
                alasan_utama = (
                    "Minat edukasi sudah ada, tetapi sistem mendeteksi perlunya penguatan pada aspek komunikasi "
                    "dan pengelolaan waktu."
                )
                langkah_utama = [
                    "Latih kemampuan menjelaskan konsep sederhana ke orang terdekat.",
                    "Gunakan rekaman video/audio pribadi untuk mengevaluasi gaya bicara.",
                    "Ikut komunitas belajar/mengajar untuk membangun kepercayaan diri."
                ]
                saran_6_12_bulan = (
                    "Jika sudah lebih nyaman, mulai membuka sesi belajar kecil-kecilan dan kumpulkan feedback."
                )

        # 5) BISNIS / JUALAN
        elif minat == "Bisnis / jualan":
            if konsistensi in ["Biasanya konsisten kalau suka", "Sangat konsisten"]:
                karier_utama = "Online Seller / Digital Marketing"
                alasan_utama = (
                    "Kamu tertarik pada bisnis dan memiliki kecenderungan konsisten. "
                    "Ini kombinasi yang baik untuk membangun usaha online dan mempelajari pemasaran digital."
                )
                langkah_utama = [
                    "Mulai dari produk yang mudah kamu pahami dan bisa kamu jelaskan dengan percaya diri.",
                    "Pelajari dasar-dasar marketing digital (copywriting, visual produk, dan iklan sederhana).",
                    "Eksperimen jualan di 1 marketplace dan 1 platform sosial sambil mengamati hasil."
                ]
                saran_6_12_bulan = (
                    "Perkuat brand, sistem operasional sederhana, dan mulai pelajari strategi retensi pelanggan "
                    "serta iklan berbayar."
                )
            else:
                karier_utama = "Eksplorasi Bisnis Digital Skala Awal"
                alasan_utama = (
                    "Minat bisnis ada, tetapi konsistensi masih perlu dilatih. "
                    "Sistem menyarankan untuk mulai dari eksperimen bisnis kecil dengan risiko rendah."
                )
                langkah_utama = [
                    "Coba proyek jualan kecil (pre-order, titip jual, atau dropship) dengan skala terbatas.",
                    "Biasakan mencatat pemasukan-pengeluaran dan respon pelanggan.",
                    "Bangun kebiasaan harian/pekanan yang terkait dengan bisnis, meski masih sederhana."
                ]
                saran_6_12_bulan = (
                    "Jika sudah menemukan pola yang cocok, baru naikkan skala dan seriuskan sistem bisnis."
                )

        # =========================
        # 3. ANALISIS FAKTOR PENDUKUNG & TANTANGAN
        # =========================

        # Pendukung
        if konsistensi in ["Biasanya konsisten kalau suka", "Sangat konsisten"]:
            faktor_pendukung.append(
                "Kamu memiliki kecenderungan konsisten, ini sangat membantu dalam membangun karier digital jangka panjang."
            )
        if perangkat in ["HP + laptop cukup kuat", "HP + laptop kuat + internet stabil"]:
            faktor_pendukung.append(
                "Perangkat dan koneksimu sudah cukup mendukung untuk sebagian besar aktivitas digital."
            )
        if bahasa_inggris in ["Bisa baca / nonton", "Bisa ngobrol / menulis", "Lancar"]:
            faktor_pendukung.append(
                "Kemampuan bahasa Inggris membuka akses ke sumber belajar dan peluang global."
            )
        if gaya_komunikasi in ["Lebih kuat lisan", "Lebih kuat tulisan", "Seimbang"]:
            faktor_pendukung.append(
                "Gaya komunikasimu bisa diarahkan untuk mendukung konten, edukasi, atau aktivitas penjualan."
            )

        # Tantangan
        if konsistensi == "Sering lompat-lompat minat":
            faktor_tantangan.append(
                "Kamu cenderung sering berganti minat, sehingga perlu strategi untuk melatih fokus jangka menengah."
            )
        if perangkat == "HP saja":
            faktor_tantangan.append(
                "Saat ini perangkatmu masih terbatas pada HP, sehingga beberapa jenis pekerjaan digital mungkin lebih menantang."
            )
        if skill_teknis == "Benar-benar pemula":
            faktor_tantangan.append(
                "Fondasi kemampuan teknis masih sangat dasar, dibutuhkan kesabaran dan komitmen belajar yang konsisten."
            )
        if gaya_komunikasi == "Kurang percaya diri":
            faktor_tantangan.append(
                "Rasa kurang percaya diri dalam komunikasi perlu dilatih pelan-pelan, terutama jika ingin banyak tampil di publik."
            )

        # =========================
        # 4. SKOR KESIAPAN
        # =========================
        skor = hitung_skor_kesiapan(skill_teknis, konsistensi, waktu_luang)
        label = label_kesiapan(skor)

        st.markdown("### 📊 Kesiapan Memulai Karier Digital")
        st.write(f"Perkiraan kesiapan (menurut sistem): **{label}**")
        st.progress(skor / 100)

        # =========================
        # 5. TAMPILKAN REKOMENDASI
        # =========================
        st.markdown("### 🎯 Jalur Karier Digital Utama")

        if karier_utama:
            st.markdown(f"> **{karier_utama}**")
            st.markdown("#### Alasan sistem memilih jalur ini:")
            st.write(alasan_utama)
        else:
            st.write(
                "Saat ini sistem belum menemukan satu jalur yang benar-benar dominan. "
                "Kamu berada di tahap eksplorasi, dan itu bukan hal yang buruk."
            )

        st.markdown("### 🚀 Langkah Praktis 1–3 Bulan ke Depan")
        if langkah_utama:
            for step in langkah_utama:
                st.write(f"- {step}")
        else:
            st.write(
                "- Pilih satu skill digital yang ingin kamu uji selama 1–2 bulan.\n"
                "- Jadwalkan waktu belajar/praktik secara rutin setiap minggu.\n"
                "- Dokumentasikan progres dan refleksi belajarmu."
            )

        st.markdown("### 🧭 Arah 6–12 Bulan Berikutnya")
        if saran_6_12_bulan:
            st.write(saran_6_12_bulan)
        else:
            st.write(
                "Fokus membangun kebiasaan belajar jangka menengah dan kumpulkan karya/portofolio "
                "yang bisa kamu tunjukkan ke orang lain."
            )

        st.markdown("### ✅ Faktor Pendukung")
        if faktor_pendukung:
            for f in faktor_pendukung:
                st.write(f"- {f}")
        else:
            st.write("- Belum terdeteksi faktor pendukung spesifik, tetapi setiap orang selalu punya potensi yang bisa dikembangkan.")

        st.markdown("### ⚠️ Hal yang Perlu Diantisipasi")
        if faktor_tantangan:
            for f in faktor_tantangan:
                st.write(f"- {f}")
        else:
            st.write("- Tidak ada tantangan besar yang terdeteksi dari jawabanmu saat ini.")

else:
    st.info("Isi data di atas, lalu klik tombol **'Proses Rekomendasi'** untuk melihat laporan karier digital kamu.")
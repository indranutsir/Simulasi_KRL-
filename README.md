# 🚆 Iclik Simulator

**Iclik Simulator** adalah aplikasi simulasi masinis KRL yang dibuat menggunakan **Python dan Pygame** sebagai proyek **Tugas Besar Perkuliahan**.

Pada simulator ini, pemain berperan sebagai masinis yang harus mengendalikan kecepatan kereta menggunakan throttle dan rem, mengatur arah perjalanan, serta menghentikan kereta sedekat mungkin dengan titik pemberhentian setiap stasiun.

Sistem permainan dilengkapi dengan **fisika gerak kereta, sistem penilaian pemberhentian, pintu otomatis, efek suara, dan grafik perjalanan**.

---

## 📌 Informasi Proyek

| Informasi             | Detail                            |
| --------------------- | --------------------------------- |
| Nama Program          | Iclik Simulator                   |
| Jenis                 | Simulator / Game Edukasi          |
| Bahasa Pemrograman    | Python                            |
| GUI / Game Engine     | Pygame                            |
| Visualisasi Grafik    | Matplotlib                        |
| Paradigma Pemrograman | Object-Oriented Programming (OOP) |
| Platform              | Windows / Linux / macOS           |
| Versi                 | **v1.0.0**                        |
| Status                | Final / Tugas Besar               |
| Lisensi               | Untuk keperluan akademik          |

---

## 🎯 Tujuan Program

Program ini dibuat untuk mensimulasikan dasar pengoperasian kereta KRL secara sederhana, terutama dalam hal:

* Mengatur throttle kereta.
* Mengatur pengereman.
* Mengatur arah perjalanan.
* Mengontrol kecepatan kereta.
* Menghentikan kereta di area stasiun.
* Menilai ketepatan posisi berhenti.
* Menampilkan skor perjalanan.
* Memberikan efek suara saat pengoperasian.
* Menampilkan grafik kecepatan dan posisi terhadap waktu.

Program tidak dimaksudkan sebagai simulator kereta profesional, melainkan sebagai simulasi sederhana yang digunakan untuk kebutuhan pembelajaran dan tugas besar.

---

# ✨ Fitur

### 🚆 Kendali Kereta

Pemain dapat mengendalikan kereta menggunakan:

* Throttle level 0–5.
* Brake level 0–4.
* Arah maju.
* Netral.
* Arah mundur.

### ⚙️ Sistem Fisika

Gerakan kereta menggunakan beberapa parameter fisika sederhana, yaitu:

* Akselerasi maksimum.
* Perlambatan maksimum.
* Rolling resistance.
* Air drag.
* Jerk limiting.

Jerk limiting digunakan agar perubahan akselerasi tidak terjadi secara tiba-tiba sehingga pergerakan kereta terasa lebih halus.

### 🚉 Sistem Stasiun

Terdapat beberapa stasiun pada jalur perjalanan:

1. Universitas Pancasila
2. Universitas Indonesia
3. Pondok Cina
4. Depok Baru
5. Depok

Setiap stasiun memiliki titik pemberhentian tertentu.

### 🏆 Sistem Penilaian

Ketepatan pemberhentian kereta akan menentukan skor.

| Kondisi  |                   Toleransi | Skor |
| -------- | --------------------------: | ---: |
| PERFECT! |                   ≤ 3 meter |  100 |
| Good     |                  ≤ 10 meter |   75 |
| OK       |                  ≤ 25 meter |   50 |
| Terlewat | > 25 meter / tidak berhenti |    0 |

Semakin dekat posisi kereta dengan titik target stasiun, semakin tinggi skor yang diperoleh.

### 🚪 Sistem Pintu

Ketika kereta berhasil berhenti di stasiun:

* Pintu terbuka secara otomatis.
* Pintu terbuka selama beberapa detik.
* Throttle tidak dapat digunakan ketika pintu terbuka.
* Setelah timer selesai, pintu akan tertutup secara otomatis.

### 🔊 Sound Effect

Program menyediakan beberapa efek suara:

* Klakson.
* Decitan rem.
* Pintu terbuka.
* Pintu tertutup.
* Bunyi indikator pemberhentian.

Program juga memiliki **silent fallback**, sehingga apabila perangkat tidak memiliki audio device, program tetap dapat berjalan tanpa berhenti karena error audio.

### 📊 Grafik Perjalanan

Setelah perjalanan selesai, pengguna dapat melihat:

* Grafik kecepatan terhadap waktu.
* Grafik posisi terhadap waktu.

Grafik dibuat menggunakan **Matplotlib**.

---

# 🎮 Kontrol

| Tombol | Fungsi                 |
| ------ | ---------------------- |
| `W`    | Menambah throttle      |
| `S`    | Mengurangi throttle    |
| `D`    | Menambah rem           |
| `A`    | Mengurangi rem         |
| `F`    | Mengatur arah maju     |
| `N`    | Mengatur posisi netral |
| `R`    | Mengatur arah mundur   |
| `H`    | Membunyikan klakson    |

> Pengaturan arah maju, netral, dan mundur hanya dapat dilakukan ketika kereta dalam keadaan berhenti.

---

# 🖥️ Persyaratan Sistem

Minimal membutuhkan:

* Python **3.10+**
* Pygame **2.5+**
* Matplotlib **3.5+**
* Sistem operasi Windows, Linux, atau macOS
* Perangkat yang mampu menjalankan aplikasi Python dengan GUI

---

# 📦 Instalasi

### 1. Clone atau ekstrak repository

Ekstrak folder proyek ke komputer.

Struktur utama proyek:

```text
Iclik_Simulator/
├── Assets/
│   ├── Sounds/
│   ├── Stasiun/
│   ├── background.png
│   ├── icon.png
│   ├── KRL205.png
│   ├── rel.png
│   └── tanah.png
│
├── config.py
├── controls.py
├── graph.py
├── main.py
├── requirements.txt
├── simulation.py
├── sound.py
├── station.py
├── train.py
├── ui.py
└── README.md
```

### 2. Buat virtual environment

Disarankan menggunakan virtual environment:

```bash
python -m venv venv
```

Aktifkan virtual environment.

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 3. Install dependency

```bash
pip install -r requirements.txt
```

Dependency yang digunakan:

```text
pygame>=2.5
matplotlib>=3.5
```

### 4. Jalankan program

```bash
python main.py
```

---

# 🧩 Struktur Program

Program menggunakan pendekatan **Object-Oriented Programming (OOP)** untuk memisahkan fungsi setiap bagian.

| File            | Fungsi                                                                   |
| --------------- | ------------------------------------------------------------------------ |
| `main.py`       | Menjalankan game loop dan mengatur state permainan                       |
| `config.py`     | Menyimpan konfigurasi, konstanta, path asset, fisika, dan aturan scoring |
| `train.py`      | Mengatur objek dan pergerakan kereta                                     |
| `controls.py`   | Mengatur input throttle, rem, dan arah                                   |
| `simulation.py` | Menggabungkan sistem fisika, kontrol, dan stasiun                        |
| `station.py`    | Mengatur stasiun, pemberhentian, pintu, dan skor                         |
| `sound.py`      | Mengatur seluruh efek suara                                              |
| `ui.py`         | Mengatur tampilan menu, HUD, tombol, dan layar akhir                     |
| `graph.py`      | Membuat grafik kecepatan dan posisi                                      |

---

# 🔄 Alur Program

Secara sederhana, alur program adalah:

```text
                ┌──────────────┐
                │   Main Menu  │
                └───────┬──────┘
                        │
                     MULAI
                        │
                        ▼
                ┌──────────────┐
                │    Playing   │
                └───────┬──────┘
                        │
            ┌───────────┼───────────┐
            ▼           ▼           ▼
         Kontrol     Fisika      Stasiun
        Kereta      Kereta       & Skor
            │           │           │
            └───────────┼───────────┘
                        │
                        ▼
                 Semua stasiun
                    selesai?
                        │
                        ▼
                ┌──────────────┐
                │    Finish    │
                └───────┬──────┘
                        │
              ┌─────────┴─────────┐
              ▼                   ▼
         Main Lagi           Lihat Grafik
```

---

# 🧮 Parameter Fisika

Beberapa parameter utama yang digunakan dalam simulasi:

```text
Maximum Speed       : 80 km/h
Maximum Acceleration: 0.8 m/s²
Maximum Deceleration: 1.0 m/s²
Rolling Resistance  : 0.03 m/s²
Air Drag Coefficient: 0.0006
Jerk Limit          : 2.5 m/s³
Track Distance      : 13.000 meter
```

Nilai tersebut digunakan untuk membuat pergerakan kereta lebih realistis dibandingkan hanya menggunakan perpindahan posisi secara langsung.

---

# 🏗️ Versi Program

## v1.0.0 — Final Release

**Status:** Stable / Final

### Fitur utama

* [x] Main menu
* [x] Sistem game loop
* [x] Kontrol throttle
* [x] Kontrol rem
* [x] Kontrol arah
* [x] Sistem fisika kereta
* [x] Jerk limiting
* [x] Rolling resistance
* [x] Air drag
* [x] Sistem stasiun
* [x] Sistem penilaian
* [x] Sistem pintu otomatis
* [x] Interlock pintu dan throttle
* [x] Sound effect
* [x] Silent fallback untuk masalah audio
* [x] Layar hasil perjalanan
* [x] Sistem replay
* [x] Grafik kecepatan terhadap waktu
* [x] Grafik posisi terhadap waktu

---

# 🐛 Known Bugs / Limitasi

Versi **v1.0.0** masih memiliki beberapa keterbatasan yang perlu diperhatikan.

### 1. Grafik dibuka pada window terpisah

Ketika tombol **Lihat Grafik** ditekan, Matplotlib membuka window baru.

Hal ini membuat grafik belum menjadi bagian langsung dari interface Pygame.

**Status:** Known Limitation

---

### 2. Tidak terdapat sistem High Score

Skor yang diperoleh hanya ditampilkan selama sesi permainan.

Skor terbaik belum disimpan secara permanen ke file/database.

**Status:** Belum diimplementasikan

---

### 3. Kecepatan maksimum masih global

Batas kecepatan maksimum saat ini menggunakan satu nilai untuk seluruh jalur:

```text
80 km/h
```

Belum terdapat sistem batas kecepatan berbeda untuk setiap segmen jalur.

**Status:** Belum diimplementasikan

---

### 4. Animasi pintu masih sederhana

Sistem pintu sudah memiliki mekanisme buka/tutup otomatis, tetapi representasi visual pintu masih berupa indikator pada UI dan belum menggunakan animasi pintu kereta secara detail.

**Status:** Known Limitation

---

### 5. Sistem fisika masih merupakan pendekatan sederhana

Fisika yang digunakan telah memiliki akselerasi, perlambatan, rolling resistance, air drag, dan jerk limiting.

Namun, model tersebut belum merepresentasikan seluruh faktor fisika kereta nyata seperti:

* Massa kereta yang berubah.
* Kemiringan lintasan.
* Kondisi rel.
* Kurva lintasan.
* Beban penumpang.
* Sistem pengereman kereta sebenarnya.

**Status:** Known Limitation

---

### 6. Asset menggunakan path relatif

Asset program menggunakan path seperti:

```text
Assets/icon.png
Assets/KRL205.png
Assets/Sounds/horn.wav
```

Karena itu program harus dijalankan dari direktori utama proyek agar asset dapat ditemukan dengan benar.

**Status:** Known Limitation

---

### 7. Belum tersedia installer executable

Program masih dijalankan melalui Python:

```bash
python main.py
```

Belum tersedia installer atau executable seperti:

```text
IclikSimulator.exe
```

**Status:** Belum diimplementasikan

---

# 📝 Changelog

## [1.0.0] — Final

### Added

* Sistem simulasi perjalanan KRL.
* Sistem throttle dan brake.
* Sistem arah maju, netral, dan mundur.
* Sistem fisika kereta.
* Jerk limiting.
* Rolling resistance.
* Air drag.
* Sistem pemberhentian stasiun.
* Sistem scoring.
* Sistem pintu otomatis.
* Interlock pintu.
* Sound effect.
* Sistem notifikasi.
* Layar hasil akhir.
* Fitur replay.
* Grafik kecepatan.
* Grafik posisi.

### Fixed

* Pergerakan kereta dibuat lebih halus menggunakan jerk limiting.
* Kereta tidak dapat bergerak ketika pintu sedang terbuka.
* Kereta tidak dapat melebihi batas kecepatan maksimum.
* Sistem audio memiliki fallback ketika audio device tidak tersedia.
* Sistem stasiun dapat mendeteksi stasiun yang terlewat.

### Known Issues

* Grafik masih menggunakan window Matplotlib terpisah.
* Belum ada penyimpanan high score.
* Belum ada batas kecepatan per segmen.
* Animasi pintu masih sederhana.
* Model fisika belum merepresentasikan seluruh kondisi kereta nyata.

---

# 👨‍💻 Pengembangan

Proyek ini dikembangkan sebagai bagian dari **Tugas Besar Perkuliahan**.

Pengembangan menggunakan prinsip modularisasi agar setiap bagian program memiliki tanggung jawab yang jelas.

Pembagian modul utama:

```text
Input
  ↓
Controls
  ↓
Simulation
  ↓
Train ─────── Station
  ↓              ↓
Physics         Score
  ↓              ↓
  └────── UI ─────┘
          ↓
       Result
          ↓
       Graph
```

---

# ⚠️ Catatan

Iclik Simulator merupakan **simulasi untuk keperluan akademik**. Parameter fisika, kontrol, sistem pengereman, dan mekanisme operasional kereta disederhanakan agar sesuai dengan ruang lingkup tugas dan kemampuan implementasi program.

Program ini **bukan simulator resmi atau representasi sistem operasi KRL yang sebenarnya**.

---

# 📄 Lisensi

Proyek ini dibuat untuk keperluan **Tugas Besar Perkuliahan**.

Penggunaan, modifikasi, dan distribusi kode mengikuti ketentuan yang ditetapkan oleh pembuat dan institusi terkait.

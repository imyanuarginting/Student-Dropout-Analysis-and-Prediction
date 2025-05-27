# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Institut

## Business Understanding

Jaya Jaya Institut merupakan institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan dikenal memiliki reputasi yang sangat baik dalam mencetak lulusan berkualitas. Selama lebih dari dua dekade, lembaga ini telah berkontribusi dalam mencetak tenaga profesional yang tersebar di berbagai bidang.

Namun, meskipun memiliki reputasi yang solid, Jaya Jaya Institut saat ini tengah menghadapi tantangan serius terkait dengan tingginya angka dropout mahasiswa. Banyak siswa yang tidak menyelesaikan pendidikannya, dan hal ini menjadi perhatian penting karena dapat memengaruhi citra institusi, efektivitas pembelajaran, serta efisiensi alokasi sumber daya pendidikan.

Pihak manajemen menyadari bahwa penyebab dropout ini bersifat multifaktor dan tidak bisa ditangani dengan pendekatan konvensional semata. Oleh karena itu, institusi ingin menerapkan pendekatan berbasis data untuk:

   * Mengidentifikasi faktor-faktor yang paling berpengaruh terhadap kemungkinan mahasiswa mengalami dropout.
   * Mengembangkan sistem pemantauan berbasis dashboard yang dapat digunakan oleh pihak institusi (akademik, dosen pembimbing, dan manajemen) untuk memantau status risiko mahasiswa dan melakukan intervensi sedini mungkin.
   * (Opsional) Memprediksi mahasiswa yang berisiko tinggi untuk dropout di masa depan, guna diarahkan ke program bimbingan atau dukungan yang lebih personal.

Melalui pendekatan ini, Jaya Jaya Institut berharap dapat menurunkan angka dropout, meningkatkan efektivitas proses pembelajaran, dan memastikan lebih banyak mahasiswa dapat menyelesaikan pendidikan mereka dengan baik.

### Permasalahan Bisnis

   * Pihak institusi kesulitan dalam mengidentifikasi karakteristik dan faktor-faktor utama yang menyebabkan mahasiswa mengalami dropout.
   * Jaya Jaya Institut belum memiliki sistem pemantauan yang efektif untuk mendeteksi dan mengantisipasi risiko dropout mahasiswa secara dini dan real-time.
   * Upaya intervensi terhadap mahasiswa berisiko saat ini masih bersifat reaktif dan tidak terarah karena belum berbasis data.
   * Tidak adanya sistem prediktif yang dapat membantu institusi memprioritaskan perhatian atau sumber daya kepada mahasiswa yang paling membutuhkan dukungan.

### Cakupan Proyek

   * Melakukan identifikasi terhadap faktor-faktor utama yang berkontribusi terhadap tingginya tingkat dropout mahasiswa di Jaya Jaya Institut.
   * Mengembangkan dashboard interaktif yang mudah digunakan untuk membantu pihak institusi memantau performa mahasiswa serta indikator risiko dropout.
   * Membangun sistem prediksi dengan tingkat akurasi yang memadai untuk mengidentifikasi mahasiswa yang berisiko tinggi mengalami dropout secara dini (Opsional).

### Persiapan

* Download Sumber Data
    * Sumber data: https://drive.google.com/file/d/17_IWXwx29Na0qdPPUYLqJ2B4Z_uU4EHq/view?usp=sharing
    * Dependensi: https://drive.google.com/file/d/1spy3iS9xs_y-e9iLA-UETcRJH7uzCmFc/view?usp=sharing
    * File untuk menjalankan aplikasi secara lokal untuk melakukan prediksi (prediction.zip): https://drive.google.com/file/d/1aSHMKR1oT9G1jP-l-GoKGSuGBkb34CnW/view?usp=sharing
    * Setelah file terunduh, lakukan ekstrak file untuk format .zip (prediction.zip) lalu simpan semua file yang telah terunduh di lokasi tempat virtual environment berada (D:\Project\ML\Student-Dropout-Analysis-and-Prediction\Include), untuk cara membuat virtual environment akan dijelaskan setelah ini.

* Membuat, Mengaktifkan Virtual Environment, dan Menginstal Dependensi
    * Jalankan perintah berikut di terminal laptop/PC kalian:
        ```
        cd D:\Project\ML
        ```
    * Buat virtual environment
        ```
        python -m venv Student-Dropout-Analysis-and-Prediction
        ```
    * Aktifkan virtual environment
        ```
        .\Student-Dropout-Analysis-and-Prediction\Scripts\Activate.ps1
        ```
    * Masuk ke direktori Student-Dropout-Analysis-and-Prediction
        ```
        cd Student-Dropout-Analysis-and-Prediction\Include
        ```
    * Install dependensi
        ```
        pip install -r requirements.txt
        ```
    * Menjalankan aplikasi secara lokal untuk melakukan prediksi (app.py)
        ```
        streamlit run app.py
        ```
    * Menonaktifkan environment
        ```
        deactivate
        ```

* link Streamlit untuk Melakukan Prediksi
    ```
    https://student-dropout-analysis-and-prediction-by-imyanuarginting.streamlit.app/
    ```

Setup Environment Jika Belum Membuat Container Metabase:
```
docker pull metabase/metabase:latest
docker run -p 3000:3000 --name metabase metabase/metabase
```

Setup Environment Jika Sudah Membuat Container Metabase Sebelumnya:
```
docker start metabase
```

Credentials Metabase:
* Email: yanuarginting@gmail.com
* Password: GloryGloryManUtd123

## Business Dashboard

Dashboard dibangun menggunakan Metabase dan mencakup:

* Gender & Marital Status vs. Status (Top 5)
* Gender & Nacionality vs. Status (Top 5)
* Gender & Previous Qualification vs. Status (Top 5)
* Gender & Course vs. Status (Top 5)
* Gender & Daytime Evening Attendance vs. Status
* Gender & Scholarship Holder vs. Status
* Gender & Tuition Fees Up To Date vs. Status
* Gender & International vs. Status
* Fathers Occupation & Mothers Occupation vs. Status (Top 5)
* Fathers Qualification & Mothers Qualification vs. Status (Top 5)

* Gender & Marital Status vs. Dropout Rate
* Gender & Nacionality vs. Dropout Rate
* Gender & Previous Qualification vs. Dropout Rate
* Gender & Course vs. Dropout Rate
* Gender & Daytime Evening Attendance vs. Dropout Rate
* Gender & Scholarship Holder vs. Dropout Rate
* Gender & Tuition Fees Up To Date vs. Dropout Rate
* Gender & International vs. Dropout Rate
* Fathers Occupation & Mothers Occupation vs. Dropout Rate
* Fathers Qualification & Mothers Qualification vs. Dropout Rate

## Conclusion

* **Kelompok risiko tertinggi** seperti:
    * **Laki‑laki**, khususnya yang **menikah, kuliah malam, tanpa beasiswa, dan belum bayar UKT**.
        * **Tekanan tanggungan keluarga**: Mahasiswa menikah sering punya tanggungan ekonomi atau keluarga yang lebih besar → waktu dan fokus studi terbagi.
        * **Kuliah malam**: Biasanya kebanyakan peserta bekerja siang hari, kelelahan fisik/kognitif lebih tinggi → menurunkan performa akademik.
        * **Tanpa beasiswa & UKT menunggak**: Stres finansial memengaruhi motivasi dan konsentrasi, bahkan bisa menyebabkan skorsing administrasi jika biaya belum lunas.
    * Mahasiswa dengan **kualifikasi sebelumnya rendah (Basic education 3rd cycle)**, serta **orang tua berpendidikan/pekerjaan rendah atau tak diketahui**.
        * **Persiapan akademik**: Siswa yang hanya sampai “Basic education 3rd cycle” mungkin kurang terlatih dalam pola belajar mandiri dan metodologi riset → kesulitan mengikuti beban kuliah.
        * **Modal sosial dan dukungan akademik**: Orang tua berpendidikan tinggi cenderung lebih mampu mendampingi, mengarahkan dan memberikan akses ke sumber belajar; sebaliknya, orang tua dengan kualifikasi/pekerjaan rendah atau “unknown” mungkin tidak punya pengalaman atau jaringan yang memadai untuk membantu anak.
    * Program studi tertentu seperti **Equinculture, Management (Evening Attendance), dan Informatics Engineering** perlu perhatian ekstra.
        * **Tingkat kesulitan kurikulum**:
            * **Informatics Engineering** sering menuntut dasar matematika dan pemrograman kuat.
            * **Equinculture** memiliki kombinasi teori dan praktik lapangan yang intensif, tidak semua mahasiswa siap.
        * **Format malam (evening attendance)**: Biasanya beban per SKS diatur padat sesuai jadwal kerja audien malam, sehingga durasi belajar efektif per minggu lebih sedikit.

* **Beasiswa & Pembayaran UKT** terbukti sangat protektif:
    * Mahasiswa penerima beasiswa dan yang membayar UKT tepat waktu memiliki dropout rate jauh lebih rendah.
       * **Security finansial**: Bebas khawatir biaya studi membuat mahasiswa bisa fokus belajar dan mengakses fasilitas kampus (perpustakaan, laboratorium, dan sebagainya).
       * **Komitmen administrasi**: Mahasiswa yang disiplin dalam kewajiban keuangan cenderung juga disiplin dalam kehadiran dan penyelesaian tugas.
* **Mahasiswa internasional** (terutama perempuan) relatif lebih tahan risiko dibanding lokal—ini bisa jadi efek seleksi awal (hanya yang sangat termotivasi yang mendaftar).
    * **Seleksi awal**: Proses penerimaan internasional umumnya lebih ketat seperti skor bahasa, rekomendasi, dan bukti finansial sehingga hanya kandidat dengan sumber daya dan motivasi tinggi yang diterima.
    * **Dukungan khusus**: Banyak kampus menyediakan program orientasi, bimbingan bahasa, dan komunitas internasional yang meningkatkan sense of belonging dan retensi.

### Recommendation Action Items (Optional)

1. **Perluas & Prioritaskan Beasiswa**
      * Fokus pada **laki‑laki di kelas malam** dan mereka dari **kualifikasi rendah**.
      * Gunakan data risiko untuk menargetkan calon penerima beasiswa.
2. **Intervensi Keuangan & Pendampingan UKT**
      * Buat mekanisme cicilan atau skema subsidi untuk mencegah mahasiswa “Telat Bayar UKT” yang dropout rate–nya di atas 80 %.
      * Sediakan konseling keuangan bagi keluarga yang mengalami kesulitan bayar.
3. **Program Mentorship & Tutorial**
      * Tawarkan **bimbingan akademik khusus** untuk mahasiswa dengan kualifikasi “Basic education 3rd cycle” dan program studi berisiko tinggi (Equinculture, Management malam, Informatics Engineering).
      * Libatkan alumni sukses atau mahasiswa senior sebagai mentor.
4. **Fleksibilitas Pelaksanaan Kuliah Malam**
      * Evaluasi jadwal dan beban mata kuliah malam—kurangi beban per semester, atur ulang evaluasi agar mahasiswa dapat mengikuti lebih baik.
5. **Pemetaan Profil Risiko Keluarga**
      * Identifikasi mahasiswa dengan **orang tua berpendidikan/pekerjaan rendah atau tak diketahui** → berikan dukungan ekstra (seminar parenting, sosialisasi akses kependidikan).
6. **Pemasaran Internasional & Program Integrasi**
      * Pertahankan skema **beasiswa/dukungan** untuk **mahasiswa internasional**, tingkatkan program orientasi & integrasi agar mereka tetap engaged.

# **Prediksi Risiko Diabetes Dan Sistem Rekomendasi Kesehatan**

## Originalitas
 Repository berikut merupakan hasil dari Team RnD Intel dan Original dibuat oleh team ini.

## Latar Belakang

Diabetes telah menjadi masalah kesehatan global yang semakin meningkat, terutama di kawasan Asia Tenggara, termasuk Indonesia. Banyak penderita diabetes yang tidak menyadari kondisi mereka, yang menyebabkan komplikasi serius jika tidak terkontrol. Oleh karena itu, penting untuk melakukan deteksi dini agar tindakan pencegahan dan pengobatan dapat dilakukan lebih cepat, sebelum komplikasi terjadi. Penelitian ini bertujuan untuk mengembangkan sebuah sistem yang dapat memprediksi risiko seseorang terkena diabetes, sehingga dapat membantu mengurangi beban penyakit ini dan meningkatkan kualitas hidup penderita diabetes di Indonesia.

## Data yang Digunakan

Dataset yang digunakan dalam penelitian ini adalah dataset diabetes yang dapat diakses melalui [Mendeley Data](https://data.mendeley.com/datasets/7zcc8v6hvp/1). Dataset ini berisi informasi tentang berbagai faktor risiko yang dapat mempengaruhi kemungkinan seseorang untuk mengidap diabetes.

## Feature Engineering

Dataset yang telah dikumpulkan melalui proses pembersihan dan pengolahan data (feature engineering) untuk mempersiapkan fitur-fitur yang relevan bagi model prediksi. Proses ini mencakup merge kedua data, pembersihan data, penanganan nilai yang hilang, dan pemilihan fitur yang penting bagi akurasi model prediksi.

## Model yang Digunakan

Model yang digunakan untuk memprediksi risiko diabetes adalah **XGBoost Classifier**, sebuah algoritma machine learning yang sangat efektif untuk tugas klasifikasi. Model ini dilatih menggunakan data yang telah diproses dan dioptimalkan dengan parameter berikut:

- **Model:** XGBoost Classifier
- **n_estimators:** 100
- **max_depth:** 3
- **learning_rate:** 0.1

Model ini telah diuji dan menunjukkan performa yang sangat baik, dengan akurasi yang mencapai **100%** pada data train dan test.

## Rekomendasi Sistem

Hasil prediksi yang diperoleh dari model ini digunakan untuk memberikan rekomendasi makanan yang sesuai dengan kondisi kesehatan individu tersebut. 

## Deployment

Sistem ini diimplementasikan dalam bentuk **web prototype** menggunakan **Streamlit**, yang memungkinkan pengguna untuk mengakses dan berinteraksi dengan aplikasi prediksi risiko diabetes secara langsung melalui antarmuka web. Pengguna dapat memasukkan data mereka, melihat hasil prediksi, dan menerima rekomendasi yang sesuai dengan kondisi kesehatan mereka.

## Cara Menjalankan Streamlit

1. Clone repositori ini:
   ```bash
   git clone https://github.com/username/repository-name.git

2. Instal dependensi yang diperlukan:
   ```
   python -m venv data_env
   source env_ecomm/bin/activate
   pip install -r requirements.txt
   ```
3. Jalankan aplikasi Streamlit:
   ```
   python -m streamlit run streamlit_data.py
   ```
## Demo
Link Streamlit : 

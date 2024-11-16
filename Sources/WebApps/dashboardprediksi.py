# Importing Libraries
import pickle
import streamlit as st
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Load the XGBoost model
model_path = "Sources/Model/xgb_model.sav"
loaded_model = pickle.load(open(model_path, 'rb'))

# Function to predict diabetes
def predict_diabetes(inputs):
    inputs = np.array(inputs).reshape(1, -1)
    prediction = loaded_model.predict(inputs)[0]
    probability = loaded_model.predict_proba(inputs)[0][1]
    return prediction, probability

# Function to generate health recommendations
# Fungsi untuk menghasilkan rekomendasi kesehatan berdasarkan fitur yang berpengaruh
# Function to generate health recommendations based on impactful features
def generate_recommendations(prediction, inputs):
    recommendations = []
    if prediction == 1:
        recommendations.append("Risiko diabetes tinggi terdeteksi! Silakan konsultasikan dengan penyedia layanan kesehatan Anda.")

        # Glucose level check
        if inputs[1] > 120:
            recommendations.append("Pertimbangkan untuk mengurangi asupan gula dan memantau kadar glukosa darah secara rutin.")

        # Diabetes Pedigree Function check
        if inputs[2] < 0.3:
            recommendations.append("Perbanyak makanan yang kaya lemak sehat dan protein untuk meningkatkan kesehatan secara keseluruhan.")

        # Feature-based recommendations
        if inputs[8] == 1:  # Polyuria
            recommendations.append("Sering buang air kecil (Polyuria) terdeteksi. Tetap terhidrasi dan pantau asupan cairan Anda.")
        if inputs[9] == 1:  # Polydipsia
            recommendations.append("Rasa haus berlebihan (Polydipsia) terdeteksi. Batasi konsumsi minuman manis dan konsultasikan dengan dokter.")
        if inputs[11] == 1:  # Polyphagia
            recommendations.append("Rasa lapar berlebihan (Polyphagia) terdeteksi. Terapkan pola makan seimbang untuk mengatur nafsu makan.")
        if inputs[16] == 1:  # Visual Blurring
            recommendations.append("Penglihatan kabur (Visual Blurring) terdeteksi. Jadwalkan pemeriksaan mata untuk memeriksa komplikasi terkait diabetes.")
        if inputs[19] == 1:  # Partial Paresis
            recommendations.append("Kelemahan otot (Partial Paresis) terdeteksi. Lakukan latihan fisik ringan atau terapi fisik.")
        if inputs[22] == 1:  # Muscle Stiffness
            recommendations.append("Kekakuan otot (Muscle Stiffness) terdeteksi. Sertakan peregangan dan aktivitas ringan dalam rutinitas Anda.")
        if inputs[18] == 1:  # Delayed Healing
            recommendations.append("Penyembuhan luka yang lambat (Delayed Healing) terdeteksi. Lakukan perawatan luka yang tepat dan konsultasikan dengan profesional kesehatan.")

        recommendations.append("Lakukan aktivitas fisik secara teratur, seperti berjalan kaki atau yoga.")
    else:
        recommendations.append("Risiko diabetes rendah. Pertahankan gaya hidup sehat untuk menjaga kondisi Anda!")
        recommendations.append("Pola makan seimbang dan pemeriksaan kesehatan rutin sangat disarankan.")

    return recommendations


# Sidebar for navigation
image = Image.open("Sources/WebApps/logo.png")
st.sidebar.image(image, use_column_width=True)
st.sidebar.title("Halaman Web")
page = st.sidebar.radio("Daftar Halaman", ["Welcome Page", "Deskripsi Data", "Prediksi Diabetes"])

# Page 1: Welcome
if page == "Welcome Page":
    st.title("Selamat datang di Website Prediksi Diabetes")

    st.markdown("""
    Website ini menggunakan model Machine Learning untuk memprediksi kemungkinan diabetes berdasarkan masukan kesehatan. 
    Navigasikan halaman untuk mempelajari lebih lanjut dan melakukan tes prediksi.
    """)

    st.markdown("""
        <div style='background-color: #e0f7fa; padding: 20px; border-radius: 10px;'>
            <h1 style='text-align: center; font-family: Arial, sans-serif; color: #000;'>
                Selamat Datang di <span style='color: #007acc;'>Portal Kesehatan Anda!</span>
            </h1>
            <p style='text-align: center; font-size: 18px; font-style: italic; color: #333;'>
                Perjalanan Anda menuju kesehatan yang lebih baik dimulai di sini.
            </p>
            <p style='text-align: center; font-size: 16px; color: #555;'>
                Jeajahi tips dan sumber daya kami untuk tetap sehat dan berkembang.
            </p>
        </div>
    """, unsafe_allow_html=True)

# Page 2: Description
elif page == "Deskripsi Data":
    st.title("Mengenai website prediksi diabetes")
    st.write("""
        Website ini membantu memprediksi risiko diabetes berdasarkan masukan pengguna terkait gejala dan parameter kesehatan.
        Web ini menggunakan model machine learning XGBoost untuk menganalisis data dan memberikan prediksi. Data yang digunakan
        pada model menggunakan data resmi yang diambil pada Data Mendeley, berikut merupakan link sumber data: [Mendeley Diabetes Data](https://data.mendeley.com/datasets/7zcc8v6hvp/1).
        
        
        **Penggunaan :**
        1. Buka halaman **Diabetes Prediction Test**.
        2. Isi rincian yang diperlukan berdasarkan kesehatan dan gejala Anda.
        3. Klik tombol untuk mendapatkan hasil prediksi Anda.
    """)
    st.write("Untuk informasi lebih lanjut, silakan kunjungi : [World Diabetes Foundation](https://www.worlddiabetesfoundation.org/).")
 
    st.header("Panduan Parameter Input")

    # Outline with collapsible sections for each parameter
    with st.expander("Pregnancies"):
        st.write("""
                  Jumlah kehamilan dapat memengaruhi risiko diabetes.Untuk referensi lebih lanjut mengenai topik ini, Anda dapat merujuk pada artikel berikut:
                 1. "Gestational diabetes mellitus": Artikel ini membahas patofisiologi, komplikasi, dan manajemen diabetes gestasional secara mendalam :https://en.wikipedia.org/wiki/Gestational_diabetes. 
                 2. "Diabetic embryopathy": Artikel ini mengulas malformasi kongenital yang terkait dengan diabetes maternal, termasuk risiko dan mekanisme terjadinya :https://en.wikipedia.org/wiki/Diabetic_embryopathy. 
                 3. "Metabolic imprinting": Artikel ini menjelaskan efek jangka panjang dari lingkungan prenatal dan postnatal pada metabolisme keturunan, termasuk bagaimana diabetes maternal dapat mempengaruhi risiko penyakit metabolik pada anak :https://en.wikipedia.org/wiki/Metabolic_imprinting.
                 """)

    with st.expander("Glucose"):
        st.write("Untuk menyatakan kadar Glukosa dalam darah. Kadar glukosa yang tinggi dapat mengindikasikan risiko diabetes.")
 # Function to draw glucose illustration
        def draw_glucose_illustration():
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.set_xlim(-6, 6)
            ax.set_ylim(-1, 5)
            ax.axis('off')
            
            # Title
            ax.text(0, 4.5, "GLUCOSE IN THE BLOOD", ha='center', fontsize=18, fontweight='bold')
            
            # Normal Level box
            normal_box = patches.Rectangle((-5, 0), 4, 3, linewidth=2, edgecolor='blue', facecolor='none')
            ax.add_patch(normal_box)
            ax.text(-3, -0.5, "NORMAL LEVEL", ha='center', fontsize=14, color='blue', fontweight='bold')
            
            # Normal blood cells and glucose molecules
            normal_red_cells = [(-4.5, 2.5), (-3.5, 2.5), (-2.5, 2.5), (-4.5, 1.5), (-3.5, 1.5), (-2.5, 1.5), (-4.5, 0.5), (-3.5, 0.5), (-2.5, 0.5)]
            normal_glucose = [(-4.2, 2), (-3.2, 2), (-2.2, 2), (-4.8, 1), (-3.2, 1), (-2.2, 1), (-4.8, 0), (-3.2, 0), (-2.2, 0)]
            
            for x, y in normal_red_cells:
                red_cell = patches.Circle((x, y), 0.3, color='red')
                ax.add_patch(red_cell)
            
            for x, y in normal_glucose:
                glucose_molecule = patches.Circle((x, y), 0.15, color='yellow')
                ax.add_patch(glucose_molecule)
            
            # Diabetes box
            diabetes_box = patches.Rectangle((1, 0), 4, 3, linewidth=2, edgecolor='red', facecolor='none')
            ax.add_patch(diabetes_box)
            ax.text(3, -0.5, "DIABETES", ha='center', fontsize=14, color='red', fontweight='bold')
            
            # Diabetic blood cells and glucose molecules
            diabetic_red_cells = [(1.5, 2.5), (2.5, 2.5), (3.5, 2.5), (4.5, 2.5), (1.5, 1.5), (2.5, 1.5), (3.5, 1.5), (4.5, 1.5), (1.5, 0.5), (2.5, 0.5), (3.5, 0.5), (4.5, 0.5)]
            diabetic_glucose = [(x, y) for x in [1.2, 1.8, 2.2, 2.8, 3.2, 3.8, 4.2, 4.8] for y in [2.7, 2.2, 1.7, 1.2, 0.7, 0.2]]
            
            for x, y in diabetic_red_cells:
                red_cell = patches.Circle((x, y), 0.3, color='red')
                ax.add_patch(red_cell)
            
            for x, y in diabetic_glucose:
                glucose_molecule = patches.Circle((x, y), 0.15, color='yellow')
                ax.add_patch(glucose_molecule)
            
            st.pyplot(fig)
        
        draw_glucose_illustration()

    with st.expander("Blood Pressure"):
        st.write("Tekanan darah dalam satuan mmHg. Tekanan darah tinggi berhubungan dengan berbagai masalah kesehatan, termasuk diabetes.")

    with st.expander("Skin Thickness"):
        st.write("Ketebalan lipatan kulit, diukur dalam milimeter. Ketebalan kulit dapat memberikan indikasi tentang kadar lemak tubuh.")

    with st.expander("Insulin"):
        st.write("Kadar insulin dalam darah diukur dalam mu U/ml. Ketidakseimbangan insulin merupakan indikator diabetes.")

    with st.expander("BMI (Body Mass Index)"):
        st.write("Indeks massa tubuh, dihitung dari berat dan tinggi badan. BMI tinggi dapat meningkatkan risiko diabetes.")

    with st.expander("Diabetes Pedigree Function"):
        st.write("Fungsi silsilah diabetes menunjukkan kemungkinan genetik seseorang untuk menderita diabetes.")

    with st.expander("Age"):
        st.write("Usia dalam tahun. Risiko diabetes dapat meningkat seiring bertambahnya usia.")

    with st.expander("Gender"):
        st.write("Jenis kelamin: 0 untuk wanita, 1 untuk pria. Risiko diabetes dapat berbeda berdasarkan jenis kelamin.")

    # Additional parameters related to symptoms
    st.subheader("Parameter Gejala")

    with st.expander("Polyuria"):
        st.write("Sering buang air kecil (Polyuria). Ini bisa menjadi gejala diabetes karena tubuh berusaha mengeluarkan glukosa berlebih.")

    with st.expander("Polydipsia"):
        st.write("Rasa haus berlebihan (Polydipsia). Ini adalah gejala umum dari diabetes.")

    with st.expander("Polyphagia"):
        st.write("Rasa lapar berlebihan (Polyphagia). Rasa lapar berlebihan adalah gejala yang umum pada diabetes.")

    with st.expander("Genital Thrush"):
        st.write("Infeksi jamur genital yang bisa sering muncul pada penderita diabetes.")

    with st.expander("Weakness"):
        st.write("Merasa lemah atau lesu, yang bisa terjadi karena ketidakseimbangan gula darah.")

    with st.expander("Irritability"):
        st.write("Perasaan mudah marah. Fluktuasi gula darah dapat memengaruhi suasana hati.")

    with st.expander("Partial Paresis"):
        st.write("Paralisis parsial atau kelemahan otot. Ini mungkin terkait dengan komplikasi diabetes.")

    with st.expander("Muscle Stiffness"):
        st.write("Kekakuan otot, yang bisa menjadi gejala komplikasi diabetes.")

    with st.expander("Alopecia"):
        st.write("Kebotakan atau rambut rontok. Ketidakseimbangan hormon terkait diabetes bisa memengaruhi rambut.")

    with st.expander("Visual Blurring"):
        st.write("Penglihatan kabur, yang dapat disebabkan oleh kadar gula darah tinggi.")

    with st.expander("Delayed Healing"):
        st.write("Luka yang lambat sembuh, gejala umum diabetes yang tidak terkontrol.")

    with st.expander("Obesity"):
        st.write("Kondisi obesitas, yang merupakan faktor risiko utama diabetes.")

    with st.expander("Sudden Weight Loss"):
        st.write("Kehilangan berat badan secara tiba-tiba, yang bisa menjadi tanda diabetes karena tubuh tidak dapat menggunakan glukosa dengan baik.")

    with st.expander("Itching"):
        st.write("Rasa gatal yang mungkin muncul akibat kadar gula darah tinggi dan infeksi kulit yang berhubungan dengan diabetes.")


# Page 3: Diabetes Prediction Test
elif page == "Prediksi Diabetes":
    st.title("Prediksi Diabetes")
    st.write("Jawablah pertanyaan-pertanyaan berikut berdasarkan status kesehatan Anda untuk menilai risiko diabetes Anda dan mendapatkan rekomendasi kesehatan yang disesuaikan.")

    # User inputs
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input('Pregnancies', min_value=0,value=1, step=1)
        SkinThickness = st.number_input('Skin Thickness', min_value=0.0, value=20.0)
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function', min_value=0.0, value=0.5)
        Polyuria = st.selectbox('Polyuria (0 = No, 1 = Yes)', [0, 1])
        Polyphagia = st.selectbox('Polyphagia (0 = No, 1 = Yes)', [0, 1])
        Itching = st.selectbox('Itching (0 = No, 1 = Yes)', [0, 1])
        PartialParesis = st.selectbox('Partial Paresis (0 = No, 1 = Yes)', [0, 1])
        Alopecia = st.selectbox('Alopecia (0 = No, 1 = Yes)', [0, 1])

    with col2:
        Glucose = st.number_input('Glucose', min_value=0.0, value=120.0)
        Insulin = st.number_input('Insulin', min_value=0.0, value=80.0)
        Age = st.number_input('Age', min_value=0, value=30, step=1)
        Polydipsia = st.selectbox('Polydipsia (0 = No, 1 = Yes)', [0, 1])
        GenitalThrush = st.selectbox('Genital Thrush (0 = No, 1 = Yes)', [0, 1])
        Irritability = st.selectbox('Irritability (0 = No, 1 = Yes)', [0, 1])
        MuscleStiffness = st.selectbox('Muscle Stiffness (0 = No, 1 = Yes)', [0, 1])
        Obesity = st.selectbox('Obesity (0 = No, 1 = Yes)', [0, 1])

    with col3:
        BloodPressure = st.number_input('Blood Pressure', min_value=0.0, value=70.0)
        BodyMassIndex = st.number_input('BMI', min_value=0.0, value=25.0)
        Gender = st.selectbox('Gender (0 = Female, 1 = Male)', [0, 1])
        SuddenWeightLoss = st.selectbox('Sudden Weight Loss (0 = No, 1 = Yes)', [0, 1])
        Weakness = st.selectbox('Weakness (0 = No, 1 = Yes)', [0, 1])
        VisualBlurring = st.selectbox('Visual Blurring (0 = No, 1 = Yes)', [0, 1])
        DelayedHealing = st.selectbox('Delayed Healing (0 = No, 1 = Yes)', [0, 1])

    # Collect user inputs into a list
    user_inputs = [
        Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
        BodyMassIndex, DiabetesPedigreeFunction, Age, Gender,
        Polyuria, Polydipsia, Polyphagia, GenitalThrush, Weakness,
        Irritability, PartialParesis, MuscleStiffness, Alopecia,
        VisualBlurring, DelayedHealing, Obesity, SuddenWeightLoss, Itching
    ]

    # Predict and generate recommendations
    if st.button("Periksa Risiko Diabetes"):
        prediction, probability = predict_diabetes(user_inputs)
        recommendations = generate_recommendations(prediction, user_inputs)

        # Display results
        if prediction == 1:
            st.error(f"Risiko tinggi diabetes terdeteksi! Kemungkinan: {probability:.2f}")
        else:
            st.success(f"Resiko rendah terkena diabetes. Kemungkinan: {probability:.2f}")

        # Display recommendations
        st.subheader("Rekomendasi Kesehatan Anda:")
        for rec in recommendations:
            st.write(f"- {rec}")

# Footer
st.write("Disclaimer: Prediksi ini berdasarkan masukan data dan membantu Anda mengetahui kondisi kesehatan Anda.")

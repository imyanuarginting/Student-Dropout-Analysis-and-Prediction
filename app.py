import streamlit as st
import pandas as pd
import joblib
import cat_dict as cd

@st.cache_data()
def load_model(model_path):
    return joblib.load(model_path)

@st.cache_data()
def load_scaler(scaler_path):
    return joblib.load(scaler_path)

# Fungsi untuk melakukan prediksi
def predict(model, scaler, input_data):
    X_new = pd.DataFrame(input_data, index=[0])
    X_new = scaler.transform(X_new)
    y_pred = model.predict(X_new)
    return y_pred[0]

def main():
    st.title('Student Dropout Prediction')
    st.markdown('Fill in the following columns with the student data you want to predict.')

    marital_status = st.selectbox(
        'Marital Status', 
        ['single',
         'married',
         'widower',
         'divorced',
         'facto union',
         'legally separated',
    ])
    application_mode = st.selectbox(
        'Application Mode', 
        ['1st phase - general contingent', 
         'Ordinance No. 612/93',
         '1st phase - special contingent (Azores Island)',
         'Holders of other higher courses',
         'Ordinance No. 854-B/99', 
         'International student (bachelor)', 
         '1st phase - special contingent (Madeira Island)', 
         '2nd phase - general contingent', 
         '3rd phase - general contingent', 
         'Ordinance No. 533-A/99, item b2 (Different Plan)', 
         'Ordinance No. 533-A/99, item b3 (Other Institution)', 
         'Over 23 years old', 
         'Transfer', 
         'Change of course', 
         'Technological specialization diploma holders',
         'Change of institution/course', 
         'Short cycle diploma holders', 
         'Change of institution/course (International)',
    ])
    application_order = st.number_input('Application Order (0-9)', value=0)
    course = st.selectbox(
        'Course', 
        ['Biofuel Production Technologies',
         'Animation and Multimedia Design',
         'Social Service (evening attendance)',
         'Agronomy',
         'Communication Design',
         'Veterinary Nursing',
         'Informatics Engineering',
         'Equinculture',
         'Management',
         'Social Service',
         'Tourism',
         'Nursing',
         'Oral Hygiene',
         'Advertising and Marketing Management', 
         'Journalism and Communication',
         'Basic Education',
         'Management (evening attendance)',
    ])
    daytime_evening_attendance = st.selectbox(
        'Daytime Evening Attendance', 
        ['daytime',
         'evening',
    ])
    previous_qualification = st.selectbox(
        'Previous Qualification', 
        ['Secondary education',
         "Higher education - bachelor's degree",
         'Higher education - degree',
         "Higher education - master's",
         'Higher education - doctorate',
         'Frequency of higher education',
         '12th year of schooling - not completed',
         '11th year of schooling - not completed',
         'Other - 11th year of schooling',
         '10th year of schooling',
         '10th year of schooling - not completed',
         'Basic education 3rd cycle (9th/10th/11th year) or equiv.',
         'Basic education 2nd cycle (6th/7th/8th year) or equiv.',
         'Technological specialization course',
         'Higher education - degree (1st cycle)',
         'Professional higher technical course',
         'Higher education - master (2nd cycle)',
    ])
    previous_qualification_grade = st.number_input('Previous Qualification Grade (0-200)', format="%0.1f")
    nacionality = st.selectbox(
        'Nacionality', 
        ['Portuguese',
         'German',
         'Spanish',
         'Italian',
         'Dutch',
         'English',
         'Lithuanian',
         'Angolan',
         'Cape Verdean',
         'Guinean',
         'Mozambican',
         'Santomean',
         'Turkish',
         'Brazilian',
         'Romanian',
         'Moldova (Republic of)',
         'Mexican',
         'Ukrainian',
         'Russian',
         'Cuban',
         'Colombian',
    ])
    mothers_qualification = st.selectbox(
        "Mother's Qualification", 
        ['Secondary Education - 12th Year of Schooling or Eq.',
         "Higher Education - Bachelor's Degree", 
         'Higher Education - Degree', 
         "Higher Education - Master's", 
         'Higher Education - Doctorate', 
         'Frequency of Higher Education', 
         '12th Year of Schooling - Not Completed', 
         '11th Year of Schooling - Not Completed', 
         '7th Year (Old)', 
         'Other - 11th Year of Schooling', 
         '10th Year of Schooling', 
         'General commerce course', 
         'Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.', 
         'Technical-professional course', 
         '7th year of schooling', 
         '2nd cycle of the general high school course', 
         '9th Year of Schooling - Not Completed', 
         '8th year of schooling', 
         'Unknown', 
         "Can't read or write", 
         'Can read without having a 4th year of schooling', 
         'Basic education 1st cycle (4th/5th year) or equiv.', 
         'Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.', 
         'Technological specialization course', 
         'Higher education - degree (1st cycle)', 
         'Specialized higher studies course', 
         'Professional higher technical course', 
         'Higher Education - Master (2nd cycle)', 
         'Higher Education - Doctorate (3rd cycle)',
    ])
    fathers_qualification = st.selectbox(
        "Father's Qualification", 
        ['Secondary Education - 12th Year of Schooling or Eq.',
         "Higher Education - Bachelor's Degree",
         'Higher Education - Degree', 
         "Higher Education - Master's", 
         'Higher Education - Doctorate', 
         'Frequency of Higher Education', 
         '12th Year of Schooling - Not Completed', 
         '11th Year of Schooling - Not Completed', 
         '7th Year (Old)', 
         'Other - 11th Year of Schooling', 
         '2nd year complementary high school course', 
         '10th Year of Schooling', 
         'General commerce course', 
         'Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.', 
         'Complementary High School Course', 
         'Technical-professional course', 
         'Complementary High School Course - not concluded', 
         '7th year of schooling', 
         '2nd cycle of the general high school course', 
         '9th Year of Schooling - Not Completed', 
         '8th year of schooling', 
         'General Course of Administration and Commerce', 
         'Supplementary Accounting and Administration', 
         'Unknown', 
         "Can't read or write", 
         'Can read without having a 4th year of schooling', 
         'Basic education 1st cycle (4th/5th year) or equiv.', 
         'Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.', 
         'Technological specialization course', 
         'Higher education - degree (1st cycle)', 
         'Specialized higher studies course', 
         'Professional higher technical course', 
         'Higher Education - Master (2nd cycle)', 
         'Higher Education - Doctorate (3rd cycle)',
    ])
    mothers_occupation = st.selectbox(
        "Mother's Occupation", 
        ['Student',
         'Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers', 
         'Specialists in Intellectual and Scientific Activities', 
         'Intermediate Level Technicians and Professions', 
         'Administrative staff', 
         'Personal Services, Security and Safety Workers and Sellers', 
         'Farmers and Skilled Workers in Agriculture, Fisheries and Forestry', 
         'Skilled Workers in Industry, Construction and Craftsmen', 
         'Installation and Machine Operators and Assembly Workers', 
         'Unskilled Workers', 
         'Armed Forces Professions', 
         'Other Situation', 
         '(blank)', 
         'Health professionals', 
         'teachers', 
         'Specialists in information and communication technologies (ICT)', 
         'Intermediate level science and engineering technicians and professions', 
         'Technicians and professionals, of intermediate level of health', 
         'Intermediate level technicians from legal, social, sports, cultural and similar services', 
         'Office workers, secretaries in general and data processing operators', 
         'Data, accounting, statistical, financial services and registry-related operators', 
         'Other administrative support staff', 
         'personal service workers', 
         'sellers', 
         'Personal care workers and the like', 
         'Skilled construction workers and the like, except electricians', 
         'Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like', 
         'Workers in food processing, woodworking, clothing and other industries and crafts', 
         'cleaning workers', 
         'Unskilled workers in agriculture, animal production, fisheries and forestry', 
         'Unskilled workers in extractive industry, construction, manufacturing and transport', 
         'Meal preparation assistants',
    ])
    fathers_occupation = st.selectbox(
        "Father's Occupation", 
        ['Student',
         'Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers', 
         'Specialists in Intellectual and Scientific Activities', 
         'Intermediate Level Technicians and Professions', 
         'Administrative staff', 
         'Personal Services, Security and Safety Workers and Sellers', 
         'Farmers and Skilled Workers in Agriculture, Fisheries and Forestry', 
         'Skilled Workers in Industry, Construction and Craftsmen', 
         'Installation and Machine Operators and Assembly Workers', 
         'Unskilled Workers', 
         'Armed Forces Professions', 
         'Other Situation', 
         '(blank)', 
         'Armed Forces Officers', 
         'Armed Forces Sergeants', 
         'Other Armed Forces personnel', 
         'Directors of administrative and commercial services', 
         'Hotel, catering, trade and other services directors', 
         'Specialists in the physical sciences, mathematics, engineering and related techniques', 
         'Health professionals', 
         'teachers', 
         'Specialists in finance, accounting, administrative organization, public and commercial relations', 
         'Intermediate level science and engineering technicians and professions', 
         'Technicians and professionals, of intermediate level of health', 
         'Intermediate level technicians from legal, social, sports, cultural and similar services', 
         'Information and communication technology technicians', 
         'Office workers, secretaries in general and data processing operators', 
         'Data, accounting, statistical, financial services and registry-related operators', 
         'Other administrative support staff', 
         'personal service workers', 
         'sellers', 
         'Personal care workers and the like', 
         'Protection and security services personnel', 
         'Market-oriented farmers and skilled agricultural and animal production workers', 
         'Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence', 
         'Skilled construction workers and the like, except electricians', 
         'Skilled workers in metallurgy, metalworking and similar', 
         'Skilled workers in electricity and electronics', 
         'Workers in food processing, woodworking, clothing and other industries and crafts', 
         'Fixed plant and machine operators', 
         'assembly workers', 
         'Vehicle drivers and mobile equipment operators', 
         'Unskilled workers in agriculture, animal production, fisheries and forestry', 
         'Unskilled workers in extractive industry, construction, manufacturing and transport', 
         'Meal preparation assistants', 
         'Street vendors (except food) and street service providers',
    ])
    admission_grade = st.number_input('Admission Grade (0-200)', format="%0.1f")
    displaced = st.selectbox(
        'Displaced', 
        ['yes',
         'no',
    ])
    educational_special_needs = st.selectbox(
        'Educational Special Needs', 
        ['yes',
         'no',
    ])
    debtor = st.selectbox(
        'Debtor', 
        ['yes',
         'no',
    ])
    tuition_fees_up_to_date = st.selectbox(
        'Tuition Fees Up To Date', 
        ['yes',
         'no',
    ])
    gender = st.selectbox(
        'Gender', 
        ['male', 
         'female',
    ])
    scholarship_holder = st.selectbox(
        'Scholarship Holder', 
        ['yes',
         'no',
    ])
    age_at_enrollment = st.number_input('Age at Enrollment', value=0)
    international = st.selectbox(
        'International', 
        ['yes',
         'no',
    ])
    curricular_units_1st_sem_credited = st.number_input('Curricular Units 1st Sem Credited', value=0)
    curricular_units_1st_sem_enrolled = st.number_input('Curricular Units 1st Sem Enrolled', value=0)
    curricular_units_1st_sem_evaluations = st.number_input('Curricular Units 1st Sem Evaluations', value=0)
    curricular_units_1st_sem_approved = st.number_input('Curricular Units 1st Sem Approved', value=0)
    curricular_units_1st_sem_grade = st.number_input('Curricular Units 1st Sem Grade', format="%0.1f")
    curricular_units_1st_sem_without_evaluations = st.number_input('Curricular Units 1st Sem Without Evaluations', value=0)
    curricular_units_2nd_sem_credited = st.number_input('Curricular Units 2nd Sem Credited', value=0)
    curricular_units_2nd_sem_enrolled = st.number_input('Curricular Units 2nd Sem Enrolled', value=0)
    curricular_units_2nd_sem_evaluations = st.number_input('Curricular Units 2nd Sem Evaluations', value=0)
    curricular_units_2nd_sem_approved = st.number_input('Curricular Units 2nd Sem Approved', value=0)
    curricular_units_2nd_sem_grade = st.number_input('Curricular Units 2nd Sem Grade', format="%0.1f")
    curricular_units_2nd_sem_without_evaluations = st.number_input('Curricular Units 2nd Sem Without Evaluations', value=0)
    unemployment_rate = st.number_input('Unemployment Rate', format="%0.1f")
    inflation_rate = st.number_input('Inflation Rate', format="%0.1f")
    gdp = st.number_input('GDP', format="%0.2f")

    # Tombol untuk memulai prediksi
    if st.button('Prediksi'):
        # Load model
        model = load_model('Include/lr_model.pkl')
        scaler = load_scaler('Include/scaler.pkl')

        # Masukkan data ke dalam dictionary
        input_data = {
            'Marital_status': [cd.marital_status_dict[marital_status]],
            'Application_mode': [cd.application_mode_dict[application_mode]],
            'Application_order': [application_order],
            'Course': [cd.course_dict[course]],
            'Daytime_evening_attendance': [cd.daytime_evening_attendance_dict[daytime_evening_attendance]],
            'Previous_qualification': [cd.previous_qualification_dict[previous_qualification]],
            'Previous_qualification_grade': [previous_qualification_grade],
            'Nacionality': [cd.nacionality_dict[nacionality]],
            'Mothers_qualification': [cd.mothers_qualification_dict[mothers_qualification]],
            'Fathers_qualification': [cd.fathers_qualification_dict[fathers_qualification]],
            'Mothers_occupation': [cd.mothers_occupation_dict[mothers_occupation]],
            'Fathers_occupation': [cd.fathers_occupation_dict[fathers_occupation]],
            'Admission_grade': [admission_grade],
            'Displaced': [cd.displaced_dict[displaced]],
            'Educational_special_needs': [cd.educational_special_needs_dict[educational_special_needs]],
            'Debtor': [cd.debtor_dict[debtor]],
            'Tuition_fees_up_to_date': [cd.tuition_fees_up_to_date_dict[tuition_fees_up_to_date]],
            'Gender': [cd.gender_dict[gender]],
            'Scholarship_holder': [cd.scholarship_holder_dict[scholarship_holder]],
            'Age_at_enrollment': [age_at_enrollment],
            'International': [cd.international_dict[international]],
            'Curricular_units_1st_sem_credited': [curricular_units_1st_sem_credited],
            'Curricular_units_1st_sem_enrolled': [curricular_units_1st_sem_enrolled],
            'Curricular_units_1st_sem_evaluations': [curricular_units_1st_sem_evaluations],
            'Curricular_units_1st_sem_approved': [curricular_units_1st_sem_approved],
            'Curricular_units_1st_sem_grade': [curricular_units_1st_sem_grade],
            'Curricular_units_1st_sem_without_evaluations': [curricular_units_1st_sem_without_evaluations],
            'Curricular_units_2nd_sem_credited': [curricular_units_2nd_sem_credited],
            'Curricular_units_2nd_sem_enrolled': [curricular_units_2nd_sem_enrolled],
            'Curricular_units_2nd_sem_evaluations': [curricular_units_2nd_sem_evaluations],
            'Curricular_units_2nd_sem_approved': [curricular_units_2nd_sem_approved],
            'Curricular_units_2nd_sem_grade': [curricular_units_2nd_sem_grade],
            'Curricular_units_2nd_sem_without_evaluations': [curricular_units_2nd_sem_without_evaluations],
            'Unemployment_rate': [unemployment_rate],
            'Inflation_rate': [inflation_rate],
            'GDP': [gdp],
        }

        # Lakukan prediksi
        prediction = predict(model, scaler, input_data)

        # Tampilkan hasil prediksi
        if prediction == 0:
            st.success('Hasil Prediksi: Tidak dropout')
        else:
            st.warning('Hasil Prediksi: Berpotensi dropout')

# Memanggil fungsi utama untuk menjalankan dashboard
if __name__ == '__main__':
    main()
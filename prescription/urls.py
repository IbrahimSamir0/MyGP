from django.urls import include,path
from . import views


app_name='prescription'


urlpatterns = [
    # path('make_prescription/',views.makePrescription, name='create_prescription'),
    # path('create_prescription',views.MakePrescription.as_view({'get': 'list','post':'create'}), name='create_prescription'),
    path('postScreen',views.postScreen, name='postScreen'),
    # path('view',views.viewOldPrescriptions, name='ViewOldPrescriptions'),
    path('postscreens',views.upload_image, name='PostScreen'),
    
    path('get_active_doctor_patients/',views.GetActiveDoctorPatients.as_view(), name='GetActiveDoctorPatients'),
    path('get_old_doctor_patients/',views.GetOldDoctorPatients.as_view(), name='GetOldDoctorPatients'),
    path('get_all_doctor_patients/',views.GetAllDoctorPatients.as_view(), name='GetAllDoctorPatients'),
    
    path('get_all_booked_patients/',views.GetAllBookedPatients.as_view(), name='GetBookedPatients'),
    path('get_specific_clinic_booked_patients/<int:id>/',views.GetBookedPatientsInSpecificClinic.as_view(), name='GetBookedPatientsInEachClinic'),
    path('get_specific_appointment_booked_patients/<int:id>/',views.GetBookedPatientsInSpecificBooking.as_view(), name='GetBookedPatientsInEachClinic'),
    path('get_Today_booked_patients/',views.GetTodayBookedPatientsInClinic.as_view(), name='GetBookedPatientsInEachClinic'),
    
    path('get_my_all_clinics/',views.ListClinical.as_view(),name='ListClinical'),
    path('get_my_all_clinics/<int:id>/',views.GetSpecificClinical.as_view(),name='ListClinical'),
    path('get_doctor_patient_specific_prescription/<int:p_id>/',views.GetSpecificDoctorPatientPrescription.as_view(), name='GetSpecificDoctorPatientPrescription'),
    path('getscreen',views.GetScreen.as_view(), name='GetScreen'),
    path('cancel_my_Prescription/',views.CancelMyPrescription.as_view(), name='cancel_my_Prescription'),
    path('get_my_active_prescription/',views.GetMyActivePrescription.as_view(), name='GetMyActivePrescription'),
    path('get_my_old_prescriptions/',views.GetMyOldPrescriptions.as_view(), name='GetMyOldPrescriptions'),
    path('get_my_old_prescriptions/<int:p_id>/',views.GetSpecificOldPrescription.as_view(), name='GetSpecificOldPrescription'),
    path('set_appointment_for_doctors/',views.SetAppointmentForDoctors.as_view(), name='SetAppointmentForDoctors'),
    path('modify_appointment_for_doctors/<int:id>/',views.ModifySpecificAppointmentForDoctor.as_view(), name='ModifySpecificAppointmentForDoctor'),
    path('get_appointments_for_doctors/',views.GetMyAllAppointmentsForDoctor.as_view(), name='GetMyAllAppointmentsForDoctor'),
    path('get_all_standard_drugs/',views.GetAllStandardDrugsName.as_view(),name='GetAllStandardDrugsName'),
    path('get_all_standard_drugs_name_filter/',views.GetAllStandardDrugsNameFilter.as_view(),name='GetAllStandardDrugsName'),
    # path('set_drug/',views.SetDrug.as_view(), name='SetDrug'),   
]
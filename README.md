# Python_FAST_Api
Hands-on Practice Fast API Python

First Project : Weather Forcast

![Weather Forcast APP](weather_forcast/app_workflow/diagram.png)


========================================================
Second Project : Hospital Management System (Using JWT Auth login , signup ) ---> in-progress

✅ HMS API Modules & Suggested Endpoints
1. Authentication
    POST /auth/signup – Register new user (doctor, nurse, admin, patient)

    POST /auth/login – Login, returns JWT token

    POST /auth/logout – Logout user

    GET /auth/me – Get current user profile

2. Patients
    GET /patients/ – List all patients

    POST /patients/ – Create new patient record

    GET /patients/{id} – Get patient by ID

    PUT /patients/{id} – Update patient details

    DELETE /patients/{id} – Delete patient

3. Doctors
    GET /doctors/ – List all doctors

    POST /doctors/ – Register a doctor

    GET /doctors/{id} – Get doctor by ID

    PUT /doctors/{id} – Update doctor details

    DELETE /doctors/{id} – Remove doctor

4. Appointments
    GET /appointments/ – List all appointments

    POST /appointments/ – Book appointment

    GET /appointments/{id} – View appointment

    PUT /appointments/{id} – Reschedule appointment

    DELETE /appointments/{id} – Cancel appointment

5. Medical Records
    GET /records/ – List all medical records

    POST /records/ – Add new medical record

    GET /records/{id} – View medical record

    PUT /records/{id} – Update record

    DELETE /records/{id} – Delete record

6. Prescriptions
    GET /prescriptions/ – All prescriptions

    POST /prescriptions/ – Issue prescription

    GET /prescriptions/{id} – View prescription

7. Billing
    GET /billing/ – List bills

    POST /billing/ – Generate new bill

    GET /billing/{id} – View bill

    PUT /billing/{id} – Update bill

    DELETE /billing/{id} – Cancel bill

8. Inventory (Medicines, Equipment)
    GET /inventory/ – List all items

    POST /inventory/ – Add inventory item

    PUT /inventory/{id} – Update item

    DELETE /inventory/{id} – Remove item

9. Rooms & Beds
    GET /rooms/ – View rooms and bed availability

    POST /rooms/ – Add new room

    PUT /rooms/{id} – Update room status (available/occupied)

10. Staff Management
    GET /staff/ – List all hospital staff

    POST /staff/ – Add staff (nurse, receptionist)

    PUT /staff/{id} – Update staff

    DELETE /staff/{id} – Remove staff

11. Reports & Analytics (Optional)
    GET /reports/summary – Get overall stats (admissions, discharges)

    GET /reports/revenue – Billing revenue report

    GET /reports/appointments – Appointment trends


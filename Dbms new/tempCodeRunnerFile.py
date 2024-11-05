ef add_doctor_view(parent):
    ctk.CTkLabel(parent, text="Add Doctor", font=("Arial", 18)).pack(pady=10)

    # Input fields for doctor name and specialization
    labels = ["Doctor Name:", "specialization:"]
    entries = []
    for label_text in labels:
        ctk.CTkLabel(parent, text=label_text).pack()
        entry = ctk.CTkEntry(parent)
        entry.pack(pady=5)
        entries.append(entry)

    # Button to add the doctor to the database
    def add_doctor():
        doctor_name, specialization = [e.get() for e in entries]

        # Insert the doctor into the database
        execute_query(
            "INSERT INTO doctors (name, specialization) VALUES (%s, %s)",
            (doctor_name, specialization)
        )
        ctk.CTkLabel(parent, text="Doctor added successfully!", text_color="green").pack()

    ctk.CTkButton(parent, text="Add Doctor", command=add_doctor).pack(pady=10)

def update_doctor_view(parent):
    ctk.CTkLabel(parent, text="Update Doctor", font=("Arial", 18)).pack(pady=10)

    # Search bar to find a doctor
    search_entry = ctk.CTkEntry(parent, placeholder_text="Search Doctor Name")
    search_entry.pack(pady=5)

    # Frame for search results
    search_results_frame = ctk.CTkFrame(parent)
    search_results_frame.pack(fill="x", padx=10, pady=5)

    # Fields to update doctor name and specialization
    update_labels = ["Doctor ID:", "Doctor Name:", "specialization:"]
    update_entries = []
    for label_text in update_labels:
        ctk.CTkLabel(parent, text=label_text).pack()
        entry = ctk.CTkEntry(parent)
        entry.pack(pady=5)
        update_entries.append(entry)

    # Function to search for a doctor and display results
    def search_doctor():
        doctor_name = search_entry.get().strip()
        results = execute_query("SELECT * FROM doctors WHERE name = %s", (doctor_name,))

        # Clear previous results
        for widget in search_results_frame.winfo_children():
            widget.destroy()

        if results:
            for row in results:
                result_label = ctk.CTkLabel(search_results_frame, text=f"Doctor ID: {row[0]}, Name: {row[1]}, specialization: {row[2]}")
                result_label.pack()

                # Adding button to fill fields with selected result
                update_button = ctk.CTkButton(search_results_frame, text="Select", command=lambda doctor=row: fill_update_fields(doctor))
                update_button.pack(pady=5)

        else:
            ctk.CTkLabel(search_results_frame, text="No results found").pack()

    # Function to fill the update fields with selected doctor details
    def fill_update_fields(doctor):
        # Populate fields with current doctor details
        for entry, value in zip(update_entries[1:], doctor[1:]):  # Skip doctor ID
            entry.delete(0, ctk.END)
            entry.insert(0, value)

        # Set the doctor ID in the first entry
        update_entries[0].delete(0, ctk.END)
        update_entries[0].insert(0, doctor[0])  # Doctor ID

    ctk.CTkButton(parent, text="Search Doctor", command=search_doctor).pack(pady=5)

    # Button to update the doctor in the database
    def update_doctor():
        doctor_id = update_entries[0].get().strip()  # Get the doctor ID

        # Get new values from the entry fields
        new_doctor_name = update_entries[1].get().strip()
        new_specialization = update_entries[2].get().strip()

        # Perform the update
        execute_query(
            "UPDATE doctors SET name=%s, specialization=%s WHERE id=%s",
            (new_doctor_name, new_specialization, doctor_id)
        )

        ctk.CTkLabel(parent, text="Doctor updated successfully!", text_color="green").pack()

    ctk.CTkButton(parent, text="Update Doctor", command=update_doctor).pack(pady=10)

def doctor_detail_view(parent):
    ctk.CTkLabel(parent, text="Doctor Detail", font=("Arial", 18)).pack(pady=10)

    # Search bar to find a doctor
    search_entry = ctk.CTkEntry(parent, placeholder_text="Search Doctor Name")
    search_entry.pack(pady=5)

    # Frame for displaying doctor details
    detail_frame = ctk.CTkFrame(parent)
    detail_frame.pack(fill="x", padx=10, pady=5)

    # Function to display all doctors
    def display_all_doctors():
        all_doctors = execute_query("SELECT * FROM doctors",)

        # Clear previous details
        for widget in detail_frame.winfo_children():
            widget.destroy()

        if all_doctors:
            for row in all_doctors:
                detail_label = ctk.CTkLabel(detail_frame, text=f"ID: {row[0]}, Name: {row[1]}, specialization: {row[2]}")
                detail_label.pack()
        else:
            ctk.CTkLabel(detail_frame, text="No doctors found").pack()

    # Function to search for a doctor and display its details
    def search_doctor_detail():
        doctor_name = search_entry.get().strip()
        results = execute_query("SELECT * FROM doctors WHERE name = %s", (doctor_name,))

        # Clear previous details
        for widget in detail_frame.winfo_children():
            widget.destroy()

        if results:
            for row in results:
                detail_label = ctk.CTkLabel(detail_frame, text=f"ID: {row[0]}, Name: {row[1]}, specialization: {row[2]}")
                detail_label.pack()
        else:
            ctk.CTkLabel(detail_frame, text="No results found").pack()

    # Button to trigger the search function
    ctk.CTkButton(parent, text="Search Doctor", command=search_doctor_detail).pack(pady=5)

    # Initially display all doctors
    display_all_doctors()
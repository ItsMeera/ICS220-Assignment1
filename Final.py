import tkinter as tk
from tkinter import messagebox
import pickle

# Function to save data to file using pickle
def save_data(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

# Function to load data from file using pickle
def load_data(filename):
    try:
        with open(filename, 'rb') as file:
            data = pickle.load(file)
        return data
    except FileNotFoundError:
        return []

# Sample data
employee_file = 'employees.pkl'
venue_file = 'venues.pkl'
supplier_file = 'suppliers.pkl'

employees = load_data(employee_file)
venues = load_data(venue_file)
suppliers = load_data(supplier_file)

# GUI functions
def display_employee():
    employee_id = int(employee_id_entry.get())
    for employee in employees:
        if employee["employee_id"] == employee_id:
            manager_name = next((e["name"] for e in employees if e["employee_id"] == employee["manager_id"]), 'None')
            messagebox.showinfo("Employee Details", f"Name: {employee['name']}\nEmployee ID: {employee['employee_id']}\nDepartment: {employee['department']}\nJob Title: {employee['job_title']}\nBasic Salary: {employee['basic_salary']}\nManager ID: {employee['manager_id']}\nManager Name: {manager_name}")
            return
    messagebox.showerror("Error", "Employee not found")

def add_employee():
    name = name_entry.get()
    employee_id = int(employee_id_entry.get())
    department = department_entry.get()
    job_title = job_title_entry.get()
    basic_salary = int(basic_salary_entry.get())
    manager_id = int(manager_id_entry.get())

    employees.append({"name": name, "employee_id": employee_id, "department": department, "job_title": job_title, "basic_salary": basic_salary, "manager_id": manager_id})
    save_data(employees, employee_file)
    messagebox.showinfo("Success", "Employee added successfully")

def delete_employee():
    employee_id = int(employee_id_entry.get())
    for i, employee in enumerate(employees):
        if employee["employee_id"] == employee_id:
            del employees[i]
            save_data(employees, employee_file)
            messagebox.showinfo("Success", "Employee deleted successfully")
            return
    messagebox.showerror("Error", "Employee not found")

def modify_employee():
    employee_id = int(employee_id_entry.get())
    for employee in employees:
        if employee["employee_id"] == employee_id:
            employee["name"] = name_entry.get()
            employee["department"] = department_entry.get()
            employee["job_title"] = job_title_entry.get()
            employee["basic_salary"] = int(basic_salary_entry.get())
            employee["manager_id"] = int(manager_id_entry.get())
            save_data(employees, employee_file)
            messagebox.showinfo("Success", "Employee modified successfully")
            return
    messagebox.showerror("Error", "Employee not found")

def add_venue():
    name = venue_name_entry.get()
    location = venue_location_entry.get()

    venues.append({"name": name, "location": location})
    save_data(venues, venue_file)
    messagebox.showinfo("Success", "Venue added successfully")

def delete_venue():
    pass  # Implement deleting venue functionality

def modify_venue():
    pass  # Implement modifying venue functionality

def add_supplier():
    name = supplier_name_entry.get()
    contact = supplier_contact_entry.get()

    suppliers.append({"name": name, "contact": contact})
    save_data(suppliers, supplier_file)
    messagebox.showinfo("Success", "Supplier added successfully")

def delete_supplier():
    pass  # Implement deleting supplier functionality

def modify_supplier():
    pass  # Implement modifying supplier functionality

# GUI
root = tk.Tk()
root.title("Event Management System")

# Employee section
employee_label = tk.Label(root, text="Employee Management", font=("Helvetica", 16))
employee_label.pack()

employee_id_label = tk.Label(root, text="Employee ID")
employee_id_label.pack()
employee_id_entry = tk.Entry(root)
employee_id_entry.pack()

display_employee_button = tk.Button(root, text="Display Employee", command=display_employee, bg="lightblue")
display_employee_button.pack()

# Add employee widgets
# ...

# Venue section
venue_label = tk.Label(root, text="Venue Management", font=("Helvetica", 16))
venue_label.pack()

venue_name_label = tk.Label(root, text="Venue Name")
venue_name_label.pack()
venue_name_entry = tk.Entry(root)
venue_name_entry.pack()

venue_location_label = tk.Label(root, text="Location")
venue_location_label.pack()
venue_location_entry = tk.Entry(root)
venue_location_entry.pack()

add_venue_button = tk.Button(root, text="Add Venue", command=add_venue, bg="lightgreen")
add_venue_button.pack()

# Add venue widgets
# ...

# Supplier section
supplier_label = tk.Label(root, text="Supplier Management", font=("Helvetica", 16))
supplier_label.pack()

supplier_name_label = tk.Label(root, text="Supplier Name")
supplier_name_label.pack()
supplier_name_entry = tk.Entry(root)
supplier_name_entry.pack()

supplier_contact_label = tk.Label(root, text="Contact")
supplier_contact_label.pack()
supplier_contact_entry = tk.Entry(root)
supplier_contact_entry.pack()

add_supplier_button = tk.Button(root, text="Add Supplier", command=add_supplier, bg="lightcoral")
add_supplier_button.pack()

# Add supplier widgets
# ...

# Add delete and modify buttons for each section
delete_employee_button = tk.Button(root, text="Delete Employee", command=delete_employee, bg="salmon")
delete_employee_button.pack()

modify_employee_button = tk.Button(root, text="Modify Employee", command=modify_employee, bg="peachpuff")
modify_employee_button.pack()

delete_venue_button = tk.Button(root, text="Delete Venue", command=delete_venue, bg="salmon")
delete_venue_button.pack()

modify_venue_button = tk.Button(root, text="Modify Venue", command=modify_venue, bg="peachpuff")
modify_venue_button.pack()

delete_supplier_button = tk.Button(root, text="Delete Supplier", command=delete_supplier, bg="salmon")
delete_supplier_button.pack()

modify_supplier_button = tk.Button(root, text="Modify Supplier", command=modify_supplier, bg="peachpuff")
modify_supplier_button.pack()

root.mainloop()
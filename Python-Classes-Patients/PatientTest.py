import Patient, Procedure, InPatient

Jones = Patient.Patient("James", "Edward", "Jones", "123 Main Street", "Billings", "Montana", 59000, "406-555-1212", "Jenny Jones", "406-555-1213")
print("First Name:", Jones.getFirstName())
print("Middle Name:", Jones.getMiddleName())
print("Last Name:", Jones.getLastName())
print("Address:", Jones.getAddress())
print("City:", Jones.getCity())
print("State:", Jones.getState())
print("Zip:", Jones.getZip())
print("Phone:", Jones.getPhoneNumber())
print("Emergency Contact:", Jones.getEmergencyContactName())
print("Emergency Phone:", Jones.getEmergencyContactPhone())

print("\n")

Procedure_1 = Procedure.Procedure("Physical Exam", "8-24-2019", "Dr. Irvine", 250.00)
Procedure_2 = Procedure.Procedure("X-ray", "8-24-2019", "Dr. Jamison", 500.00)
Procedure_3 = Procedure.Procedure("Blood Test", "8-24-2019", "Dr. Smith", 200.00)


print("Procedure:", Procedure_1.getProcedureName())
print("Date", Procedure_1.getProcedureDate())
print("Practitioner:", Procedure_1.getPractitionerName())
print("Charge:", Procedure_1.getProcedureCharge())

print("\n")

print("Procedure:", Procedure_2.getProcedureName())
print("Date", Procedure_2.getProcedureDate())
print("Practitioner:", Procedure_2.getPractitionerName())
print("Charge:", Procedure_2.getProcedureCharge())

print("\n")

print("Procedure:", Procedure_3.getProcedureName())
print("Date", Procedure_3.getProcedureDate())
print("Practitioner:", Procedure_3.getPractitionerName())
print("Charge:", Procedure_3.getProcedureCharge())

print("\n")


Jones.addProcedure(Procedure_1)
Jones.addProcedure(Procedure_2)

print("Procedures performed on the patient are")

for procedure in Jones.getProcedureList():
    print("\n")
    print("Procedure:", procedure.getProcedureName())
    print("Date", procedure.getProcedureDate())
    print("Practitioner:", procedure.getPractitionerName())
    print("Charge:", procedure.getProcedureCharge())

print("\nThe total charge for Jones is ", Jones.calculateCharge())

print("\n")

Smith = InPatient.InPatient("Will", "Thomas", "Smith", "456 South Street", "Dallas", "Texas", 75050, "214-555-1234", "Carol Smith", "214-555-4567", 3)
print("First Name:", Smith.getFirstName())
print("Middle Name:", Smith.getMiddleName())
print("Last Name:", Smith.getLastName())
print("Address:", Smith.getAddress())
print("City:", Smith.getCity())
print("State:", Smith.getState())
print("Zip:", Smith.getZip())
print("Phone:", Smith.getPhoneNumber())
print("Emergency Contact:", Smith.getEmergencyContactName())
print("Emergency Phone:", Smith.getEmergencyContactPhone())
print("Days", Smith.getDays())

print("The total charge for Smith is $",Smith.getDays()*50)

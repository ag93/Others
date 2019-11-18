import Patient

class InPatient(Patient.Patient):
    def __init__(self, FName, MName, LName, Address, City, State, Zip, Ph_no, em_name, em_ph, days):
        self.__days = days
        super().__init__(FName, MName, LName, Address, City, State, Zip, Ph_no, em_name, em_ph)
        
    def setDays(self, days):
        self.__days = days
        
    def getDays(self):
        return self.__days


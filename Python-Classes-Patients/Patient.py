class Patient:
    def __init__(self, FName, MName, LName, Address, City, State, Zip, Ph_no, em_name, em_ph):
        self.__first_name = FName
        self.__middle_name = MName
        self.__last_name = LName
        self.__address = Address
        self.__city = City
        self.__state = State
        self.__zip = Zip
        self.__phone_number = Ph_no
        self.__emergency_contact_name = em_name
        self.__emergency_contact_phone = em_ph
        self.__procedure_list = []
        
    def getFirstName(self):
        return self.__first_name
    
    def getMiddleName(self):
        return self.__middle_name
    
    def getLastName(self):
        return self.__last_name
    
    def getAddress(self):
        return self.__address
    
    def getCity(self):
        return self.__city
    
    def getState(self):
        return self.__state
    
    def getZip(self):
        return self.__zip
    
    def getPhoneNumber(self):
        return self.__phone_number
    
    def getEmergencyContactName(self):
        return self.__emergency_contact_name
    
    def getEmergencyContactPhone(self):
        return self.__emergency_contact_phone
    
    def getProcedureList(self):
        return self.__procedure_list
    
#------------------------------------------------------------------------------
    
    def setFirstName(self, f_name):
        self.__first_name = f_name
    
    def setMiddleName(self, m_name):
        self.__middle_name = m_name
    
    def setLastName(self, l_name):
        self.__last_name = l_name
    
    def setAddress(self, address):
        self.__address = address
    
    def setCity(self, city):
        self.__city = city
    
    def setState(self, state):
        self.__state = state
    
    def setZip(self, zip_code):
        self.__zip = zip_code
    
    def setPhoneNumber(self, ph):
        self.__phone_number = ph
    
    def setEmergencyContactName(self, em_c_name):
        self.__emergency_contact_name = em_c_name
    
    def setEmergencyContactPhone(self, em_c_ph):
        self.__emergency_contact_phone = em_c_ph
        
    def addProcedure(self, procedure):
        self.__procedure_list.append(procedure)
        
    def calculateCharge(self):
        procedures = self.getProcedureList()
        total_charge = 0
        for procedure in procedures:
            total_charge += procedure.getProcedureCharge()
            
        return total_charge
        
#------------------------------------------------------------------------------        
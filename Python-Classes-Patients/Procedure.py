class Procedure:
    def __init__(self, p_name, p_date, p_prac_name, p_charge):
        self.__procedure_name = p_name
        self.__procedure_date = p_date
        self.__procedure_practitioner_name = p_prac_name
        self.__procedure_charge = p_charge
        
    def getProcedureName(self):
        return self.__procedure_name
    
    def getProcedureDate(self):
        return self.__procedure_date
    
    def getPractitionerName(self):
        return self.__procedure_practitioner_name
    
    def getProcedureCharge(self):
        return self.__procedure_charge
    
#------------------------------------------------------------------------------
        
    def setProcedureName(self, p_name):
        self.__procedure_name = p_name
    
    def setProcedureDate(self, p_date):
        self.__procedure_date = p_date
    
    def setPractitionerName(self, prac_name):
        self.__procedure_practitioner_name = prac_name
    
    def setProcedureCharge(self, p_charge):
        self.__procedure_charge = p_charge
#------------------------------------------------------------------------------






        

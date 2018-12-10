package zarzadzanie_personelem.Entity;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class EmployeeOfferForm {
    
    private static final Logger log = LoggerFactory.getLogger(EmployeeOfferForm.class);
        
    private boolean valid;

    public boolean isValid() {
        return valid;
    }

    private String id_restauracji;
    private String stanowisko;
    private String etat;
    private String telefon;

    public String getId_restauracji() {
        return id_restauracji;
    }

    public String getStanowisko() {
        return stanowisko;
    }

    public String getEtat() {
        return etat;
    }

    public String getTelefon() {
        return telefon;
    }

    public void validate(){
        if(!validateTelephone()){
            valid = false;
            return;
        }
        valid = true;
    }
    
    private boolean validateTelephone(){
        if(!telefon.matches("[\\d+ ]+")){
            log.info("Telephone number {} has illegal signs", telefon);
            return false;            
        }
        String tmpPhone = telefon;
        tmpPhone = tmpPhone.replaceAll(" ", "");
        if(tmpPhone.codePointAt(0) == '+' && tmpPhone.length() != 12){
            log.info("Telephone number with plus sign, {}, does not have 9 signs", telefon);
            return false;            
        }
        Integer amountOfNumbers = tmpPhone.replaceAll("\\D", "").length();
        if(amountOfNumbers != 9 && amountOfNumbers != 11 && amountOfNumbers != 13){
            log.info("Telephone number , {}, has a different size than 9, 11 or 13", telefon);
            return false;            
        }
        return true;
    }
}

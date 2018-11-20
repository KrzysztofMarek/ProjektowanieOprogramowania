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
        valid = true;
    }
}

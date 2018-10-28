package zarzadzanie_personelem.Entity;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class EmployeeForm {
    
    private static final Logger log = LoggerFactory.getLogger(EmployeeForm.class);
        
    private boolean valid;

    public boolean isValid() {
        return valid;
    }

    private String id_restauracji;
    private String imie;
    private String nazwisko;
    private String telefon;
    private String stanowisko;
    private String login;
    private String haslo;


    public String getId_restauracji() {
        return id_restauracji;
    }

    public String getImie() {
        return imie;
    }

    public String getNazwisko() {
        return nazwisko;
    }

    public String getTelefon() {
        return telefon;
    }

    public String getStanowisko() {
        return stanowisko;
    }

    public String getLogin() {
        return login;
    }

    public String getHaslo() {
        return haslo;
    }

    public void validate(){
        if(telefon.length() != 9){
            log.info("Telefon length is {} instead o 9", telefon.length());
            valid = false;
            return;
        }

        valid = true;
    }
}

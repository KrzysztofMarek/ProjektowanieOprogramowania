package zarzadzanie_siecia.Entity;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class RestaurantForm {
    
    private static final Logger log = LoggerFactory.getLogger(RestaurantForm.class);
        
    private boolean valid;

    public boolean isValid() {
        return valid;
    }

    private String nazwa;
    private String adres;

    public static Logger getLog() {
        return log;
    }

    public String getNazwa() {
        return nazwa;
    }

    public String getAdres() {
        return adres;
    }

    public void validate(){
        
        if(!validateName()){
            valid = false;
            return;
        }
        valid = true;
    }
    
    private boolean validateName(){
        if(nazwa.length() > 30){
            log.info("String {} has more than 30 signs", nazwa);
            return false;            
        }
        if(!nazwa.matches("[\\w- ]+")){
            log.info("Some signs of {} are illegal", nazwa);
            return false;            
        }
        if(!Character.isUpperCase(nazwa.codePointAt(0))){
            log.info("First letter of {} is not capitalized", nazwa);
            return false;            
        }        
        return true;
    }
}

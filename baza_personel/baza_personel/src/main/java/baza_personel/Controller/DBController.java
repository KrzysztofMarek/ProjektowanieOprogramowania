package baza_personel.Controller;

import baza_personel.Entity.Connector;
import baza_personel.Entity.MockConnector;
import baza_personel.Entity.SQLConnector;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.env.Environment;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

@RestController
public class DBController {
 
    @Autowired
    private Environment env;
    
    Connector connector = new MockConnector();
    
    private static final Logger log = LoggerFactory.getLogger(DBController.class);
        
    @PostMapping("/dodajPracownika")
    public String addEmployee(
            @RequestBody String employeeForm) 
    {
        try{
            log.info("Adding employee {}", employeeForm);
            return connector.createEmployee(
                    employeeForm, 
                    env.getProperty("createEmployeeAddress")
            );
        }catch(Exception e){
            return e.toString();
        }
    }
        
    @PostMapping("/dodajOgloszenie")
    public String addEmployeeOffer(
            @RequestBody String employeeOfferForm) 
    {
        try{
            log.info("Adding employee offer {}", employeeOfferForm);
            return connector.createEmployeeOffer(
                    employeeOfferForm, 
                    env.getProperty("createEmployeeOfferAddress")
            );
        }catch(Exception e){
            return e.toString();
        }
    }
        
    @GetMapping("/pobierzOgloszenie")
    public String getEmployeeOffers() 
    {
        try{
            log.info("Getting employee offers");
            return connector.getEmployeeOffers( 
                    env.getProperty("getEmployeeOffers")
            );
        }catch(Exception e){
            return e.toString();
        }
    }
}

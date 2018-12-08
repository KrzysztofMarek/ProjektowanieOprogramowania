package zarzadzanie_personelem.Controller;

import zarzadzanie_personelem.Entity.EmployeeCreator;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.env.Environment;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import zarzadzanie_personelem.Entity.EmployeeOfferCreator;

@RestController
public class EmployeeController {
 
    @Autowired
    private Environment env;
    
    private static final Logger log = LoggerFactory.getLogger(EmployeeController.class);
        
    @CrossOrigin
    @PostMapping("/dodaj_pracownika")
    public String addEmployee(
            @RequestBody String employeeForm) 
    {
        try{
            log.info("Adding employee {}", employeeForm);
            return (new EmployeeCreator()).createEmployee(
                    employeeForm, 
                    env.getProperty("createEmployeeAddress")
            );
        }catch(Exception e){
            return e.toString();
        }
    }
    
    @CrossOrigin
    @PostMapping("/dodaj_ogloszenie")
    public String addOffer(
            @RequestBody String employeeOfferForm) 
    {
        try{
            log.info("Adding employee offer {}", employeeOfferForm);
            return (new EmployeeOfferCreator()).createEmployeeOffer(
                    employeeOfferForm, 
                    env.getProperty("createEmployeeOfferAddress")
            );
        }catch(Exception e){
            return e.toString();
        }
    }
    
    @CrossOrigin
    @GetMapping("/pobierz_ogloszenia")
    public String getOffers() 
    {
        try{
            log.info("Fetching employee offers");
            return (new EmployeeOfferCreator()).getEmployeeOffers(
                    env.getProperty("getEmployeeOffersAddress")
            );
        }catch(Exception e){
            return e.toString();
        }
    }
}

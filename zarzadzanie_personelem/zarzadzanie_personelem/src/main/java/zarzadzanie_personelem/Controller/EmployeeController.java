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
import org.springframework.web.bind.annotation.RequestParam;
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
    @GetMapping("/pobierz_pracownikow")
    public String getEmployees() 
    {
        try{
            log.info("Fetching employees");
            return (new EmployeeCreator()).getEmployees(
                    env.getProperty("getEmployeesAddress")
            );
        }catch(Exception e){
            return e.toString();
        }
    }
    
    @CrossOrigin
    @GetMapping("/pobierz_pracownikow")
    public String getEmployeesOfRestaurant(
            @RequestParam("id_restauracji") String id_restauracji) 
    {
        try{
            log.info("Fetching employees");
            return (new EmployeeCreator()).getEmployees(
                    id_restauracji,
                    env.getProperty("getEmployeesAddress")
            );
        }catch(Exception e){
            return e.toString();
        }
    }
    
    @CrossOrigin
    @GetMapping("/usun_pracownika")
    public String removeEmployee(
            @RequestParam("id_pracownika") String id_pracownika) 
    {
        try{
            log.info("Removing employee {}", id_pracownika);
            return (new EmployeeCreator()).removeEmployee(
                    id_pracownika,
                    env.getProperty("removeEmployeeAddress")
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

package baza_personel.Controller;

import baza_personel.Entity.SQLConnector;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.env.Environment;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;

@RestController
public class DBController {
 
    @Autowired
    private Environment env;
    
    SQLConnector connector = new SQLConnector();
    
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
    
    @GetMapping("/pobierzPracownikow")
    public String getEmployees() 
    {
        try{
            log.info("Fetching employees");
            return connector.getEmployees( 
                    env.getProperty("getEmployeesAddress")
            );
        }catch(Exception e){
            return e.toString();
        }
    }
    
    @GetMapping("/usunPracownika")
    public String removeEmployee(
            @RequestParam("id_pracownika") String id_pracownika) 
    {
        try{
            log.info("Removing employee {}", id_pracownika);
            return connector.removeEmployee(
                    id_pracownika, 
                    env.getProperty("removeEmployeeAddress")
            );
        }catch(Exception e){
            return e.toString();
        }
    }
    
    @GetMapping("/restauracjaIstnieje")
    public String restaurantExists(
            @RequestParam("id_restauracji") String id_restauracji) 
    {
        try{
            log.info("Checking if restaurant {} exists", id_restauracji);
            return connector.restaurantExists(
                    id_restauracji, 
                    env.getProperty("restaurantExistsAddress")
            );
        }catch(Exception e){
            return e.toString();
        }
    }
}

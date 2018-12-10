package baza_zarzadzanie_siecia.Controller;

import baza_zarzadzanie_siecia.Entity.Connector;
import baza_zarzadzanie_siecia.Entity.SQLConnector;
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

@RestController
public class DBController {
 
    @Autowired
    private Environment env;
    
    Connector connector = new SQLConnector();
    
    private static final Logger log = LoggerFactory.getLogger(DBController.class);
        
    @PostMapping("/dodaj_restauracje")
    public String addRestaurant(
            @RequestBody String restaurantForm) 
    {
        try{
            log.info("Adding restaurant {}", restaurantForm);
            return connector.createRestaurant(
                    restaurantForm, 
                    env.getProperty("createRestaurantAddress")
            );
        }catch(Exception e){
            return e.toString();
        }
    }
    
    @CrossOrigin
    @GetMapping("/pobierz_restauracje")
    public String getRestaurant() 
    {
        try{
            log.info("Fetching restaurant");
            return connector.getRestaurant(
                    env.getProperty("getRestaurantAddress")
            );
        }catch(Exception e){
            return e.toString();
        }
    }   
    
    @CrossOrigin
    @PostMapping("/przydziel_menadzera")
    public String assignManager(
            @RequestBody String assignManagerForm) 
    {
        try{
            log.info("Assign manager {}", assignManagerForm);
            return connector.assignManager(
                    assignManagerForm, 
                    env.getProperty("assignManagerAddress")
            );
        }catch(Exception e){
            return e.toString();
        }
    }
    
    @CrossOrigin
    @GetMapping("/usun_restauracje")
    public String removeRestaurant(
            @RequestParam("id_restauracji") String restaurantIdForm) 
    {
        try{
            log.info("Remove restaurant {}", restaurantIdForm);
            return connector.removeRestaurant(
                    restaurantIdForm, 
                    env.getProperty("removeRestaurantAddress")
            );
        }catch(Exception e){
            return e.toString();
        }
    }
}

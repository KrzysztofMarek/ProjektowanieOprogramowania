package zarzadzanie_siecia.Controller;

import zarzadzanie_siecia.Entity.RestaurantCreator;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.env.Environment;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

@RestController
public class NetworkController {
 
    @Autowired
    private Environment env;
    
    private static final Logger log = LoggerFactory.getLogger(NetworkController.class);
        
    @CrossOrigin
    @PostMapping("/dodaj_restauracje")
    public String addRestaurant(
            @RequestBody String restaurantForm) 
    {
        try{
            log.info("Adding restaurant {}", restaurantForm);
            return (new RestaurantCreator()).createRestaurant(
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
            log.info("Fetching restaurants");
            return (new RestaurantCreator()).getRestaurant( 
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
            log.info("Assigning manager {}", assignManagerForm);
            return (new RestaurantCreator()).assignManager(
                    assignManagerForm,
                    env.getProperty("assignManagerAddress")
            );
        }catch(Exception e){
            return e.toString();
        }
    }
    
    @CrossOrigin
    @PostMapping("/usun_restauracje")
    public String removeRestaurant(
            @RequestBody String restaurantIdForm) 
    {
        try{
            log.info("Removing restaurant {}", restaurantIdForm);
            return (new RestaurantCreator()).removeRestaurant(
                    restaurantIdForm,
                    env.getProperty("removeRestaurantAddress")
            );
        }catch(Exception e){
            return e.toString();
        }
    }
}

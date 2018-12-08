package zarzadzanie_siecia.Controller;

import zarzadzanie_siecia.Entity.RestaurantCreator;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.env.Environment;
import org.springframework.web.bind.annotation.CrossOrigin;
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
}

package baza_zarzadzanie_siecia.Controller;

import baza_zarzadzanie_siecia.Entity.Connector;
import baza_zarzadzanie_siecia.Entity.MockConnector;
import baza_zarzadzanie_siecia.Entity.SQLConnector;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.env.Environment;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

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
}

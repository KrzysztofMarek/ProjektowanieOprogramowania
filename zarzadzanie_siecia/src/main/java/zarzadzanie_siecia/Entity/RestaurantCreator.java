/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package zarzadzanie_siecia.Entity;

import com.google.gson.Gson;
import java.util.HashMap;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.client.RestTemplate;

/**
 *
 * @author adas
 */
public class RestaurantCreator {
    
    private static final Logger log = LoggerFactory.getLogger(RestaurantCreator.class);

    public String createRestaurant(final String restaurantFormJson, final String url) {
        RestaurantForm restaurantForm = (new Gson()).fromJson(restaurantFormJson, RestaurantForm.class);
        restaurantForm.validate();
        if(restaurantForm.isValid()){
            return saveRestaurantToDB(restaurantForm, url);
        }else{
            return (new Gson()).toJson("Invalid input");
        }
    }
    
    private String saveRestaurantToDB(final RestaurantForm restaurantForm, final String url){
        RestTemplate restTemplate = new RestTemplate();
        String responseDB = restTemplate.postForObject(url, restaurantForm, String.class);
        
        HashMap<String, String> responseUser = new HashMap();
        responseUser.put("message", responseDB);
        return (new Gson()).toJson(responseUser);
    }   
    
}

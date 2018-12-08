/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package baza_zarzadzanie_siecia.Entity;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.client.RestTemplate;

/**
 *
 * @author adas
 */
public class SQLConnector implements Connector {
    
    private static final Logger log = LoggerFactory.getLogger(SQLConnector.class);

    @Override
    public String createRestaurant(final String restaurantFormJson, final String url){   
        
        log.info("Sending {} to {}", restaurantFormJson, url);
        RestTemplate restTemplate = new RestTemplate();
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        HttpEntity<String> entity = new HttpEntity<String>(restaurantFormJson, headers);
        ResponseEntity<String> response = restTemplate.exchange(url, HttpMethod.POST, entity, String.class);
        if(response.getStatusCode() == HttpStatus.OK){
            return "Udało się!";
        }else{
            return "Nie udało się!";    
        }
    }
    
}

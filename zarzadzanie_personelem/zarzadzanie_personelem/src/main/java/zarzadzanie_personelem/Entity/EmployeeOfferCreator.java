/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package zarzadzanie_personelem.Entity;

import com.google.gson.Gson;
import java.util.HashMap;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.client.RestTemplate;
import utils.EasyCache;

/**
 *
 * @author adas
 */
public class EmployeeOfferCreator {
    
    private static final Logger log = LoggerFactory.getLogger(EmployeeOfferCreator.class);

    public String createEmployeeOffer(final String employeeOfferFormJson, final String url) {
        log.info("Transforming json to object");
        EmployeeOfferForm employeeOfferForm = (new Gson()).fromJson(employeeOfferFormJson, EmployeeOfferForm.class);
        log.info("Validating received form");
        employeeOfferForm.validate();
        if(employeeOfferForm.isValid()){
            log.info("Saving to cache");
            saveEmployeeOfferToCache(employeeOfferForm);
            log.info("Saved to cache");
            return saveEmployeeOfferToDB(employeeOfferForm, url);
        }else{
            return (new Gson()).toJson("Invalid input");
        }
    }
    
    private String saveEmployeeOfferToDB(final EmployeeOfferForm employeeOfferForm, final String url){
        RestTemplate restTemplate = new RestTemplate();
        String responseDB = restTemplate.postForObject(url, employeeOfferForm, String.class);
        
        HashMap<String, String> responseUser = new HashMap();
        responseUser.put("message", responseDB);
        return (new Gson()).toJson(responseUser);
    }   
    
    private void saveEmployeeOfferToCache(final EmployeeOfferForm employeeOfferForm) {
        log.info((new Gson()).toJson(EasyCache.getAllElements()));
        EasyCache.addElement(employeeOfferForm);
        log.info((new Gson()).toJson(EasyCache.getAllElements()));
    }
    
    public String getEmployeeOffers(final String url) {
        if(EasyCache.getSize() != 0){
            return (new Gson()).toJson(EasyCache.getAllElements());
        }else{
            return (new Gson()).toJson(getEmployeeOffersFromDB(url));
        }
    }
    private String getEmployeeOffersFromDB(final String url){
        RestTemplate restTemplate = new RestTemplate();
        String responseDB = restTemplate.getForObject(url, String.class);
        
        EasyCache.addJsonArray(responseDB, EmployeeOfferForm.class);
        
        return responseDB;
    }   
    
}

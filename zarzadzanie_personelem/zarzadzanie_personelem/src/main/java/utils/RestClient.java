/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package utils;

import com.google.gson.Gson;
import java.util.HashMap;
import org.springframework.web.client.RestTemplate;

/**
 *
 * @author adas
 */
public class RestClient {
    
    public static HashMap<String,String> sendGETRaw(final String url){
        
        RestTemplate restTemplate = new RestTemplate();
        String responseDB = restTemplate.getForObject(url, String.class);
        HashMap<String, String> responseUser = new HashMap();
        responseUser.put("message", responseDB);
        return responseUser;
    }
    
    public static String sendGET(final String url){
        
        RestTemplate restTemplate = new RestTemplate();
        String responseDB = restTemplate.getForObject(url, String.class);
        HashMap<String, String> responseUser = new HashMap();
        responseUser.put("message", responseDB);
        return (new Gson()).toJson(responseUser);
    }
    
    public static <T> String sendPOST(final String url, final T form){
        
        RestTemplate restTemplate = new RestTemplate();
        String responseDB = restTemplate.postForObject(url, form, String.class);
        HashMap<String, String> responseUser = new HashMap();
        responseUser.put("message", responseDB);
        return (new Gson()).toJson(responseUser);
        
    }
    
}

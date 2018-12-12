/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package baza_personel.Entity;

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
public class SQLConnector{
    
    private static final Logger log = LoggerFactory.getLogger(SQLConnector.class);

    public String createEmployee(final String employeeFormJson, final String url) {        
        
        log.info("Sending {} to {}", employeeFormJson, url);
        RestTemplate restTemplate = new RestTemplate();
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        HttpEntity<String> entity = new HttpEntity<>(employeeFormJson, headers);
        ResponseEntity<String> response = restTemplate.exchange(url, HttpMethod.POST, entity, String.class);
        if(response.getStatusCode() == HttpStatus.OK){
            return "Udało się!";
        }else{
            return "Nie udało się!";    
        }
    }

    public String getEmployees(final String url) {
        RestTemplate restTemplate = new RestTemplate();
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        HttpEntity<String> entity = new HttpEntity<>(headers);
        log.info("Sending GET to {}", url);
        ResponseEntity<String> response = restTemplate.exchange(url, HttpMethod.GET, entity, String.class);
        if(response.getStatusCode() == HttpStatus.OK){
            return response.getBody();
        }else{
            return "Nie udało się!";    
        }
    }

    public String getEmployees(String id_restauracji, String url) {   
        String urlWithId = url + "?id_resturacji=" + id_restauracji;
        
        RestTemplate restTemplate = new RestTemplate();
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        HttpEntity<String> entity = new HttpEntity<>(headers);
        log.info("Sending GET to {}", url);
        ResponseEntity<String> response = restTemplate.exchange(url, HttpMethod.GET, entity, String.class);
        if(response.getStatusCode() == HttpStatus.OK){
            return response.getBody();
        }else{
            return "Nie udało się!";    
        }
    }

    public String removeEmployee(final String id_pracownika, final String url) {
        String urlWithId = url + "?id_pracownika=" + id_pracownika;        
        
        RestTemplate restTemplate = new RestTemplate();
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        HttpEntity<String> entity = new HttpEntity<>(headers);
        ResponseEntity<String> response = restTemplate.exchange(urlWithId, HttpMethod.GET, entity, String.class);
        if(response.getStatusCode() == HttpStatus.OK){
            return response.getBody();
        }else{
            return "Nie udało się!";    
        }
    }

    public String restaurantExists(final String id_restauracji, final String url) {
        String urlWithId = url + "?id_restauracji=" + id_restauracji;        
        
        RestTemplate restTemplate = new RestTemplate();
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        HttpEntity<String> entity = new HttpEntity<>(headers);
        ResponseEntity<String> response = restTemplate.exchange(urlWithId, HttpMethod.GET, entity, String.class);
        if(response.getStatusCode() == HttpStatus.OK){
            return "Yes";
        }else{
            return "Nie udało się!";    
        }
    }

    public String getManagers(final String url) {     
        
        RestTemplate restTemplate = new RestTemplate();
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        HttpEntity<String> entity = new HttpEntity<>(headers);
        ResponseEntity<String> response = restTemplate.exchange(url, HttpMethod.GET, entity, String.class);
        if(response.getStatusCode() == HttpStatus.OK){
            return response.getBody();
        }else{
            return "Nie udało się!";    
        }
    }
    
}

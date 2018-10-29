/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package zarzadzanie_personelem.Entity;

import com.google.gson.Gson;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.client.RestTemplate;

/**
 *
 * @author adas
 */
public class EmployeeCreator {
    
    private static final Logger log = LoggerFactory.getLogger(EmployeeCreator.class);

    public String createEmployee(final String employeeFormJson, final String url) {
        EmployeeForm employeeForm = (new Gson()).fromJson(employeeFormJson, EmployeeForm.class);
        employeeForm.validate();
        if(employeeForm.isValid()){
            return saveEmployeeToDB(employeeForm, url);
        }else{
            return "Invalid input";
        }
    }
    
    private String saveEmployeeToDB(final EmployeeForm employeeForm, final String url){
        RestTemplate restTemplate = new RestTemplate();
        return restTemplate.postForObject(url, employeeForm, String.class);      
    }   
    
}

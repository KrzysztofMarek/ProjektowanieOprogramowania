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

    public String createEmployee(String employeeFormJson) {
        EmployeeForm employeeForm = (new Gson()).fromJson(employeeFormJson, EmployeeForm.class);
        employeeForm.validate();
        if(employeeForm.isValid()){
            return saveEmployeeToDB(employeeForm);
        }else{
            return "Invalid input";
        }
    }
    
    private String saveEmployeeToDB(EmployeeForm employeeForm){
        final String uri = "http://localhost:9091/dodajPracownika";

        RestTemplate restTemplate = new RestTemplate();
        return restTemplate.postForObject(uri, employeeForm, String.class);      
    }   
    
}

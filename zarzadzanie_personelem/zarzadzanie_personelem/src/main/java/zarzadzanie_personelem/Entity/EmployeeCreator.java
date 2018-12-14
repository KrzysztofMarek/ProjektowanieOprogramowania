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
import utils.RestClient;

/**
 *
 * @author adas
 */
public class EmployeeCreator {
    
    private static final Logger log = LoggerFactory.getLogger(EmployeeCreator.class);

    public String createEmployee(
            final String employeeFormJson, 
            final String urlAddEmployee,
            final String urlCheckRestaurant
    ) {
        EmployeeForm employeeForm = (new Gson()).fromJson(employeeFormJson, EmployeeForm.class);
        log.info("Validating employee data");
        employeeForm.validate();
        if(validateEmployee(employeeForm, urlCheckRestaurant)){
            log.info("Adding employee to DB");
            return saveEmployeeToDB(employeeForm, urlAddEmployee);
        }else{
            return (new Gson()).toJson("Invalid input");
        }
    }
    
    private boolean validateEmployee(final EmployeeForm employeeForm, final String url){
        if(!employeeForm.isValid()){
            log.info("Data is incorrect");
            return false;
        }
        
        if(!restaurantExists(employeeForm.getId_restauracji(), url)){
            log.info("Restaurant does not exist.");
            return false;
        }
        
        return true;
    }
    
    private boolean restaurantExists(final String id, final String url){        
        String urlWithId = url + "?id_restauracji=" + id;

        String response = RestClient.sendGETRaw(urlWithId).get("message");
        return response.equals("Yes");        
    }
    
    private String saveEmployeeToDB(final EmployeeForm employeeForm, final String url){
        return RestClient.sendPOST(url, employeeForm);
    }   

    public String getEmployees(final String url) {        
        return RestClient.sendGET(url);        
    }
    
    public String getEmployees(final String id_restauracji, final String url) {
        String urlWithId = url + "?id_restauracji=" + id_restauracji;
        
        return RestClient.sendGET(urlWithId);
    }

    public String removeEmployee(final String id_pracownika, final String url) {
        String urlWithId = url + "?id_pracownika=" + id_pracownika;
        
        return RestClient.sendGET(urlWithId);
    }

    public String getManagers(final String url) {    
        return RestClient.sendGET(url);        
    }

    
}

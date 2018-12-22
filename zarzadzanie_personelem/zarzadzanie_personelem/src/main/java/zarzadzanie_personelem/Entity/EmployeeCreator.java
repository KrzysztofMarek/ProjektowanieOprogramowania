/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package zarzadzanie_personelem.Entity;

import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import com.google.gson.reflect.TypeToken;
import java.util.ArrayList;
import java.util.HashMap;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;
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
        log.info("Data is correct");
        
        if(!restaurantExists(employeeForm.getId_restauracji(), url)){
            log.info("Restaurant does not exist.");
            return false;
        }
        log.info("Restaurant is correct");
        
        return true;
    }
    
    private boolean restaurantExists(final String id, final String url){        
        String urlWithId = url + "?id_restauracji=" + id;
        log.info("Sending GET to {}", urlWithId);                

        String response = RestClient.sendGETRaw(urlWithId).get("message");
        return response.equals("Yes");        
    }
    
    private String saveEmployeeToDB(final EmployeeForm employeeForm, final String url){
        return RestClient.sendPOST(url, employeeForm);
    }   

    public String getEmployees(
            final String session, 
            final String getUrl,
            final String authUrl
    ) {
        ResponseEntity<String> response = getManagerId(session, authUrl);
        String managerType = getManagerType(response);
        
        if(managerType.equals("Network")){
            return RestClient.sendGET(getUrl);            
        }else if(managerType.equals("Restaurant")){
            String Id = getManagerId(response);
            return getEmployeesOfRestaurant(Id, getUrl);
        }else{
            return getInvalidTypeMessage();
        }        
    }
    
    private ResponseEntity<String> getManagerId(final String session, final String authUrl){
        HttpHeaders headers = new HttpHeaders();
        headers.add("Cookie", "session="+session);

        RestTemplate restTemplate = new RestTemplate();
        return restTemplate.exchange(
            authUrl,
            HttpMethod.GET,
            new HttpEntity<>(headers),
            String.class
        );
    }
    
    private String getManagerType(ResponseEntity<String> response){
        // TO BE IMPLEMENTED WHEN LOGIN RETURNS PROPER INFO
        if(response.getStatusCodeValue() == 200){
            return "Network";            
        }else{
            log.info("Bad response code");
            return "Error";
        }
    }
    
    private String getManagerId(ResponseEntity<String> response){
        // TO BE IMPLEMENTED WHEN LOGIN RETURNS PROPER INFO
        return "1";
    }
    
    private String getInvalidTypeMessage(){
        String message = "Unable to authenticate";
        HashMap<String, String> map = new HashMap<>();
        map.put("message", message);
        return new Gson().toJson(map);
    }
    
    public String getEmployeesOfRestaurant(final String id_restauracji, final String url) {        
        HashMap<String,String> response = RestClient.sendGETRaw(url);
        ArrayList<EmployeeForm> employees = castToEmployees(response.get("message"));
        ArrayList<EmployeeForm> employeesOfRestaurant = filterEmployeesOfRestaurant(employees, id_restauracji);
        return new Gson().toJson(employeesOfRestaurant);        
    }

    public String removeEmployee(final String id_pracownika, final String url) {
        String urlWithId = url + "?id_pracownika=" + id_pracownika;
        
        return RestClient.sendGET(urlWithId);
    }

    public String getManagers(final String url) {    
        HashMap<String,String> response = RestClient.sendGETRaw(url);        
        log.info("Processing response {}", response);
        ArrayList<EmployeeForm> employees = castToEmployees(response.get("message"));
        ArrayList<EmployeeForm> managers = filterManagers(employees);
        return new Gson().toJson(managers);
    }

    private ArrayList<EmployeeForm> castToEmployees(String response) {
        Gson gson = new Gson();
        
        JsonObject responseObject = gson.fromJson(response, JsonObject.class);
        JsonArray employeeListFormObject = responseObject
                .get("lista_pracownikow").getAsJsonArray();
        
        ArrayList<EmployeeForm> employeeListForm = new Gson().fromJson(
                employeeListFormObject, 
                new TypeToken<ArrayList<EmployeeForm>>(){}.getType()
        );
        return employeeListForm;
    }

    private ArrayList<EmployeeForm> filterManagers(ArrayList<EmployeeForm> employees) {
        employees.removeIf(employee -> !employee.getStanowisko().equals("menadzer restauracji"));
        return employees;
    }

    private ArrayList<EmployeeForm> filterEmployeesOfRestaurant(ArrayList<EmployeeForm> employees, final String id) {
        employees.removeIf(employee -> !employee.getId_restauracji().equals(id));
        return employees;
    }

    
}

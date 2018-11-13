/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package baza_personel.Entity;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 *
 * @author adas
 */
public class MockConnector implements Connector{
    
    private static final Logger log = LoggerFactory.getLogger(MockConnector.class);

    @Override
    public String createEmployee(final String employeeFormJson, final String url) {
        return "Nice job!"; 
    }
    @Override
    public String createEmployeeOffer(final String employeeOfferFormJson, final String url) {
        return "You are the best!"; 
    }
    @Override
    public String getEmployeeOffers(final String url) { 
        HashMap<String, String> data = new HashMap();
        data.put("id_restauracji", "1");
        data.put("stanowisko", "test");
        
        ArrayList<Map<String, String>> dataArray = new ArrayList();
        dataArray.add(data);
        return (new Gson()).toJson(dataArray);
    }
}

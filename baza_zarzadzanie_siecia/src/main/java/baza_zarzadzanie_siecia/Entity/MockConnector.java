/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package baza_zarzadzanie_siecia.Entity;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 *
 * @author adas
 */
public class MockConnector implements Connector{
    
    private static final Logger log = LoggerFactory.getLogger(MockConnector.class);

    @Override
    public String createRestaurant(final String employeeFormJson, final String url) {
        return "You are perfect!"; 
    }

    @Override
    public String getRestaurant(String property) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public String assignManager(String assignManagerForm, String property) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public String removeRestaurant(String restaurantIdForm, String property) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
}

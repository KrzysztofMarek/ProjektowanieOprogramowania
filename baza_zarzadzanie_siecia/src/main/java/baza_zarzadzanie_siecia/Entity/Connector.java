/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package baza_zarzadzanie_siecia.Entity;


/**
 *
 * @author adas
 */
public interface Connector {
    
    public String createRestaurant(final String restaurantFormJson, final String url);

    public String getRestaurant(String property);

    public String assignManager(String assignManagerForm, String property);

    public String removeRestaurant(String restaurantIdForm, String property);
}

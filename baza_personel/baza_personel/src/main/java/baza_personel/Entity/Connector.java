/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package baza_personel.Entity;


/**
 *
 * @author adas
 */
public interface Connector {
    
    public String createEmployee(final String employeeFormJson, final String url);
    
    public String createEmployeeOffer(final String employeeOfferFormJson, final String url);
    
    public String getEmployeeOffers(final String url);
    
}

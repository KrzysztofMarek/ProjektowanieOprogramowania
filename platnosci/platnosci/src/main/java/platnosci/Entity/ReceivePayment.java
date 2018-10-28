/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package platnosci.Entity;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 *
 * @author adas
 */
public class ReceivePayment implements PaymentInterface{
    
    private static final Logger log = LoggerFactory.getLogger(ReceivePayment.class);

    public String pay(PaymentForm paymentForm) {
        paymentForm.validate();
        if(paymentForm.isValid()){
            return getPaymentRedirect(paymentForm);
        }else{
            return "Invalid input";
        }
    } 
    
    private String getPaymentRedirect(PaymentForm paymentForm){
        return "https://localhost:4202/";
    }
}

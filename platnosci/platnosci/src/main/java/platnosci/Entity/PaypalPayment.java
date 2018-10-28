package platnosci.Entity;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class PaypalPayment implements PaymentInterface{
    
    private static final Logger log = LoggerFactory.getLogger(PaypalPayment.class);

    public String pay(PaymentForm paymentForm) {
        paymentForm.validate();
        if(paymentForm.isValid()){
            return getPaymentRedirect(paymentForm);
        }else{
            return "Invalid input";
        }
    } 
    
    private String getPaymentRedirect(PaymentForm paymentForm){
        return "https://www.paypal.com/pl/home";
    }
}

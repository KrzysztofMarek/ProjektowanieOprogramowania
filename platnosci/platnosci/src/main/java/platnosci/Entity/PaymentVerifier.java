package platnosci.Entity;

import com.google.gson.Gson;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class PaymentVerifier {
    
    private static final Logger log = LoggerFactory.getLogger(PaymentVerifier.class);
    
    public String process(String paymentFormJson){
        PaymentForm paymentForm = (new Gson()).fromJson(paymentFormJson, PaymentForm.class);
        
        paymentForm.validate();
        if(!paymentForm.isValid()){
            return "Invalid input";
        }
               
        PaymentInterface paymentProcessor = getPaymentProcessor(paymentForm);
        if(paymentProcessor == null){
            return "Could not process payment";
        }
        
        return paymentProcessor.pay(paymentForm);
    }
    
    private PaymentInterface getPaymentProcessor(PaymentForm paymentForm){
        String paymentMethod = paymentForm.getSposób_zapłaty();
        switch(PaymentMethods.valueOf(paymentMethod)){
            case PAYPAL:
                return new PaypalPayment();
            case PAYU:
                return new PayuPayment();
            default:
                return null;
        }
    }
}

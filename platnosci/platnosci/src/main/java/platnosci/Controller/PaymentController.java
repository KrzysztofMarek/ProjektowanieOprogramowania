package platnosci.Controller;

import platnosci.Entity.PaymentVerifier;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

@RestController
public class PaymentController {
 
    private static final Logger log = LoggerFactory.getLogger(PaymentController.class);
        
    @PostMapping("/zaplac")
    public String addEmployee(
            @RequestBody String paymentForm) 
    {
        try{
            log.info("Received payment form {}", paymentForm);
            return (new PaymentVerifier()).process(paymentForm);
        }catch(Exception e){
            return e.toString();
        }
    }
}

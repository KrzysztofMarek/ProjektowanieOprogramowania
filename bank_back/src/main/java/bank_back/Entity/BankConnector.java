package bank_back.Entity;

import bank_back.Controller.BankController;
import com.google.gson.Gson;
import java.util.HashMap;
import java.util.Random;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.core.env.Environment;
import org.springframework.web.client.RestTemplate;
import utils.EasyCache;

public class BankConnector {
    
    private static final Logger log = LoggerFactory.getLogger(BankConnector.class);
    
    public String success(String id, Environment env){        
        String token = EasyCache.getElement(id);
        String url = env.getProperty("mockPaymentAddressSuccess");
        
        RestTemplate restTemplate = new RestTemplate();
        log.info("Sending failure response with token {}", token);
        return restTemplate.postForObject(url, token, String.class);    
    }
    
    public String failure(String id, Environment env){
        String token = EasyCache.getElement(id);
        String url = env.getProperty("mockPaymentAddressFailure");
        
        RestTemplate restTemplate = new RestTemplate();
        log.info("Sending failure response with token {}", token);
        return restTemplate.postForObject(url, token, String.class);             
    }
    
    public String startPayment(String paymentJson, Environment env){
        String url = env.getProperty("mockPaymentAddressStartPayment");
        String redirectForm = generateRedirectForm(env);
        
        return redirectForm;   
    }
    
    private String generateRedirectForm(Environment env){
        String base_url = env.getProperty("mockPaymentAddress");
        
        Random rand = new Random();
        String id = Integer.toString(rand.nextInt(100));
        String token = Integer.toString(rand.nextInt(100000));
        EasyCache.addElement(id, token);
        
        String redirectLink = base_url + "/" + id;
        
        HashMap<String, String> redirectForm = new HashMap();
        redirectForm.put("id", id);
        redirectForm.put("token", token);
        redirectForm.put("redirectLink", redirectLink);
        
        return (new Gson()).toJson(redirectForm);
    }
}

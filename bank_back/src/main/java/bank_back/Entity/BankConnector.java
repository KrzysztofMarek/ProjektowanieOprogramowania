package bank_back.Entity;

import bank_back.Controller.BankController;
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
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
        
        String body = getPostBody(token, id);
        
        String message = restTemplate.postForObject(url, body, String.class);
        HashMap<String, String> response = new HashMap();
        response.put("message", message);
        return (new Gson()).toJson(response);    
    }
    
    public String failure(String id, Environment env){
        String token = EasyCache.getElement(id);
        String url = env.getProperty("mockPaymentAddressFailure");
        
        RestTemplate restTemplate = new RestTemplate();
        log.info("Sending failure response with token {}", token);
        
        String body = getPostBody(token, id);
        
        String message = restTemplate.postForObject(url, body, String.class);
        HashMap<String, String> response = new HashMap();
        response.put("message", message);
        return (new Gson()).toJson(response);    
    }
    
    public String startPayment(String paymentJson, Environment env){
        String url = env.getProperty("mockPaymentAddressStartPayment");
        String redirectForm = generateRedirectForm(paymentJson, env);
        
        return redirectForm;   
    }
    
    private String generateRedirectForm(String paymentJson, Environment env){
        HashMap<String, String> paymentForm = new Gson().fromJson(
            paymentJson,
            new TypeToken<HashMap<String, String>>(){}.getType()
        );
        String base_url = env.getProperty("mockPaymentAddress");
        
        Random rand = new Random();
        String id = paymentForm.get("id_zamowienia");
        String token = Integer.toString(rand.nextInt(100000));
        EasyCache.addElement(id, token);
        
        String redirectLink = base_url + "/" + id;
        
        HashMap<String, String> redirectForm = new HashMap();
        redirectForm.put("id", id);
        redirectForm.put("token", token);
        redirectForm.put("redirectLink", redirectLink);
        
        return (new Gson()).toJson(redirectForm);
    }

    private String getPostBody(String token, String id) {
        HashMap<String, String> body = new HashMap<>();
        body.put("id", id);
        body.put("token", token);
        return new Gson().toJson(body);
    }
}

package platnosci.Entity;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import java.util.HashMap;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.core.env.Environment;
import org.springframework.web.client.RestTemplate;
import utils.EasyCache;

public class PaymentVerifier {
    
    private static final Logger log = LoggerFactory.getLogger(PaymentVerifier.class);
    
    public String process(String paymentFormJson, Environment env){
        PaymentForm paymentForm = (new Gson()).fromJson(paymentFormJson, PaymentForm.class);
        
        paymentForm.validate();
        if(!paymentForm.isValid()){
            return "Invalid input";
        }
             
        PaymentAbstract paymentProcessor;
        if(env.getProperty("config").equals("prod")){
            paymentProcessor = getPaymentProcessor(paymentForm, env);
            if(paymentProcessor == null){
                return "Could not process payment";
            }            
        }else{
            paymentProcessor = new MockPayment(env.getProperty("mockPaymentAddress"));
        }
        
        String redirectForm = paymentProcessor.pay(paymentForm);
        return processRedirectForm(redirectForm);
    }
    
    private String sendPOST(final String id, final String status, final String url){
        
        RestTemplate restTemplate = new RestTemplate();
        
        HashMap<String, String> responseUser = new HashMap();
        responseUser.put("id", id);
        responseUser.put("status", status);
        String form = new Gson().toJson(responseUser);
        
        return restTemplate.postForObject(url, form, String.class);
    }
    
    public String confirm(final String data, final String url){
        HashMap<String, String> unpackedData = new Gson().fromJson(
                data, 
                new TypeToken<HashMap<String, String>>(){}.getType()
        );
        
        String response = sendPOST(unpackedData.get("id"), "SUCCESS", url);
        HashMap<String, String> responseMap = new Gson().fromJson(
            response,
            new TypeToken<HashMap<String, String>>(){}.getType()
        );
        EasyCache.addElement(unpackedData.get("token"), responseMap.get("redirect"));
                
        return "Cool";
    }
    
    public String cancel(final String data, final String url){
        HashMap<String, String> unpackedData = new Gson().fromJson(
                data, 
                new TypeToken<HashMap<String, String>>(){}.getType()
        );
        
        String response = sendPOST(unpackedData.get("id"), "FAILURE", url);
        HashMap<String, String> responseMap = new Gson().fromJson(
            response,
            new TypeToken<HashMap<String, String>>(){}.getType()
        );
        EasyCache.addElement(unpackedData.get("token"), responseMap.get("redirect"));
                
        
        return "Cool";
    }
    
    public String get_status(String id){
        String token = EasyCache.getElement(id);
        if(token == null){
            return "Invalid id";
        }
        
        HashMap<String, String> response = new HashMap();
        response.put("status", EasyCache.getElement(token));
        return (new Gson()).toJson(response);
    }
    
    private PaymentAbstract getPaymentProcessor(PaymentForm paymentForm, Environment env){
        String paymentMethod = paymentForm.getSposób_zapłaty();
        switch(PaymentMethods.valueOf(paymentMethod)){
            case BLIK:
                return new BlikPayment(env.getProperty("blikPaymentAddress"));
            case CARD:
                return new CardPayment(env.getProperty("cardPaymentAddress"));
            case PRZELEW:
                return new PrzelewPayment(env.getProperty("przelewPaymentAddress"));
            default:
                return null;
        }
    }
    
    private String processRedirectForm(final String redirectForm){
        HashMap<String, String> redirectData = (new Gson()).fromJson(
                redirectForm,
                new TypeToken<HashMap<String, String>>(){}.getType()
        );
        EasyCache.addElement(redirectData.get("id"), redirectData.get("token"));
        EasyCache.addElement(redirectData.get("token"), "started");
        
        HashMap<String, String> response = new HashMap();
        response.put("redirectLink", redirectData.get("redirectLink"));
        return (new Gson()).toJson(response);
    }    

    public String payInternal(String paymentForm, String url) {
        HashMap<String, String> request = new Gson().fromJson(
                paymentForm, 
                new TypeToken<HashMap<String, String>>(){}.getType()
        );
        EasyCache.addElement(
                request.get("id"), 
                request.get("zamowienie")
        );
        String urlWithId = url+"?id_zamowienia="+request.get("id");
        HashMap<String, String> response = new HashMap<>();
        response.put("redirectLink", urlWithId);
        return new Gson().toJson(response);
    }

    public String getOrder(String orderId) {
        String order = EasyCache.getElement(orderId);
        
        return new Gson().toJson(order);
    }
}

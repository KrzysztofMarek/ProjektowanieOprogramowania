package Controllers;

import Models.*;
import lombok.extern.slf4j.Slf4j;

import java.io.IOException;
import org.json.JSONArray;
import org.json.JSONObject;
import org.springframework.http.HttpHeaders;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import ExternalServices.DbService;
import ExternalServices.PaymentService;

@Slf4j
@RestController
public class OrderController {

    private DbService dbService = new DbService();
    private PaymentService paymentService = new PaymentService();

    @CrossOrigin
    @RequestMapping(value="/dodaj_zamowienie", method=RequestMethod.POST )
    @ResponseBody
    public ResponseEntity<Object> CreateOrder(@RequestBody NewOrder newOrder) {

        Integer orderId = null;

        try {
            orderId = dbService.AddOrder(newOrder);
        } catch (Exception e) {
            return ResponseEntity.status(503).body(null);
        }

        if(orderId != null){
            String redirectUrl = null;

            /*try {
                redirectUrl = paymentService.PayForOrder(orderId, newOrder.id_klienta, newOrder.kwota, 0);
            } catch (Exception e){
                return ResponseEntity.status(503).headers(headers).body(null);
            }*/

            JSONObject json = new JSONObject();
            json.put("id_zamowienia", orderId);
            json.put("redirect", redirectUrl);

            return ResponseEntity.status(200).body(json.toString());

            
        }else{
            return ResponseEntity.status(400).body(null);
        }
		
    }

    @CrossOrigin
    @RequestMapping(value="/pobierz_liste_zamowien", method=RequestMethod.GET)
    @ResponseBody
    public ResponseEntity<Object> GetOrders(@RequestParam(value = "id_klienta", required = false, defaultValue = "0") Integer clientId){
        String json;

        try {
            json = dbService.GetOrders(clientId);
            return ResponseEntity.status(200).body(json);
        } catch (Exception e) {
            return ResponseEntity.status(404).body(null);
		}
    }

    @CrossOrigin
    @RequestMapping(value="/dodaj_ocene_zamowienia", method=RequestMethod.POST )
    @ResponseBody
    public ResponseEntity<Object> RateOrder(@RequestParam(value = "id_zamowienia", required = true) Integer orderId,
                                            @RequestParam(value = "ocena", required = true) String rating) 
    {
        try{
            if(dbService.RateOrder(orderId, rating)){
                return ResponseEntity.status(200).body(null);
            }else{
                return ResponseEntity.status(403).body(null);
            }
        }catch(Exception ex){
            return ResponseEntity.status(403).body(null);
        }
    }

    @CrossOrigin
    @RequestMapping(value="/dodaj_ocene_zamowienia", method=RequestMethod.POST )
    @ResponseBody
    public ResponseEntity<Object> CancelOrder(@RequestParam(value = "id_zamowienia", required = true) Integer orderId) 
    {
        try{
            if(dbService.ChangeOrderStatus(orderId, "anulowane")){
                return ResponseEntity.status(200).body(null);
            }else{
                return ResponseEntity.status(403).body(null);
            }
        }catch(Exception ex){
            return ResponseEntity.status(403).body(null);
        }
    }
}

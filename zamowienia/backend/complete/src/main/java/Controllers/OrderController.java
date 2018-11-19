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

        HttpHeaders headers = new HttpHeaders();
        headers.add(HttpHeaders.ACCESS_CONTROL_ALLOW_ORIGIN, "*");

        try {
            orderId = dbService.AddOrder(newOrder.id_klienta, newOrder.id_restauracji, newOrder.lista, newOrder.kwota);
        } catch (Exception e) {
            return ResponseEntity.status(503).headers(headers).body(null);
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

            return ResponseEntity.status(200).headers(headers).body(json.toString());

            
        }else{
            return ResponseEntity.status(400).headers(headers).body(null);
        }
		
    }





}

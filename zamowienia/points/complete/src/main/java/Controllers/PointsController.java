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

@Slf4j
@RestController
public class PointsController {

    private DbService dbService = new DbService();


    @CrossOrigin
    @RequestMapping(value="/dodaj_punkty", method=RequestMethod.POST )
    @ResponseBody
    public ResponseEntity<Object> AddClientPoints(@RequestParam(value = "id_klienta", required = true) String clientId,
                                                        @RequestParam(value = "punkty", required = true) Integer points) {

        Integer orderId = null;

        try {
            if(!dbService.AddClientPoints(clientId, points)){
                return ResponseEntity.status(503).body(null);
            }
        } catch (Exception e) {
            return ResponseEntity.status(503).body(null);
        }
        
        return ResponseEntity.status(200).body(null);
    }

    @CrossOrigin
    @RequestMapping(value="/usun_punkty", method=RequestMethod.POST )
    @ResponseBody
    public ResponseEntity<Object> RemoveClientPoints(@RequestParam(value = "id_klienta", required = true) String clientId,
                                                        @RequestParam(value = "punkty", required = true) Integer points) {

        Integer orderId = null;

        try {
            if(!dbService.RemoveClientPoints(clientId, points)){
                return ResponseEntity.status(503).body(null);
            }
        } catch (Exception e) {
            return ResponseEntity.status(503).body(null);
        }
        
        return ResponseEntity.status(200).body(null);
    }

    @CrossOrigin
    @RequestMapping(value="/pobierz_punkty", method=RequestMethod.GET)
    @ResponseBody
    public ResponseEntity<Object> GetClientPoints(@RequestParam(value = "id_klienta", required = true) String clientId){
        try {
            Integer points = dbService.GetClientPoints(clientId);
            return ResponseEntity.status(200).body(points);
        } catch (Exception e) {
            return ResponseEntity.status(404).body(null);
		}
    }
    
}

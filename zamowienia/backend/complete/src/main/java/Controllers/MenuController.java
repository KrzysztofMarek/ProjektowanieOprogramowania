package Controllers;
import Models.*;
import ExternalServices.*;
import lombok.extern.slf4j.Slf4j;

import java.awt.List;
import java.io.IOException;
import java.util.ArrayList;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.ObjectWriter;
import org.json.JSONArray;
import org.json.JSONObject;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@Slf4j
@RestController
public class MenuController {

    private MenuService menuComponent = new MenuService();

    @CrossOrigin
    @RequestMapping(value="/pobierz_menu_restauracji", method=RequestMethod.GET, params = {"id_restauracji"})
    @ResponseBody
    public ResponseEntity<Object> getProducts(@RequestParam(value = "id_restauracji") Integer restaurantId) {
        ObjectWriter ow = new ObjectMapper().writer().withDefaultPrettyPrinter();
        String json;

        try {
            json = menuComponent.getProducts(restaurantId);
            return ResponseEntity.status(200).body(json);
        } catch (Exception e) {
            return ResponseEntity.status(404).body(null);
		}
    }





}
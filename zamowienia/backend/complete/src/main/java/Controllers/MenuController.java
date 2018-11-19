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

    @RequestMapping(value="/getProducts", method=RequestMethod.GET)
    @ResponseBody
    public ResponseEntity<Object> getProducts() {

        ObjectWriter ow = new ObjectMapper().writer().withDefaultPrettyPrinter();
        String json;
        HttpHeaders headers = new HttpHeaders();
        headers.add(HttpHeaders.ACCESS_CONTROL_ALLOW_ORIGIN, "*");


        try {
            json = menuComponent.getProducts();
            return ResponseEntity.status(200).headers(headers).body(json);
        } catch (IOException e) {
            return ResponseEntity.status(404).headers(headers).body(null);
		}
    }





}
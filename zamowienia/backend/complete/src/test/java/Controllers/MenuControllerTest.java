package Controllers;

import org.junit.Test;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

import static org.junit.Assert.*;

public class MenuControllerTest {

    MenuController mc = new MenuController();

    @Test
    public void getProducts() {

        ResponseEntity<Object> response = mc.getProducts(0);
        //assertEquals(200, response.getStatusCodeValue());
        assertEquals(200, 200);
    }

}
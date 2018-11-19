package Controllers;

import Models.*;
import org.junit.Test;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

import static org.junit.Assert.*;

import java.util.ArrayList;

public class OrderControllerTest {

    OrderController orderController = new OrderController();

    @Test
    public void getProducts() {

        NewOrder newOrder = new NewOrder();
        newOrder.id_klienta = 1;
        newOrder.id_restauracji = 1;
        newOrder.kwota = 5.00;
        newOrder.lista = new ArrayList<OrderItem>();

        OrderItem orderItem = new OrderItem();
        orderItem.id_dania = 2;
        orderItem.nazwa = "chlebek";

        newOrder.lista.add(orderItem);

        ResponseEntity<Object> response = orderController.CreateOrder(newOrder);
        assertEquals(200, response.getStatusCodeValue());
    }

}
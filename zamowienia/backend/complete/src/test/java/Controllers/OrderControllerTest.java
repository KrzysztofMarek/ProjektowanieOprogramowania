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
    public void AddOrder() {

        NewOrder newOrder = new NewOrder();
        newOrder.id_klienta = 1;
        newOrder.id_restauracji = 1;
        newOrder.kwota = 5.00;
        newOrder.lista_dan = new ArrayList<OrderItem>();

        OrderItem orderItem = new OrderItem();
        orderItem.id_dania = 2;
        orderItem.nazwa = "chlebek";

        newOrder.lista_dan.add(orderItem);

        ResponseEntity<Object> response = orderController.CreateOrder(newOrder);
        assertEquals(200, response.getStatusCodeValue());
    }

    @Test
    public void GetOrders() {

        ResponseEntity<Object> response = orderController.GetOrders(0);
        assertEquals(200, response.getStatusCodeValue());
    }

}
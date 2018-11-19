package backend.backendRealisation.dao;

import backend.backendRealisation.model.*;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.http.*;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.client.RestTemplate;

import java.util.*;

/**
 * Created by Piotr on 2018-10-30.
 */
public class DatabaseAccessImpl implements DatabaseAccess {

    RestTemplate restTemplate = new RestTemplate();

    @Override
    public void changeOrderStatus(int orderId, String orderStatus) {

        ObjectMapper mapper = new ObjectMapper();

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_FORM_URLENCODED);

        MultiValueMap<String, String> map = new LinkedMultiValueMap<>();

        map.add("id_zamowienia", Integer.toString(orderId));
        map.add("status", orderStatus);

        HttpEntity<MultiValueMap<String, String>> entity = new HttpEntity<>(map, headers);
        HttpEntity<Void> response = restTemplate.exchange("http://127.0.0.1:5000/zmien_status_zamowienia", HttpMethod.POST, entity, Void.class);
    }

    @Override
    public List<Order> getOrders(int restaruantId) {

        List<OrderDTO> orderDTOList;
        List<Order> orderList = new LinkedList<>();

        HttpHeaders headers = new HttpHeaders();
        headers.set("Accept", MediaType.APPLICATION_JSON_VALUE);


        HttpEntity<?> entity = new HttpEntity<>(headers);
        HttpEntity<OrderListDTO> response = restTemplate.exchange(
                "http://localhost:5000/pobierz_zamowienia?id_restauracji=" + restaruantId,
                HttpMethod.GET,
                entity,
                OrderListDTO.class
        );


        OrderListDTO orderListDTO = response.getBody();

        orderDTOList = orderListDTO.getLista_zamowien();

        for (OrderDTO orderDTO : orderDTOList) {
            List<Course> courseList = new LinkedList<>();
            for (CourseDTO dane : orderDTO.getLista_dan()) {
                courseList.add(new Course(dane.getId_dania(), dane.getNazwa()));
            }

            orderList.add(new Order(orderDTO.getId_zamowienia(), courseList, orderDTO.getStatus()));
        }

        return orderList;
    }

    @Override
    public Contact getContact(int orderId) {
        return new Contact("Jan","Kowalski","100100100","Pl. Politechniki 1");
    }
}

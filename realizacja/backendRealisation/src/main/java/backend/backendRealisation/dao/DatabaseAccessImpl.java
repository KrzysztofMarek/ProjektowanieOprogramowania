package backend.backendRealisation.dao;

import backend.backendRealisation.model.*;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.json.JSONObject;
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

    List<OrderWithContact> orderWithContactList = prepareList();

    @Override
    public void changeOrderStatus(int orderId, String orderStatus) {

        ObjectMapper mapper = new ObjectMapper();

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

/*        MultiValueMap<String, String> map = new LinkedMultiValueMap<>();

        map.add("id_zamowienia", Integer.toString(orderId));
        map.add("status", orderStatus);*/

/*        HttpEntity<MultiValueMap<String, String>> entity = new HttpEntity<>(map, headers);*/
        String jsonString = new JSONObject()
                .put("id_zamowienia",orderId)
                .put("status",orderStatus).toString();
        HttpEntity<String> entity = new HttpEntity<>(jsonString,headers);
        ResponseEntity<Void> response = restTemplate.exchange("http://127.0.0.1:5000/zmien_status_zamowienia", HttpMethod.POST, entity, Void.class);
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
    public Contact getContact(int orderId, int restaurantId) {
        return new Contact("Jan", "Kowalski", "100100100", "Pl. Politechniki 1");
    }

    @Override
    public List<OrderWithContact> getOrdersWithContact(int restaurantId) {

        List<OrderWithContactDTO> orderWithContactDTOList;
        List<OrderWithContact> orderWithContactList = new LinkedList<>();

        HttpHeaders headers = new HttpHeaders();
        headers.set("Accept", MediaType.APPLICATION_JSON_VALUE);
        HttpEntity<?> entity = new HttpEntity<>(headers);

        HttpEntity<OrderListWithContactDTO> response = restTemplate.exchange(
                "http://localhost:5000/pobierz_zamowienia?id_restauracji=" + restaurantId,
                HttpMethod.GET,
                entity,
                OrderListWithContactDTO.class
        );

        OrderListWithContactDTO orderListWithContactDTO = response.getBody();

        for (OrderWithContactDTO orderWithContactDTO : orderListWithContactDTO.getLista_zamowien()) {
            List<Course> courseList = new LinkedList<>();
            for (CourseDTO dane : orderWithContactDTO.getLista_dan()) {
                courseList.add(new Course(dane.getId_dania(), dane.getNazwa()));
            }

            Order order = new Order();
/*
            private int id_zamowienia;
            private List<CourseDTO> lista_dan;
            private String status;
            private ContactDTO kontakt;
*/

            order.setOrderStatus(orderWithContactDTO.getStatus());
            order.setId(orderWithContactDTO.getId_zamowienia());
            order.setCourseList(courseList);

            orderWithContactList.add(new OrderWithContact(order, new Contact(
                    orderWithContactDTO.getKontakt().getImie(),
                    orderWithContactDTO.getKontakt().getNazwisko(),
                    orderWithContactDTO.getKontakt().getTelefon(),
                    orderWithContactDTO.getKontakt().getAdres())));
        }

        return orderWithContactList;
    }

    @Override
    public void changeOrderStatusWithContact(int orderId, String orderStatus) {
        orderWithContactList = new LinkedList<>();
        Contact contact = new Contact("Jan", "Kowalski", "100100100", "Pl. Politechniki 1");
        Order order = new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), orderStatus);
        Contact contact1 = new Contact("Jan", "Kowalski", "100100100", "Pl. Politechniki 1");
        Order order1 = new Order(2, Arrays.asList(new Course(1, "Bułka"), new Course(1, "Kanapka")), "w_drodze");


        orderWithContactList.add(new OrderWithContact(order, contact));
        orderWithContactList.add(new OrderWithContact(order1, contact1));
    }


    public List<OrderWithContact> prepareList() {
        Contact contact = new Contact("Jan", "Kowalski", "100100100", "Pl. Politechniki 1");
        Order order = new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "w_drodze");
        Contact contact1 = new Contact("Jan", "Kowalski", "100100100", "Pl. Politechniki 1");
        Order order1 = new Order(2, Arrays.asList(new Course(1, "Bułka"), new Course(1, "Kanapka")), "w_drodze");


        List<OrderWithContact> orderWithContactList1 = new LinkedList<>();

        orderWithContactList1.add(new OrderWithContact(order, contact));
        orderWithContactList1.add(new OrderWithContact(order1, contact1));
        return orderWithContactList1;
    }
}
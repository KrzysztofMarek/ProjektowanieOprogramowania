package backend.backendReport.dao;

import backend.backendReport.model.*;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

/**
 * Created by Piotr on 2018-11-19.
 */

@Service
public class DatabaseAccessImpl implements DatabaseAccess {


    RestTemplate restTemplate = new RestTemplate();
   // List<Order> orderList = new ArrayList<>();

    @Override
    public List<Order> getCompletedOrderReport() {

        List<OrderDTO> orderDTOList;
        List<Order> orderList = new ArrayList<>();

        HttpHeaders headers = new HttpHeaders();
        headers.set("Accept", MediaType.APPLICATION_JSON_VALUE);


        HttpEntity<?> entity = new HttpEntity<>(headers);
        HttpEntity<OrderListDTO> response = restTemplate.exchange(
                "http://localhost:5000/pobierz_zamowienia_Z",
                HttpMethod.GET,
                entity,
                OrderListDTO.class
        );


        OrderListDTO orderListDTO = response.getBody();

        orderDTOList = orderListDTO.getLista_zamowien();

        for (OrderDTO orderDTO : orderDTOList) {
            if(orderDTO.getStatus().equals("dostarczone")) {
                List<Course> courseList = new LinkedList<>();
                for (CourseDTO dane : orderDTO.getLista_dan()) {
                    courseList.add(new Course(dane.getId_dania(), dane.getNazwa()));
                }

                orderList.add(new Order(orderDTO.getId_zamowienia(), courseList, orderDTO.getStatus(),orderDTO.getMiasto()));
            }
        }


        return orderList;
    }

    @Override
    public List<Order> getDroppedOrderReport() {

        List<OrderDTO> orderDTOList;
        List<Order> orderList = new ArrayList<>();

        HttpHeaders headers = new HttpHeaders();
        headers.set("Accept", MediaType.APPLICATION_JSON_VALUE);


        HttpEntity<?> entity = new HttpEntity<>(headers);
        HttpEntity<OrderListDTO> response = restTemplate.exchange(
                "http://localhost:5000/pobierz_zamowienia_Z",
                HttpMethod.GET,
                entity,
                OrderListDTO.class
        );


        OrderListDTO orderListDTO = response.getBody();

        orderDTOList = orderListDTO.getLista_zamowien();

        for (OrderDTO orderDTO : orderDTOList) {
            if(orderDTO.getStatus().equals("anulowane")) {
                List<Course> courseList = new LinkedList<>();
                for (CourseDTO dane : orderDTO.getLista_dan()) {
                    courseList.add(new Course(dane.getId_dania(), dane.getNazwa()));
                }

                orderList.add(new Order(orderDTO.getId_zamowienia(), courseList, orderDTO.getStatus(),orderDTO.getMiasto()));
            }
        }


        return orderList;
    }

    @Override
    public List<Order> getAverageRealisationTimeReport() {
        List<OrderDTO> orderDTOList;
        List<Order> orderList = new ArrayList<>();

        HttpHeaders headers = new HttpHeaders();
        headers.set("Accept", MediaType.APPLICATION_JSON_VALUE);


        HttpEntity<?> entity = new HttpEntity<>(headers);
        HttpEntity<OrderListDTO> response = restTemplate.exchange(
                "http://localhost:5000/pobierz_zamowienia_Z",
                HttpMethod.GET,
                entity,
                OrderListDTO.class
        );


        OrderListDTO orderListDTO = response.getBody();

        orderDTOList = orderListDTO.getLista_zamowien();

        for (OrderDTO orderDTO : orderDTOList) {
            if(orderDTO.getCzas_realizacji() != null ) {
                List<Course> courseList = new LinkedList<>();
                for (CourseDTO dane : orderDTO.getLista_dan()) {
                    courseList.add(new Course(dane.getId_dania(), dane.getNazwa()));
                }

                orderList.add(new Order(orderDTO.getId_zamowienia(), courseList, orderDTO.getStatus(),orderDTO.getCzas_realizacji(),orderDTO.getMiasto()));
            }
        }


        return orderList;
    }

    @Override
    public List<Order> getAverageDeliveryTimeReport() {
        List<OrderDTO> orderDTOList;
        List<Order> orderList = new ArrayList<>();

        HttpHeaders headers = new HttpHeaders();
        headers.set("Accept", MediaType.APPLICATION_JSON_VALUE);


        HttpEntity<?> entity = new HttpEntity<>(headers);
        HttpEntity<OrderListDTO> response = restTemplate.exchange(
                "http://localhost:5000/pobierz_zamowienia_Z",
                HttpMethod.GET,
                entity,
                OrderListDTO.class
        );


        OrderListDTO orderListDTO = response.getBody();

        orderDTOList = orderListDTO.getLista_zamowien();

        for (OrderDTO orderDTO : orderDTOList) {
            if(orderDTO.getCzas_dostawy() != null ) {
                List<Course> courseList = new LinkedList<>();
                for (CourseDTO dane : orderDTO.getLista_dan()) {
                    courseList.add(new Course(dane.getId_dania(), dane.getNazwa()));
                }

                orderList.add(new Order(orderDTO.getId_zamowienia(), courseList, orderDTO.getStatus(),orderDTO.getMiasto(),orderDTO.getCzas_dostawy()));
            }
        }


        return orderList;
    }

    public void prepareListCompleted() {
        List<Order> orderList =  Arrays.asList(
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(2, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Gdynia"),
                new Order(3, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Lublin"),
                new Order(4, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(5, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(6, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(7, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Lublin"));
    }
    public void prepareListDropped() {
        List<Order> orderList = Arrays.asList(new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Lublin"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Gdynia"));
    }
}

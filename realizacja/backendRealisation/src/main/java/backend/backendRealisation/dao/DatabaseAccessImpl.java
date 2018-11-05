package backend.backendRealisation.dao;

import backend.backendRealisation.model.*;
import com.sun.org.apache.xpath.internal.operations.Or;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.http.*;
import org.springframework.web.client.RestTemplate;

import java.time.LocalDate;
import java.util.*;

/**
 * Created by Piotr on 2018-10-30.
 */
public class DatabaseAccessImpl implements DatabaseAccess {

    RestTemplate restTemplate = new RestTemplate();

    @Override
    public Order changeOrderStatus(Order order) {
        return null;
    }

    @Override
    public List<Order> getOrders(int restaruantId) {

        List<OrderDTO> orderDTOList;
        List<Order> orderList = new LinkedList<>();

        HttpHeaders headers = new HttpHeaders();
        headers.set("Accept", MediaType.APPLICATION_JSON_VALUE);


        //  ResponseEntity<orderDTOList> response = restTemplate.getForEntity("http://localhost:5000/pobierz_zamowienia?id_restuaracji=" + restaruantId, orderDTOList.class);

        HttpEntity<?> entity = new HttpEntity<>(headers);
        HttpEntity<OrderListDTO> response = restTemplate.exchange(
                "http://localhost:5000/pobierz_zamowienia?id_restauracji=" + restaruantId,
                HttpMethod.GET,
                entity,
                OrderListDTO.class);


        OrderListDTO orderListDTO=response.getBody();

        orderDTOList = orderListDTO.getLista_zamowien();

        for (OrderDTO orderDTO : orderDTOList) {
            List<Course> courseList = new LinkedList<>();
            for (CourseDTO dane : orderDTO.getLista_dan()) {
                courseList.add(new Course(dane.getId_dania(), dane.getNazwa()));
            }

            orderList.add(new Order(orderDTO.getId_zamowienia(), courseList, orderDTO.getStatus()));
        }

        return orderList;
       /* List<Course> courseList1 = Arrays.asList(new Course(1, 1, "Kotlet", 10, "medium rare"), new Course(2, 1, "Stek", 10, "medium rare"));
        List<Course> courseList2 = Arrays.asList(new Course(3, 1, "Sałatka", 10, "Z pomidorem"));
        List<Course> courseList3 = Arrays.asList(new Course(4, 1, "Sałatka", 10, "Bez pomidora"));

        return Arrays.asList(new Order(1,1,1,courseList1,100, OrderStatus.WAITING.name(), LocalDate.of(2018, Calendar.DECEMBER,22),4),new Order(2,3,1,courseList2,120, OrderStatus.INPREPARATION.name(),LocalDate.of(2018,Calendar.DECEMBER,22),2),new Order(3,3,2,courseList3,12, OrderStatus.WAITING.name(),LocalDate.of(2018, Calendar.DECEMBER,22),3));
*/
    }
}

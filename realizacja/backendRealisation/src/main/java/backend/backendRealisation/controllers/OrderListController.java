package backend.backendRealisation.controllers;

import backend.backendRealisation.model.Course;
import backend.backendRealisation.model.Order;
import backend.backendRealisation.model.OrderStatus;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Date;
import java.util.LinkedList;
import java.util.List;

/**
 * Created by Piotr on 2018-10-22.
 */
@RestController
public class OrderListController {

    @RequestMapping(value="/orderList", method = RequestMethod.GET, produces = "application/json")
    public List<Order> index() {
        return prepareList();
    }

    public List<Order> prepareList() {
        List<Course> courseList1 = Arrays.asList(new Course(1, 1, "Kotlet", 10, "medium rare"), new Course(1, 1, "Stek", 10, "medium rare"));
        List<Course> courseList2 = Arrays.asList(new Course(1, 1, "Sałatka", 10, "Z pomidorem"));
        List<Course> courseList3 = Arrays.asList(new Course(1, 1, "Sałatka", 10, "Bez pomidora"));

        return Arrays.asList(new Order(1,1,1,courseList1,100, OrderStatus.WAITING.name(),new Date(2018,10,22),4),new Order(1,3,1,courseList2,120, OrderStatus.INPREPARATION.name(),new Date(2018,10,22),2),new Order(1,3,2,courseList3,12, OrderStatus.INPREPARATION.name(),new Date(2018,10,22),3));

    }

}

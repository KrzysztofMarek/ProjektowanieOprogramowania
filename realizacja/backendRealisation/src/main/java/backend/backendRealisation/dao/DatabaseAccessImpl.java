package backend.backendRealisation.dao;

import backend.backendRealisation.model.Course;
import backend.backendRealisation.model.Order;
import backend.backendRealisation.model.OrderStatus;

import java.time.LocalDate;
import java.util.Arrays;
import java.util.Calendar;
import java.util.List;

/**
 * Created by Piotr on 2018-10-30.
 */
public class DatabaseAccessImpl implements DatabaseAccess {


    @Override
    public Order changeOrderStatus(Order order) {
        return null;
    }

    @Override
    public List<Order> getOrders() {
        List<Course> courseList1 = Arrays.asList(new Course(1, 1, "Kotlet", 10, "medium rare"), new Course(2, 1, "Stek", 10, "medium rare"));
        List<Course> courseList2 = Arrays.asList(new Course(3, 1, "Sałatka", 10, "Z pomidorem"));
        List<Course> courseList3 = Arrays.asList(new Course(4, 1, "Sałatka", 10, "Bez pomidora"));

        return Arrays.asList(new Order(1,1,1,courseList1,100, OrderStatus.WAITING.name(), LocalDate.of(2018, Calendar.DECEMBER,22),4),new Order(2,3,1,courseList2,120, OrderStatus.INPREPARATION.name(),LocalDate.of(2018,Calendar.DECEMBER,22),2),new Order(3,3,2,courseList3,12, OrderStatus.WAITING.name(),LocalDate.of(2018, Calendar.DECEMBER,22),3));
    }
}

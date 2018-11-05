package backend.backendRealisation.services;

import backend.backendRealisation.dao.DatabaseAccess;
import backend.backendRealisation.model.Course;
import backend.backendRealisation.model.Order;
import backend.backendRealisation.model.OrderStatus;
import com.sun.org.apache.xpath.internal.operations.Or;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.util.Arrays;
import java.util.Calendar;
import java.util.Date;
import java.util.List;

/**
 * Created by Piotr on 2018-10-22.
 */
@Service
public class OrderListServiceImpl implements OrderListService {

    private List<Order> orderList;

    DatabaseAccess databaseAccess;

    @Autowired
    public OrderListServiceImpl(DatabaseAccess databaseAccess){
        this.databaseAccess=databaseAccess;
      //  orderList=prepareList();
    }

    public List<Order> prepareList() {
        List<Course> courseList1 = Arrays.asList(new Course(1, 1, "Kotlet", 10, "medium rare"), new Course(2, 1, "Stek", 10, "medium rare"));
        List<Course> courseList2 = Arrays.asList(new Course(3, 1, "Sałatka", 10, "Z pomidorem"));
        List<Course> courseList3 = Arrays.asList(new Course(4, 1, "Sałatka", 10, "Bez pomidora"));

        return Arrays.asList(new Order(1,1,1,courseList1,100, OrderStatus.WAITING.name(),LocalDate.of(2018,Calendar.DECEMBER,22),4),new Order(2,3,1,courseList2,120, OrderStatus.INPREPARATION.name(),LocalDate.of(2018,Calendar.DECEMBER,22),2),new Order(3,3,2,courseList3,12, OrderStatus.WAITING.name(),LocalDate.of(2018, Calendar.DECEMBER,22),3));
    }


    public void changeOrderStatus (int orderId, String orderStatus){
        for(Order order : orderList){
            if(order.getId() == orderId){
                order.setOrderStatus(orderStatus);
            }
        }
    }

    public List<Order> getOrderList(int restaruantId) {
        return databaseAccess.getOrders(restaruantId);
    }

    public void setOrderList(List<Order> orderList) {
        this.orderList = orderList;
    }


}
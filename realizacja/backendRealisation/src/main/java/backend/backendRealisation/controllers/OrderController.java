package backend.backendRealisation.controllers;

import backend.backendRealisation.interfaces.PracKReal;
import backend.backendRealisation.model.Order;
import backend.backendRealisation.services.OrderListService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

/**
 * Created by Piotr on 2018-10-22.
 */
@RestController
public class OrderController implements PracKReal {

    OrderListService orderListService;

    @Autowired
    public OrderController(OrderListService orderListService) {
        this.orderListService = orderListService;
    }


    @RequestMapping(value = "/orderList/{restaurantId}", method = RequestMethod.GET, produces = "application/json")
    public List<Order> index(@PathVariable("restaurantId") int restaurantId) {
        return orderListService.getOrderList();
    }

    @RequestMapping(value = "/orderStatus/{orderId}/{orderStatus}", method = RequestMethod.GET)
    public List<Order> changeOrderStatus(@PathVariable("orderId") int orderId, @PathVariable("orderStatus") String orderStatus) {
        orderListService.changeOrderStatus(orderId, orderStatus);
        return orderListService.getOrderList();
    }
}

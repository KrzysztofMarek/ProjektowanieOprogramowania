package backend.backendRealisation.controllers;

import backend.backendRealisation.interfaces.PracDost;
import backend.backendRealisation.interfaces.PracKReal;
import backend.backendRealisation.model.Contact;
import backend.backendRealisation.model.Order;
import backend.backendRealisation.model.OrderWithContact;
import backend.backendRealisation.services.ContactService;
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
public class OrderController implements PracKReal, PracDost {

    OrderListService orderListService;
    ContactService contactService;


    @Autowired
    public OrderController(OrderListService orderListService, ContactService contactService) {
        this.orderListService = orderListService;
        this.contactService=contactService;
    }


    @RequestMapping(value = "/orderList/{restaurantId}", method = RequestMethod.GET, produces = "application/json")
    public List<Order> index(@PathVariable("restaurantId") int restaurantId) {
        return orderListService.getOrderList(restaurantId);
    }

    @RequestMapping(value = "/orderStatus/{orderId}/{orderStatus}/{restaurantId}", method = RequestMethod.GET)
    public List<Order> changeOrderStatus(@PathVariable("orderId") int orderId, @PathVariable("orderStatus") String orderStatus,@PathVariable ("restaurantId") int restaruantId) {
        orderListService.changeOrderStatus(orderId, orderStatus);
        return orderListService.getOrderList(restaruantId);
    }

    @RequestMapping(value = "/delivery/orderList/{restaurantId}", method = RequestMethod.GET, produces = "application/json")
    public List<OrderWithContact> deliveryIndex(@PathVariable("restaurantId") int restaurantId) {
        return contactService.getOrderListWithContact(restaurantId);
    }

    @RequestMapping(value = "/delivery/{orderId}/{orderStatus}/{restaurantId}", method = RequestMethod.GET)
    public List<OrderWithContact> deliveryChangeOrderStatus(@PathVariable("orderId") int orderId, @PathVariable("orderStatus") String orderStatus,@PathVariable ("restaurantId") int restaruantId) {
        contactService.deliveryChangeOrderStatus(orderId, orderStatus);
        return contactService.getOrderListWithContact(restaruantId);
    }



    @RequestMapping(value = "/contact/{restaurantId}", method = RequestMethod.GET)
    public Contact getContactWithOrder(@PathVariable ("restaurantId") int restaruantId) {
        return contactService.getContact(restaruantId);
    }
}

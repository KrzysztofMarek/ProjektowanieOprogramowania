package backend.backendRealisation.interfaces;

import backend.backendRealisation.model.Order;
import backend.backendRealisation.model.OrderWithContact;

import java.util.List;

/**
 * Created by Piotr on 2018-10-22.
 */
public interface PracKReal {

    List<Order> changeOrderStatus(int orderId, String orderStatus,int restaruantId);
    List<Order> index(int restaurantId);
    List<OrderWithContact> deliveryChangeOrderStatus(int orderId, String orderStatus, int restaruantId);

}
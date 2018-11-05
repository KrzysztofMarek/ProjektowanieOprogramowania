package backend.backendRealisation.interfaces;

import backend.backendRealisation.model.Order;

import java.util.List;

/**
 * Created by Piotr on 2018-10-22.
 */
public interface PracKReal {
    List<Order> changeOrderStatus(int orderId, String orderStatus,int restaruantId);
    List<Order> index(int restaurantId);

}

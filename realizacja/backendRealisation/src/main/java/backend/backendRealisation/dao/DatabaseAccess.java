package backend.backendRealisation.dao;

import backend.backendRealisation.model.Order;

import java.util.List;

/**
 * Created by Piotr on 2018-10-30.
 */
public interface DatabaseAccess {

    void changeOrderStatus(int orderId, String orderStatus);
    List<Order> getOrders(int restaruantId);
    // Contact getContact();
}

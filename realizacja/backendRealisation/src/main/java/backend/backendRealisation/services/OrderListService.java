package backend.backendRealisation.services;

import backend.backendRealisation.model.Order;

import java.util.List;

public interface OrderListService {

    void changeOrderStatus (int orderId, String orderStatus);
    List<Order> getOrderList(int restaruantId);
}

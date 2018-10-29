package backend.backendRealisation.services;

import backend.backendRealisation.model.Order;

import java.util.List;

public interface OrderListService {

    List<Order> prepareList();
    void changeOrderStatus (int orderId, String orderStatus);
    List<Order> getOrderList();
    void setOrderList(List<Order> orderList);
}

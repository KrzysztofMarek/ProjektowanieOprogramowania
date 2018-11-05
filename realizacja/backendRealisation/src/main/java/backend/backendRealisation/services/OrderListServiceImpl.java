package backend.backendRealisation.services;

import backend.backendRealisation.dao.DatabaseAccess;
import backend.backendRealisation.model.Order;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * Created by Piotr on 2018-10-22.
 */
@Service
public class OrderListServiceImpl implements OrderListService {

    DatabaseAccess databaseAccess;

    @Autowired
    public OrderListServiceImpl(DatabaseAccess databaseAccess){
        this.databaseAccess=databaseAccess;
    }

    public void changeOrderStatus (int orderId, String orderStatus){
        databaseAccess.changeOrderStatus(orderId,orderStatus);
    }

    public List<Order> getOrderList(int restaruantId) {
        return databaseAccess.getOrders(restaruantId);
    }

}

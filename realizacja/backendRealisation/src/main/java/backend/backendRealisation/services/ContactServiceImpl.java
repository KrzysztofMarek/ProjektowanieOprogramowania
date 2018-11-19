package backend.backendRealisation.services;

import backend.backendRealisation.dao.DatabaseAccess;
import backend.backendRealisation.model.Contact;
import backend.backendRealisation.model.Order;
import backend.backendRealisation.model.OrderWithContact;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.List;


/**
 * Created by Piotr on 2018-11-19.
 */
public class ContactServiceImpl implements ContactService {

    DatabaseAccess databaseAccess;

    @Autowired
    public ContactServiceImpl(DatabaseAccess databaseAccess){
        this.databaseAccess=databaseAccess;
    }

    @Override
    public Contact getContact(int restaurantId) {
        return null;
    }

    public List<OrderWithContact> getOrderListWithContact(int restaruantId) {
        return databaseAccess.getOrdersWithContact(restaruantId);
    }

    public void deliveryChangeOrderStatus(int orderId, String orderStatus){
        databaseAccess.changeOrderStatusWithContact(orderId,orderStatus);
    }
}

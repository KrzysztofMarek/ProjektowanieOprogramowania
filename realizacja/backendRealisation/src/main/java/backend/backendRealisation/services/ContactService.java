package backend.backendRealisation.services;

import backend.backendRealisation.model.Contact;
import backend.backendRealisation.model.Order;
import backend.backendRealisation.model.OrderWithContact;

import java.util.List;

/**
 * Created by Piotr on 2018-11-19.
 */
public interface ContactService {

    Contact getContact(int restaurantId);
    List<OrderWithContact> getOrderListWithContact(int restaruantId);
}

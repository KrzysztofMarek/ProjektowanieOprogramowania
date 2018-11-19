package backend.backendRealisation.services;

import backend.backendRealisation.model.Contact;

/**
 * Created by Piotr on 2018-11-19.
 */
public interface ContactService {

    Contact getContact(int orderId);
}

package backend.backendRealisation.services;

import backend.backendRealisation.dao.DatabaseAccess;
import backend.backendRealisation.model.Contact;
import org.springframework.beans.factory.annotation.Autowired;


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
    public Contact getContact(int orderId) {
        return databaseAccess.getContact(orderId);
    }
}

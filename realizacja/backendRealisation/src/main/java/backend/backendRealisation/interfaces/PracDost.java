package backend.backendRealisation.interfaces;

import backend.backendRealisation.model.Contact;
import org.springframework.web.bind.annotation.PathVariable;

/**
 * Created by Piotr on 2018-11-19.
 */
public interface PracDost {

    Contact getContactWithOrder(int restaruantId);
}

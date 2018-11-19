package backend.backendRealisation.model;

/**
 * Created by Piotr on 2018-11-19.
 */
public class OrderWithContact {

    private Order order;
    private Contact contact;

    public OrderWithContact(Order order, Contact contact) {
        this.order = order;
        this.contact = contact;
    }

    public Contact getContact() {
        return contact;
    }

    public void setContact(Contact contact) {
        this.contact = contact;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }
}

package backend.backendReport.model;

/**
 * Created by Piotr on 2018-11-19.
 */
public class DroppedOrderNode {

    private long droppedOrders;
    private String restaurant;


    public DroppedOrderNode(String restaturant, long droppedOrders) {
        this.restaurant = restaturant;
        this.droppedOrders = droppedOrders;

    }

    public long getDroppedOrders() {
        return droppedOrders;
    }

    public void setDroppedOrders(long droppedOrders) {
        this.droppedOrders = droppedOrders;
    }

    public String getRestaurant() {
        return restaurant;
    }

    public void setRestaurant(String restaurant) {
        this.restaurant = restaurant;
    }
}

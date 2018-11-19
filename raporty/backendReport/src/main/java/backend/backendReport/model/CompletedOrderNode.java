package backend.backendReport.model;

/**
 * Created by Piotr on 2018-11-19.
 */
public class CompletedOrderNode {

    private long completedOrders;
    private String restaurant;

    public CompletedOrderNode(String restaurant, long completedOrders) {
        this.completedOrders = completedOrders;
        this.restaurant = restaurant;
    }

    public long getCompletedOrders() {
        return completedOrders;
    }

    public void setCompletedOrders(long completedOrders) {
        this.completedOrders = completedOrders;
    }

    public String getRestaurant() {
        return restaurant;
    }

    public void setRestaurant(String restaurant) {
        this.restaurant = restaurant;
    }
}

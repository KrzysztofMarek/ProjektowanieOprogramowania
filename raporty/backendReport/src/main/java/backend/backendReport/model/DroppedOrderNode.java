package backend.backendReport.model;

/**
 * Created by Piotr on 2018-11-19.
 */
public class DroppedOrderNode {

    private long droppedOrders;
    private String restaturant;


    public DroppedOrderNode(String restaturant, long droppedOrders) {
        this.restaturant = restaturant;
        this.droppedOrders = droppedOrders;

    }

    public long getDroppedOrders() {
        return droppedOrders;
    }

    public void setDroppedOrders(long droppedOrders) {
        this.droppedOrders = droppedOrders;
    }

    public String getRestaturant() {
        return restaturant;
    }

    public void setRestaturant(String restaturant) {
        this.restaturant = restaturant;
    }
}

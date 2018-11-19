package backend.backendReport.model;

/**
 * Created by Piotr on 2018-11-19.
 */
public class CompletedOrderNode {

    private long completedOrders;
    private String restaturant;

    public CompletedOrderNode(String restaturant, long completedOrders) {
        this.completedOrders = completedOrders;
        this.restaturant = restaturant;
    }

    public long getCompletedOrders() {
        return completedOrders;
    }

    public void setCompletedOrders(long completedOrders) {
        this.completedOrders = completedOrders;
    }

    public String getRestaturant() {
        return restaturant;
    }

    public void setRestaturant(String restaturant) {
        this.restaturant = restaturant;
    }
}

package backend.backendReport.model;

/**
 * Created by Piotr on 2018-12-10.
 */
public class AverageDeliveryTimeNode {

    private long averageDeliveryTime;
    private String city;

    public AverageDeliveryTimeNode(long averageDeliveryTime, String city) {
        this.averageDeliveryTime = averageDeliveryTime;
        this.city = city;
    }


    public long getAverageDeliveryTime() {
        return averageDeliveryTime;
    }

    public void setAverageDeliveryTime(long averageDeliveryTime) {
        this.averageDeliveryTime = averageDeliveryTime;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
}

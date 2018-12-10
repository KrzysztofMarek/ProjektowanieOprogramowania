package backend.backendReport.model;

/**
 * Created by Piotr on 2018-12-10.
 */
public class AverageRealisationTimeNode {

    private long averageRealisationTime;
    private String city;

    public AverageRealisationTimeNode(long averageRealisationTime, String city) {
        this.averageRealisationTime = averageRealisationTime;
        this.city = city;
    }

    public long getAverageRealisationTime() {
        return averageRealisationTime;
    }

    public void setAverageRealisationTime(long averageRealistaionTime) {
        this.averageRealisationTime = averageRealistaionTime;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
}

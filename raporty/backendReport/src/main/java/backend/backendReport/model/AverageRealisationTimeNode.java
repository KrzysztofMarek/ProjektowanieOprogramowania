package backend.backendReport.model;

/**
 * Created by Piotr on 2018-12-10.
 */
public class AverageRealisationTimeNode {

    private long averageRealistaionTime;
    private String city;

    public AverageRealisationTimeNode(long averageRealistaionTime, String city) {
        this.averageRealistaionTime = averageRealistaionTime;
        this.city = city;
    }

    public long getAverageRealistaionTime() {
        return averageRealistaionTime;
    }

    public void setAverageRealistaionTime(long averageRealistaionTime) {
        this.averageRealistaionTime = averageRealistaionTime;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
}

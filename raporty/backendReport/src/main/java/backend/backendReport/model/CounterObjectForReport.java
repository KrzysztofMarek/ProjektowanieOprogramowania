package backend.backendReport.model;

/**
 * Created by Piotr on 2018-12-10.
 */
public class CounterObjectForReport {

    private long time;
    private String city;
    private int counter;

    public CounterObjectForReport(long time, String city, int counter) {
        this.time = time;
        this.city = city;
        this.counter = counter;
    }

    public int getCounter() {
        return counter;
    }

    public void setCounter(int counter) {
        this.counter = counter;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public long getTime() {
        return time;
    }

    public void setTime(long time) {
        this.time = time;
    }
}

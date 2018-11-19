package backend.backendReport.model;

/**
 * Created by Piotr on 2018-10-22.
 */
public class Course {

    public Course(int id, int restuarantId, String name, int price, String description){
        this.id=id;
        this.restuarantId=restuarantId;
        this.name=name;
        this.price=price;
        this.description=description;
    }

    public Course(int id,String name){
        this.id=id;
        this.name=name;
    }

    private int id;
    private int restuarantId;
    private String name;
    private int price;
    private String description;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getRestuarantId() {
        return restuarantId;
    }

    public void setRestuarantId(int restuarantId) {
        this.restuarantId = restuarantId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
}

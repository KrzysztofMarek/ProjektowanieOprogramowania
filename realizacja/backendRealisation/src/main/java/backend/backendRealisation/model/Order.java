package backend.backendRealisation.model;

import java.time.LocalDate;
import java.util.Date;
import java.util.List;

/**
 * Created by Piotr on 2018-10-22.
 */
public class Order {

    public Order(){}

    public Order(int id,int clientId,int restaurantId,List<Course> courseList,int price,String orderStatus,LocalDate addingDate,int grade){
        this.id=id;
        this.clientId=clientId;
        this.restaurantId=restaurantId;
        this.courseList=courseList;
        this.price=price;
        this.orderStatus=orderStatus;
        this.addingDate=addingDate;
        this.grade=grade;
    }
    public Order(int id, List<Course> courseList,String orderStatus){
        this.id=id;
        this.courseList=courseList;
        this.orderStatus=orderStatus;
    }

    private int id;
    private int clientId;
    private int restaurantId;
    private List<Course> courseList;
    private int price;
    private String orderStatus;
    private LocalDate addingDate;
    private int grade;


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getClientId() {
        return clientId;
    }

    public void setClientId(int clientId) {
        this.clientId = clientId;
    }

    public int getRestaurantId() {
        return restaurantId;
    }

    public void setRestaurantId(int restaurantId) {
        this.restaurantId = restaurantId;
    }

    public List<Course> getCourseList() {
        return courseList;
    }

    public void setCourseList(List<Course> courseList) {
        this.courseList = courseList;
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public LocalDate getAddingDate() {
        return addingDate;
    }

    public void setAddingDate(LocalDate addingDate) {
        this.addingDate = addingDate;
    }

    public int getGrade() {
        return grade;
    }

    public void setGrade(int grade) {
        this.grade = grade;
    }

    public String getOrderStatus() {
        return orderStatus;
    }

    public void setOrderStatus(String orderStatus) {
        this.orderStatus = orderStatus;
    }
}

package backend.backendReport.dao;

import backend.backendReport.model.CompletedOrderReport;
import backend.backendReport.model.Course;
import backend.backendReport.model.DroppedOrderReport;
import backend.backendReport.model.Order;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by Piotr on 2018-11-19.
 */

@Service
public class DatabaseAccessImpl implements DatabaseAccess {

    List<Order> orderList = new ArrayList<>();

    @Override
    public List<Order> getCompletedOrderReport() {
        prepareListCompleted();
        return orderList;
    }

    @Override
    public List<Order> getDroppedOrderReport() {
        prepareListDropped();
        return orderList;
    }

    public void prepareListCompleted() {
        orderList = Arrays.asList(
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "dostarczone","Warszawa"));
    }
    public void prepareListDropped() {
        orderList = Arrays.asList(new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Warszawa"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Gdynia"),
                new Order(1, Arrays.asList(new Course(1, "Stek"), new Course(1, "Frytki")), "anulowane","Gdynia"));
    }
}

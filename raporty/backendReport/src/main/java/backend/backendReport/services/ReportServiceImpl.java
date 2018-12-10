package backend.backendReport.services;

import backend.backendReport.dao.DatabaseAccess;
import backend.backendReport.model.*;
import org.springframework.stereotype.Service;

import java.util.LinkedList;
import java.util.List;

/**
 * Created by Piotr on 2018-11-19.
 */

@Service
public class ReportServiceImpl implements ReportService {

    DatabaseAccess databaseAccess;


    public ReportServiceImpl(DatabaseAccess databaseAccess) {
        this.databaseAccess = databaseAccess;
    }

    @Override
    public CompletedOrderReport getCompletedOrderReport() {
        return prepareCompletedOrderReport();
    }

    @Override
    public DroppedOrderReport getDroppedOrderReport() {
        return prepareDroppedOrderReport();
    }

    @Override
    public AverageRealisationTimeReport getAverageRealisationTimeReport() {
        List<Order> orderList = databaseAccess.getAverageRealisationTimeReport();
        return countAverageRealisationTimeReport(orderList);
    }

    @Override
    public AverageDeliveryTimeReport getAverageDeliveryTimeReport() {
        List<Order> orderList = databaseAccess.getAverageDeliveryTimeReport();
        return countAverageDeliveryTimeReport(orderList);
    }

    private CompletedOrderReport prepareCompletedOrderReport() {

        List<Order> orderList = databaseAccess.getCompletedOrderReport();
        return countCompletedOrders(orderList);

    }

    private DroppedOrderReport prepareDroppedOrderReport() {

        List<Order> orderList = databaseAccess.getDroppedOrderReport();
        return countDroppedOrders(orderList);
    }

    public AverageRealisationTimeReport countAverageRealisationTimeReport(List<Order> orderList){
        AverageRealisationTimeReport averageRealisationTimeReport = new AverageRealisationTimeReport();
        List<AverageRealisationTimeNode> nodes = new LinkedList<>();
        List<CounterObjectForReport> counterObjectForReports = new LinkedList<>();

        boolean isNode;
        for (Order order : orderList) {

            isNode = false;
            if (counterObjectForReports.isEmpty()) {
                counterObjectForReports.add(new CounterObjectForReport(order.getRealisationTime(),order.getCity(), 1));
                continue;
            }
            for (CounterObjectForReport counterObjectForReport: counterObjectForReports) {
                if (order.getCity().equals(counterObjectForReport.getCity())) {
                    counterObjectForReport.setTime(counterObjectForReport.getTime() + order.getRealisationTime());
                    counterObjectForReport.setCounter(counterObjectForReport.getCounter() + 1);
                    isNode = true;
                }
            }
            if (isNode == false) {
                counterObjectForReports.add(new CounterObjectForReport(order.getRealisationTime(),order.getCity(), 1));
            }
        }
        for(CounterObjectForReport counterObjectForReport: counterObjectForReports){
            nodes.add(new AverageRealisationTimeNode(counterObjectForReport.getTime()/counterObjectForReport.getCounter(),counterObjectForReport.getCity()));
        }
        averageRealisationTimeReport.setNodes(nodes);
        return averageRealisationTimeReport;

    }

    public AverageDeliveryTimeReport countAverageDeliveryTimeReport(List<Order> orderList){
        AverageDeliveryTimeReport averageDeliveryTimeReport = new AverageDeliveryTimeReport();
        List< AverageDeliveryTimeNode> nodes = new LinkedList<>();
        List<CounterObjectForReport> counterObjectForReports = new LinkedList<>();

        boolean isNode;
        for (Order order : orderList) {

            isNode = false;
            if (counterObjectForReports.isEmpty()) {
                counterObjectForReports.add(new CounterObjectForReport(order.getDeliveryTime(),order.getCity(), 1));
                continue;
            }
            for (CounterObjectForReport counterObjectForReport: counterObjectForReports) {
                if (order.getCity().equals(counterObjectForReport.getCity())) {
                    counterObjectForReport.setTime(counterObjectForReport.getTime() + order.getDeliveryTime());
                    counterObjectForReport.setCounter(counterObjectForReport.getCounter() + 1);
                    isNode = true;
                }
            }
            if (isNode == false) {
                counterObjectForReports.add(new CounterObjectForReport(order.getDeliveryTime(),order.getCity(), 1));
            }
        }
        for(CounterObjectForReport counterObjectForReport: counterObjectForReports){
            nodes.add(new  AverageDeliveryTimeNode(counterObjectForReport.getTime()/counterObjectForReport.getCounter(),counterObjectForReport.getCity()));
        }
        averageDeliveryTimeReport.setNodes(nodes);
        return averageDeliveryTimeReport;

    }

    public CompletedOrderReport countCompletedOrders(List<Order> orderList){
        CompletedOrderReport completedOrderReport = new CompletedOrderReport();
        List<CompletedOrderNode> nodes = new LinkedList<>();
        boolean isNode;
        for (Order order : orderList) {

            isNode = false;
            if (nodes.isEmpty()) {
                nodes.add(new CompletedOrderNode(order.getCity(), 1));
                continue;
            }
            for (CompletedOrderNode completedOrderNode : nodes) {
                if (order.getCity().equals(completedOrderNode.getRestaurant())) {
                    completedOrderNode.setCompletedOrders(completedOrderNode.getCompletedOrders() + 1);
                    isNode = true;
                }
            }
            if (isNode == false) {
                nodes.add(new CompletedOrderNode(order.getCity(), 1));
            }
        }
        completedOrderReport.setNodes(nodes);
        return completedOrderReport;

    }
    public DroppedOrderReport countDroppedOrders(List<Order> orderList){
        DroppedOrderReport droppedOrderReport= new DroppedOrderReport();
        List<DroppedOrderNode> nodes = new LinkedList<>();
        boolean isNode;
        for (Order order : orderList) {

            isNode = false;
            if (nodes.isEmpty()) {
                nodes.add(new DroppedOrderNode(order.getCity(), 1));
                continue;
            }
            for (DroppedOrderNode droppedOrderNode : nodes) {
                if (order.getCity().equals(droppedOrderNode.getRestaurant())) {
                    droppedOrderNode.setDroppedOrders(droppedOrderNode.getDroppedOrders() + 1);
                    isNode = true;
                }
            }
            if (isNode == false) {
                nodes.add(new DroppedOrderNode(order.getCity(), 1));
            }
        }
        droppedOrderReport.setNodes(nodes);
        return droppedOrderReport;
    }


}

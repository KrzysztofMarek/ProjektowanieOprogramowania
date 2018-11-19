package backend.backendReport.dao;

import backend.backendReport.model.CompletedOrderReport;
import backend.backendReport.model.DroppedOrderReport;
import backend.backendReport.model.Order;

import java.util.List;

/**
 * Created by Piotr on 2018-11-19.
 */
public interface DatabaseAccess {

    List<Order> getCompletedOrderReport();
    List<Order> getDroppedOrderReport();
}

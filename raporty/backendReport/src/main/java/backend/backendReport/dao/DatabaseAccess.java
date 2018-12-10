package backend.backendReport.dao;

import backend.backendReport.model.*;

import java.util.List;

/**
 * Created by Piotr on 2018-11-19.
 */
public interface DatabaseAccess {

    List<Order> getCompletedOrderReport();
    List<Order> getDroppedOrderReport();
    List<Order> getAverageRealisationTimeReport();
    List<Order> getAverageDeliveryTimeReport();
}

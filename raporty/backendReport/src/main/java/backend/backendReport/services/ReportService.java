package backend.backendReport.services;

import backend.backendReport.model.AverageDeliveryTimeReport;
import backend.backendReport.model.AverageRealisationTimeReport;
import backend.backendReport.model.CompletedOrderReport;
import backend.backendReport.model.DroppedOrderReport;

/**
 * Created by Piotr on 2018-11-19.
 */
public interface ReportService {

    CompletedOrderReport getCompletedOrderReport();
    DroppedOrderReport getDroppedOrderReport();
    AverageRealisationTimeReport getAverageRealisationTimeReport();
    AverageDeliveryTimeReport getAverageDeliveryTimeReport();
    void createCompletedOrderPdf();
    void createDroppedOrderPdf();
    void createAverageDeliveryTimePdf();
    void createAverageRealisationTimePdf();
}
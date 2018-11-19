package backend.backendReport.services;

import backend.backendReport.model.CompletedOrderReport;
import backend.backendReport.model.DroppedOrderReport;

/**
 * Created by Piotr on 2018-11-19.
 */
public interface ReportService {

    CompletedOrderReport getCompletedOrderReport();
    DroppedOrderReport getDroppedOrderReport();


}

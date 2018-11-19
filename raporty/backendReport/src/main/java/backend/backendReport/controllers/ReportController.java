package backend.backendReport.controllers;

import backend.backendReport.interfaces.Report;
import backend.backendReport.model.CompletedOrderReport;
import backend.backendReport.model.DroppedOrderReport;
import backend.backendReport.services.ReportService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

/**
 * Created by Piotr on 2018-11-19.
 */

@RestController
public class ReportController implements Report{

    ReportService reportService;

    @Autowired
    public ReportController (ReportService reportService){
        this.reportService=reportService;
    }

    @RequestMapping(value = "/fetch-completed-order-report", method = RequestMethod.GET, produces = "application/json")
    public CompletedOrderReport getCompletedOrderReport() {
        return reportService.getCompletedOrderReport();
    }

    @RequestMapping(value = "/fetch-droppedd-order-report", method = RequestMethod.GET, produces = "application/json")
    public DroppedOrderReport getDroppedOrderReport() {
        return reportService.getDroppedOrderReport();
    }
}

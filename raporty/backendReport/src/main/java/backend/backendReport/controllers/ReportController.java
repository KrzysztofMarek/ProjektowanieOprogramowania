package backend.backendReport.controllers;

import backend.backendReport.interfaces.Report;
import backend.backendReport.model.AverageDeliveryTimeReport;
import backend.backendReport.model.AverageRealisationTimeReport;
import backend.backendReport.model.CompletedOrderReport;
import backend.backendReport.model.DroppedOrderReport;
import backend.backendReport.services.ReportService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

/**
 * Created by Piotr on 2018-11-19.
 */

@RestController
public class ReportController implements Report {

    ReportService reportService;

    @Autowired
    public ReportController(ReportService reportService) {
        this.reportService = reportService;
    }

    @RequestMapping(value = "/fetch-completed-order-report", method = RequestMethod.GET, produces = "application/json")
    public CompletedOrderReport getCompletedOrderReport() {
        return reportService.getCompletedOrderReport();
    }

    @RequestMapping(value = "/fetch-dropped-order-report", method = RequestMethod.GET, produces = "application/json")
    public DroppedOrderReport getDroppedOrderReport() {
        return reportService.getDroppedOrderReport();
    }

    @RequestMapping(value = "/fetch-average-realisation-time", method = RequestMethod.GET, produces = "application/json")
    public AverageRealisationTimeReport getAverageRealisationTime() {
        return reportService.getAverageRealisationTimeReport();
    }

    @RequestMapping(value = "/fetch-average-delivery-time", method = RequestMethod.GET, produces = "application/json")
    public AverageDeliveryTimeReport getAverageDeliveryTime() {
        return reportService.getAverageDeliveryTimeReport();
    }

    @RequestMapping(value = "/create-completed-order-pdf", method = RequestMethod.GET, produces = "application/json")
    public void createCompletedOrderPdf() {
        reportService.createCompletedOrderPdf();
    }
    @RequestMapping(value = "/create-dropped-order-pdf", method = RequestMethod.GET, produces = "application/json")
    public void createDroppedOrderPdf() {
        reportService.createDroppedOrderPdf();
    }
    @RequestMapping(value = "/create-average-realisation-pdf", method = RequestMethod.GET, produces = "application/json")
    public void createAverageRealisationOrderPdf() {
        reportService.createAverageRealisationTimePdf();
    }
    @RequestMapping(value = "/create-average-delivery-pdf", method = RequestMethod.GET, produces = "application/json")
    public void createAverageDeliveryOrderPdf() {
        reportService.createAverageDeliveryTimePdf();
    }
}
